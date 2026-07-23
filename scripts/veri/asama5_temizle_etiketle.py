"""
AŞAMA 5 — Temizleme + aylık yön etiketi üretimi (MVP 2025).

Bu script YENİ KAYNAK ÇEKMEZ; Aşama 1-3'ün ürettiği ham tabloları (data/raw/)
okur, tutarsızlıkları giderir ve hedef değişkeni (up/down/stable) üretir.

DÜZELTİLEN İKİ SORUN:
1) Proxy fiyat serisi TEK KAYNAĞA (BETAM sahibindex "cari fiyat") sabitlenir.
   2025-02 için BETAM hiç rapor yayımlamadı (BETAM'ın kendi arşiv sayfası VE
   "Nisan 2025" raporunun tüm metni/ayrıca kontrol edildi - Şubat'a dair hiçbir
   sayı yok). Bu ay icin BETAM sütunu NaN birakilir; arabam.com degeri AYRI bir
   referans sütununda (proxy_fiyat_arabamcom_referans_tl) tutulur, omurgaya
   KARISTIRILMAZ.
2) Yıllık (yoy) ve aylık (mom) yüzde değişim karışıklığı: BETAM raporları
   metinde bazen aylık, bazen yalnızca yıllık değişim veriyor (rapor bazında
   TUTARSIZ). Tutarlılık için proxy_nominal_aylik_pct / proxy_reel_aylik_pct /
   proxy_aylik_log_degisim TÜM aylarda ham cari_fiyat_tl serisinden YERELDE
   hesaplanır (metinden ayıklanmaz) - böylece 12 ay boyunca aynı yöntemle
   üretilmiş, karşılaştırılabilir bir seri elde edilir. Rapor metinlerindeki
   ham yıllık/aylık % değerleri data/raw/proxy_fiyat/proxy_fiyat_2025_raw.csv'de zaten
   kaynak-alıntılı olarak saklıdır (bu script onları SİLMEZ, sadece bu işlenmiş
   tabloya taşımaz).

SIZINTI/AS-OF NOTU: Bu script yalnızca GEÇMİŞE dönük betimleyici bir etiket
üretir (t ayının etiketi t ve t-1 verisiyle hesaplanır); ileride model
eğitiminde t anındaki feature'ların yalnızca t-1 ve öncesini kullanması ayrı
bir validasyon-protokolü konusudur (Faz 07), burada ele alınmaz.
"""
from pathlib import Path

import numpy as np
import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw"
PROCESSED_DIR = REPO_KOKU / "data" / "processed" / "mvp"

# --- Parametrik ayarlar (kolayca degistirilebilir) ---
ESIK_K = 0.5          # oynaklik-uyarlamali bant carpani: |log_degisim| < k*sigma -> stable
TERCILE_SAYISI = 3    # tercile etiketi icin dilim sayisi


def _log_degisim(seri: pd.Series) -> pd.Series:
    """ln(x_t / x_{t-1}); x veya x_{t-1} NaN ise sonuc NaN (dogal pandas davranisi)."""
    return np.log(seri / seri.shift(1))


def _oynaklik_bandi_etiket(log_degisim: pd.Series, k: float) -> tuple[pd.Series, float]:
    sigma = log_degisim.std(ddof=1)  # yalnizca gecerli (NaN olmayan) gozlemler uzerinden
    esik = k * sigma

    def etiketle(x):
        if pd.isna(x):
            return "eksik"
        if x >= esik:
            return "up"
        if x <= -esik:
            return "down"
        return "stable"

    return log_degisim.map(etiketle), sigma


