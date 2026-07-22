# Temizleme Raporu — MVP 2025 (Aşama 5)

Kaynak kod: `scripts/veri/asama5_temizle_etiketle.py` (Aşama 1-3'ün ham
tablolarını okur; yeni kaynak çekmez, model eğitmez).

## 1. Şubat 2025 (proxy fiyat kaynak farkı) nasıl çözüldü

BETAM'ın "Nisan 2025" raporu (Şubat'tan sonraki ilk BETAM raporu) tüm metni
tarandı — sayfada Şubat'a ait hiçbir sayısal veri (tablo, grafik, revize seri)
bulunamadı; yalnızca Mart verisi var. BETAM'ın arşiv/kategori sayfası da
"Şubat 2025" → doğrudan "Nisan 2025" atladığını doğruladı: **BETAM bu ay için
hiç rapor yayımlamamış.**

Karar: `proxy_fiyat_cari_tl` (omurga) 2025-02 için **NaN** bırakıldı — arabam.com
değeri (888.689 TL) bu sütuna KARIŞTIRILMADI. Bunun yerine ayrı bir
`proxy_fiyat_arabamcom_referans_tl` sütununda (yalnızca bu ay için dolu)
saklandı. Sonuç: omurga tek kaynaklı (BETAM) kalır; arabam.com değeri
kaybolmaz, ama etikete karışmaz.

**Yan etki:** 2025-01→02 ve 2025-02→03 log-değişim geçişleri de bu yüzden NaN
oldu (bir ay eksik olunca komşu iki geçiş de tanımsızlaşır). Toplam 11 olası
aylık geçişten yalnızca **9'u geçerli**.

## 2. Yıllık/aylık yüzde karışması giderildi mi

Evet — ama rapor metninden ayıklama yoluyla değil, **yeniden hesaplama**
yoluyla. BETAM raporları ay ay tutarsız biçimde bazen aylık, bazen yalnızca
yıllık değişim veriyordu (ör. Ocak/Nisan/Mayıs raporlarında aylık reel değişim
açıkça vardı, Haziran sonrası raporlarda yoktu). Farklı ayların farklı
yöntemlerle (bazısı metinden, bazısı hesaplanarak) üretilmiş değerlerini aynı
sütunda karıştırmak yerine, **12 ayın tamamı için** `proxy_nominal_aylik_pct`,
`proxy_reel_aylik_pct` ve `proxy_aylik_log_degisim` doğrudan ham
`proxy_fiyat_cari_tl` serisinden yerelde ve tek bir tutarlı yöntemle
hesaplandı. Ham rapor metnindeki yıllık/aylık yüzdeler silinmedi —
`data/raw/proxy_fiyat_2025_raw.csv`'de kaynak alıntısıyla birlikte duruyor.

## 3. Kullanılan eşik ve sınıf dağılımı

Yöntem: oynaklık-uyarlamalı bant, `k = 0.5` (`sigma` = geçerli 9 aylık
log-değişimin standart sapması).

- **sigma (nominal):** 0.01251
- **sigma (reel):** 0.01235

| Etiket | up | stable | down | eksik |
|---|---|---|---|---|
| `proxy_yon_nominal` | 8 | 1 | 0 | 3 |
| `proxy_yon_reel` | 1 | 6 | 2 | 3 |
| `proxy_yon_tercile` | 3 | 3 | 3 | 3 |

**Gözlem:** Nominal etiket neredeyse hep "up" (8/9 geçerli ay) — bu, TL
enflasyonu/kur kaybının nominal fiyatı sürekli yukarı ittiğini, dolayısıyla
nominal bazda bir "yön sınıflandırması"nın bu ölçekte pek bilgilendirici
olmadığını gösteriyor (Faz 3/N6'nın öngördüğü tam da bu tür bir dengesizlik
riski). Reel (TÜFE ile deflate edilmiş) etiket çok daha dengeli (stable
ağırlıklı, 2 down, 1 up) — enflasyon etkisi arındırılınca gerçek fiyat
hareketinin çok daha "stable" göründüğünü gösteriyor. Tercile etiket, tanım
gereği her zaman dengelidir (yalnızca karşılaştırma referansı).

**Sonuç:** Bu MVP ölçeğinde (12 ay, 9 geçerli geçiş) **reel etiket nominal
etiketten daha bilgilendirici** görünüyor — nominal etiket, gerçek bir yön
sinyali değil çoğunlukla enflasyon trendini yakalıyor olabilir. Bu, tam veri
setinde (daha uzun pencere) yeniden test edilmesi gereken bir gözlemdir, kesin
bir sonuç değildir (9 gözlemle istatistiksel güç çok düşüktür — bkz. veri
sözlüğü uyarı b).

## 4. Yapılmayanlar (kapsam dışı, bilinçli)

- Yeni dışsal kaynak çekilmedi (ODMD, ÖTV, faiz vb. — sonraki aşama).
- Tam hedonik/mix düzeltmesi yapılmadı; yalnızca veri sözlüğünde uyarı olarak
  belirtildi (N1, N10 ileride ele alınacak).
- Model eğitilmedi, tahmin yapılmadı.
- Eksik veri (Şubat) uydurulmadı; NaN/"eksik" olarak bırakıldı.

## 5. Önerilen sıradaki adım

İki makul seçenek var:

1. **Seriyi genişlet (2021-2024):** 9 geçerli geçiş istatistiksel olarak çok
   zayıf (sigma tahmini gürültülü — veri sözlüğü uyarı b). BETAM sahibindex
   Aralık 2023'ten beri yayımlanıyor; geriye doğru 2024 (ve varsa 2023 sonu)
   ay ay eklenerek gözlem sayısı ~20-24'e çıkarılabilir, bu da eşik/sigma
   tahminini ciddi ölçüde sağlamlaştırır.
2. **İlk dışsal faktörü ekle (kur veya ÖTV event):** USD/TRY zaten çekili;
   bir sonraki mantıklı adım ÖTV event-dummy'sini (24 Temmuz 2025 düzenlemesi,
   Faz 2 bulgusu) tabloya eklemek ve nominal/reel etiketle görsel/korelasyon
   düzeyinde ilk ilişkiyi incelemektir.

Öneri: **(1)'i önce yapmak** daha temel — çünkü mevcut 9 gözlemle üretilen her
istatistik (sigma, tercile sınırları) zaten kırılgan; seri uzatılmadan yeni
dışsal değişken eklemek bu kırılganlığı gizleyebilir. Ama nihai karar proje
sahibine aittir.
