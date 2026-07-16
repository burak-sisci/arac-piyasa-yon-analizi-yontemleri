---
faz_no: 06
faz_adi: "Model Mimarileri ve Ensemble Stratejileri"
tarih: 2026-07-13
kapsam_ozeti: "Düşük-frekanslı dengesiz yön sınıflaması için model ailesi seçimi, ordinal yaklaşım, kalibrasyon ve ensemble"
bagimli_oldugu_fazlar: [01, 03, 05]
durum: tamamlandi
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 27
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-15
---

# Faz 06 — Model Mimarileri ve Ensemble Stratejileri: Karşılaştırmalı Literatür Taraması

## TL;DR

- **Gerekçeli birincil baseline, sınıf-ağırlıklı gradient boosting (LightGBM/XGBoost/CatBoost) ailesidir**: tablo verisinde ağaç-tabanlı ensemble'ların baskınlığı düşük-orta örneklemde de korunur (Grinsztajn ve ark. 2022; McElfresh ve ark. 2023), N9 ile tutarlıdır ve N4'ün sıralamasını (class weighting → threshold-moving → post-hoc kalibrasyon) doğrudan destekler. Derin öğrenme (LSTM/GRU/TCN/Transformer) bu veri rejiminde (aylık frekans, segment başına az gözlem) baseline OLMAMALI, yalnızca gözlem sayısı arttığında İLERİ DENEME olarak düşünülmelidir.
- **"stable" sınıfının doğal sıralaması (up<stable<down) ordinal yaklaşımla değerlendirilebilir**: Frank & Hall (2001) tipi kümülatif ikili ayrıştırma tablo/ağaç modellerinde nominal softmax'a kıyasla ordinal metriklerde (QWK, MAE) genellikle ölçülü kazanç sağlar; ancak kazanç sınıf sayısı arttıkça büyür — 3 sınıfta etki mütevazıdır ve garanti değildir. Bu bir İLERİ DENEME olarak konumlandırılmalı, baseline ise nominal kalmalıdır.
- **Kalibrasyon ihmal edilmemeli**: GBM'ler eğitimde log-loss'a aşırı-uyum nedeniyle overconfident olma eğilimindedir; post-hoc kalibrasyon (küçük kalibrasyon setinde Platt scaling, izotonik regresyon yalnızca yeterli veri varsa) N4'ün üçüncü adımıdır. Çok-sınıflı kalibrasyon binary'ye göre daha zordur ve az-gözlem izotonik regresyonu overfit ettirir.

## Key Findings

1. **Ağaç-tabanlı ensemble baskınlığı örneklem-boyutuna görece dayanıklıdır ama sınırsız değildir.** Grinsztajn ve ark. (2022) ağaç modellerinin üstünlüğünü üç indüktif önyargıya bağlar: (a) düzensiz/pürüzlü hedef fonksiyonlarını daha iyi öğrenme, (b) bilgisiz (uninformative) özniteliklere dayanıklılık, (c) rotasyona-değişmez OLMAMA. Bu üç özellik ilan-tabanlı, gürültülü, karışık öznitelikli tablo verisiyle örtüşür. McElfresh ve ark. (2023, NeurIPS Datasets & Benchmarks, arXiv:2305.02997), 176 veri seti üzerinde 19 algoritmayı karşılaştırarak "the 'NN vs. GBDT' debate is overemphasized: for a surprisingly high number of datasets, either the performance difference between GBDTs and NNs is negligible, or light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs" bulur; GBDT üstünlüğünün özellikle "larger datasets, datasets with a high size-to-number-of-features ratio, and 'irregular' datasets"te belirginleştiğini raporlar.

2. **Az-gözlem rejiminde iki uçlu kanıt vardır.** Bir uçta, LightGBM'in yaprak-bazlı (leaf-wise) büyümesi küçük veride overfit riskini artırır; bu, CatBoost'un simetrik ağaçları veya XGBoost'un level-wise yapısıyla veya güçlü düzenlileştirmeyle hafifletilebilir. Diğer uçta, TabPFN (Hollmann ve ark., Nature 2025, 637(8045):319–326, doi:10.1038/s41586-024-08328-6) "yields dominant performance for datasets with up to 10,000 samples and 500 features. In 2.8 s, TabPFN outperforms an ensemble of the strongest baselines tuned for 4 h" — sınıflandırmada 5.140× hızlanma, en güçlü baseline CatBoost — bu, çok-küçük veri için ciddi bir İLERİ DENEME adayıdır.

3. **Derin öğrenme bu veri rejiminde baseline değildir.** Şwartz-Ziv & Armon (2022) derin modellerin XGBoost'u yalnızca XGBoost ile ensemble edildiğinde geçtiğini bulur. Kredi-skorlama (dengesiz + küçük) çalışmalarında derin öğrenme ağaç modellerini geçememiştir. LSTM'ler kısa/az serilerde overfit'e yatkındır ve UCR literatüründe genelleme zorlukları belgelenmiştir.