def _tercile_etiket(log_degisim: pd.Series, n: int) -> pd.Series:
    gecerli = log_degisim.dropna()
    if len(gecerli) < n:
        return pd.Series("eksik", index=log_degisim.index)
    dilimler = pd.qcut(gecerli, n, labels=["down", "stable", "up"], duplicates="drop")
    sonuc = pd.Series("eksik", index=log_degisim.index, dtype=object)
    sonuc.loc[dilimler.index] = dilimler.astype(str)
    return sonuc


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    usdtry = pd.read_csv(RAW_DIR / "usdtry" / "usdtry_2025_aylik.csv")[
        ["referans_ayi", "usdtry_aysonu", "usdtry_ortalama"]
    ]

    tufe = pd.read_csv(RAW_DIR / "tufe" / "tufe_2025_aylik.csv").rename(
        columns={"yayim_tarihi": "tufe_yayim_tarihi"}
    )[["referans_ayi", "tufe_endeks", "tufe_aylik_degisim", "tufe_yayim_tarihi"]]

    proxy_ham = pd.read_csv(RAW_DIR / "proxy_fiyat" / "proxy_fiyat_2025_raw.csv")

    # --- GOREV 1: tek-kaynak omurga + ayri referans sutunu ---
    betam_maske = proxy_ham["kaynak"] == "BETAM sahibindex"
    proxy = proxy_ham[["referans_ayi", "proxy_dom_gun", "proxy_satis_orani_pct",
                        "proxy_ilan_sayisi", "yayim_ayi"]].copy()
    proxy["proxy_fiyat_cari_tl"] = proxy_ham["proxy_fiyat_cari_tl"].where(betam_maske)
    proxy["proxy_kaynak"] = np.where(
        betam_maske, "BETAM sahibindex",
        "eksik (BETAM rapor yayımlamadı)",
    )
    proxy["proxy_fiyat_arabamcom_referans_tl"] = proxy_ham["proxy_fiyat_cari_tl"].where(~betam_maske)
    proxy = proxy.rename(columns={"yayim_ayi": "proxy_yayim_ayi"})

    birlesik = usdtry.merge(tufe, on="referans_ayi", how="outer")
    birlesik = birlesik.merge(proxy, on="referans_ayi", how="outer")
    birlesik = birlesik.sort_values("referans_ayi").reset_index(drop=True)

    # --- GOREV 2: aylik nominal/reel % degisim - TUMU yerelde, ayni yontemle hesaplanir ---
    birlesik["proxy_nominal_aylik_pct"] = birlesik["proxy_fiyat_cari_tl"].pct_change() * 100
    birlesik["proxy_reel_gosterge"] = birlesik["proxy_fiyat_cari_tl"] / birlesik["tufe_endeks"]
    birlesik["proxy_reel_aylik_pct"] = birlesik["proxy_reel_gosterge"].pct_change() * 100

    # --- GOREV 3: hedef degisken (log-degisim + oynaklik-uyarlamali bant + tercile) ---
    birlesik["proxy_aylik_log_degisim"] = _log_degisim(birlesik["proxy_fiyat_cari_tl"])
    birlesik["proxy_reel_aylik_log_degisim"] = _log_degisim(birlesik["proxy_reel_gosterge"])

    birlesik["proxy_yon_nominal"], sigma_nominal = _oynaklik_bandi_etiket(
        birlesik["proxy_aylik_log_degisim"], ESIK_K
    )
    birlesik["proxy_yon_reel"], sigma_reel = _oynaklik_bandi_etiket(
        birlesik["proxy_reel_aylik_log_degisim"], ESIK_K
    )
    birlesik["proxy_yon_tercile"] = _tercile_etiket(
        birlesik["proxy_aylik_log_degisim"], TERCILE_SAYISI
    )
    birlesik["kullanilan_esik_k"] = ESIK_K
    birlesik["kullanilan_sigma_nominal"] = sigma_nominal
    birlesik["kullanilan_sigma_reel"] = sigma_reel

    birlesik = birlesik.drop(columns=["proxy_reel_gosterge"])

    kolon_sirasi = [
        "referans_ayi",
        "usdtry_aysonu", "usdtry_ortalama",
        "tufe_endeks", "tufe_aylik_degisim", "tufe_yayim_tarihi",
        "proxy_fiyat_cari_tl", "proxy_fiyat_arabamcom_referans_tl", "proxy_kaynak",
        "proxy_nominal_aylik_pct", "proxy_reel_aylik_pct",
        "proxy_aylik_log_degisim", "proxy_reel_aylik_log_degisim",
        "proxy_yon_nominal", "proxy_yon_reel", "proxy_yon_tercile",
        "kullanilan_esik_k", "kullanilan_sigma_nominal", "kullanilan_sigma_reel",
        "proxy_dom_gun", "proxy_satis_orani_pct", "proxy_ilan_sayisi",
        "proxy_yayim_ayi",
    ]
    birlesik = birlesik[kolon_sirasi]

    csv_yolu = PROCESSED_DIR / "mvp_2025_etiketli.csv"
    xlsx_yolu = PROCESSED_DIR / "mvp_2025_etiketli.xlsx"
    birlesik.to_csv(csv_yolu, index=False, encoding="utf-8-sig")
    birlesik.to_excel(xlsx_yolu, index=False, sheet_name="mvp_2025_etiketli")

    # --- Ozet (rapor icin) ---
    gecerli_gecis = birlesik["proxy_aylik_log_degisim"].notna().sum()
    print("=== ASAMA 5 - TEMIZLEME + ETIKETLEME OZETI ===")
    print(f"Satir sayisi: {len(birlesik)}")
    print(f"Gecerli (NaN olmayan) aylik log-degisim gecisi sayisi: {gecerli_gecis} / 11 olasi gecis")
    print("  (2025-02 BETAM'da eksik oldugundan Ocak->Subat VE Subat->Mart gecisleri de NaN'dir)")
    print(f"Kullanilan esik: k={ESIK_K}")
    print(f"sigma (nominal log-degisim, gecerli gozlemler uzerinden): {sigma_nominal:.5f}")
    print(f"sigma (reel log-degisim, gecerli gozlemler uzerinden): {sigma_reel:.5f}")
    print()
    print("--- Sinif dagilimi: proxy_yon_nominal ---")
    print(birlesik["proxy_yon_nominal"].value_counts().to_string())
    print()
    print("--- Sinif dagilimi: proxy_yon_reel ---")
    print(birlesik["proxy_yon_reel"].value_counts().to_string())
    print()
    print("--- Sinif dagilimi: proxy_yon_tercile ---")
    print(birlesik["proxy_yon_tercile"].value_counts().to_string())
    print()
    print("--- Tablo (kilit sutunlar) ---")
    print(birlesik[["referans_ayi", "proxy_fiyat_cari_tl", "proxy_aylik_log_degisim",
                     "proxy_yon_nominal", "proxy_yon_reel", "proxy_yon_tercile"]].to_string(index=False))
    print()
    print(f"Cikti: {csv_yolu} , {xlsx_yolu}")


if __name__ == "__main__":
    main()
