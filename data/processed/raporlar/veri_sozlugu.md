# Veri Sözlüğü — MVP 2025 Birleşik Tablo

İki dosya, iki aşama:
- `data/processed/mvp_2025_birlesik.csv` (+ `.xlsx`) — Aşama 4 çıktısı, ham
  birleştirme (üç kaynak, düzeltme yok).
- `data/processed/mvp_2025_etiketli.csv` (+ `.xlsx`) — **Aşama 5 çıktısı**,
  temizlenmiş + aylık yön etiketi eklenmiş sürüm. Aşağıdaki sözlük önce ortak
  temel sütunları, sonra Aşama 5'e özgü yeni sütunları ve zorunlu uyarıları
  açıklar.

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
| `proxy_fiyat` (yalnız `_birlesik`) | TL (cari, nominal) | BETAM sahibindex (11 ay) / arabam.com (yalnız 2025-02) | C / D | Aylık | Değişken (bkz. `proxy_yayim_ayi`) | **KRİTİK (karar N1): mix/kompozisyon düzeltmesizdir** — ham ortalama ilan fiyatıdır. MVP'de yer-tutucu hedef olarak kullanılır, NİHAİ HEDEF DEĞİLDİR. Nihai hedef ileride hedonik düzeltmeyle (N10) üretilecektir. **Not:** `_etiketli` tablosunda bu sütun `proxy_fiyat_cari_tl` (BETAM-only omurga) ve `proxy_fiyat_arabamcom_referans_tl` (yalnız referans) olarak İKİYE ayrılmıştır — bkz. Aşama 5 bölümü. |
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

## Aşama 5 — `mvp_2025_etiketli.csv` sütunları (temizleme + hedef değişken)

| Sütun | Birim | Nasıl üretildi | Bilinen sınır |
|---|---|---|---|
| `proxy_fiyat_cari_tl` | TL | **BETAM-only omurga.** `data/raw/proxy_fiyat_2025_raw.csv`'deki `proxy_fiyat_cari_tl`'den yalnızca `kaynak == "BETAM sahibindex"` satırları alınır. | 2025-02 için **NaN** (BETAM o ay rapor yayımlamadı — bkz. yukarıdaki "Bilinen boşluk"). Ayrıca seri **2024-12 taban içermez** (yalnızca 2025 çekildi), bu yüzden 2025-01'in kendi log-değişimi de tanımsızdır (NaN). |
| `proxy_fiyat_arabamcom_referans_tl` | TL | arabam.com'dan (yalnızca 2025-02) — **karşılaştırma amaçlı, omurgaya karıştırılmaz.** | Yalnızca 2025-02'de dolu, diğer aylarda NaN. |
| `proxy_kaynak` | Metin | `"BETAM sahibindex"` veya `"eksik (BETAM rapor yayımlamadı)"`. | — |
| `proxy_nominal_aylik_pct`, `proxy_reel_aylik_pct` | % | **TÜM aylar için `proxy_fiyat_cari_tl` (nominal) / TÜFE'ye bölünmüş gösterge (reel) üzerinden yerelde `pct_change()` ile hesaplandı** — rapor metnindeki (bazen yıllık, bazen aylık, ay bazında tutarsız biçimde verilen) hazır yüzdeler KULLANILMADI. Ham metin-kaynaklı yıllık/aylık değerler `data/raw/proxy_fiyat_2025_raw.csv`'de saklıdır, silinmedi. | 2025-01→02 ve 02→03 geçişleri NaN (yukarıdaki gibi). |
| `proxy_aylik_log_degisim`, `proxy_reel_aylik_log_degisim` | log-oran | `ln(x_t / x_{t-1})`; sırasıyla nominal ve reel (TÜFE-deflate edilmiş) cari fiyattan. **Hedef değişkenin temel büyüklüğü budur.** | Aynı NaN deseni. |
| `proxy_yon_nominal`, `proxy_yon_reel` | up / stable / down / eksik | Oynaklık-uyarlamalı bant: `sigma` = geçerli log-değişimlerin std sapması; `|log_değişim| < k·sigma` → stable, aksi halde işarete göre up/down. | **(b) 12 gözlemle (gerçekte yalnızca 9 geçerli geçiş) sigma tahmini gürültülüdür — bu bir prototiptir, gerçek seride segment-bazlı ve daha uzun pencereyle yeniden kalibre edilecektir.** |
| `proxy_yon_tercile` | down / stable / up / eksik | Geçerli log-değişimler 3 eşit dilime (`pd.qcut`) bölünür. | Yapı gereği tam dengeli (3/3/3); yalnızca karşılaştırma amaçlıdır. |
| `kullanilan_esik_k` | sayı | Sabit, bu koşuda `0.5` (script başında parametrik). | — |
| `kullanilan_sigma_nominal`, `kullanilan_sigma_reel` | sayı | Bu koşuda hesaplanan std sapma değerleri (tüm satırlarda aynı — seri-geneli tek değer). | 9 gözlemle hesaplandı (bkz. b). |

### Zorunlu uyarılar

**(a) Hedef geçicidir (karar N1).** `proxy_fiyat_cari_tl` mix/kompozisyon
düzeltmesizdir (ham ortalama ilan fiyatı). Bu aşamada tam hedonik düzeltme
YAPILMAMIŞTIR — bu, sonraki bir aşamanın (N10) işidir. `proxy_yon_*` etiketleri
bu düzeltilmemiş fiyattan türetildiği için **geçicidir**; hedonik düzeltme
sonrası muhtemelen değişecektir.

**(b) 12 gözlem (gerçekte 9 geçerli geçiş) ile sigma/eşik gürültülüdür.** Bu bir
prototiptir; istatistiksel güç çok düşüktür. Tek bir aykırı ay bile sigma'yı ve
dolayısıyla tüm etiketleri önemli ölçüde değiştirebilir.

**(c) Şubat kaynak farkı.** BETAM 2025-02 için rapor yayımlamadı. `proxy_fiyat_cari_tl`
bu ay için bilinçli olarak NaN bırakıldı (omurga tek kaynak kalsın diye);
arabam.com değeri yalnızca ayrı bir referans sütununda tutuldu. Sonuç: 2025-02
için hedef etiket YOK ("eksik"), ayrıca 2025-01→02 ve 02→03 geçişleri de bu
yüzden NaN'dır (toplamda 3 ay "eksik" etiketli).

**(d) Hedef henüz "ilan fiyatı yönü"dür (K8), işlem fiyatı DEĞİL.** Bu proxy,
gerçekleşen satış fiyatının değil, kamuya açık ilan fiyatının yönünü ölçer;
K8+N9 kritik varsayımı (Faz 8/N13) bu MVP'de test edilmemiştir.

## Genel uyarı

Bu, **12 aylık bir MVP prototip veri setidir** — pipeline ve as-of-date
mimarisini test etmek içindir, **model eğitmek için değildir** (12 gözlem
eğitim için yetersizdir). Veri dosyalarının kendisi `.gitignore` gereği
Git-dışıdır; yalnızca bu sözlük, üretim kodu (`scripts/veri/`) ve
kaynak-arşiv promptları (`prompts/veri/`) versiyonlanır.