4. **Global (cross-learning) yaklaşım az-gözlemi telafi eder.** Montero-Manso & Hyndman (2021) tek bir global modelin, serilerin benzerliğine dair varsayım olmaksızın, lokal (segment-başı) modelleri eşleyebileceğini veya geçebileceğini teorik olarak gösterir; global modelin karmaşıklığı seri sayısıyla sabit kalırken lokal modelinki artar. M5 yarışmasında (Makridakis, Spiliotis & Assimakopoulos 2022, IJF) Walmart'a ait 42.840 hiyerarşik seride kazanan takımların tamamı cross-learning kullanmıştır ("the winning teams all used cross-learning forecasting approaches — a single model is trained on multiple related time series") ve çoğu LightGBM'e dayanmıştır.

5. **Sınıf dengesizliği N4 sırasıyla ele alınmalıdır (SMOTE değil).** GBM'lerde class weight (`scale_pos_weight`/`class_weight`), cost-sensitive özel kayıp ve focal loss uygun araçlardır. Asimetrik yön-maliyeti (N9) bir maliyet matrisi C aracılığıyla kayba gömülebilir; ordinal yapıda "up↔down" (reversal) hatası "up↔stable" (off-by-one) hatasından daha ağır cezalandırılmalıdır.

6. **Kalibrasyon ile ensemble etkileşir.** Stacking'te meta-öğrenici (lojistik regresyon) alt-modellerin kalibrasyon farklarını düzeltebilir ve overconfident XGBoost çıktısını yeniden kalibre edebilir; ancak kalibrasyonun stacking'te veri-sızıntısı olmadan (out-of-fold) uygulanması şarttır.

## Details

### 1. Giriş: Bu Problem Sınıfının Model Seçimine Getirdiği Kısıtlar

Bu problem beş kısıtı aynı anda taşır: (i) düşük frekans (aylık) → segment başına az gözlem; (ii) sınıf dengesizliği (stable baskın, up/down azınlık ve karar-ilgili); (iii) segment-düzeyi hiyerarşi; (iv) dışsal-değişken tabanlı rejim değişimi (N8); (v) hedefin doğal sıralaması (up<stable<down). Bu kısıtlar birbirini pekiştirir: az gözlem parametre-yoğun modelleri (derin öğrenme) cezalandırır; dengesizlik naif accuracy'yi yanıltıcı kılar (N5 zaten MCC/macro-F1'i birincil yapar); rejim değişimi tek bir durağan (stationary) model varsayımını zayıflatır.

Model seçimi validasyon protokolüne bağımlıdır (ayrı fazın konusu); burada yalnızca şu ilke geçerlidir: N5 gereği rastgele k-fold yasaktır, dolayısıyla model karşılaştırmaları zaman-farkında bir protokolle yapılmalıdır. Bu döküman puan tablosu üretmez; her model ailesi için "ne zaman / neden / hangi tuzak" haritası sunar.

**Projeye Uygulanabilirlik:** Kısıtların bileşimi, "basit, düzenlileştirilmiş, kalibre edilebilir, dışsal rejim değişkenlerini etkileşim olarak alabilen" bir model ailesini öne çıkarır — bu profil gradient boosting'e işaret eder.

### 2. Gradient Boosting Aileleri (baseline adayı)

**Neden baskın:** Grinsztajn ve ark. (2022, NeurIPS Datasets & Benchmarks) ağaç-tabanlı modellerin tablo verisindeki üstünlüğünü üç indüktif önyargıyla açıklar: pürüzlü hedef fonksiyonlarını öğrenme, bilgisiz özniteliklere dayanıklılık ve rotasyona-değişmez olmama. Bu üçüncü nokta kritiktir: MLP'ler rotasyona-değişmez olduğundan bilgisiz öznitelik eklendikçe performansları kötüleşir; ağaçlar her özniteliğe ayrı baktığından bu sorundan görece muaftır. İlan verisi çok sayıda potansiyel-bilgisiz öznitelik içerdiğinden bu avantaj doğrudan geçerlidir.

**Sınırlar:** LightGBM'in leaf-wise büyümesi küçük veride aşırı-karmaşık ağaçlar üretip overfit edebilir; bu nedenle küçük segmentlerde CatBoost'un simetrik (oblivious) ağaçları veya sıkı `num_leaves`/`min_child_samples` düzenlileştirmesi tercih edilmelidir. GBM eğitimi hiperparametre ayarına duyarlıdır ancak DL'e kıyasla ayar yükü düşüktür.

**Dengesiz sınıf davranışı:** Standart GBM çoğunluk sınıfına yanlıdır; "rare events bias" küçük örneklemde eğitim verisinden verimli tahmin edilemez (Nguyen & Cooper tarzı düzeltmeler literatürde önerilir). Çözüm N4 ile uyumludur: önce class weight / `scale_pos_weight`, ardından threshold-moving. jcheminf (2022) çalışması, özel kayıp fonksiyonlarının (focal, LDAM tarzı) çoğu veri setinde cross-entropy'yi anlamlı geçtiğini ama yeterli hiperparametre ayarıyla bunların cross-entropy'ye yakınsayabildiğini gösterir — yani özel kayıp bir "sihirli değnek" değil, ayarlanabilir bir araçtır.

