"""
GENIŞLETME AŞAMA 3a — ODMD sıfır araç (otomobil + hafif ticari) satış adetleri,
2024-01 -> 2026-06 (kaynak seviyesi C — resmi dernek basın bülteni PDF'i).

YÖNTEM NOTU: ODMD basın bülteni PDF'leri normal metin-tabanlı web araçlarıyla
(WebFetch) OKUNAMADI (ham PDF stream döndü); Claude'un kendi PDF-sayfa-goruntu
okuyucusuyla (Read araci, PDF sayfalarini goruntu olarak isler) BASARIYLA
okundu. Her bulten, ekinde ("Ek 1/2/3") 2010'dan itibaren TÜM aylarin
TAMAMLANMIŞ yillik satirlarini iceren bir tablo yayimliyor - bu sayede 30 ay
icin 30 ayri bulten degil, yalnizca 2 GUNCEL bulten (2024 sonunu iceren "3
Aralik 2024" + 2025/2026 baslangicini iceren "2 Haziran 2026") YETERLI oldu.

Kaynaklar:
- ODMD Basın Bülteni 3 Aralık 2024 (Ek 1: Otomobil+HTA, Ek 2: yalnız Otomobil)
  https://www.odmd.org.tr/folders/2837/categorial1docs/4791/ODMD%20Bas%C4%B1n%20Bulteni%203%20Aral%C4%B1k%202024.pdf
  -> 2024'ün TAMAMLANMIŞ satırı (Ocak-Aralık, çünkü bu bülten sonraki yılda
     yayımlanan bir bültenden değil, doğrudan bu PDF'in kendi "10 yıllık
     tarihçe" ekinden okunmuştur — bkz. asağıdaki KAYNAK notu).
- ODMD Basın Bülteni 2 Haziran 2026 (Ek 1, Ek 2)
  https://www.odmd.org.tr/folders/2837/categorial1docs/6111/ODMD%20Bas%C4%B1n%20Bulteni%202%20Haziran%202026.docx.pdf
  -> 2024 (tamamlanmış, çapraz-doğrulama), 2025 (tamamlanmış), 2026 Ocak-Mayıs.
- Haziran 2026 TOPLAM rakamı ayrı bir kaynaktan (haber, web araması):
  alomaliye.com, "Otomotiv Pazarı İlk Yarıda Yüzde 8,19 Daraldı" (2 Temmuz 2026)
  -> yalnızca TOPLAM (Otomobil+HTA) verilmiş, otomobil-yalnız kırılımı YOK.

BİLİNEN SINIR: Haziran 2026 için yalnızca toplam (105.041 adet) var,
otomobil-yalnız kırılımı bu turda bulunamadı (haber metninde yok) - NaN.
"""
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw"

# Ek 1 (Otomobil + Hafif Ticari Araç toplamı) — "3 Aralık 2024" ve
# "2 Haziran 2026" bültenlerinin Ek-1 tablolarından birebir okunmuştur.
ODMD_TOPLAM = {
    "2024-01": 79701, "2024-02": 105990, "2024-03": 109828, "2024-04": 75919,
    "2024-05": 100305, "2024-06": 106238, "2024-07": 94037, "2024-08": 90134,
    "2024-09": 87740, "2024-10": 97274, "2024-11": 121094, "2024-12": 170249,
    "2025-01": 68654, "2025-02": 90730, "2025-03": 116900, "2025-04": 105352,
    "2025-05": 107730, "2025-06": 118611, "2025-07": 107718, "2025-08": 101650,
    "2025-09": 110302, "2025-10": 116149, "2025-11": 132984, "2025-12": 191620,
    "2026-01": 75362, "2026-02": 88039, "2026-03": 101997, "2026-04": 104298,
    "2026-05": 83442,
    "2026-06": 105041,  # alomaliye.com haberinden (yalnızca toplam)
}

# Ek 2 (yalnız Otomobil) — ayni iki bultenin Ek-2 tablosundan.
ODMD_OTOMOBIL = {
    "2024-01": 64041, "2024-02": 82277, "2024-03": 87071, "2024-04": 61448,
    "2024-05": 80260, "2024-06": 87858, "2024-07": 73396, "2024-08": 69288,
    "2024-09": 69634, "2024-10": 75662, "2024-11": 94595, "2024-12": 134811,
    "2025-01": 55944, "2025-02": 76021, "2025-03": 91828, "2025-04": 85411,
    "2025-05": 85123, "2025-06": 93676, "2025-07": 84195, "2025-08": 82215,
    "2025-09": 88274, "2025-10": 90695, "2025-11": 104795, "2025-12": 146319,
    "2026-01": 61055, "2026-02": 69776, "2026-03": 79857, "2026-04": 80182,
    "2026-05": 65386,
    # 2026-06: BİLİNMİYOR (haber yalnızca toplamı verdi) -> NaN
}


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    aylar = sorted(ODMD_TOPLAM.keys())
    df = pd.DataFrame({
        "referans_ayi": aylar,
        "odmd_toplam_adet": [ODMD_TOPLAM[a] for a in aylar],
        "odmd_otomobil_adet": [ODMD_OTOMOBIL.get(a) for a in aylar],
    })
    df["odmd_hta_adet"] = df["odmd_toplam_adet"] - df["odmd_otomobil_adet"]

    csv_yolu = RAW_DIR / "odmd_2024_bugun_aylik.csv"
    xlsx_yolu = RAW_DIR / "odmd_2024_bugun_aylik.xlsx"
    df.to_csv(csv_yolu, index=False, encoding="utf-8-sig")
    df.to_excel(xlsx_yolu, index=False, sheet_name="odmd_aylik")

    print("=== GENISLETME 3a - ODMD SIFIR ARAC SATISI OZET ===")
    print(f"Kaynak seviyesi: C (ODMD basın bülteni PDF, Ek 1/2 tabloları)")
    print(f"Kapsam: {aylar[0]} .. {aylar[-1]} ({len(aylar)} ay)")
    print(f"odmd_otomobil_adet eksik ay: {df[df['odmd_otomobil_adet'].isna()]['referans_ayi'].tolist()}")
    print()
    print(df.to_string(index=False))
    print(f"\nCikti: {csv_yolu} , {xlsx_yolu}")


if __name__ == "__main__":
    main()
