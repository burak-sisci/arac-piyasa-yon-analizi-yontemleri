"""
GENIŞLETME AŞAMA 2b — Alım gücü proxy'si (brüt ücret-maaş endeksi),
2024-01 -> 2026-06 (kaynak seviyesi B — resmi TÜİK indirilebilir tablosu).

ONCEKI DENEME (pm_rapor_genisletme_asama2_5.md, Bolum 3.1): TÜİK veri portali
WebFetch ile okunamiyordu - HATA LISTESINE birakilmisti.

COZUM (bu turda): TÜİK veri portali JS render eden tarayici araciyla
gezilerek "İstihdam, İşsizlik ve Ücret > İşgücü Girdi Endeksleri" bulteninde
(en guncel: "I. Çeyrek: Ocak-Mart 2026", Sayı 57966) "Dinamik Tablolar"
bolumunden indirilen "İşgücü Girdi Endeksleri (2021=100).xls" tablosu
bulundu. BU TEK TABLO 2009-2026 arasi TAM CEYREKLIK TARIHCEYI icerir (ODMD
tarzi cok-yillik tablo - tek belge yeterli oldu, noter devir'deki gibi 2.
bir belgeye gerek kalmadi).

DEGISKEN SECIMI: "Brüt ücret-maaş endeksi" (Arındırılmamış, B-N toplam
sektor: sanayi+insaat+ticaret-hizmet), NOMINAL bir ucret endeksidir
(2021=100). "Alim gucu" (satin alma gucu) icin bu, TÜFE'ye bolunerek
(reel deflate) kullanilmalidir - o hesaplama BU SCRIPT'TE YAPILMAZ (asama5
tarzi etiketleme/turetme adiminin isi), burada yalnizca HAM nominal endeks
CEKILIR.

FREKANS UYARISI (onemli, ay bazinda okurken dikkat): Bu veri ÇEYREKLIKTIR
(TÜİK bu anketi aylik degil, ceyreklik yayimlar). Aylik veri setine
eklenebilmesi icin HER CEYREGIN degeri, o ceyregin 3 ayina da AYNEN
TEKRARLANARAK (forward-fill benzeri, gercek aylik varyasyon UYDURULMADAN)
atanmistir - bu KESINLIKLE ay-ay degisim gostermez, yalnizca ceyrek-ceyrek
degisim yansitir. proxy_yayim_ayi mantigina benzer sekilde, `alim_gucu_ceyrek`
sutunu hangi ceyregin degeri oldugunu acikca isaretler (sizinti/karistirma
riskini onlemek icin).

KAPSAM SINIRI: 2026-Q2 (Nisan-Haziran) HENUZ YAYIMLANMADI (bir sonraki
bulten 21 Agustos 2026) - bu yuzden 2026-04, 2026-05, 2026-06 icin bu
degisken NaN'dir (yapisal/normal gecikme, diger serilerdeki 2026-07 NaN'i
gibi).
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "alim_gucu"

# TÜİK "İşgücü Girdi Endeksleri (2021=100)" tablosunun B-N (toplam: sanayi+
# insaat+ticaret-hizmet) blogundan, "Brüt ücret-maaş endeksi (Arındırılmamış)"
# sutunundan birebir okunmustur.
KAYNAK_URL = "https://veriportali.tuik.gov.tr/tr/press/57966"  # İşgücü Girdi Endeksleri, I. Çeyrek 2026
CEYREK_DEGERLERI = {
    "2024-Q1": 693.111053,
    "2024-Q2": 741.916146,
    "2024-Q3": 796.607993,
    "2024-Q4": 839.337735,
    "2025-Q1": 1002.940987,
    "2025-Q2": 1069.033682,
    "2025-Q3": 1116.447515,
    "2025-Q4": 1147.643883,
    "2026-Q1": 1374.314470,
    # 2026-Q2: HENUZ YAYIMLANMADI (bir sonraki bulten 21 Agustos 2026)
}

CEYREK_AYLARI = {
    "Q1": ["01", "02", "03"],
    "Q2": ["04", "05", "06"],
    "Q3": ["07", "08", "09"],
    "Q4": ["10", "11", "12"],
}


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    satirlar = []
    for ceyrek_anahtari, deger in CEYREK_DEGERLERI.items():
        yil, ceyrek = ceyrek_anahtari.split("-")
        for ay in CEYREK_AYLARI[ceyrek]:
            satirlar.append(dict(
                referans_ayi=f"{yil}-{ay}",
                brut_ucret_maas_endeksi_2021_100=deger,
                alim_gucu_ceyrek=ceyrek_anahtari,
            ))

    df = pd.DataFrame(satirlar).sort_values("referans_ayi").reset_index(drop=True)
    df = df[(df["referans_ayi"] >= "2024-01") & (df["referans_ayi"] <= "2026-06")]
    df["kaynak_url"] = KAYNAK_URL

    hedef_csv = RAW_DIR / "alim_gucu_2024_bugun_aylik.csv"
    hedef_xlsx = RAW_DIR / "alim_gucu_2024_bugun_aylik.xlsx"
    df.to_csv(hedef_csv, index=False, encoding="utf-8-sig")
    df.to_excel(hedef_xlsx, index=False, sheet_name="alim_gucu_aylik")

    beklenen_aylar = pd.period_range("2024-01", "2026-06", freq="M").astype(str).tolist()
    gelen_aylar = df["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== GENISLETME 2b - ALIM GUCU PROXY'Sİ (BRUT UCRET-MAAS ENDEKSI) OZETI ===")
    print("Kaynak seviyesi: B (resmi TÜİK indirilebilir .xls tablosu, ceyreklik -> aylik genisletildi)")
    print(f"Kapsam: 2024-01 .. 2026-06 ({len(df)} satir)")
    print(f"Eksik ay: {eksik_aylar if eksik_aylar else 'yok'} (2026-Q2 henuz yayimlanmadi)")
    print()
    print(df.to_string(index=False))
    print(f"\nCikti: {hedef_csv} , {hedef_xlsx}")


if __name__ == "__main__":
    main()
