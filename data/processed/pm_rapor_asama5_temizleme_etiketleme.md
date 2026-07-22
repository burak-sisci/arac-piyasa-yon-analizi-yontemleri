# PM Raporu — Aşama 5: Temizleme ve Aylık Yön Etiketi Üretimi

**Tarih:** 2026-07-22
**Kapsam:** MVP 2025 veri setinin (Aşama 1-4'te çekilen USD/TRY, TÜFE, proxy
fiyat) temizlenmesi ve hedef değişkenin (aylık yön etiketi) üretilmesi.
**Yürüten:** Claude Code (bu oturum) — model eğitimi/tahmin YAPILMADI, yeni
kaynak çekilmedi.

---

## 1. Ne Yapıldı

Adım adım:

1. `scripts/veri/asama5_temizle_etiketle.py` oluşturuldu. Bu script Aşama 1-3'ün
   ham çıktılarını (`data/raw/usdtry_2025_aylik.csv`, `data/raw/tufe_2025_aylik.csv`,
   `data/raw/proxy_fiyat_2025_raw.csv`) okur; yeni kaynak çekmez.
2. **Proxy fiyat serisi tek kaynağa (BETAM sahibindex) sabitlendi.** 2025-02
   için BETAM'ın "Nisan 2025" raporunun tüm metni yeniden tarandı (yalnızca
   başlık paragrafı değil) — Şubat'a dair hiçbir sayı bulunamadı; BETAM arşiv
   sayfası da Şubat→Nisan atladığını doğruladı. Sonuç: `proxy_fiyat_cari_tl`
   (omurga) 2025-02'de NaN; arabam.com değeri ayrı bir referans sütununa
   (`proxy_fiyat_arabamcom_referans_tl`) alındı, omurgaya karıştırılmadı.
3. **Yıllık/aylık yüzde karışıklığı giderildi:** BETAM raporlarının metninde
   ay ay tutarsız biçimde verilen (bazen aylık, bazen yalnızca yıllık) değişim
   yüzdeleri KULLANILMADI; `proxy_nominal_aylik_pct`, `proxy_reel_aylik_pct`,
   `proxy_aylik_log_degisim`, `proxy_reel_aylik_log_degisim` 12 ayın tamamı
   için ham fiyat serisinden **yeniden ve tek yöntemle** hesaplandı.
4. **Hedef değişken üretildi:** oynaklık-uyarlamalı bant (`k=0.5` × sigma) ile
   `proxy_yon_nominal` ve `proxy_yon_reel` (TÜFE-deflate edilmiş); ayrıca
   karşılaştırma için tercile-tabanlı `proxy_yon_tercile`.
5. Çıktı: `data/processed/mvp_2025_etiketli.csv` (+ `.xlsx`) — **Git-dışı**
   (`.gitignore` gereği, yalnızca kod/belge versiyonlanır).
6. `data/processed/veri_sozlugu.md` güncellendi: yeni sütunlar + 4 zorunlu
   uyarı (a: hedef geçici/N1, b: 9 gözlemle sigma gürültülü, c: Şubat kaynak
   farkı, d: hedef hâlâ ilan fiyatı yönü/K8, işlem fiyatı değil).
7. `data/processed/temizleme_raporu.md` oluşturuldu (sınıf dağılımı + gözlemler
   + sıradaki adım önerisi).
8. Commit `431bb35` ("veri: temizleme ve aylık yön etiketi üretimi"), push
   edildi (`origin/main`).

---

## 2. Sayısal Özet

- **Tablo boyutu:** 12 satır × 23 sütun (`mvp_2025_etiketli.csv`).
- **Toplam eksik (NaN) hücre:** 38/276 (%13,8).
  - `proxy_ilan_sayisi`: 12/12 eksik (hiçbir kaynak mutlak sayı yayımlamıyor).
  - `proxy_fiyat_arabamcom_referans_tl`: 11/12 eksik (yalnızca 2025-02 dolu — beklenen).
  - `proxy_nominal_aylik_pct` / `proxy_reel_aylik_pct` / iki log-değişim sütunu: her biri 3/12 eksik (2025-01, 02, 03 — Şubat gapının yan etkisi).
  - `proxy_fiyat_cari_tl`, `proxy_dom_gun`, `proxy_satis_orani_pct`: her biri 1/12 eksik (2025-02).
  - Kalan tüm sütunlar (USD/TRY, TÜFE, etiketler, meta) 0 eksik.
