# Veri Sözlüğü — MVP 2025 Birleşik Tablo

Dosya: `data/processed/mvp_2025_birlesik.csv` (+ `.xlsx`)
Kapsam: 2025-01 — 2025-12, aylık, tek satır = tek ay (anahtar: `referans_ayi`).
Kaynak seviyeleri: A (resmi API) → B (resmi indirme) → C (resmi sayfa/PDF
çıkarımı) → D (ikincil güvenilir kaynak) → E (manuel giriş). Bkz.
`prompts/veri/01_mvp_cekirdek_veri_prompt.md`.

| Sütun | Birim | Kaynak | Seviye | Frekans | Yayım Gecikmesi | Bilinen Sınır |
|---|---|---|---|---|---|---|
| `referans_ayi` | YYYY-MM | — | — | Aylık | — | Birleştirme anahtarı. |
| `usdtry_aysonu` | TL/USD | TCMB EVDS3 (`TP.DK.USD.A`/`.S` ortalaması) | A | Günlük→aylık türetilmiş | Yok (günlük kur, gecikmesiz yayımlanır) | Ay-sonu son iş günü değeri; hafta sonu/tatil günleri NaN'dır ve ay-sonu hesaplanırken atlanır. |
| `usdtry_ortalama` | TL/USD | TCMB EVDS3 | A | Günlük→aylık türetilmiş (yerelde, pandas ile) | Yok | Ayın tüm iş günü gözlemlerinin ortalamasıdır; EVDS'in kendi aylık agregasyonu KULLANILMAMIŞTIR. |
| `tufe_endeks` | Endeks (2003=100) | TCMB EVDS3 (`TP.FG.J0`, TÜİK TÜFE) | A | Aylık (doğal) | ~3 iş günü (bkz. `tufe_yayim_tarihi`) | — |
| `tufe_aylik_degisim` | % | Yerelde türetilmiş (`tufe_endeks.pct_change()`) | A (türetilmiş) | Aylık | — | EVDS'in hazır "değişim" serisi KULLANILMAMIŞTIR; ham endeksten hesaplanmıştır. |
| `tufe_yayim_tarihi` | Tarih (YYYY-MM-DD) | Yerelde hesaplanmış | — | — | — | **YAKLAŞIKTIR**: referans ayını takip eden ayın takvim-3'ü (Faz 2 tarama bulgusu: "TÜFE ayın 3'ü"). EVDS gerçek yayım/vintage tarihini ayrı alan olarak döndürmez; hafta sonuna denk gelen aylarda gerçek resmi yayım 1-2 gün kayabilir. |
| `proxy_fiyat` | TL (cari, nominal) | BETAM sahibindex (11 ay) / arabam.com (yalnız 2025-02) | C / D | Aylık | Değişken (bkz. `proxy_yayim_ayi`) | **KRİTİK (karar N1): mix/kompozisyon düzeltmesizdir** — ham ortalama ilan fiyatıdır. MVP'de yer-tutucu hedef olarak kullanılır, NİHAİ HEDEF DEĞİLDİR. Nihai hedef ileride hedonik düzeltmeyle (N10) üretilecektir. |
| `proxy_ilan_sayisi` | Adet | — | — | — | — | **TÜM AYLARDA EKSİK.** Ne BETAM ne arabam.com bu veriyi mutlak sayı olarak yayımlıyor (yalnızca % değişim bazen verilir); uydurulmamış, NaN bırakılmıştır. |
| `proxy_dom` | Gün (ilanda kalma süresi / kapatılan ilan yaşı) | BETAM sahibindex | C | Aylık | Değişken | 2025-02 için **eksik** (o ay BETAM raporu hiç yayımlanmadı, arabam.com bu metriği yayımlamıyor). |
| `proxy_kaynak` | Metin | — | — | — | — | Hangi kaynaktan geldiğini gösterir (`BETAM sahibindex` veya arabam.com alternatif notu). |
| `proxy_kaynak_rapor` | Metin | — | — | — | — | Kaynak rapor/yazı başlığı (izlenebilirlik). Tam alıntılar ve URL'ler: `scripts/veri/asama3_proxy_fiyat.py` içindeki `KAYITLAR` listesi. |
| `proxy_yayim_ayi` | YYYY-MM | — | — | — | — | Kaynak raporun/yazının yayımlandığı ay (referans ayı DEĞİL). |

## Kritik keşif — BETAM yayım gecikmesi deseni (as-of date için önemli)

BETAM "sahibindex Otomobil Piyasası Görünümü" raporu **"{Ay} {Yıl}" başlığıyla
yayımlanır ama HEP bir önceki ayın verisini anlatır** (ör. "Şubat 2025" başlıklı
rapor Ocak 2025 fiyatını verir; "Ocak 2026" başlıklı rapor Aralık 2025 fiyatını
verir). Bu desen 2025-01'den 2025-12'ye kadar **11 rapor üzerinde doğrulanmıştır**
(her satırın birebir alıntısı `asama3_proxy_fiyat.py` içindedir). Bu yüzden
`referans_ayi` (verinin ait olduğu ay) ile `proxy_yayim_ayi` (raporun
yayımlandığı ay) bilinçli olarak ayrı sütunlardır — sızıntı riskini önlemek
için bir model bu veriyi yalnızca `proxy_yayim_ayi` geçtikten SONRA "bilinmiş"
sayabilir.

## Bilinen boşluk

**2025-02 (Şubat) için BETAM raporu hiç yayımlanmamıştır** (Şubat 2025 →
doğrudan Nisan 2025'e geçilmiş; BETAM'ın kendi kategori/arşiv sayfasında
doğrulanmıştır). Bu ay için alternatif kaynağa (arabam.com Aylık Fiyat Endeksi)
geçilmiş, yalnızca `proxy_fiyat` doldurulmuştur; `proxy_dom` bu ay için NaN'dır
(arabam.com bu metriği yayımlamaz) — uydurulmamıştır.

## Genel uyarı

Bu, **12 aylık bir MVP prototip veri setidir** — pipeline ve as-of-date
mimarisini test etmek içindir, **model eğitmek için değildir** (12 gözlem
eğitim için yetersizdir). Veri dosyalarının kendisi `.gitignore` gereği
Git-dışıdır; yalnızca bu sözlük, üretim kodu (`scripts/veri/`) ve
kaynak-arşiv promptları (`prompts/veri/`) versiyonlanır.
