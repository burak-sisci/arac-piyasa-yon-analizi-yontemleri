"""
AŞAMA 3 — Proxy ikinci el otomobil fiyat serisi (2025, aylık).

Kaynak seviyesi: C (resmi sayfadan yapılandırılmış çıkarım) — BETAM "sahibindex
Otomobil Piyasası Görünümü" aylık blog yazıları API/CSV SUNMAZ; bu yüzden Aşama
1/2'deki gibi programatik/otomatik yeniden-çalıştırılabilir bir API çağrısı
YOKTUR. Bu script, her ay için BETAM (birincil) veya arabam.com (alternatif,
yalnızca 2025-02 için — asagida gerekce var) sayfalarindan MANUEL olarak
dogrulanmis (WebFetch ile sayfa icerigi okunup alintilanarak) degerleri
YAPISAL bir tabloya doker. Her satirin kaynagi (rapor basligi + URL + birebir
alinti) asagidaki KAYIT listesinde saklidir - izlenebilirlik icin.

KRITIK KESIF (as-of-date acisindan onemli): BETAM raporu "{Ay} {Yil}" basligiyla
yayimlanir ama HEP bir onceki ("{Ay-1}") ayin verisini anlatir. Ornegin "Subat
2025" basligindaki rapor Ocak 2025 fiyatini verir; "Ocak 2026" basligindaki
rapor Aralik 2025 fiyatini verir. Bu kalip 2025-01'den 2025-12'ye kadar 11
rapor uzerinde DOGRULANMISTIR (bkz. her KAYIT'taki "kaynak_alinti"). Bu yuzden
referans_ayi (verinin AIT OLDUGU ay) ile yayim_ayi (raporun YAYIMLANDIGI ay,
rapor basligindaki ay) BILINCLI olarak AYRI sutunlardir.

BILINEN BOSLUK: BETAM, "Mart 2025" basliginda hic rapor yayimlamamistir (Subat
2025 -> Nisan 2025'e dogrudan gecmis; BETAM'in kendi arsiv/kategori sayfasinda
dogrulanmistir). Bu, Subat 2025 (2025-02) referans ayi icin BETAM'dan veri
OLMADIGI anlamina gelir. UYDURMA yerine alternatif kaynaga (arabam.com Aylik
Fiyat Endeksi) gecilmis (kaynak seviyesi C, ama farkli sağlayici -
"kaynak" sutununda acikca isaretlenmistir). arabam.com bu ay icin ilanda-kalma-
suresi/talep-endeksi/satis-orani YAYIMLAMADIGI icin bu alanlar 2025-02 icin
bos (NaN) birakilmistir - uydurulmamistir.

KRITIK UYARI (karar N1, veri sozlugune de yazilacak): Bu proxy seri MIX/
KOMPOZISYON DUZELTMESIZDIR (ham ortalama ilan fiyati). MVP'de YER-TUTUCU
hedef olarak kullanilir, NIHAI HEDEF DEGILDIR.

Cikti: data/raw/proxy_fiyat/proxy_fiyat_2025_raw.csv (+ .xlsx) - tum cikarilan alanlar ve
kaynak izi dahil.
"""
import sys
from pathlib import Path

import pandas as pd

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "proxy_fiyat"