- **Kaynak seviyeleri:** USD/TRY = A (TCMB EVDS3 API); TÜFE = A (TCMB EVDS3
  API); proxy fiyat = C (BETAM, 11 ay) + D (arabam.com, yalnızca referans, 1 ay).
- **Sınıf dağılımı (12 ay, "eksik" dahil):**

  | Etiket | up | stable | down | eksik |
  |---|---|---|---|---|
  | `proxy_yon_nominal` | 8 | 1 | 0 | 3 |
  | `proxy_yon_reel` | 1 | 6 | 2 | 3 |
  | `proxy_yon_tercile` | 3 | 3 | 3 | 3 |

  Kullanılan parametreler: `k=0.5`, `sigma_nominal=0.01251`, `sigma_reel=0.01235`
  (yalnızca 9 geçerli aylık geçiş üzerinden hesaplandı — 11 olası geçişten
  2'si Şubat gapı nedeniyle NaN).

---

## 3. Karşılaşılan Sorunlar (saklanmadı)

1. **BETAM'ın "{Ay} {Yıl}" başlık deseni, içerikte hep ÖNCEKİ ayı anlatıyor**
   (ör. "Şubat 2025" raporu → Ocak verisi). Bu, önceki aşamada (Aşama 3)
   keşfedilip doğrulanmıştı; bu aşamada `proxy_yayim_ayi` sütunu üzerinden
   korunuyor, yeniden bir sorun çıkarmadı — ama PM'in bilmesi için burada da
   not ediyorum çünkü bu aşamanın tüm log-değişim mantığı buna dayanıyor.
2. **BETAM 2025-02 için hiç rapor yayımlamamış** (gerçek yayın boşluğu, benim
   arama/erişim hatam değil — arşiv sayfasından teyit edildi). Bu, tek bir
   eksik ayın etikette **3 aya** (kendisi + iki komşu geçiş) yayılmasına yol
   açtı. Beklenmedik ve önemli bir etki: veri setinin dörtte biri (3/12 ay)
   tek bir kaynak boşluğu yüzünden etiketsiz kaldı.
3. **9 geçerli gözlemle sigma tahmini çok gürültülü.** Görev talimatı "~11
   değişim gözlemi" varsayıyordu; Şubat gapı nedeniyle gerçek sayı 9. Bunu
   varsaymadan, gerçek sayıyı raporladım (bkz. Bölüm 2).
4. **Nominal etiketin neredeyse tamamen "up" çıkması** (8/9 geçerli ay) ilk
   bakışta bir hata gibi görünebilir — ama kontrol ettim, bu gerçek bir
   bulgudur: 2025 boyunca TL enflasyonu/kur kaybı nominal fiyatı sürekli
   yukarı itmiş. Bunu "düzelteceğim" bir hata olarak ELE ALMADIM (uydurma
   olur); bunun yerine reel (TÜFE-deflate) etiketi ayrıca ürettim ve bu
   dengesizliği açıkça raporladım (`temizleme_raporu.md` Bölüm 3).
5. **`proxy_yon_tercile` sütunu tanım gereği her zaman 3/3/3 dengeli** —
   bu bir "iyi sonuç" değil, yöntemin matematiksel bir özelliğidir (tercile
   her zaman dengeler); bunu yanlışlıkla "başarı" gibi sunmamak için raporda
   açıkça "yalnızca karşılaştırma referansı" diye işaretledim.

---

## 4. Veri Örneği (ham, `mvp_2025_etiketli.csv`)

**İlk 3 satır:**

```
referans_ayi  usdtry_aysonu  tufe_endeks  proxy_fiyat_cari_tl  proxy_fiyat_arabamcom_referans_tl                     proxy_kaynak  proxy_aylik_log_degisim proxy_yon_nominal proxy_yon_reel proxy_yon_tercile
     2025-01       35.75320      2819.65             935136.0                                NaN                 BETAM sahibindex                      NaN             eksik          eksik             eksik
     2025-02       36.39795      2883.75                  NaN                           888689.0  eksik (BETAM rapor yayımlamadı)                      NaN             eksik          eksik             eksik
     2025-03       37.96650      2954.69             950515.0                                NaN                 BETAM sahibindex                      NaN             eksik          eksik             eksik
```

**Son 3 satır:**

```
referans_ayi  usdtry_aysonu  tufe_endeks  proxy_fiyat_cari_tl  proxy_fiyat_arabamcom_referans_tl     proxy_kaynak  proxy_aylik_log_degisim proxy_yon_nominal proxy_yon_reel proxy_yon_tercile
     2025-10       41.93775      3453.09            1086000.0                                NaN BETAM sahibindex                 0.026121                up         stable                up
     2025-11       42.40060      3482.96            1101000.0                                NaN BETAM sahibindex                 0.013718                up         stable            stable
     2025-12       42.90090      3513.87            1108000.0                                NaN BETAM sahibindex                 0.006338                up         stable              down
```

(Not: İlk 3 satırın `proxy_aylik_log_degisim` NaN olması iki farklı sebepten:
2025-01'in kendi öncesi — 2024-12 — hiç çekilmedi; 2025-02/03 ise Şubat gapı
yüzünden NaN.)

---

## 5. Varsayımlar ve Kararlar

| Karar | Bağlayıcı karara (K/N) uygun mu? | Not |
|---|---|---|
| Proxy fiyatı BETAM-only omurgaya sabitleme, arabam.com'u ayrı referans sütununda tutma | Görev talimatına birebir uygun ("omurga tek kaynak olmalı") | Doğrudan bir K/N maddesi değil, bu görevin kendi talimatı. |
| `k=0.5` eşik çarpanı | K2 ("oynaklık-uyarlamalı bant") ile uyumlu, ama K2 spesifik bir k değeri vermiyor | **Kendi inisiyatifim** — görev talimatındaki "Başlangıç k=0.5" önerisini aynen kullandım, parametrik bıraktım. |
| Tercile etiketin nominal log-değişim üzerinden hesaplanması (reel değil) | Görev net belirtmemişti hangi baz kullanılsın | **Kendi kararım** — "temel büyüklük" (nominal) ile tutarlı olsun diye. |
| `tufe_yayim_tarihi`'nin "yaklaşık" (takvim-3'ü) olarak işaretlenmesi | Aşama 2'den devralınan, önceden onaylı bir yaklaşım | Yeni bir karar değil. |
| Şubat'ın "eksik" bırakılıp uydurulmaması | Görev talimatına birebir uygun ("Eksik veriyi uydurma") | — |

