"""
AŞAMA 4 — Üç kaynağı (USD/TRY, TÜFE, proxy fiyat) birleştirme.

Girdi (Aşama 1-3'ün ürettiği ham/ara tablolar, kaynak adına göre alt klasörde):
    data/raw/usdtry/usdtry_2025_aylik.csv
    data/raw/tufe/tufe_2025_aylik.csv
    data/raw/proxy_fiyat/proxy_fiyat_2025_raw.csv

Çıktı: data/processed/mvp/mvp_2025_birlesik.csv (+ .xlsx) — tek satır = tek ay,
anahtar = referans_ayi (YYYY-MM).

Not: "Çekme raporu" (hangi kaynağın hangi seviyeden geldiği, eksik ay/uyarılar)
bilinçli olarak ayrı bir dosya olarak üretilmez (proje sahibinin talebi); bu
bilgi oturum sonundaki özet mesajda verilir.
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw"
PROCESSED_DIR = REPO_KOKU / "data" / "processed" / "mvp"


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    usdtry = pd.read_csv(RAW_DIR / "usdtry" / "usdtry_2025_aylik.csv")
    usdtry = usdtry[["referans_ayi", "usdtry_aysonu", "usdtry_ortalama"]]

    tufe = pd.read_csv(RAW_DIR / "tufe" / "tufe_2025_aylik.csv")
    tufe = tufe.rename(columns={"yayim_tarihi": "tufe_yayim_tarihi"})
    tufe = tufe[["referans_ayi", "tufe_endeks", "tufe_aylik_degisim", "tufe_yayim_tarihi"]]

    proxy = pd.read_csv(RAW_DIR / "proxy_fiyat" / "proxy_fiyat_2025_raw.csv")
    proxy = proxy.rename(columns={
        "proxy_fiyat_cari_tl": "proxy_fiyat",
        "proxy_dom_gun": "proxy_dom",
        "yayim_ayi": "proxy_yayim_ayi",
    })
    proxy = proxy[["referans_ayi", "proxy_fiyat", "proxy_ilan_sayisi", "proxy_dom",
                   "kaynak", "kaynak_rapor_basligi", "proxy_yayim_ayi"]]
    proxy = proxy.rename(columns={
        "kaynak": "proxy_kaynak",
        "kaynak_rapor_basligi": "proxy_kaynak_rapor",
    })

    birlesik = usdtry.merge(tufe, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(proxy, on="referans_ayi", how="outer")
    birlesik = birlesik.sort_values("referans_ayi").reset_index(drop=True)

    kolon_sirasi = [
        "referans_ayi",
        "usdtry_aysonu", "usdtry_ortalama",
        "tufe_endeks", "tufe_aylik_degisim", "tufe_yayim_tarihi",
        "proxy_fiyat", "proxy_ilan_sayisi", "proxy_dom",
        "proxy_kaynak", "proxy_kaynak_rapor", "proxy_yayim_ayi",
    ]
    birlesik = birlesik[kolon_sirasi]

    csv_yolu = PROCESSED_DIR / "mvp_2025_birlesik.csv"
    xlsx_yolu = PROCESSED_DIR / "mvp_2025_birlesik.xlsx"
    birlesik.to_csv(csv_yolu, index=False, encoding="utf-8-sig")
    birlesik.to_excel(xlsx_yolu, index=False, sheet_name="mvp_2025")

    print("=== ASAMA 4 - BIRLESTIRME OZETI ===")
    print(f"Satir sayisi: {len(birlesik)} (beklenen: 12)")
    print(f"Eksik hucre sayisi (NaN): {int(birlesik.isna().sum().sum())}")
    print()
    print(birlesik.to_string(index=False))
    print()
    print(f"Cikti: {csv_yolu} , {xlsx_yolu}")


if __name__ == "__main__":
    main()
