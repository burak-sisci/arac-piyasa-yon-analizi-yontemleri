"""
GENIŞLETME AŞAMA 4 — ÖTV/vergi olay-bazlı event dummy, 2024-01 -> 2026-06.

ARAŞTIRMA SONUCU: 2024-01 - 2026-06 penceresinde tek büyük, iyi-belgelenmiş
yapısal ÖTV düzenlemesi bulundu:

- **24 Temmuz 2025** (yürürlük): 7555 sayılı Kanun'un 13. maddesi + 10115
  sayılı Cumhurbaşkanı Kararı (Resmî Gazete, 23-24 Temmuz 2025). ÖTV Kanunu'na
  ekli (II) sayılı listedeki araçlar için matrah grupları/oranları yeniden
  tanımlandı; matrah sistemi motor hacmi/gücünden ARINDIRILIP vergisiz satış
  fiyatı bazlı hale getirildi. Elektrikli otomobillerde en düşük ÖTV oranı
  %10'dan %25'e çıktı, matrah eşiği 1.650.000 TL'ye güncellendi.
  Kaynak: verginet.net Vergi Sirküleri 2025-74; watmobilite.com.

BULUNAMAYAN / DOĞRULANAMAYAN: Ocak 2024, Ocak 2025 ve Ocak 2026'da rutin
matrah-dilimi enflasyon güncellemesi olup olmadığı (ÖTV matrah dilimleri
genellikle yıllık TÜFE'ye endeksli güncellenir) kamuya açık, kolay erişilebilir
kaynaklarda AÇIKÇA teyit edilemedi. Bu bir "hata" değil, bir "literatürde net
değil" bulgusu olarak işaretlenmiştir — daha derin bir Resmî Gazete taraması
gerektirir (sonraki adım önerisi).
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "otv"

BASLANGIC_AY = "2024-01"
BITIS_AY = "2026-06"

OLAYLAR = [
    dict(tarih="2025-07-24", referans_ayi="2025-07",
         aciklama="7555 sayılı Kanun m.13 + 10115 sayılı Cumhurbaşkanı Kararı: "
                   "ÖTV matrah sistemi motor hacmi/gücünden vergisiz-satış-fiyatı "
                   "bazına geçti; EV'lerde en düşük ÖTV %10->%25, matrah eşiği "
                   "1.650.000 TL.",
         kaynak_url="https://www.verginet.net/dtt/11/Vergi-Sirkuleri-2025-74.aspx"),
]


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    aylar = pd.period_range(BASLANGIC_AY, BITIS_AY, freq="M").astype(str).tolist()
    df = pd.DataFrame({"referans_ayi": aylar})
    df["otv_event_ay_mi"] = 0
    df["otv_ay_farki"] = None  # duzenlemeden bu yana gecen ay sayisi (negatifse once)
    df["otv_aciklama"] = ""

    for olay in OLAYLAR:
        idx = df.index[df["referans_ayi"] == olay["referans_ayi"]]
        if len(idx):
            df.loc[idx, "otv_event_ay_mi"] = 1
            df.loc[idx, "otv_aciklama"] = olay["aciklama"]

    olay_ayi = pd.Period(OLAYLAR[0]["referans_ayi"], freq="M")
    df["otv_ay_farki"] = df["referans_ayi"].apply(
        lambda a: (pd.Period(a, freq="M") - olay_ayi).n
    )

    csv_yolu = RAW_DIR / "otv_olaylari_2024_bugun_aylik.csv"
    xlsx_yolu = RAW_DIR / "otv_olaylari_2024_bugun_aylik.xlsx"
    df.to_csv(csv_yolu, index=False, encoding="utf-8-sig")
    df.to_excel(xlsx_yolu, index=False, sheet_name="otv_olaylari")

    print("=== GENISLETME 4 - OTV OLAY-DUMMY OZET ===")
    print(f"Kapsam: {BASLANGIC_AY} .. {BITIS_AY}")
    print(f"Tespit edilen olay sayisi: {len(OLAYLAR)} (2025-07)")
    print("UYARI: Ocak-2024/2025/2026 rutin matrah guncellemesi dogrulanamadi (literaturde net degil).")
    print()
    print(df.to_string(index=False))
    print(f"\nCikti: {csv_yolu} , {xlsx_yolu}")


if __name__ == "__main__":
    main()