# Her kayit: WebFetch ile ilgili sayfadan CEKILEN ve dogrulanan degerler.
# "kaynak_alinti" = sayfadaki birebir cumle (izlenebilirlik icin).
KAYITLAR = [
    dict(
        referans_ayi="2025-01", proxy_fiyat_cari_tl=935136,
        proxy_fiyat_nominal_yillik_pct=8.7, proxy_fiyat_reel_yillik_pct=-23.5,
        proxy_fiyat_reel_aylik_pct=-2.0,
        proxy_talep_aylik_pct=0.0, proxy_talep_yillik_pct=11.2,
        proxy_satis_orani_pct=20.3, proxy_dom_gun=21.1,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Şubat 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/02/sahibindex-otomobil-piyasasi-gorunumu-subat-2025/",
        yayim_ayi="2025-02",
        kaynak_alinti="Ocakta ortalama otomobil fiyatı 935 bin 136 TL olmuştur; "
                       "Otomobil talep endeksi aralık ayına kıyasla değişmemesine "
                       "rağmen geçen yılın ocak ayına kıyasla yüzde 11,2 daha yüksektir.",
    ),
    dict(
        referans_ayi="2025-02", proxy_fiyat_cari_tl=888689,
        proxy_fiyat_nominal_yillik_pct=None, proxy_fiyat_reel_yillik_pct=None,
        proxy_fiyat_reel_aylik_pct=-1.58,
        proxy_talep_aylik_pct=None, proxy_talep_yillik_pct=None,
        proxy_satis_orani_pct=None, proxy_dom_gun=None,
        kaynak="arabam.com (ALTERNATİF - BETAM bu ay için rapor yayımlamadı)",
        kaynak_rapor_basligi="İkinci El Otomobilde Neler Oluyor? Şubat Verileri Açıklandı",
        kaynak_url="https://www.arabam.com/blog/genel/ikinci-el-otomobilde-neler-oluyor-subat-verileri-aciklandi/",
        yayim_ayi="2025-02 (tahmini; blog yazısı yayın tarihi sayfada net verilmedi)",
        kaynak_alinti="ocak ayında 877.029 TL olan ilan fiyatları şubat ayında "
                       "ortalama 888.689 TL oldu. Enflasyondan arındırılmış reel "
                       "fiyatlar, ocak ayına kıyasla %1,58 oranında düşüş yaşadı.",
    ),
    dict(
        referans_ayi="2025-03", proxy_fiyat_cari_tl=950515,
        proxy_fiyat_nominal_yillik_pct=10.6, proxy_fiyat_reel_yillik_pct=-19.9,
        proxy_fiyat_reel_aylik_pct=-2.1,
        proxy_talep_aylik_pct=11.8, proxy_talep_yillik_pct=5.3,
        proxy_satis_orani_pct=21.3, proxy_dom_gun=21.3,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Nisan 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/04/sahibindex-otomobil-piyasasi-gorunumu-nisan-2025/",
        yayim_ayi="2025-04",
        kaynak_alinti="Ortalama satılık otomobil cari fiyatı geçen yılın mart ayına "
                       "kıyasla yüzde 10,6 artmış ve Mart'ta ortalama otomobil fiyatı "
                       "950 bin 515 TL olmuştur.",
    ),
    dict(
        referans_ayi="2025-04", proxy_fiyat_cari_tl=947790,
        proxy_fiyat_nominal_yillik_pct=9.2, proxy_fiyat_reel_yillik_pct=-20.8,
        proxy_fiyat_reel_aylik_pct=-3.2,
        proxy_talep_aylik_pct=12.4, proxy_talep_yillik_pct=34.5,
        proxy_satis_orani_pct=22.4, proxy_dom_gun=23.0,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Mayıs 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/05/sahibindex-otomobil-piyasasi-gorunumu-mayis-2025/",
        yayim_ayi="2025-05",
        kaynak_alinti="nisanda ortalama otomobil fiyatı 947 bin 790 TL olmuştur; "
                       "otomobil reel fiyatı geçen yılın aynı ayına göre yüzde 20,8, "
                       "bir önceki aya göre ise yüzde 3,2 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-05", proxy_fiyat_cari_tl=962726,
        proxy_fiyat_nominal_yillik_pct=9.9, proxy_fiyat_reel_yillik_pct=-18.8,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=-2.2, proxy_talep_yillik_pct=25.1,
        proxy_satis_orani_pct=21.7, proxy_dom_gun=20.8,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Haziran 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/06/sahibindex-otomobil-piyasasi-gorunumu-haziran-2025/",
        yayim_ayi="2025-06",
        kaynak_alinti="mayısta ortalama otomobil fiyatı 962 bin 726 TL olmuştur; "
                       "otomobil reel fiyatı geçen yılın aynı ayına göre yüzde 18,8 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-06", proxy_fiyat_cari_tl=968926,
        proxy_fiyat_nominal_yillik_pct=11.2, proxy_fiyat_reel_yillik_pct=-17.6,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=-11.3, proxy_talep_yillik_pct=None,
        proxy_satis_orani_pct=21.4, proxy_dom_gun=22.4,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Temmuz 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/07/sahibindex-otomobil-piyasasi-gorunumu-temmuz-2025/",
        yayim_ayi="2025-07",
        kaynak_alinti="haziranda ortalama otomobil fiyatı 968 bin 926 TL olmuştur; "
                       "otomobil reel fiyatı geçen yılın aynı ayına göre yüzde 17,6 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-07", proxy_fiyat_cari_tl=990751,
        proxy_fiyat_nominal_yillik_pct=14.9, proxy_fiyat_reel_yillik_pct=-13.9,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=19.1, proxy_talep_yillik_pct=17.2,
        proxy_satis_orani_pct=25.5, proxy_dom_gun=22.9,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Ağustos 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/08/sahibindex-otomobil-piyasasi-gorunumu-agustos-2025/",
        yayim_ayi="2025-08",
        kaynak_alinti="temmuzda ortalama otomobil fiyatı 990 bin 751 TL olmuştur; "
                       "otomobil reel fiyatı geçen yılın aynı ayına göre yüzde 13,9 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-08", proxy_fiyat_cari_tl=1022000,
        proxy_fiyat_nominal_yillik_pct=18.2, proxy_fiyat_reel_yillik_pct=-11.1,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=0.7, proxy_talep_yillik_pct=11.4,
        proxy_satis_orani_pct=24.9, proxy_dom_gun=19.8,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Eylül 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/09/sahibindex-otomobil-piyasasi-gorunumu-eylul-2025/",
        yayim_ayi="2025-09",
        kaynak_alinti="Ortalama satılık otomobil cari fiyatı geçen yılın ağustos ayına "
                       "kıyasla yüzde 18,2 artmış ve ortalama otomobil fiyatı 1 milyon 22 "
                       "bin TL olmuştur; otomobil reel fiyatı geçen yılın aynı ayına göre "
                       "yüzde 11,1 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-09", proxy_fiyat_cari_tl=1058000,
        proxy_fiyat_nominal_yillik_pct=20.3, proxy_fiyat_reel_yillik_pct=-9.8,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=-7.2, proxy_talep_yillik_pct=3.9,
        proxy_satis_orani_pct=24.0, proxy_dom_gun=19.1,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Ekim 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/10/sahibindex-otomobil-piyasasi-gorunumu-ekim-2025/",
        yayim_ayi="2025-10",
        kaynak_alinti="Ortalama satılık otomobil cari fiyatı geçen yılın eylül ayına "
                       "kıyasla yüzde 20,3 artmış ve ortalama otomobil fiyatı 1 milyon 58 "
                       "bin TL olmuştur; otomobil reel fiyatı geçen yılın aynı ayına göre "
                       "yüzde 9,8 düşmüştür.",
    ),
    dict(
        referans_ayi="2025-10", proxy_fiyat_cari_tl=1086000,
        proxy_fiyat_nominal_yillik_pct=22.2, proxy_fiyat_reel_yillik_pct=-9.8,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=-2.9, proxy_talep_yillik_pct=-0.8,
        proxy_satis_orani_pct=23.0, proxy_dom_gun=20.0,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Kasım 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/11/sahibindex-otomobil-piyasasi-gorunumu-kasim-2025/",
        yayim_ayi="2025-11",
        kaynak_alinti="ortalama otomobil fiyatı 1 milyon 86 bin TL olmuştur; "
                       "enflasyondan arındırılmış reel fiyatlar aynı dönemde yüzde 9,8 "
                       "oranında azalmıştır; Otomobil talep endeksi bir önceki aya göre "
                       "yüzde 2,9, geçen yılın aynı ayına göre ise yüzde 0,8 azalmıştır.",
    ),
    dict(
        referans_ayi="2025-11", proxy_fiyat_cari_tl=1101000,
        proxy_fiyat_nominal_yillik_pct=22.4, proxy_fiyat_reel_yillik_pct=-6.6,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=-7.1, proxy_talep_yillik_pct=-1.6,
        proxy_satis_orani_pct=21.2, proxy_dom_gun=20.7,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Aralık 2025",
        kaynak_url="https://betam.bahcesehir.edu.tr/2025/12/sahibindex-otomobil-piyasasi-gorunumu-aralik-2025/",
        yayim_ayi="2025-12",
        kaynak_alinti="Ortalama satılık otomobil cari fiyatı geçen yılın kasım ayına "
                       "kıyasla yüzde 22,4 artmış ve ortalama otomobil fiyatı 1 milyon 101 "
                       "bin TL olmuştur; Otomobil talep endeksi bir önceki aya göre yüzde "
                       "7,1, geçen yılın aynı ayına göre ise yüzde 1,6 azalmıştır.",
    ),
    dict(
        referans_ayi="2025-12", proxy_fiyat_cari_tl=1108000,
        proxy_fiyat_nominal_yillik_pct=22.0, proxy_fiyat_reel_yillik_pct=-6.8,
        proxy_fiyat_reel_aylik_pct=None,
        proxy_talep_aylik_pct=10.0, proxy_talep_yillik_pct=10.0,
        proxy_satis_orani_pct=25.2, proxy_dom_gun=21.6,
        kaynak="BETAM sahibindex", kaynak_rapor_basligi="Ocak 2026",
        kaynak_url="https://betam.bahcesehir.edu.tr/2026/01/sahibindex-otomobil-piyasasi-gorunumu-ocak-2026/",
        yayim_ayi="2026-01",
        kaynak_alinti="Ortalama satılık otomobil cari fiyatı geçen yılın aralık ayına "
                       "kıyasla yüzde 22 artmış ve ortalama otomobil fiyatı 1 milyon 108 "
                       "bin TL olmuştur.",
    ),
]


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(KAYITLAR)
    df["proxy_ilan_sayisi"] = None  # Hicbir ay icin mutlak sayi yayimlanmadi (bilinen bosluk).
    df = df.sort_values("referans_ayi").reset_index(drop=True)

    ham_csv = RAW_DIR / "proxy_fiyat_2025_raw.csv"
    ham_xlsx = RAW_DIR / "proxy_fiyat_2025_raw.xlsx"
    df.to_csv(ham_csv, index=False, encoding="utf-8-sig")
    df.to_excel(ham_xlsx, index=False, sheet_name="proxy_fiyat_raw")

    beklenen_aylar = pd.period_range("2025-01", "2025-12", freq="M").astype(str).tolist()
    gelen_aylar = df["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]
    eksik_alan_sayisi = df["proxy_dom_gun"].isna().sum()

    print("=== ASAMA 3 - PROXY FIYAT SERISI OZET ===")
    print("Kaynak seviyesi: C (BETAM sahibindex - 11 ay) + D/alternatif (arabam.com - 1 ay: 2025-02)")
    print("KRITIK KESIF: BETAM raporu '{Ay} {Yil}' basligiyla yayimlanir ama ONCEKI ayin")
    print("verisini icerir (ör. 'Subat 2025' raporu -> Ocak 2025 fiyati). Dogrulandi (11/11 rapor).")
    print()
    print(f"Hedef aralikta gelen ay sayisi: {len(gelen_aylar)} / {len(beklenen_aylar)}")
    print(f"Tamamen eksik ay: {eksik_aylar if eksik_aylar else 'yok'}")
    print("BILINEN BOSLUK: 2025-02 icin BETAM raporu hic yayimlanmamis (Subat->Nisan atlanmis);")
    print("  arabam.com alternatif kaynagindan yalnizca FIYAT dolduruldu; talep_endeksi/")
    print("  satis_orani/dom bu ay icin NaN birakildi (uydurulmadi).")
    print(f"proxy_ilan_sayisi: TUM aylarda eksik (hicbir kaynak mutlak ilan sayisi yayimlamadi).")
    print()
    print(f"Ham tablo (tum cikarilan alanlar + kaynak izi): {ham_csv} , {ham_xlsx}")
    print()
    print("--- Ham proxy tablo (temel sutunlar) ---")
    print(df[["referans_ayi", "proxy_fiyat_cari_tl", "proxy_dom_gun", "kaynak", "kaynak_rapor_basligi"]].to_string(index=False))


if __name__ == "__main__":
    main()
