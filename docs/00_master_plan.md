---
doküman_tipi: master_plan
proje: "Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması"
tarih: 2026-07-13
durum: tamamlandi 
kapsam: "Literatür taramasının faz yapısı, sıralaması, çıktı standartları ve kalite kriterleri. Bu dökümanda kaynak taraması YAPILMAMIŞTIR."
---

# Master Plan: Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması

## 0. Genel Yaklaşım ve Gerekçe Özeti

Bu tarama **8 faza** bölünmüştür. Aday listedeki (a)-(h) konularının hepsi korunmuştur; hiçbiri birleştirilmemiştir, çünkü her biri farklı bir arama stratejisi, farklı bir kaynak türü ve farklı bir "kapsam dışı" sınırı gerektiriyor:

- **(b) Finansal piyasa yön tahmini** ile **(c) araç fiyat tahmini akademik literatürü** birleştirilseydi, olgun bir alanın (borsa/kripto) metodolojik derinliği ile dar ve çoğunlukla regresyon-odaklı bir alanın (araç fiyatı) bulguları aynı dökümanda karışırdı. Bunlar ayrı fazlar olarak tutulmalı; biri "yöntem ithalatı", diğeri "domain gerçekliği" sağlıyor.
- **(d) Feature engineering** ile **(g) araç piyasasına özgü dinamikler** de ayrı tutulmalıdır: (g) *neyin* fiyatı etkilediğini (ekonomik/yapısal sebep-sonuç), (d) ise bu bilgiyi *nasıl* ölçülebilir bir feature'a çevireceğimizi ele alır. Karıştırılırsa, ya iktisadi gerekçe kaybolur ya da teknik uygulanabilirlik.
- **(h) Başarısızlık modları/tuzaklar** ayrı bir faz olarak sona bırakılmıştır çünkü bu bir "kırmızı takım" (red-team) fazıdır — önceki 7 fazın bulgularını sızıntı/yanlılık riski açısından geriye dönük denetler. Erken yapılırsa denetleyecek bir şey olmaz.