**Projeye Uygulanabilirlik:** GBM ailesi gerekçeli birincil baseline'dır. Segment başına gözlem düşükse CatBoost veya sıkı-düzenlileştirilmiş XGBoost, gözlem çoksa LightGBM önerilir. Class weight → threshold-moving → kalibrasyon sırası (N4) doğrudan uygulanır.

### 3. Ordinal/Yorumlanabilir Modeller (up<stable<down sıralaması)

Hedefin doğal sıralaması vardır: up<stable<down (veya ters). Ordinal sınıflandırma bu sıralamayı kullanır; nominal multinomial ise sıralamayı atar. Teorik olarak ordinal model, doğru olduğunda, daha az parametre kullanır ve daha verimlidir (Tutz 2022, WIREs; Agresti geleneği). Klasik ordinal araç, proportional-odds (cumulative logit) modelidir; ancak paralel-eğim (proportional odds) varsayımı test edilmeli (Brant testi) ve ihlalde partial proportional odds veya nominal multinomial'e düşülmelidir.

**Ağaç ensemble'larıyla ordinal:** XGBoost/LightGBM/CatBoost'un hiçbiri native ordinal amaç fonksiyonu sunmaz (LightGBM Issue #5882 ve CatBoost Issue #2817 gibi açık kullanıcı talepleri bunu doğrular; CatBoost yalnızca nominal `MultiClass`/`MultiClassOneVsAll` sunar). Standart, kütüphane-bağımsız teknik Frank & Hall (2001, ECML, LNCS 2167, ss. 145–156, DOI:10.1007/3-540-44795-4_13) kümülatif ikili ayrıştırmasıdır: K sıralı sınıf için K−1 ikili sınıflandırıcı P(y>V_i) tahmin eder, sınıf olasılıkları komşu kümülatiflerin farkından geri kazanılır. 3 sınıf için bu 2 ikili boosted model demektir: {up} vs {stable,down} ve {up,stable} vs {down}. Frank & Hall'un temel ampirik iddiası: yöntem karar ağacıyla uygulandığında sınıfları sırasız küme olarak alan naif yaklaşımı geçer, ve altta yatan öğrenme şemasına değişiklik gerektirmeden uygulanabilir. Alternatifler: OrdinalGBT (LightGBM için latent-threshold kayıp) ve GBNet/GBOrd (McCullagh 1980 cumulative logit'i GBM ile birleştirir; native olmadığı için gradyan/Hessian'ı özel hesaplar).

**Kazanç var mı?** Ordinal splitting-criteria çalışması (Pattern Recognition, 2025; arXiv:2412.13697; 45 ordinal veri seti) ordinal kriterlerin (OGini en iyisi) nominal muadillerini MAE/QWK/RPS'te anlamlı geçtiğini, ancak avantajın özellikle 6+ sınıfta belirginleştiğini raporlar. 3 sınıfta kazanç daha mütevazıdır ve veri-bağımlıdır (Classifier Pooling, 2026). Cao/Mirjalili/Raschka CORAL (2020) ve Shi/Cao/Raschka CORN (2021) derin ordinal yaklaşımlar sunar ama bunlar DL tabanlı olduğundan az-gözlem rejiminde uygun değildir.

**Dengesizlikle etkileşim:** Ordinal problemlerde tipik olarak uç/boundary sınıflar azınlıktır — bu bizim durumumuza uyar (up/down azınlık, karar-ilgili). Pérez-Ortiz ve ark. (2015, IEEE TKDE 27(5):1233–1245) generic yeniden-örneklemenin (SMOTE) sınıfları nominal küme gibi ele alarak sıralama bilgisini kaybettirdiğini ve azınlık sınıflarda kötü ordinal sonuç verdiğini vurgular. **Bu N4 ile tam tutarlıdır: SMOTE zaten yasak.** Ordinal yapı korunacaksa dengesizlik, sıralamayı bozmayan araçlarla (class weight + ordinal kayıp) ele alınmalıdır; Cruz ve ark. (2017, LNCS) ranking-tabanlı ağırlıklı yaklaşımla azınlık sınıfların karar sınırına eşit katkısını sağlar.

**Projeye Uygulanabilirlik:** Ordinal yaklaşım İLERİ DENEME'dir, baseline değil. Somut adım: baseline nominal GBM kurulduktan sonra Frank & Hall (2001) 2-ikili-model ayrıştırması denenip QWK/MCC'de nominal'e üstünlük aranmalıdır. Kazanç 3 sınıfta garanti değildir; "literatürde net değil" — sadece deneysel doğrulanmalıdır.

### 4. Derin Öğrenme: Düşük-Frekanslı Kısa Seride Değeri ve Riski

**Az-gözlem uyarısı (kritik):** LSTM/GRU/TCN/Transformer parametre-yoğundur ve aylık frekansta segment başına gözlem düşükken overfit kaçınılmazdır. Şwartz-Ziv & Armon (2022) derin modellerin XGBoost'u tek başına geçemediğini, yalnızca XGBoost ile ensemble edildiğinde katkı sağladığını raporlar. Kredi-skorlama gibi dengesiz+küçük veride derin öğrenme ağaç modellerini geçememiş, NAS/AutoML bile hafifçe geri kalmıştır (arXiv 1907.12363). LSTM literatüründe küçük UCR veri setlerinde overfit ve genelleme sorunları belgelidir.

**Global eğitim istisnası:** Derin modeller lokal (segment-başı) eğitildiğinde başarısız olur ama global (tüm segmentler havuzlanarak) eğitildiğinde rekabetçi olabilir (Montero-Manso & Hyndman 2021; Hewamalage ve ark.). Bu, az-gözlem sorununu cross-learning ile telafi eden tek DL yolu olarak öne çıkar. Yine de M4'te (2018) altı saf ML yönteminin hiçbiri Comb benchmark'ından daha isabetli olamamış, kazanan Smyl'in hibrit ES-RNN'i olmuş, ikincilik XGBoost-ağırlıklandırmalı Montero-Manso ve ark. yöntemine gitmiştir; M5'te (2020) ise LightGBM "numerous, correlated series and exogenous/explanatory variables" işlemede etkili olduğunu kanıtlayarak hakim olmuştur (Makridakis ve ark.).

**Foundation-model istisnası:** TabPFN (Hollmann ve ark., Nature 2025) ≤10.000 örnek, ≤500 öznitelikte boosted tree'leri geçtiğini ve kalibre çıktı ürettiğini raporlar; bu, çok-küçük tablo verisi için gerçek bir İLERİ DENEME adayıdır. Ancak makalenin kendi sınırlamaları açıktır: "TabPFN excels in handling small- to medium-sized datasets with up to 10,000 samples and 500 features"; daha büyük veri ve yüksek-düzensiz regresyonda avantaj azalır, çıkarım hızı CatBoost gibi optimize yaklaşımlardan yavaş olabilir ve bellek kullanımı veri boyutuyla doğrusal artar.

**Projeye Uygulanabilirlik:** Deep learning baseline OLMAMALI. Yalnızca (a) segment başına gözlem yeterince büyürse ve (b) global/cross-learning kurgusuyla eğitilirse İLERİ DENEME'dir. Çok-küçük veride TabPFN doğrudan denenebilir. Her durumda GBM baseline'ı geçme eşiği aranmalıdır (N6).

### 5. Global vs Local vs Hiyerarşik Model Tasarımı (segment yapısı)

Üç seçenek: (a) tek global model (tüm segmentler, segment kimliği öznitelik olarak), (b) segment-başı ayrı lokal modeller, (c) hiyerarşik/panel (partial pooling) yaklaşım. Montero-Manso & Hyndman (2021) global modelin lokal modelleri, serilerin ilişkili olması gerekmeksizin, eşleyebileceğini/geçebileceğini gösterir; kilit içgörü, global modelin karmaşıklığının seri sayısıyla sabit kalması, lokalinkinin ise artmasıdır. Az-gözlemli segmentlerde lokal model gürültüdür; global model cross-learning ile "güç ödünç alır".

**Hiyerarşik/partial pooling:** Bayesyen hiyerarşik (multilevel) modeller, az gözlemli grupları popülasyon ortalamasına doğru "shrink" ederek James-Stein tipi kazanç sağlar (Gelman & Hill geleneği); grup ne kadar az gözlemliyse shrinkage o kadar güçlüdür. Bu, segment-başı gürültüyü azaltmanın ilkeli yoludur. Uyarı: grup sayısı çok azsa (≈<5) veya gruplar doğaları gereği çok farklıysa hiyerarşik model uygun değildir.

**M-competition dersi:** M5'te kazanan takımlar cross-learning + hiyerarşinin farklı seviyelerinde ayrı modeller eğitme yaklaşımını birleştirdi. GBM tabanlı global model (segment kimliği + rejim değişkenleri öznitelik olarak) pratik bir orta yoldur.

**Rejim-farkındalık (N8):** Dışsal rejim değişkenleri (kur şoku, ÖTV, arz şoku) latent HMM yerine gözlemlenebilir öznitelik olarak modele girer. Ağaç ensemble'ları bu değişkenlerle arz değişkeni (N2) arasındaki çift-yönlü etkileşimi (kıtlık→prim yukarı; kampanya→aşağı) doğal olarak split'lerle yakalayabilir; ayrıca açık etkileşim öznitelikleri veya rejim-başı ayrı ağaç dalları güçlendirir. Threshold-switching (gözlemlenen eşik değişkeni) çerçevesi N8 ile kavramsal olarak uyumludur (latent değil).

**Projeye Uygulanabilirlik:** Gerekçeli tercih: segment kimliğini ve dışsal rejim değişkenlerini öznitelik alan tek global GBM. Segment sayısı azsa ve heterojense hiyerarşik/panel yaklaşım İLERİ DENEME'dir. Saf segment-başı lokal modeller az-gözlem nedeniyle önerilmez.

### 6. Sınıf Dengesizliği ve Asimetrik Maliyetin Model Düzeyinde Ele Alınışı

N4 sırası bağlayıcıdır: class weighting → threshold-moving → post-hoc kalibrasyon; SMOTE/resampling yasak. Bu sıralama literatürle uyumludur çünkü model-düzeyi maliyet ayarı, sentetik veri üretiminin ordinal yapıyı/olasılık dağılımını bozma riskini taşımaz.

**Araçlar:** (a) Class weight — GBM'de doğrudan; (b) cost-sensitive özel kayıp — maliyet matrisi C ile beklenen maliyet minimize edilir (Ling & Sheng geleneği; Angle-Based Cost-Sensitive Multicategory, arXiv 2003.03691); (c) focal loss — kolay örneklerin ağırlığını (1−p)^γ ile düşürür, hem dengesizliği hem overconfidence'ı ele alır (Lin ve ark. 2017; Mukhoti ve ark. 2020 kalibrasyon faydasını gösterir).

**Asimetrik yön-maliyeti (N9) somut kayıp tasarımı:** Residual value literatüründeki asimetrik maliyet çerçevesi bir 3×3 maliyet matrisine çevrilir. Ordinal doğa gereği matris "off-by-one" (ör. gerçek=up, tahmin=stable) hatalarını hafif, "reversal" (gerçek=up, tahmin=down) hatalarını ağır cezalandırmalıdır — kuadratik-ağırlıklı (QWK benzeri) bir maliyet yapısı bu sıralamayı doğal biçimde kodlar. İş-anlamlı asimetri (ör. yukarı yönü kaçırmanın maliyeti aşağıyı kaçırmaktan farklıysa) matrise ayrıca gömülür. NIST (2023) asimetrik focal loss'un toplam ekonomik maliyeti weighted-BCE'ye kıyasla belirli eşik/oran aralıklarında (0.2<τ<0.5, C>64) %15–40 düşürdüğünü raporlar — yani asimetrik kayıp tasarımı ölçülebilir kazanç sağlayabilir ama maliyet oranına duyarlıdır.

**Uyarı:** Cost-sensitive learning'in temel zorluğu gerçek maliyetlerin çoğu zaman bilinmemesidir (He & Garcia geleneği); C matrisi bir hiperparametre gibi ayarlanmalı ve N5 metriği (MCC/macro-F1) ile doğrulanmalıdır. Class weight ile maliyet matrisi birlikte kullanıldığında çift-sayım riskine dikkat.

**Projeye Uygulanabilirlik:** Baseline: class weight + threshold-moving. İLERİ DENEME: ordinal-farkında kuadratik maliyet matrisiyle cost-sensitive kayıp veya focal loss. Her ikisi de N4/N5 ile tutarlıdır; SMOTE denenmeyecektir.

### 7. Kalibrasyon ve Ensemble

**GBM kalibrasyon davranışı:** Boosting, exponential/log-loss'a aşırı-uyum nedeniyle olasılıkları uçlara iter ve overconfident olur; Niculescu-Mizil & Caruana (2005) boosted tree'lerin kalibrasyondan (Platt/izotonik) belirgin fayda gördüğünü, hatta küçük kalibrasyon setlerinde bile iyileşme olduğunu gösterir. Küçük kalibrasyon setinde (≈<2000 örnek) Platt scaling izotonik regresyonu geçer, çünkü izotonik daha az kısıtlı olduğundan overfit eder. Bu, bizim az-gözlem rejimimiz için doğrudan belirleyicidir: **Platt scaling (veya çok-sınıflı genellemesi) az-gözlemde izotonik regresyona tercih edilmelidir.**

**Çok-sınıflı kalibrasyon zorlukları:** Platt ve izotonik doğrudan binary'dir; çok-sınıfa one-vs-rest ile genişletilir (Zadrozny & Elkan 2002) ama bu sınıf-bazlı kalibrasyonların toplamının 1 olmasını garanti etmez ve normalizasyon gerektirir. Temperature scaling tek-parametreli alternatif olarak accuracy'yi bozmadan ECE'yi düşürür. Classwise-ECE çok-sınıflı kalibrasyonu ölçmek için kullanılmalıdır.

**Focal loss'un kalibrasyona etkisi:** Mukhoti ve ark. (2020, NeurIPS) focal loss'un cross-entropy'ye kıyasla daha iyi kalibre modeller ürettiğini (KL-diverjans ile entropi arasında denge kurarak) gösterir; temperature scaling ile birleştirildiğinde state-of-the-art kalibrasyon. Bu, dengesizlik + kalibrasyon hedeflerini aynı anda ele almanın bir yolu.

**Ensemble'ın kalibrasyona etkisi:** Stacking, meta-öğrenici (lojistik regresyon) aracılığıyla alt-modellerin kalibrasyon farklarını öğrenip düzeltebilir; FT-Transformer + XGBoost stacking'i overconfident XGBoost'u yeniden kalibre edip ECE'yi düşürebilir (arXiv 2606.07582). DLBCL çalışması (BMC 2020) alt-modeli önce kalibre edip sonra stacklamanın hem ayrım hem kalibrasyonu iyileştirdiğini gösterir. Kritik uyarı: kalibrasyon stacking'te yalnızca meta-seviyede ve out-of-fold uygulanmalı, aksi halde veri sızıntısı olur. Bagging/RF ise sıklıkla underconfident'tır (uçlardan ortaya kayma) — yani ensemble türü kalibrasyon yönünü değiştirir.

**Projeye Uygulanabilirlik:** N4'ün üçüncü adımı (post-hoc kalibrasyon) az-gözlem nedeniyle Platt/temperature scaling ile yapılmalı, izotonik yalnızca kalibrasyon seti büyükse. Ensemble denenirse (İLERİ DENEME) alt-modeller out-of-fold kalibre edilip sonra birleştirilmeli. Kalibrasyon, N5'in olasılık-tabanlı karar eşiği (threshold-moving) için ön koşuldur.

### 8. MODEL SEÇİM KARAR AĞACI (ana teslimat)

Bu bölüm koşula-bağlı bir karar çerçevesidir; puan tablosu değildir. Üç eksen kullanılır: **segment başına gözlem sayısı**, **sınıf dengesizliği şiddeti**, **rejim değişimi yoğunluğu**.

**Gerekçeli birincil baseline: segment kimliğini ve dışsal rejim değişkenlerini (N8) öznitelik olarak alan, class-weighted, tek global gradient boosting modeli (küçük segmentlerde CatBoost/sıkı-düzenlileştirilmiş XGBoost; büyük veride LightGBM), ardından threshold-moving ve Platt/temperature post-hoc kalibrasyon (N4 sırası).** Bu seçim N9 (ağaç-ensemble baskınlığı), N4, N5 ve N8 ile tam tutarlıdır.

Karar tablosu:

| Koşul (segment başı gözlem / dengesizlik / rejim) | BASELINE | İLERİ DENEME | Kaçınılacak / Tuzak |
|---|---|---|---|
| Çok az gözlem (ör. onlarca), yüksek dengesizlik | Global GBM (CatBoost), class weight + threshold-moving; Platt kalibrasyon | TabPFN (küçük-veri foundation model); hiyerarşik/partial-pooling GBM | Lokal segment-başı modeller (gürültü); izotonik kalibrasyon (overfit); herhangi bir RNN/Transformer |
| Az-orta gözlem, orta dengesizlik | Global LightGBM/XGBoost, class weight → threshold → kalibrasyon | Frank & Hall (2001) ordinal 2-ikili-model; focal/cost-sensitive kayıp; stacking (out-of-fold kalibreli) | Nominal softmax'ın ordinal kazancı sağlayacağını varsaymak; kalibrasyonu atlamak |
| Orta-yüksek gözlem, düşük dengesizlik | Global GBM | Global DL (cross-learning; TCN/DeepAR tarzı); ordinal derin (CORN/CORAL) | Saf lokal DL (Montero-Manso: lokal DL başarısız) |
| Yoğun rejim değişimi (sık dışsal şok) | Rejim değişkenli global GBM + açık etkileşim öznitelikleri | Rejim-başı ayrı model dalları; threshold-switching çerçeve | Latent HMM rejim tespiti (N8'e aykırı) |

Karar akışı (şematik):
1. **Baseline'ı kur:** class-weighted global GBM + rejim değişkenleri → threshold-moving → Platt/temperature kalibrasyon. MCC'yi naif baseline'a karşı ölç (N6).
2. **Ordinal kazanç ara:** Frank & Hall 2-ikili-model ayrıştırmasını dene; QWK/MCC'de nominal baseline'ı geçiyorsa benimse, geçmiyorsa nominal kal.
3. **Dengesizlik yetersizse:** focal loss veya ordinal-farkında kuadratik maliyet matrisi (N9) dene.
4. **Segment gürültülüyse:** hiyerarşik/partial-pooling'e geç.
5. **Gözlem büyürse ve baseline platolarsa:** global DL veya TabPFN'i İLERİ DENEME olarak, her zaman GBM baseline'ı geçme eşiğiyle (N6) değerlendir.

### 9. Açık Sorular / Literatürde Net Olmayanlar

- **3 sınıfta ordinal kazancın büyüklüğü net değil:** Ordinal üstünlüğü çoğunlukla 6+ sınıfta belirgindir (Pattern Recognition 2025); 3 sınıfta kazanç veri-bağımlı ve mütevazıdır. Sadece deneysel doğrulanabilir.
- **Cost-sensitive maliyet matrisinin optimal değeri:** Gerçek asimetrik maliyetler bilinmediğinden C matrisi ayarlanmalı; literatür net bir "varsayılan" vermez.
- **Class weight + cost-sensitive kayıp + kalibrasyonun birlikte etkileşimi:** Bu üçlünün art arda uygulanmasının kalibrasyonu net iyileştirip iyileştirmediği (özellikle çok-sınıfta) literatürde tam çözülmemiştir.
- **Rejim etkileşimini GBM'in kendiliğinden mi yoksa açık öznitelikle mi yakalaması gerektiği:** Ağaçlar etkileşimi yakalayabilir ama az-gözlemde açık etkileşim özniteliği daha güvenilir olabilir; net kanıt sınırlı.
- **TabPFN'in dengesiz + rejim-değişimli finansal-tip veride davranışı:** TabPFN kanıtı çoğunlukla genel OpenML veri setlerinden; bu spesifik problem sınıfında performansı doğrulanmamış.

## Recommendations

1. **Hemen (baseline kurulumu):** Segment kimliği + dışsal rejim değişkenlerini (N8) öznitelik alan, class-weighted tek global GBM kur. Küçük segmentlerde CatBoost veya sıkı-düzenlileştirilmiş XGBoost; büyük veride LightGBM. N4 sırasını izle: class weight → threshold-moving → Platt/temperature kalibrasyon. Naif baseline üzeri MCC iyileşmesini (N6) birincil başarı ölçütü yap.
2. **Kısa vade (ordinal deneme):** Frank & Hall (2001) kümülatif 2-ikili-model ayrıştırmasını GBM ile dene. Eşik/karar: QWK ve MCC'de nominal baseline'ı istatistiksel olarak geçerse benimse; geçmezse nominal kal. Bu, 3 sınıfta garanti olmadığı için sıkı doğrulanmalı.
3. **Kısa vade (dengesizlik derinleştirme):** Baseline azınlık (up/down) sınıflarda yetersizse, ordinal-farkında kuadratik maliyet matrisi (reversal>off-by-one) veya focal loss dene. SMOTE denenmeyecek (N4).
4. **Orta vade (segment yapısı):** Segment sayısı az ve heterojense hiyerarşik/partial-pooling (shrinkage) yaklaşımını İLERİ DENEME olarak değerlendir.
5. **Orta vade (kalibrasyon + ensemble):** Post-hoc kalibrasyonu az-gözlemde Platt/temperature ile yap. Stacking denenirse alt-modelleri out-of-fold kalibre et, sonra birleştir; meta-öğrenici lojistik regresyon overconfident GBM'i düzeltebilir.
6. **Koşullu (DL/foundation):** Yalnızca segment başına gözlem yeterince büyürse global/cross-learning DL; veya çok-küçük veride TabPFN. Her ikisi de GBM baseline'ı geçme eşiğiyle (N6) yargılanmalı; geçemezse terk edilmeli.

**Öneriyi değiştirecek eşikler/benchmarklar:** (a) Segment başına gözlem birkaç yüzü aşarsa DL İLERİ DENEME'si anlamlanır; (b) ordinal ayrıştırma QWK'de nominal'i geçmezse ordinal terk edilir; (c) kalibrasyon seti büyürse izotonik Platt'ı geçebilir; (d) TabPFN limitleri (≤10k örnek, ≤500 öznitelik) aşılırsa avantajı kaybolur.

## Caveats

- **Az-gözlem her öneride belirleyicidir:** Aylık frekansta segment başına gözlem düşüktür; bu, DL ve karmaşık modelleri baseline olmaktan çıkarır ve izotonik kalibrasyon/derin ordinal gibi veri-aç yöntemleri riskli kılar. Bu kısıt tüm bölümlerde açıkça hesaba katılmıştır.
- **N4 ile tutarlılık:** SMOTE/resampling tüm önerilerden hariç tutulmuştur; ordinal-imbalance literatüründeki oversampling yöntemleri (Pérez-Ortiz 2015 vb.) bilinçli olarak DIŞLANMIŞTIR çünkü N4 bunu yasaklar. Yerine class weight + cost-sensitive kayıp önerilir.
- **N5 ile tutarlılık:** Tüm karşılaştırmalar MCC/macro-F1 ile yapılmalı; accuracy yalnızca tanımlayıcı. Puan tablosu bilinçli olarak üretilmemiştir.
- **Kaynak kalitesi:** Grinsztajn (2022), McElfresh (2023), Montero-Manso & Hyndman (2021), Mukhoti (2020), Niculescu-Mizil & Caruana (2005), Frank & Hall (2001), Pérez-Ortiz (2015, IEEE TKDE), Hollmann ve ark. (Nature 2025) hakemli/birincil kaynaklardır. GitHub issue'ları (native ordinal amaç yokluğu kanıtı) birincil ama hakemsizdir. Bazı blog/Medium kaynakları yalnızca kavramsal doğrulama için kullanılmıştır.
- **Kapsam dışı:** Feature türetimi, validasyon/backtest protokol detayı, label tasarımı ve genel başarısızlık modları bu dökümanda bilinçli olarak derinlemesine işlenmemiştir (ayrı fazlar).

## Kaynakça

- Grinsztajn, L., Oyallon, E., Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?* NeurIPS Datasets & Benchmarks. arXiv:2207.08815
- McElfresh, D. ve ark. (2023). *When Do Neural Nets Outperform Boosted Trees on Tabular Data?* NeurIPS Datasets & Benchmarks. arXiv:2305.02997
- Shwartz-Ziv, R., Armon, A. (2022). *Tabular Data: Deep Learning is Not All You Need.* Information Fusion.
- Borisov, V. ve ark. (2022). *Deep Neural Networks and Tabular Data: A Survey.*
- Hollmann, N. ve ark. (2022/2025). *TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second* / *Accurate predictions on small data with a tabular foundation model.* ICLR 2023 / Nature 637(8045):319–326, doi:10.1038/s41586-024-08328-6. arXiv:2207.01848
- Frank, E., Hall, M. (2001). *A Simple Approach to Ordinal Classification.* ECML, LNCS 2167, ss. 145–156. DOI:10.1007/3-540-44795-4_13
- Tutz, G. (2022). *Ordinal regression: A review and a taxonomy of models.* WIREs Computational Statistics.
- Cao, W., Mirjalili, V., Raschka, S. (2020). *Rank Consistent Ordinal Regression for Neural Networks (CORAL).* Pattern Recognition Letters 140:325–331.
- Shi, X., Cao, W., Raschka, S. (2021/2023). *Deep Neural Networks for Rank-Consistent Ordinal Regression Based on Conditional Probabilities (CORN).* Pattern Analysis & Applications. arXiv:2111.08851
- Pérez-Ortiz, M., Gutiérrez, P., Hervás-Martínez, C., Yao, X. (2015). *Graph-based approaches for over-sampling in the context of ordinal regression.* IEEE TKDE 27(5):1233–1245. DOI:10.1109/TKDE.2014.2365780
- Cruz, R. ve ark. (2017). *Ordinal Class Imbalance with Ranking.* LNCS, Springer. DOI:10.1007/978-3-319-58838-4_1
- Montero-Manso, P., Hyndman, R. (2021). *Principles and algorithms for forecasting groups of time series: Locality and globality.* International Journal of Forecasting.
- Makridakis, S., Spiliotis, E., Assimakopoulos, V. (2022). *M5 accuracy competition: Results, findings, and conclusions.* International Journal of Forecasting.
- Hewamalage, H., Bergmeir, C., Bandara, K. (2021/2022). *Global Models for Time Series Forecasting: A Simulation Study.* Pattern Recognition. arXiv:2012.12485
- Lin, T.-Y. ve ark. (2017). *Focal Loss for Dense Object Detection.* ICCV.
- Mukhoti, J. ve ark. (2020). *Calibrating Deep Neural Networks using Focal Loss.* NeurIPS. arXiv:2002.09437
- Niculescu-Mizil, A., Caruana, R. (2005). *Obtaining Calibrated Probabilities from Boosting / Predicting Good Probabilities with Supervised Learning.* ICML.
- Platt, J. (1999). *Probabilistic Outputs for SVMs.* Advances in Large Margin Classifiers.
- Zadrozny, B., Elkan, C. (2002). *Transforming classifier scores into accurate multiclass probability estimates.* ACM SIGKDD.
- NIST (2023). *Addressing misclassification costs in machine learning through asymmetric loss functions.*
- Ling, C., Sheng, V. (2008). *Cost-Sensitive Learning and the Class Imbalance Problem.*
- Angle-Based Cost-Sensitive Multicategory Classification (2020). arXiv:2003.03691
- Splitting criteria for ordinal decision trees: an experimental study (2025). Pattern Recognition. arXiv:2412.13697
- jcheminf (2022). *Tuning gradient boosting for imbalanced bioassay modelling with custom loss functions.* Journal of Cheminformatics.
- Frank & Hall alternatifleri / native-eksiklik kanıtı: GBNet (Horrell 2025, JOSS 10(111):8047); OrdinalGBT (Python); LightGBM Issue #5882; CatBoost Issue #2817.
- Gelman, A., Hill, J. *Data Analysis Using Regression and Multilevel/Hierarchical Models* (partial pooling/shrinkage geleneği).

## Kullanılan Nihai Arama Sorguları

İngilizce:
- deep learning vs gradient boosting tabular data small sample Grinsztajn
- gradient boosting imbalanced classification small data behavior
- ordinal classification ordered categories methods review
- LSTM time series classification limited data small sample overfitting
- global vs local models forecasting many series cross-learning Montero-Manso
- probability calibration multiclass gradient boosting overconfident Platt isotonic
- focal loss calibration miscalibration classification Mukhoti
- ordinal classification vs nominal multinomial performance comparison ordered
- cost-sensitive learning multiclass loss function asymmetric misclassification cost
- regime switching classification exogenous variables structural break forecasting
- stacking ensemble effect on calibration probability estimates
- CORAL CORN ordinal regression neural network rank consistent
- M5 competition lessons LightGBM gradient boosting winning cross-learning Makridakis
- TabPFN small tabular datasets classification prior-data fitted network
- Grinsztajn tree-based uninformative features rotation invariance tabular why
- stock price direction prediction up down classification machine learning imbalanced
- hierarchical Bayesian panel partial pooling shrinkage few observations per group
- (subagent) Frank & Hall ordinal classification gradient boosting + cost-sensitive/imbalanced ordinal classification

Türkçe:
- dengesiz sınıflandırma gradyan artırma (kavramsal doğrulama)
- sıralı sınıflandırma yöntemleri (kavramsal doğrulama)