---

## 6. Açık Sorular / PM Onayı Gereken Noktalar

1. **`k=0.5` eşiği kabul edilebilir mi?** Bu bir başlangıç değeri; farklı bir
   k, sınıf dağılımını (özellikle nominal etikette) önemli ölçüde değiştirir.
2. **Nihai hedef nominal mi, reel mi olacak?** Görev metninde de "sonra
   kararlaştırılır" denmişti — hâlâ açık. Bu MVP'de reel etiket daha dengeli
   çıktı ama 9 gözlemle bu gözlem kesin değil.
3. **3 ayın (2025-01, 02, 03) etiketsiz kalması kabul edilebilir mi**, yoksa
   BETAM'a doğrudan ulaşılıp Şubat verisi başka bir yoldan (ör. arşiv talebi)
   mi tamamlanmalı?
4. **Seriyi 2021-2024'e genişletme mi, yoksa ilk dışsal faktörü (ÖTV event)
   eklemek mi önceliklendirilsin?** (Önerim Bölüm 7'de — ama bu benim
   başlatacağım bir şey değil.)

---

## 7. Önerilen Sonraki Adım (yalnızca öneri — başlatılmadı)

**Seriyi 2021-2024'e genişletmek**, ilk dışsal faktörü (ÖTV event-dummy)
eklemekten önce gelmeli — çünkü mevcut 9 gözlemle üretilen her istatistik
(sigma, eşik, tercile sınırları) zaten kırılgan; üstüne yeni bir değişken
eklemek bu kırılganlığı çözmez, gizleyebilir. BETAM sahibindex Aralık
2023'ten beri yayımlanıyor; geriye doğru eklenirse gözlem sayısı ~20-24'e
çıkar.

**Bu adımı BEN BAŞLATMIYORUM — proje sahibi/PM onayı bekliyorum.**
