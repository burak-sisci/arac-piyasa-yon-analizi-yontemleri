"""
GENIŞLETME AŞAMA 5 — Tüm genişletilmiş serilerin birleştirilmesi, 2024-01 -> 2026-06.

Kapsam üst sınırı 2026-06'dır (proxy fiyat ve ODMD'nin kendi yapısal yayım
gecikmesi nedeniyle - bkz. ilgili script'lerin docstring'leri).

DAHIL EDILEN: USD/TRY (A), TÜFE (A, ama 2026-01'de kesiliyor - bkz. UYARI),
proxy fiyat/BETAM (C+D), taşıt kredisi faizi + politika faizi (A),
ODMD sıfır araç satışı (C), ÖTV event-dummy.

DAHIL EDILMEYEN (Asama 2/3'te BLOKLANDI - PM'e birakildi, bkz. PM raporlari):
noter devir adedi, alim gucu proxy'si, erisilebilirlik endeksi, tuketici
guveni, OSD uretim/ihracat.

HEDEF ETIKET: Bu script SADECE BIRLESTIRIR; etiket uretimi (Asama 5'in
"HEDEF ETIKET" alt-basligi, k*sigma bandi vb.) ayrı bir onay/adimdir ve
burada YAPILMADI - cunku TUFE 2026-02'den itibaren eksik oldugundan REEL
etiket suan icin 2026-02..06 araliginda uretilemez (bkz. UYARI).
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw"
PROCESSED_DIR = REPO_KOKU / "data" / "processed" / "genisletme"

HEDEF_BASLANGIC = "2024-01"
HEDEF_BITIS = "2026-06"


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    usdtry = pd.read_csv(RAW_DIR / "usdtry" / "usdtry_2024_bugun_aylik.csv")[
        ["referans_ayi", "usdtry_aysonu", "usdtry_ortalama"]
    ]

    tufe = pd.read_csv(RAW_DIR / "tufe" / "tufe_2024_bugun_aylik.csv").rename(
        columns={"yayim_tarihi": "tufe_yayim_tarihi"}
    )[["referans_ayi", "tufe_endeks", "tufe_aylik_degisim", "tufe_yillik_degisim", "tufe_yayim_tarihi"]]

    proxy_ham = pd.read_csv(RAW_DIR / "proxy_fiyat" / "proxy_fiyat_2024_bugun_raw.csv")
    betam_maske = proxy_ham["kaynak"] == "BETAM sahibindex"
    proxy = proxy_ham[["referans_ayi", "proxy_dom_gun", "proxy_satis_orani_pct", "yayim_ayi"]].copy()
    proxy["proxy_fiyat_cari_tl"] = proxy_ham["proxy_fiyat_cari_tl"].where(betam_maske)
    proxy["proxy_kaynak"] = betam_maske.map({True: "BETAM sahibindex", False: "eksik (BETAM rapor yayımlamadı)"})
    proxy["proxy_fiyat_arabamcom_referans_tl"] = proxy_ham.get("proxy_fiyat_arabamcom_referans_tl")
    proxy = proxy.rename(columns={"yayim_ayi": "proxy_yayim_ayi"})

    faizler = pd.read_csv(RAW_DIR / "faiz" / "faizler_2024_bugun_aylik.csv")

    odmd = pd.read_csv(RAW_DIR / "odmd" / "odmd_2024_bugun_aylik.csv")

    otv = pd.read_csv(RAW_DIR / "otv" / "otv_olaylari_2024_bugun_aylik.csv")

    birlesik = usdtry.merge(tufe, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(proxy, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(faizler, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(odmd, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(otv, on="referans_ayi", how="outer")

    birlesik = birlesik[
        (birlesik["referans_ayi"] >= HEDEF_BASLANGIC) & (birlesik["referans_ayi"] <= HEDEF_BITIS)
    ].sort_values("referans_ayi").reset_index(drop=True)

    csv_yolu = PROCESSED_DIR / "veri_2024_bugun_birlesik.csv"
    xlsx_yolu = PROCESSED_DIR / "veri_2024_bugun_birlesik.xlsx"
    birlesik.to_csv(csv_yolu, index=False, encoding="utf-8-sig")
    birlesik.to_excel(xlsx_yolu, index=False, sheet_name="veri_2024_bugun")

    print("=== GENISLETME 5 - BIRLESTIRME OZETI ===")
    print(f"Kapsam: {HEDEF_BASLANGIC} .. {HEDEF_BITIS} ({len(birlesik)} satir)")
    print(f"Toplam sutun: {birlesik.shape[1]}")
    print(f"Toplam eksik hucre: {int(birlesik.isna().sum().sum())} / {birlesik.size}")
    print()
    print("Sutun basina eksik:")
    print(birlesik.isna().sum().to_string())
    print(f"\nCikti: {csv_yolu} , {xlsx_yolu}")


if __name__ == "__main__":
    main()
