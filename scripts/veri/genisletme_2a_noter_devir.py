"""
GENIŞLETME AŞAMA 2a — Noter devir adedi (el değiştiren araç sayısı),
2024-01 -> 2026-06 (kaynak seviyesi B — resmi TÜİK indirilebilir tablosu).

ONCEKI DENEME (pm_rapor_genisletme_asama2_5.md, Bolum 3.1): TÜİK veri portali
(veriportali.tuik.gov.tr) WebFetch ile okunamiyordu (JS-render SPA) - HATA
LISTESINE birakilmisti. AYRICA: WebSearch ile toplanan birkac aylik veride
CIDDI BIR YIL-KARISMASI HATASI tespit edildi (2024 sorgulari 2025/2026
verisi donduruyordu) - bu yuzden o veriler KULLANILMADI, TAMAMEN YENIDEN
COZULDU.

COZUM (bu turda): TÜİK veri portali, JS render eden bir tarayici araciyla
gezilerek OKUNABILDI (WebFetch'in aksine). Her "Motorlu Kara Taşıtları"
aylik bulteninin "Tablolar" bolumunde "Aylara göre devri yapılan motorlu
kara taşıtları sayısı" adinda DOGRUDAN INDIRILEBILIR bir .xls dosyasi var
(TÜİK'in kendi resmi API'si, /api/tr/data/downloads?... formatinda). Bu
tablo HER ZAMAN "cari yil + bir onceki yil" karsilastirmasi seklinde
(ODMD'nin aksine, TUM tarihceyi degil yalnizca 2 yili icerir) - bu yuzden
2 FARKLI BULTEN gerekti (ODMD'deki gibi "tek bulten -> tum tarihce" degil):
- "Motorlu Kara Taşıtları - Aralık 2025" bulteni (Sayi 54047, yayim 16 Ocak
  2026) -> 2024 (tam yil) + 2025 (tam yil) tablosu.
- "Motorlu Kara Taşıtları - Haziran 2026" bulteni (Sayi 58043, yayim 17
  Temmuz 2026) -> 2025 (tam yil, capraz-dogrulama) + 2026 Ocak-Haziran
  (kismi yil) tablosu.
2025 degerleri HER IKI bultende de BIREBIR AYNI cikti (capraz-dogrulandi).

YIL-KARISMASI DUZELTMESI (onemli, izlenebilirlik icin): Onceki turda
WebSearch'ten toplanan bazi degerler bu resmi tabloyla KARSILASTIRILDI:
- "Subat 2024 = 762.109" (eski, WebSearch) YANLIS - bu aslinda Subat 2025'in
  degeri. Dogru Subat 2024 = 847.861.
- "Mayis 2024 = 752.150" (eski, WebSearch) YANLIS - bu aslinda Mayis 2026'nin
  degeri. Dogru Mayis 2024 = 920.604.
- "Ocak 2024 = 782.589" ve "Mart 2024 = 865.144" (eski, WebSearch) DOGRU
  cikti - bu resmi tabloyla birebir eslesiyor.
Bu, projenin genel bir uyarisi olarak not edilmeli: WebSearch'ten toplanan
TÜİK istatistikleri (ozellikle yil bilgisi iceren) DOGRULANMADAN
kullanilmamalidir.
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "noter_devir"

# Her deger, ilgili TÜİK bülteninin "Aylara göre devri yapılan motorlu kara
# taşıtları sayısı" adlı resmi .xls tablosundan (Toplam, Otomobil sütunları)
# birebir okunmuştur.
KAYITLAR = [
    # --- 2024 (kaynak: "Aralık 2025" bülteni, Sayı 54047) ---
    dict(referans_ayi="2024-01", noter_devir_toplam_adet=782589, noter_devir_otomobil_adet=530744),
    dict(referans_ayi="2024-02", noter_devir_toplam_adet=847861, noter_devir_otomobil_adet=573508),
    dict(referans_ayi="2024-03", noter_devir_toplam_adet=865144, noter_devir_otomobil_adet=580492),
    dict(referans_ayi="2024-04", noter_devir_toplam_adet=801439, noter_devir_otomobil_adet=515415),
    dict(referans_ayi="2024-05", noter_devir_toplam_adet=920604, noter_devir_otomobil_adet=588886),
    dict(referans_ayi="2024-06", noter_devir_toplam_adet=676083, noter_devir_otomobil_adet=435828),
    dict(referans_ayi="2024-07", noter_devir_toplam_adet=957920, noter_devir_otomobil_adet=621748),
    dict(referans_ayi="2024-08", noter_devir_toplam_adet=935945, noter_devir_otomobil_adet=613752),
    dict(referans_ayi="2024-09", noter_devir_toplam_adet=992171, noter_devir_otomobil_adet=658566),
    dict(referans_ayi="2024-10", noter_devir_toplam_adet=1006009, noter_devir_otomobil_adet=680849),
    dict(referans_ayi="2024-11", noter_devir_toplam_adet=917715, noter_devir_otomobil_adet=630035),
    dict(referans_ayi="2024-12", noter_devir_toplam_adet=985633, noter_devir_otomobil_adet=673727),
    # --- 2025 (kaynak: "Aralık 2025" bülteni; "Haziran 2026" bülteniyle capraz-dogrulandi) ---
    dict(referans_ayi="2025-01", noter_devir_toplam_adet=813093, noter_devir_otomobil_adet=551610),
    dict(referans_ayi="2025-02", noter_devir_toplam_adet=762109, noter_devir_otomobil_adet=520697),
    dict(referans_ayi="2025-03", noter_devir_toplam_adet=821238, noter_devir_otomobil_adet=555093),
    dict(referans_ayi="2025-04", noter_devir_toplam_adet=957499, noter_devir_otomobil_adet=644473),
    dict(referans_ayi="2025-05", noter_devir_toplam_adet=960640, noter_devir_otomobil_adet=645718),
    dict(referans_ayi="2025-06", noter_devir_toplam_adet=840022, noter_devir_otomobil_adet=559842),
    dict(referans_ayi="2025-07", noter_devir_toplam_adet=1015974, noter_devir_otomobil_adet=680114),
    dict(referans_ayi="2025-08", noter_devir_toplam_adet=985244, noter_devir_otomobil_adet=659915),
    dict(referans_ayi="2025-09", noter_devir_toplam_adet=1019994, noter_devir_otomobil_adet=680684),
    dict(referans_ayi="2025-10", noter_devir_toplam_adet=981225, noter_devir_otomobil_adet=666842),
    dict(referans_ayi="2025-11", noter_devir_toplam_adet=897877, noter_devir_otomobil_adet=608924),
    dict(referans_ayi="2025-12", noter_devir_toplam_adet=1158490, noter_devir_otomobil_adet=798616),
    # --- 2026 (kaynak: "Haziran 2026" bülteni, Sayı 58043) ---
    dict(referans_ayi="2026-01", noter_devir_toplam_adet=827673, noter_devir_otomobil_adet=582180),
    dict(referans_ayi="2026-02", noter_devir_toplam_adet=806588, noter_devir_otomobil_adet=556805),
    dict(referans_ayi="2026-03", noter_devir_toplam_adet=870992, noter_devir_otomobil_adet=597104),
    dict(referans_ayi="2026-04", noter_devir_toplam_adet=919896, noter_devir_otomobil_adet=605480),
    dict(referans_ayi="2026-05", noter_devir_toplam_adet=752150, noter_devir_otomobil_adet=503057),
    dict(referans_ayi="2026-06", noter_devir_toplam_adet=941964, noter_devir_otomobil_adet=608484),
]

KAYNAK_URL_2024_2025 = "https://veriportali.tuik.gov.tr/tr/press/54047"  # Motorlu Kara Taşıtları - Aralık 2025
KAYNAK_URL_2025_2026 = "https://veriportali.tuik.gov.tr/tr/press/58043"  # Motorlu Kara Taşıtları - Haziran 2026


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(KAYITLAR).sort_values("referans_ayi").reset_index(drop=True)
    df["kaynak_url"] = df["referans_ayi"].apply(
        lambda a: KAYNAK_URL_2024_2025 if a < "2026-01" else KAYNAK_URL_2025_2026
    )

    hedef_csv = RAW_DIR / "noter_devir_2024_bugun_aylik.csv"
    hedef_xlsx = RAW_DIR / "noter_devir_2024_bugun_aylik.xlsx"
    df.to_csv(hedef_csv, index=False, encoding="utf-8-sig")
    df.to_excel(hedef_xlsx, index=False, sheet_name="noter_devir_aylik")

    beklenen_aylar = pd.period_range("2024-01", "2026-06", freq="M").astype(str).tolist()
    gelen_aylar = df["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== GENISLETME 2a - NOTER DEVIR ADEDI OZETI ===")
    print("Kaynak seviyesi: B (resmi TÜİK indirilebilir .xls tablosu, 2 bülten)")
    print(f"Kapsam: 2024-01 .. 2026-06 ({len(df)} satir)")
    print(f"Eksik ay: {eksik_aylar if eksik_aylar else 'yok'}")
    print()
    print(df[["referans_ayi", "noter_devir_toplam_adet", "noter_devir_otomobil_adet"]].to_string(index=False))
    print(f"\nCikti: {hedef_csv} , {hedef_xlsx}")


if __name__ == "__main__":
    main()