Sıralama, aday listedeki a→h harf sırasından **farklıdır**; bağımlılık grafiğine göre yeniden düzenlenmiştir (Bölüm 3'te gerekçelendirilmiştir). Aşağıdaki tablo harf→faz-no eşlemesini gösterir (izlenebilirlik için):

| Faz No | Aday Madde | Faz Adı |
|---|---|---|
| Faz 1 | (a) | Problem Çerçeveleme ve Label Tasarımı |
| Faz 2 | (g) | Araç Piyasasına Özgü Dinamikler |
| Faz 3 | (b) | Finansal Piyasa Yön Tahmini Literatürü |
| Faz 4 | (c) | Araç Fiyat Tahmini Akademik Literatürü |
| Faz 5 | (d) | Feature Engineering ve Alternatif Veri Kaynakları |
| Faz 6 | (e) | Model Mimarileri ve Ensemble Stratejileri |
| Faz 7 | (f) | Validasyon, Metrik Seçimi, Backtest Metodolojisi |
| Faz 8 | (h) | Başarısızlık Modları, Tuzaklar, Data Leakage Riskleri |

---

## 1. Faz Listesi

| Faz | Amaç (tek cümle) | Bağımlılık |
|---|---|---|
| 1. Problem Çerçeveleme ve Label Tasarımı | "up/down/stable" tanımını, ufku ve threshold'u literatüre dayandırmak | — |
| 2. Araç Piyasasına Özgü Dinamikler | Fiyatı etkileyen yapısal/makro faktörleri çıkarmak | Faz 1 |
| 3. Finansal Piyasa Yön Tahmini Literatürü | Olgun bir alandan transfer edilebilir metodoloji dersleri çıkarmak | Faz 1 |
| 4. Araç Fiyat Tahmini Akademik Literatürü | Doğrudan domain literatüründen feature/yöntem çıkarmak | Faz 1 |
| 5. Feature Engineering ve Alternatif Veri | Faz 2/3/4 bulgularını somut feature adaylarına çevirmek | Faz 2, 3, 4 |
| 6. Model Mimarileri ve Ensemble | En uygun model ailesini literatürden belirlemek | Faz 1, 5 |
| 7. Validasyon, Metrik, Backtest | Sızıntısız değerlendirme protokolü tasarlamak | Faz 1, 6 |
| 8. Başarısızlık Modları ve Tuzaklar | Tüm fazları risk/leakage açısından denetlemek | Faz 1-7 |

**Neden 8 ve neden 5-6 değil:** Ekip ileri seviye olduğu için temel ML/istatistik tekrarına yer yok — bu, her fazın çok dar ve derin olmasını, dolayısıyla fazların birbirine karışmamasını gerektiriyor. Daha az sayıda geniş faz (örn. "veri ve modelleme" gibi tek bir faz), her biri farklı arama stratejisi gerektiren bu 8 alt-konuyu tek dökümanda toplayıp hem aranabilirliği hem de "tamamlandı" tanımını bulanıklaştırırdı.

---

## 2. Faz Detayları

### Faz 1 — Problem Çerçeveleme ve Label Tasarımı

**Amaç ve Kapsam**
Yön sınıflandırması probleminin (kaç sınıf, hangi ufuk, "stable" bandı nasıl tanımlanır) literatürdeki en iyi pratiklerle netleştirilmesi. *Dahil:* label taksonomileri (2-sınıf/3-sınıf/quantile-tabanlı), threshold belirleme yöntemleri (sabit, oynaklığa-göre-uyarlanmış, istatistiksel testli), meta-labeling yaklaşımları, farklı ufuklarda etiketleme karşılaştırmaları. *Hariç:* genel sınıflandırma algoritmaları (Faz 6), genel feature engineering (Faz 5), spesifik model implementasyonu.
*Gerekçe:* Bu faz ilk sırada olmalı çünkü aşağıdaki her fazın "ne aradığı" (yön tahmini mi, regresyon mu, kaç sınıf) bu fazın çıktısına bağlı.

**Anahtar Kelimeler**
EN: `price direction classification`, `triple barrier labeling`, `threshold selection financial time series classification`, `multi-class stable up down labeling`, `meta-labeling`
TR: `fiyat yönü sınıflandırma`, `zaman serisi etiketleme yöntemi`, `eşik değeri seçimi fiyat tahmini`, `üç sınıflı fiyat tahmini`

**Çıktı Başlık İskeleti**
1. Giriş ve Problem Tanımı
2. Label Taksonomileri (2/3/N-sınıf karşılaştırması)
3. Threshold/Bant Belirleme Yöntemleri
4. Tahmin Ufku Seçimi ve Trade-off'lar
5. Class Imbalance – Label Tasarımı Etkileşimi
6. Meta-Labeling ve Alternatif Yaklaşımlar
7. Projeye Uygulanabilirlik Notları
8. Kaynakça

**Bağımlılık:** Yok (başlangıç fazı)

**Derinlik:** 12-18 kaynak. Öncelik: peer-reviewed finansal ML makaleleri, yüksek atıflı working paper'lar (arXiv q-fin, SSRN), ileri düzey kitap bölümleri. Blog/tutorial içerik hariç.

---

### Faz 2 — Araç Piyasasına Özgü Dinamikler

**Amaç ve Kapsam**
Araç fiyatlarını (özellikle Türkiye ikinci el/yeni araç piyasası) etkileyen yapısal/makro faktörlerin literatür ve sektör raporlarından çıkarılması. *Dahil:* kur geçişkenliği, vergi politikası şokları (ÖTV/MTV), arz şokları (çip krizi, üretim kesintileri), EV geçişinin İYA residual value'suna etkisi, Türkiye'ye özgü kurumsal veri kaynakları. *Hariç:* genel makroekonomi teorisi (temel bilgi), feature mühendisliği teknikleri (Faz 5).
*Gerekçe:* Label tasarımı (Faz 1) genellikle "kaç sınıf/hangi ufuk" sorusuna soyut/metodolojik cevap verir; bu fazın amacı o kararı **iktisadi olarak anlamlı** hale getirmek (örn. threshold, araç piyasasının tipik oynaklığını yansıtmalı). Bu yüzden Faz 1'den hemen sonra gelir.

**Not (staj bağlamı):** Projeniz Arabam.com'daki stajınızla örtüşüyorsa, bu fazda Arabam.com'un kamuya açık "Fiyat Endeksi" gibi yayınları doğal bir birincil kaynak adayı olarak değerlendirilebilir — bunu aşağıda açık nokta olarak da işaretliyorum.

**Anahtar Kelimeler**
EN: `used car price exchange rate pass-through`, `automotive supply shock chip shortage price effect`, `EV transition used car residual value`, `vehicle tax policy price impact`
TR: `ikinci el araç fiyat kur etkisi`, `ÖTV değişikliği araç fiyatı`, `çip krizi araç fiyatları`, `elektrikli araç geçişi ikinci el fiyat`, `Türkiye otomotiv arz talep`

**Çıktı Başlık İskeleti**
1. Giriş: Araç Piyasasının Kendine Özgü Yapısı
2. Kur Geçişkenliği ve İthal Girdi Etkisi
3. Vergi Politikası Şokları ve Fiyat Sıçramaları
4. Arz Şokları ve Gecikmeli Etkiler
5. EV Geçişi ve İYA Residual Value Dinamiği
6. Türkiye'ye Özgü Kurumsal Veri Kaynakları (ODMD, OSD, TÜİK, sektör fiyat endeksleri)
7. Projeye Uygulanabilirlik: Dinamik → Feature/Label Eşlemesi
8. Kaynakça

**Bağımlılık:** Faz 1 (label ufku/threshold ile birlikte okunmalı)

**Derinlik:** 10-15 kaynak. Öncelik: sektör raporları (ODMD, OSD, JATO Dynamics, TCMB), akademik kur geçişkenliği makaleleri; güncel şok haberleri yalnızca destekleyici olarak.

---

### Faz 3 — Finansal Piyasa Yön Tahmini Literatürü (hisse/kripto/emtia)

**Amaç ve Kapsam**
En olgun alandan transfer edilebilir metodolojik dersleri çıkarmak. *Dahil:* yön sınıflandırma çalışmaları, sınıflandırma-vs-regresyon-sonra-eşikleme tartışması, feature aileleri (teknik/temel/sentiment/mikroyapı), backtest overfitting/p-hacking eleştirileri, finansal piyasalar ile araç piyasası arasındaki yapısal farkların (likidite, işlem sıklığı, mikroyapı yokluğu) transfer edilebilirliğe etkisi. *Hariç:* genel derin öğrenme mimarisi açıklamaları (temel bilgi), araç-özgü literatür (Faz 4).
*Gerekçe:* Bu alan en çok yayına sahip olduğu için hem en fazla metodolojik olgunluğu hem de en fazla "sahte başarı" riskini taşıyor — dolayısıyla overfitting eleştirisi bu fazın zorunlu bir alt-başlığı.

**Anahtar Kelimeler**
EN: `stock price direction prediction machine learning`, `cryptocurrency price movement classification`, `commodity price direction forecasting`, `financial machine learning overfitting backtest`, `market microstructure direction prediction`
TR: `borsa yön tahmini makine öğrenmesi`, `kripto fiyat yönü tahmini`, `finansal makine öğrenmesi backtest overfitting`

**Çıktı Başlık İskeleti**
1. Giriş ve Alanın Olgunluk Seviyesi
2. Yön Sınıflandırma Yaklaşımları (Sınıflandırma vs. Regresyon-Sonrası-Eşikleme)
3. En Sık Kullanılan Feature Aileleri
4. Backtest Overfitting ve p-hacking Eleştirileri
5. Yapısal Farklar: Finansal Piyasalar vs. Araç Piyasası (Transfer Edilebilirlik)
6. Projeye Aktarılabilir Somut Dersler
7. Kaynakça

**Bağımlılık:** Faz 1

**Derinlik:** 15-20 kaynak (en geniş taranacak faz). Öncelik: yüksek atıflı akademik makaleler + metodolojik eleştiri makaleleri; ticari "trading strategy" blog içerikleri hariç.

---

### Faz 4 — Araç Fiyat Tahmini Akademik Literatürü

**Amaç ve Kapsam**
Doğrudan araç fiyat tahmini üzerine yapılmış akademik çalışmaları taramak. *Dahil:* ikinci el araç fiyat tahmini (çoğunlukla regresyon), hedonik fiyatlama modelleri, amortisman/residual value modelleri, bu regresyon-odaklı çalışmaların yön tahminine adaptasyon potansiyeli. *Hariç:* genel finansal piyasa çalışmaları (Faz 3), feature üretim tekniklerinin detayı (Faz 5 — burada sadece *hangi* feature'ların önemli çıktığı not edilir).
*Gerekçe:* Bu alan neredeyse tamamen regresyon (fiyat seviyesi) odaklı; yön sınıflandırmasına doğrudan uygulanabilir çalışma azdır. Bu fazın en kritik alt-başlığı "regresyondan sınıflandırmaya adaptasyon boşluğu" analizidir — literatürün *olmadığı* yerleri de belgelemek, var olan bulgular kadar değerlidir.

**Anahtar Kelimeler**
EN: `used car price prediction machine learning`, `hedonic price model automobile`, `vehicle depreciation prediction model`
TR: `ikinci el araç fiyat tahmini`, `araç fiyatı hedonik model`, `araç değer kaybı tahmini`

**Çıktı Başlık İskeleti**
1. Giriş: Alanın Regresyon-Ağırlıklı Doğası
2. Hedonik Fiyatlama Modelleri ve Öne Çıkan Feature'lar
3. ML Tabanlı Fiyat Tahmini Çalışmaları (yöntem karşılaştırması)
4. Amortisman/Residual Value Modelleri
5. Regresyondan Yön Sınıflandırmasına Adaptasyon: Metodolojik Boşluk Analizi
6. Projeye Uygulanabilirlik Notları
7. Kaynakça

**Bağımlılık:** Faz 1

**Derinlik:** 10-15 kaynak. Öncelik: peer-reviewed makaleler (transportation research, applied economics dergileri); tezler dikkatli değerlendirilerek dahil edilebilir; sektör beyaz kağıtları düşük öncelik.

---

### Faz 5 — Feature Engineering ve Alternatif Veri Kaynakları

**Amaç ve Kapsam**
Faz 2/3/4'ten çıkan bulguları somut feature aday listesine çevirmek. *Dahil:* lag/gecikme yapıları, ilan-bazlı sinyaller (ilan sayısı/talep proxy'si, fiyat revizyon sıklığı), sentiment/haber/arama trendi entegrasyonu, bu probleme özgü feature seçim/boyut indirgeme bulguları. *Hariç:* genel "feature engineering nasıl yapılır" temel bilgisi, model mimarisi (Faz 6).
*Gerekçe:* Bu faz üç fazın (2/3/4) kesişiminde oturur — domain bilgisi (2), olgun-alan tekniği (3) ve domain-literatürü feature ipuçları (4) burada somut bir feature listesine damıtılır. Bu üçü tamamlanmadan bu faza başlamak, temelsiz bir feature listesi üretme riski taşır.

**Anahtar Kelimeler**
EN: `alternative data price prediction`, `search trends price forecasting`, `listing data used car market signal`, `lag feature engineering time series price`
TR: `alternatif veri fiyat tahmini`, `ilan verisi talep sinyali`, `arama trendi fiyat tahmini`

**Çıktı Başlık İskeleti**
1. Giriş ve Feature Kategorileri Taksonomisi
2. Klasik Feature Aileleri (Faz 3/4'ten Devralınanlar)
3. İlan-Bazlı ve Pazar-Yeri-Özgü Sinyaller
4. Alternatif Veri: Arama Trendleri, Sentiment, Haber Akışı
5. Lag/Gecikme Yapıları ve Zaman Penceresi Seçimi
6. Feature Seçimi/Boyut İndirgeme: Bu Probleme Özgü Bulgular
7. Projeye Uygulanabilirlik: Öncelikli Feature Listesi (Taslak)
8. Kaynakça

**Bağımlılık:** Faz 2, Faz 3, Faz 4

**Derinlik:** 12-18 kaynak. Öncelik: uygulamalı akademik makaleler + veri sağlayıcı teknik raporları.

---

### Faz 6 — Model Mimarileri ve Ensemble Stratejileri

**Amaç ve Kapsam**
Yön sınıflandırması için hangi model ailelerinin bu tarz orta-boyut, tablo+zaman-serisi karışık veri setlerinde iyi performans gösterdiğini belirlemek. *Dahil:* GBM vs. derin sekans model karşılaştırmaları (tabular data'da GBM'in DL'i yendiği literatür — ileri düzey tartışma), ensemble/stacking stratejileri, class imbalance'a model-seviyesi çözümler, confidence/uncertainty-aware tahmin. *Hariç:* model eğitim temelleri (hyperparameter tuning 101 vb.), feature engineering (Faz 5).
*Gerekçe:* Model seçimi hem problem tipine (Faz 1) hem de mevcut feature zenginliğine (Faz 5 — örn. zengin sekans verisi varsa sequence model mantıklı, tabular ise GBM) bağlı olduğu için bu iki fazdan sonra gelir.

**Anahtar Kelimeler**
EN: `gradient boosting vs deep learning tabular data`, `ensemble stacking financial classification`, `class imbalance time series classification`, `confidence-aware classification financial prediction`
TR: `tablo veri gradient boosting derin öğrenme karşılaştırma`, `ensemble model finansal sınıflandırma`, `sınıf dengesizliği zaman serisi sınıflandırma`

**Çıktı Başlık İskeleti**
1. Giriş: Problem Tipine Uygun Model Ailesi Seçimi
2. GBM vs. Sekans Modelleri: Karşılaştırmalı Bulgular
3. Transformer-Tabanlı Zaman Serisi Sınıflandırma Yaklaşımları
4. Ensemble/Stacking Stratejileri (Probleme Özgü)
5. Class Imbalance'a Model-Seviyesi Çözümler
6. Confidence/Uncertainty-Aware Tahmin Yaklaşımları
7. Projeye Uygulanabilirlik: Önerilen Baseline Model Ailesi
8. Kaynakça

**Bağımlılık:** Faz 1, Faz 5 (dolaylı olarak Faz 3)

**Derinlik:** 15-20 kaynak. Öncelik: son 3-5 yıla ait karşılaştırmalı benchmark çalışmaları.

---

### Faz 7 — Validasyon, Metrik Seçimi, Backtest Metodolojisi

**Amaç ve Kapsam**
Zaman serisi doğasından kaynaklanan validasyon tuzaklarını önleyecek metrik/backtest tasarımını netleştirmek. *Dahil:* walk-forward/purged/embargoed CV, sınıflandırma metriklerinin yön tahmininde yorumlanması ("stable" sınıfının değerlendirmedeki payı, accuracy'nin yanıltıcılığı), ekonomik/karar-odaklı değerlendirme metrikleri. *Hariç:* genel istatistik/ML metrik tanımları (temel bilgi), model mimarisi.
*Gerekçe:* Hangi validasyon protokolünün gerekli olduğu, hangi modellerin kullanılacağına (Faz 6 — örn. sekans modelleri farklı bir CV şeması gerektirebilir) bağlı olduğu için Faz 6'dan sonra gelir.

**Anahtar Kelimeler**
EN: `purged cross validation financial time series`, `walk forward validation backtest`, `classification metrics imbalanced financial prediction`, `economic significance forecast evaluation`
TR: `zaman serisi çapraz doğrulama sızıntı`, `backtest metodolojisi finansal tahmin`, `dengesiz sınıf değerlendirme metrikleri`

**Çıktı Başlık İskeleti**
1. Giriş: Neden Standart K-Fold CV Yetersiz
2. Walk-Forward / Purged / Embargoed CV Yöntemleri
3. Sınıflandırma Metriklerinin Yön Tahmini Bağlamında Yorumlanması
4. "Stable" Sınıfının Değerlendirmeye Etkisi
5. Ekonomik/Karar-Odaklı Değerlendirme Metrikleri
6. Backtest Tasarımı: Önerilen Protokol Taslağı
7. Projeye Uygulanabilirlik Notları
8. Kaynakça

**Bağımlılık:** Faz 1, Faz 6

**Derinlik:** 12-15 kaynak. Purged CV literatürü dar ve az sayıda otoriter kaynağa sahiptir — bunların mutlaka bulunması önceliklidir.

---

### Faz 8 — Başarısızlık Modları, Tuzaklar, Data Leakage Riskleri

**Amaç ve Kapsam**
Önceki tüm fazları "kırmızı takım" gözüyle gözden geçirip bu spesifik projede en sık karşılaşılacak hata kaynaklarını tek bir checklist'te toplamak. *Dahil:* klasik finansal ML leakage türleri (target/temporal leakage), ilan verisine özgü tuzaklar (duplicate listing, asking price vs. transaction price karışıklığı, mevsimsellik confound'u), literatürde raporlanan başarısız yaklaşımların meta-analizi. *Hariç:* yeni metodolojik öneriler (bunlar Faz 5-6-7'de zaten yapıldı) — burada yalnızca risk tespiti var.
*Gerekçe:* Bu faz tanım gereği sona bırakılmalı; denetleyecek bir "önceki bulgu" seti olmadan risk analizi yapılamaz.

**Anahtar Kelimeler**
EN: `data leakage financial machine learning`, `survivorship bias price prediction`, `asking price vs transaction price bias`, `common pitfalls market prediction models`
TR: `veri sızıntısı finansal makine öğrenmesi`, `hayatta kalma yanlılığı fiyat tahmini`, `ilan fiyatı işlem fiyatı farkı`

**Çıktı Başlık İskeleti**
1. Giriş: Neden Ayrı Bir Tuzaklar Fazı
2. Klasik Data Leakage Türleri ve Bu Projedeki Karşılıkları
3. İlan/Pazar Verisi Özgü Tuzaklar
4. Survivorship ve Selection Bias Riskleri
5. Literatürdeki Başarısız Yaklaşımların Meta-Analizi
6. Kapsamlı Risk Checklist'i (Faz 1-7 Çapraz Referanslı)
7. Kaynakça

**Bağımlılık:** Faz 1-7 (tümü)

**Derinlik:** 10-12 kaynak + tüm önceki fazların bulgu özetleri. Öncelik: metodoloji eleştirisi makaleleri, post-mortem/vaka analizleri.

---

## 3. Faz Sıralaması ve Gerekçesi

```
Aşama 1:  Faz 1 (solo, zorunlu ilk adım)
              │
Aşama 2:  ┌───┼───┐
          Faz 2  Faz 3  Faz 4     ← birbirinden bağımsız, paralel/istenilen sırada yapılabilir
          └───┼───┘
Aşama 3:      Faz 5              ← Aşama 2'nin üçünü de gerektirir
              │
Aşama 4:      Faz 6
              │
Aşama 5:      Faz 7
              │
Aşama 6:      Faz 8               ← sentez/kırmızı-takım, tüm fazları gerektirir
```

**Neden bu sıra:**
- Faz 1 zorunlu ilk adımdır: "ne arıyoruz" tanımlanmadan hiçbir arama stratejisi anlamlı olmaz.
- Faz 2/3/4 birbirine bağımlı değildir — biri domain (2), biri metodoloji-ithalatı (3), biri domain-literatürü (4) sağlar. Tek kişilik bir çalışmada bile sıraları değiştirilebilir; birden fazla kişi çalışıyorsa gerçek paralellik mümkündür.
- Faz 5, Aşama 2'nin üçünü de gerektirir çünkü feature listesi hem domain bilgisine hem olgun-alan tekniğine hem domain-literatürü ipuçlarına dayanır — eksik girdiyle yapılırsa temelsiz bir feature listesi ortaya çıkar.
- Faz 6, Faz 5'in feature yapısını bilmeden anlamlı model seçimi yapamaz (örn. zengin sekans verisi vs. sade tablo verisi farklı model ailelerini gerektirir).
- Faz 7, Faz 6'nın hangi modellerin kullanılacağını bilmeden uygun validasyon şemasını tasarlayamaz.
- Faz 8 tanım gereği son adımdır — denetleyecek bir bulgu seti gerektirir.

---

## 4. Dosya ve İsimlendirme Standardı

**Dosya adlandırma şeması:** `NN_faz_adi_kisa.md` (NN = yürütme sırasına göre 01-08, iki haneli, sıfır dolgulu)

```
00_master_plan_literatur_taramasi.md   (bu döküman)
01_problem_cerceveleme_label_tasarimi.md
02_arac_piyasasi_dinamikleri.md
03_finansal_piyasa_yon_tahmini.md
04_arac_fiyat_akademik_literatur.md
05_feature_engineering_alternatif_veri.md
06_model_mimarileri_ensemble.md
07_validasyon_metrik_backtest.md
08_basarisizlik_modlari_tuzaklar.md
09_sentez_ve_karar_dokumani.md          (Bölüm 6'da tanımlanan sentez çıktısı)
```

*Gerekçe:* Numaralandırma orijinal a-h harf sırasını değil, **yürütme sırasını** yansıtır (bkz. Bölüm 0'daki eşleme tablosu) — böylece dosya listesi klasörde açıldığında doğrudan doğru okuma sırasını gösterir.

**Standart metadata bloğu** (her faz dökümanının başına YAML front-matter olarak eklenecek):

```yaml
---
faz_no: 01
faz_adi: "Problem Çerçeveleme ve Label Tasarımı"
tarih: 2026-07-13
kapsam_ozeti: "Yön sınıflandırması için label taksonomisi, threshold ve ufuk seçimi"
bagimli_oldugu_fazlar: []
durum: taslak            # taslak | inceleniyor | tamamlandi
hedef_kaynak_sayisi: 15
gerceklesen_kaynak_sayisi: 0
son_guncelleme: 2026-07-13
---
```

*Gerekçe:* `bagimli_oldugu_fazlar` alanı sayesinde bir faz güncellendiğinde hangi diğer fazların gözden geçirilmesi gerektiği otomatik olarak izlenebilir (örn. Faz 1 revize edilirse, `bagimli_oldugu_fazlar: [01]` içeren tüm dosyalar işaretlenir).

---

## 5. Kalite Kriterleri (Faz "Tamamlandı" Kontrol Listesi)

Bir faz çıktısı, aşağıdakilerin **hepsi** sağlanmadan `tamamlandi` durumuna geçemez:

- [ ] Her somut iddia en az bir kaynağa atıfla destekleniyor (yazar/kurum + yıl, mümkünse DOI/link).
- [ ] İçerik, ekibin zaten bildiği temel ML/istatistik bilgisini tekrarlamıyor (varsa çıkarılmış).
- [ ] Her ana bulgu bölümünün altında somut, aksiyon alınabilir bir "Projeye Uygulanabilirlik" notu var.
- [ ] Kaynak çeşitliliği yeterli — tek tip kaynağa (örn. yalnızca blog) dayanmıyor.
- [ ] Çelişkili bulgular varsa açıkça işaretlenmiş, tek taraflı sunulmamış.
- [ ] İçerik, fazın tanımlanmış kapsamının dışına taşmıyor (scope creep kontrolü).
- [ ] Arama stratejisi (anahtar kelimeler) dökümanda şeffaf şekilde belirtilmiş (tekrarlanabilirlik için).
- [ ] Önceki fazlarla çelişen bir bulgu varsa bu açıkça çapraz-referanslanmış.
- [ ] Metadata bloğu eksiksiz doldurulmuş, `durum` alanı güncel.

*Gerekçe:* Bu liste, "kaynak sayısı" gibi niceliksel bir hedeften çok, ekibin ileri seviyesine uygun **niteliksel titizliği** (temel bilgi sızmaması, çelişkilerin gizlenmemesi, uygulanabilirliğin somut olması) garanti altına almak için tasarlandı.

---

## 6. Sentez ve Sunum Planı

Tüm fazlar tamamlandığında iki çıktı üretilecek:

**A. Sentez Dökümanı (`09_sentez_ve_karar_dokumani.md`) — İskelet:**
1. Yönetici Özeti (karar vericiler için, 1 sayfa)
2. Problem Tanımı ve Nihai Label Kararı (Faz 1+2 sentezi)
3. Metodolojik Temel: Finansal ve Araç-Özgü Literatürün Kesişimi (Faz 3+4)
4. Önerilen Feature Seti (Faz 5)
5. Önerilen Model Mimarisi ve Ensemble Stratejisi (Faz 6)
6. Validasyon ve Backtest Protokolü (Faz 7)
7. Risk Checklist'i (Faz 8)
8. **"Gelmiş Geçmiş En İyi Baseline" Spesifikasyonu** — label + feature listesi + model + validasyon + metrik tanımının tek sayfada somutlaştığı bölüm
9. Açık Sorular / Gelecek Araştırma Yönleri
10. Birleşik Kaynakça

**B. Karar-Odaklı Sunum — İskelet:**
1. Kapak
2. Amaç ve Kapsam
3. Yöntem: Faz Yapısı (bu master plana atıf)
4. Önerilen Problem Tanımı (Label/Ufuk/Threshold)
5. Ana Metodolojik Dersler
6. Önerilen Feature Seti (öncelik sıralı)
7. Önerilen Model/Ensemble Stratejisi
8. Validasyon/Backtest Protokolü
9. Kritik Riskler ve Ele Alınma Şekli
10. "Best Baseline" — Tek Sayfa Sistem Şeması
11. Sonraki Adımlar
12. Ekler/Kaynakça

*Gerekçe:* Sentez dökümanı derinlik için, sunum ise geliştirici ekibin/yöneticilerin hızlıca karar vermesi için var — ikisi aynı bilgiyi farklı yoğunlukta sunar, bu yüzden ayrı tutuldu.

---

## Onaya/Karara Bağlı Noktalar

1. **Tahmin ufku** (1 gün / 1 hafta / 1 ay?) belirtilmemiş — Faz 1'de literatürden seçenekler sunulacak, ama işe başlarken bir ön tercihiniz var mı?
2. **"Stable" bandının genişliği** için bir iş kısıtı var mı (örn. "±%2 altı stable sayılsın" gibi), yoksa tamamen literatür bulgusuna mı bırakılsın?
3. **Kapsam:** Proje tanımında "ikinci el / yeni araç piyasası" birlikte geçiyor, ama bu ikisi çok farklı dinamiklere sahip (biri arz-kısıtlı üretim zinciri, diğeri stok/ilan piyasası). Faz 2 ve 4'te ikisi tek alt-bölümde mi ele alınsın, yoksa ayrı alt-fazlara mı bölünsün?
4. **Coğrafi kapsam:** Faz 2 Türkiye'ye özgü dinamiklere odaklanıyor — yalnızca Türkiye pazarı mı hedefleniyor, yoksa uluslararası karşılaştırma (örn. Faz 3/4'teki genel literatür dışında) da isteniyor mu?
5. **Faz 2'de Arabam.com referansı:** Projenin konusu stajınızla (Arabam.com, Data Science Intern) örtüştüğü için Faz 2'ye Arabam.com'un kamuya açık fiyat endeksini örnek kaynak olarak ekledim. Bu uygun mu, yoksa şirket-içi veri/rapor kullanımı konusunda dikkatli olunması gereken bir gizlilik sınırı var mı?
6. **Kaynak türü kapsamı:** Yalnızca akademik (peer-reviewed) kaynaklar mı esas alınsın, yoksa sektör raporları/gri literatür de "resmi kaynak" sayılsın mı (özellikle Faz 2 ve 4 için bu önemli)?
7. **Faz çıktı uzunluğu:** Her faz dökümanı için bir üst sınır (örn. ~3000 kelime) belirlensin mi, yoksa kapsamlı olması önceliklendirilsin mi?
