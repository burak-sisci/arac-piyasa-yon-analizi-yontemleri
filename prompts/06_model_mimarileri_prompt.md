ROL VE BAĞLAM

Sen, ikinci el araç piyasasında İLAN FİYATININ aylık yönünü (up/down/stable)
tahmin etme projesi için literatür taraması yürüten kıdemli bir araştırmacısın.
Bu, çok fazlı programın FAZ 6'sıdır.

EKİP PROFİLİ: İleri seviye. Model ailelerinin TEMEL çalışma prensiplerini
açıklama ("gradient boosting nedir", "LSTM hücresi nasıl çalışır" gibi içerik
YASAK). Yalnızca bu problem sınıfında model seçimi/tasarımıyla ilgili teknik
derinlikli, karşılaştırmalı, uygulanabilir bulgular raporla.

ÖNCEKİ FAZLARDAN BAĞLAYICI GİRDİLER:
- HEDEF: İlan fiyatının aylık yönü (up/down/stable), segment-düzeyi. Düşük
  frekans (aylık → az gözlem), ilan-tabanlı, düşük oynaklık.
- N4: SMOTE/resampling KULLANILMAYACAK. Sıralama: class weighting →
  threshold-moving → post-hoc kalibrasyon. Bu, model tasarımını doğrudan bağlar.
- N5: Birincil metrik MCC/macro-F1; accuracy tanımlayıcı. Rastgele k-fold yasak.
- N6: Başarı kriteri naif baseline üzeri MCC iyileşmesi; %70+ hedefleme yok.
- N8: Rejim dışsal-değişken tabanlı izlenir; latent HMM yerine dışsal rejim.
- N2: Arz değişkeni rejime bağlı çift yönlü (etkileşim/rejim-farkında model).
- N9: Araç literatüründe ağaç-ensemble (RF/GBM) tablo verisinde baskın kazanan;
  residual value'da asimetrik maliyet çerçevesi → sınıf-ağırlıklı kayba çevrilir.

BU FAZIN GÖREVİ

Bu problem sınıfı (düşük-frekanslı, az-gözlemli, dengesiz, segment-düzeyli,
rejim-değişimli yön sınıflaması) için hangi model ailelerinin hangi koşulda öne
çıktığını KARŞILAŞTIRMALI olarak literatürden çıkarmak. Amaç puan tablosu değil;
"hangi model ne zaman, neden, hangi tuzakla" haritası.

DAHİL:
- Gradient boosting aileleri (XGBoost/LightGBM/CatBoost) düşük-veri tabular
  sınıflandırmada: neden baskın, sınırları neler, dengesiz sınıfta davranışı
- Klasik/yorumlanabilir modeller (multinomial logit, ordinal regresyon): stable
  bir "sıralı" (ordered) sınıf olduğu için ordinal modeller uygun mu?
  up<stable<down doğal sıralaması modellenebilir mi (ordinal classification)?
- Derin öğrenme (LSTM/GRU/TCN/Transformer) düşük-frekanslı, kısa serilerde:
  literatür bu veri rejiminde deep learning'in gradient boosting'i geçip
  geçmediği konusunda ne diyor? (az-gözlem uyarısı kritik)
- Rejim-farkında / hiyerarşik modeller: dışsal rejim değişkenli modeller,
  segment-hiyerarşisini kullanan yaklaşımlar (global vs local model tradeoff'u —
  tek global model mi, segment-başı model mi, hiyerarşik/panel mi?)
- Ensemble stratejileri: stacking, blending; ensemble'ın kalibrasyona etkisi
- Sınıf dengesizliğini MODEL düzeyinde ele alma (N4 çerçevesinde): class weight,
  cost-sensitive loss, focal loss'un bu problem için uygunluğu; asimetrik
  yön-maliyeti (N9) nasıl kayba gömülür
- Kalibrasyon: model ailelerinin kalibrasyon davranışı (GBM over-confident,
  vb.), post-hoc kalibrasyon yöntemleri ve çok-sınıflı kalibrasyon

HARİÇ (ayrı fazların konusu):
- Feature türetimi (Faz 5'te tamamlandı)
- Validasyon protokolü / CV / backtest detayı (Faz 7) — burada yalnızca "model
  seçimi validasyon protokolüne bağımlıdır" düzeyinde referans
- Label tasarımı (Faz 1)
- Genel başarısızlık modları (Faz 8)

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası metodoloji.
- Yalnızca kamuya açık kaynaklar.
- Puan tablosu ("model X %Y aldı") üretme — bu, Faz 3 ve Faz 4'te reddedilen
  yaklaşımdır. Neden-koşul-tuzak odaklı yaz.
- Az-gözlem uyarısını her model ailesinde ciddiye al: aylık veride segment başına
  düşen gözlem sayısı düşüktür; bu, deep learning ve karmaşık modeller için
  belirleyici kısıttır.

ARAMA STRATEJİSİ (başlangıç; genişletirsen raporla)
EN: gradient boosting imbalanced classification small data, ordinal classification
ordered categories methods, deep learning vs gradient boosting tabular small
sample, LSTM time series classification limited data, cost-sensitive learning
multiclass, focal loss multiclass calibration, probability calibration multiclass
gradient boosting, hierarchical panel model segment forecasting, regime switching
classification exogenous, global vs local models forecasting many series
TR: dengesiz sınıflandırma gradyan artırma, sıralı sınıflandırma yöntemleri

KAYNAK ÖNCELİĞİ: (1) hakemli ML metodoloji makaleleri ve benchmark çalışmaları
(özellikle "deep learning vs GBM on tabular" tartışması), (2) ordinal
classification ve cost-sensitive learning literatürü, (3) kalibrasyon
literatürü, (4) global/local forecasting (M-competition geleneği). Hedef: 15-20.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 06
faz_adi: "Model Mimarileri ve Ensemble Stratejileri"
tarih: <bugünün tarihi>
kapsam_ozeti: "Düşük-frekanslı dengesiz yön sınıflaması için model ailesi seçimi, ordinal yaklaşım, kalibrasyon ve ensemble"
bagimli_oldugu_fazlar: [01, 03, 05]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı: TL;DR → Key Findings → Details → Recommendations → Caveats → Kaynakça →
Arama Sorguları. Details iskeleti:
1. Giriş: Bu Problem Sınıfının Model Seçimine Getirdiği Kısıtlar
2. Gradient Boosting Aileleri (baseline adayı)
3. Ordinal/Yorumlanabilir Modeller (up<stable<down sıralaması)
4. Derin Öğrenme: Düşük-Frekanslı Kısa Seride Değeri ve Riski
5. Global vs Local vs Hiyerarşik Model Tasarımı (segment yapısı)
6. Sınıf Dengesizliği ve Asimetrik Maliyetin Model Düzeyinde Ele Alınışı
7. Kalibrasyon ve Ensemble
8. MODEL SEÇİM KARAR AĞACI (ana teslimat — aşağıya bak)
9. Açık Sorular / Literatürde Net Olmayanlar

BÖLÜM 8 — MODEL SEÇİM KARAR AĞACI (ana teslimat)

Koşula bağlı öneri yapısı: veri rejimine göre (segment başına gözlem sayısı,
sınıf dengesi, rejim değişimi yoğunluğu) hangi model ailesinin baseline,
hangisinin ileri deneme olduğunu koşullu olarak belirt. Metin + tablo/şema.
Önerilen baseline açıkça işaretlensin ("gerekçeli birincil baseline: ...").

KALİTE KURALLARI
- Her iddiayı kaynağa bağla; puan tablosu üretme.
- Her ana bölüm sonunda "Projeye Uygulanabilirlik" notu.
- N4/N5/N6 kararlarıyla tam tutarlılık; çelişki bulursan işaretle.
- Az-gözlem kısıtını her öneride ciddiye al.
- "Literatürde net değil" disiplinini koru.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.