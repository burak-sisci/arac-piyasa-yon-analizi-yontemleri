---
faz_no: 03
faz_adi: "Finansal Piyasa Yön Tahmini Literatürü"
tarih: 2026-07-13
kapsam_ozeti: "Finansal yön tahmini literatüründen araç piyasasına aktarılabilir metodolojik dersler ve aktarılamazlık sınırları"
bagimli_oldugu_fazlar: [01]
durum: tamamlandi 
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 24
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-13
---

# Faz 03 — Finansal Piyasa Yön Tahmini Literatüründen Araç Piyasasına Aktarılabilir Metodolojik Dersler

## TL;DR

- Finansal yön tahmini literatürünün en sağlam ve **aktarılabilir** çıktısı metodolojik disiplindir (leakage kontrolü, çoklu-test düzeltmesi, ekonomik anlamlılık ayrımı), performans rakamları değildir; literatürdeki yüksek doğruluk iddialarının (%80-96) büyük kısmı metodolojik artefakt olarak yeniden değerlendirilmektedir ve gerçek out-of-sample yön doğruluğu tipik olarak %50-58 bandındadır.
- Araç piyasasının düşük etkinliği projenin **lehine** bir argümandır: Adaptive Market Hypothesis (Lo 2004) çerçevesinde öngörülebilirlik zamana ve piyasa koşuluna göre değişir ve etkinliğin düşük olduğu piyasalarda daha yüksektir — ancak bu, yüksek doğruluk garantisi değil, "sinyal sıfır değil" ihtimalinin daha güçlü olması anlamına gelir.
- En kritik negatif bulgu: Finansal ML'nin sınıf-dengesizliği araç kutusunun büyük kısmı (özellikle SMOTE ve agresif resampling) araç piyasasına **düşük** aktarılabilirliktedir; literatür resampling yerine class weighting / cost-sensitive loss / threshold-moving ve olasılık kalibrasyonunu önermektedir.
- Değerlendirmede accuracy tek başına yanıltıcıdır; MCC ve macro-F1 tercih edilmeli, ve "istatistiksel doğruluk" ile "ekonomik anlamlılık" arasındaki kopukluk açıkça raporlanmalıdır — bu ayrım araç piyasasına doğrudan aktarılabilir.
- Rejim değişimi (concept drift) araç piyasasında birebir karşılığı olan (kur şoku, vergi/ÖTV değişikliği, arz krizi) bir problemdir; literatürün sliding-window retraining ve drift-detection dersleri aktarılabilir, ancak yüksek-frekanslı drift-detection algoritmalarının çoğu aylık ufka **aktarılamaz**.

## Key Findings

1. **Gerçekçi yön doğruluğu üst sınırı düşüktür ve yüksek iddialar metodolojik olarak şüphelidir.** Kontrollü, sızıntısız çalışmalarda günlük/saatlik yön doğruluğu %50-58 bandındadır; 918 deneylik kontrollü bir karşılaştırmada MSE-eğitimli derin öğrenme mimarileri saatlik veride ortalama %50.08 (yani yazı-tura) yön doğruluğu vermiştir (arXiv 2603.16886). Buna karşın %80-96 iddia eden çalışmalar (Khaidem vd. 2016; Xinjie 2014 türevi) leakage ve look-ahead bias riski taşır.

2. **Piyasa etkinliği ile öngörülebilirlik ters ilişkilidir ve zaman-değişkendir (Adaptive Market Hypothesis).** Lo (2004) AMH, öngörülebilirliğin sabit olmadığını, piyasa koşullarıyla döngüsel biçimde değiştiğini öne sürer; Kim, Shamsuddin & Lim (2011, Dow Jones 1900-2009) öngörülebilirliğin kriz/belirsizlik dönemlerinde yükseldiğini, balon dönemlerinde düştüğünü göstermiştir. Araç piyasasının düşük etkinliği ve yüksek işlem maliyeti bu çerçevede öngörülebilirlik lehinedir.

3. **Sınıf dengesizliğinde resampling (özellikle SMOTE) olasılık kalibrasyonunu bozar; class weighting / cost-sensitive / threshold-moving üstündür.** van den Goorbergh, van Smeden, Timmerman & Van Calster (2022, JAMIA 29(9):1525-1534) Monte Carlo simülasyonu ve gerçek vaka çalışmasıyla şunu göstermiştir (birebir): *"The use of random undersampling, random oversampling, or SMOTE yielded poorly calibrated models: the probability to belong to the minority class was strongly overestimated. These methods did not result in higher areas under the ROC curve... similar results were obtained by shifting the probability threshold instead... Outcome imbalance is not a problem in itself, imbalance correction may even worsen model performance."*

4. **Accuracy yanıltıcıdır; MCC en güvenilir tekil metriktir.** Chicco & Jurman (2020, BMC Genomics 21:6, DOI 10.1186/s12864-019-6413-7): MCC *"produces a high score only if the prediction obtained good results in all of the four confusion matrix categories (true positives, false negatives, true negatives, and false positives)"* iken accuracy ve F1 *"can dangerously show overoptimistic inflated results, especially on imbalanced datasets."*

5. **İstatistiksel doğruluk ≠ ekonomik anlamlılık.** Pagliaro (2025, Electronics) derlemesi ve LQ45 (2016-2025) çalışması, istatistiksel olarak anlamlı modellerin işlem maliyeti sonrası ekonomik değer üretemediğini; birçok modelin Buy&Hold'un altında kaldığını raporlar. Bu ayrım araç piyasasına doğrudan aktarılır.

6. **Rejim değişimi model performansını çökertir; araç piyasasında birebir karşılığı vardır.** Concept drift literatürü (Gama vd.; Lu vd. 2019 "Learning under Concept Drift") sliding-window retraining, drift-detection (DDM, ADWIN, Page-Hinkley) ve ensemble adaptasyonunu önerir. Araç piyasasında kur şoku/ÖTV değişikliği = ani (abrupt) drift; enflasyon trendi = tedrijî (gradual) drift.

7. **Reprodüksiyon krizi finansal ML'de sistemiktir; yüksek performans iddialarına güvenilmemelidir.** Kapoor & Narayanan (2023, Patterns) 17 alanda leakage kaynaklı tekrarlanamazlık belgelemiştir (hakemli sürümde 294 makale). Harvey, Liu & Zhu (2016, RFS) faktör literatüründe t-istatistiği eşiğinin 2.0 değil 3.0 olması gerektiğini; Bailey & López de Prado (2014) çoklu testin Sharpe oranını şişirdiğini ve Deflated Sharpe Ratio gerektiğini göstermiştir. Nikolopoulos (2026, arXiv 2604.15531) "spurious predictability" mekanizmasını formelleştirmiştir.

## Details

### 1. Giriş: Neden Finansal Literatür? Aktarılabilirlik Çerçevesi

Fiyat *yönü* tahmini (up/down/stable) probleminin metodolojik olarak en olgun literatürü finansal piyasalardır (hisse, emtia, FX, kripto). Bu faz bir "finansal ML özeti" değildir; amaç, bu literatürden **metodolojik dersler** çıkarıp her birini araç piyasasının özellikleri filtresinden geçirmektir.

Araç piyasasının tanımlayıcı özellikleri (Faz 1'den): düşük frekans (aylık ufuk), endeks/segment düzeyi, ilan-tabanlı veri, düşük oynaklık, yüksek işlem maliyeti (alım-satım spreadi, komisyon, tescil), düşük piyasa etkinliği. Finansal literatürün büyük kısmı ise tam tersi bir piyasada üretilmiştir: yüksek frekans (günlük/dakikalık/tick), tekil varlık, işlem-tabanlı likit veri, yüksek oynaklık, düşük işlem maliyeti, yüksek etkinlik. Bu asimetri, "hangi bulgunun aktarılabilir olduğu" sorusunu her bölümde zorunlu kılar.

Temel gözlem: Finansal literatürün **pozitif** bulguları (belirli model X şu doğruluğu aldı) çoğu zaman aktarılamaz; **negatif ve metodolojik** bulguları (şu yöntem şu koşulda başarısız oldu, şu metrik yanıltıcı, şu validasyon leakage üretir) yüksek oranda aktarılabilir. Bu fazın tezi budur.

### 2. Yön Tahmininde Gerçekçi Performans Üst Sınırı

Literatürde yön doğruluğu iddiaları geniş bir yelpazede dağılır: bir uçta yazı-tura seviyesi (~%50), diğer uçta %90+ iddiaları. Bu dağılımın kendisi bir uyarı işaretidir.

**Gerçekçi bant.** Sızıntısız, kesin ayrık zaman-serisi ayrımı olan çalışmalarda günlük yön doğruluğu tipik olarak %50-58 bandındadır. 918 deneylik kontrollü bir karşılaştırma (arXiv 2603.16886, "A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting"), 9 model × 3 varlık sınıfı × 2 ufuk kombinasyonunda ortalama yön doğruluğunu %50.08 bulmuş ve "MSE-eğitimli derin öğrenme mimarileri saatlik finansal veride yazı-tura eşdeğeri yön tahmini üretir" sonucuna varmıştır. Dai & Zhang (2013) sonraki-gün modeliyle %44.52-58.2 aralığı raporlamıştır.

**Yüksek iddiaların metodolojik çaprazlaması.** %85-95 (Khaidem vd. 2016, Random Forest) veya %96.92 (belirli zaman-penceresinde) gibi iddialar, metodolojik eleştiri literatürüyle çaprazlandığında zayıflar. Kapoor & Narayanan (2023) bu tür yüksek sonuçların birincil nedeninin **leakage** olduğunu göstermiştir. Özellikle exponential smoothing/pürüzsüzleştirme uygulanmış hedef değişken (Khaidem vd.), gelecek bilgisini sızdırabilir. Bir çalışmada 88 günlük pencere için %96.92 doğruluk, temel bir look-ahead / overfitting sinyalidir.

**Neden düşük?** Getiri serileri martingale-fark yapısına yakındır; işaret (up/down) tahmini regresyondan daha kolay olsa da sinyal-gürültü oranı düşüktür. Nikolopoulos (2026), optimize edilmiş in-sample kazanan istatistiğinin Global Null (martingale-difference) altında bile Θ(√(log K_eff)) hızıyla büyüdüğünü göstermiştir — yani hiç sinyal olmasa bile yeterli sayıda spesifikasyon denenirse yüksek in-sample doğruluk ortaya çıkar.

> **Projeye Uygulanabilirlik:** Araç piyasası projesi için gerçekçi bir yön doğruluğu hedefi, üç-sınıf (up/down/stable) problemde naif/persistence baseline'ın anlamlı biçimde üzerinde bir MCC/macro-F1'dir; %70+ accuracy iddiaları peşinde koşmak metodolojik tehlike işaretidir. Aylık ufuk ve düşük oynaklık, günlük finansal serilere kıyasla daha az gürültü içerebilir (lehte), ama örneklem sayısı da düşer (aleyhte). Hedef, mutlak doğruluk değil, güvenilir biçimde ölçülmüş bir "naif baseline üzeri iyileşme" olmalıdır.

### 3. Sinyal-Gürültü, Piyasa Etkinliği ve Öngörülebilirlik

İleri seviye ekip EMH tanımını bilmektedir; burada yalnızca projeyle ilgili çıkarımlara odaklanıyoruz.

**Etkin piyasada yön tahmini neden zor?** Weak-form etkinlik altında fiyat geçmiş fiyat bilgisinden öngörülemez (random walk / martingale-difference). Han, Linton, Oka & Whang türü çalışmalar günlük getiri işaretinin istatistiksel olarak anlamlı ölçüde öngörülebildiğini gösterse de (Directional Predictability of Daily Stock Returns), bu öngörülebilirlik küçüktür ve işlem maliyeti sonrası çoğu zaman erir.

**Adaptive Market Hypothesis (AMH) — projenin lehine argüman.** Lo (2004) AMH, öngörülebilirliğin sabit olmadığını; piyasa koşullarına, katılımcı kompozisyonuna ve rekabete göre zamanla değiştiğini öne sürer. Kim vd. (2011, DJIA 1900-2009) öngörülebilirliğin kriz/belirsizlik dönemlerinde yükseldiğini, balon dönemlerinde ve "normal" dönemlere kıyasla değiştiğini göstermiştir. Urquhart & Hudson gelişmekte olan/az etkin piyasalarda öngörülebilirliğin daha yüksek olduğunu belgelemiştir. Grossman-Stiglitz paradoksu: mükemmel etkinlik imkânsızdır çünkü bilgi maliyetliyse kimse bilgi toplamaz.

**Araç piyasasına çıkarım.** Araç piyasası düşük etkinlikli (ilan-tabanlı, yüksek arama maliyeti, heterojen ürün, arbitraj zorluğu) olduğundan, AMH çerçevesinde öngörülebilirliğin daha yüksek olması *beklenir*. Bu, projenin temel varsayımını literatüre dayandıran en güçlü argümandır. **Ancak literatür bunu bir garanti olarak sunmaz:** düşük etkinlik "sinyal vardır" demek değil, "sinyal sıfır olmayabilir ve işlem maliyeti onu silmeyebilir" demektir. Ayrıca araç piyasasında amaç trading alpha değil, satın-alma/satış/stok kararlarını iyileştirmek olduğu için "ekonomik anlamlılık" eşiği finansal trading'den farklı ve daha ulaşılabilir olabilir.

> **Projeye Uygulanabilirlik:** Düşük etkinlik lehte bir ön koşuldur ama test edilmesi gereken bir hipotezdir, kabul edilmiş bir gerçek değil. AMH'nin doğrudan çıkarımı: model performansı zaman içinde sabit olmayacaktır (bkz. Bölüm 6). Baseline kurarken "piyasa etkin olmadığı için yüksek doğruluk almalıyız" beklentisi kurulmamalı; bunun yerine "naif baseline'ı yenip yenemediğimiz" ampirik olarak ölçülmelidir.

### 4. Sınıf Dengesizliği ve Maliyet-Duyarlı Öğrenme

Bu bölüm bu fazın en önemli **negatif bulgu** kümesini içerir.

**Yaklaşımlar.** Literatür dört ana aile tanımlar: (a) resampling (oversampling/SMOTE, undersampling), (b) class weighting / cost-sensitive learning, (c) loss fonksiyonu tasarımı (focal loss), (d) threshold-moving (karar eşiği kaydırma).

**SMOTE ve resampling'in gizli maliyeti (kritik negatif bulgu).** Klinik risk-tahmini literatürü (van den Goorbergh, van Smeden, Timmerman & Van Calster, 2022, JAMIA 29(9):1525-1534, DOI 10.1093/jamia/ocac093) Monte Carlo simülasyonu ve gerçek vaka çalışmasıyla şunu göstermiştir: random over/undersampling ve SMOTE'un tümü kötü kalibre modeller üretir (azınlık sınıfına ait olasılığın güçlü aşırı-tahmini), ROC eğrisi altındaki alanı (AUC) iyileştirmez ve aynı sensitivite/spesifisite iyileşmesi yalnızca karar eşiğini kaydırarak elde edilebilir; hatta **imbalance düzeltmesi model performansını kötüleştirebilir**. Kredi kartı sahtekârlık verisinde SMOTE'un tek müdahale olarak uygulanması yanlış-alarmları 165 kat artırırken (5 CV katında 35'ten 5.775'e) ROC-AUC'yi neredeyse değiştirmemiştir (~0.9806; IJCT). Bir tree-ensemble çalışması (arXiv 2606.29720) undersampling'in asıl tehlike olduğunu, SMOTE'un kalibrasyon maliyetinin küçük ama gerçek olduğunu ve tek bir post-hoc rekalibrasyon (Platt/isotonic) adımının hasarı gidereceğini göstermiştir.

**Focal loss ve cost-sensitive.** Focal loss (Lin vd. 2017) kolay örnekleri aşağı, zor örnekleri yukarı ağırlıklandırır; kredi skorlama ve sahtekârlık tespitinde etkilidir (LightGBM-focal, arXiv 2501.12285). Cost-sensitive learning yanlış-sınıflandırma maliyetlerini açıkça modele katar. Ancak finansal literatürde bile yanlış-sınıflandırma maliyetleri çoğu zaman gözlemlenemez/erişilemez.

**Threshold-moving ve kalibrasyon.** PT-bagging (arXiv 1606.08698) ve genel imbalance literatürü, doğal sınıf dağılımını koruyup karar eşiğini a posteriori kaydırmanın hem iyi kalibre olasılıklar verdiğini hem de ilgi metriğine uyarlanabildiğini gösterir.

> **Projeye Uygulanabilirlik:** Araç piyasasında olasılık kalibrasyonu (up/down/stable olasılıkları karar-desteği için kullanılacaksa) kritiktir. **Öneri: SMOTE gibi sentetik oversampling'e "otomatik refleks" olarak başvurmayın** (düşük aktarılabilirlik). Bunun yerine class weighting + threshold-moving + post-hoc kalibrasyon kombinasyonu tercih edilmeli. Not: Sınıf dengesizliğinin kaynağı olan label tasarımı (up/down/stable eşikleri) Faz 1 konusudur ve burada tekrar edilmez; ancak Faz 1'de seçilen "stable" bandı genişliği doğrudan dengesizlik oranını belirleyeceği için bu iki faz arasında sıkı bağ vardır — çapraz-referans önerilir.

### 5. Değerlendirme Metodolojisi: İstatistiksel vs Ekonomik Anlamlılık

**Accuracy neden yanıltıcı?** Dengesiz sınıflarda çoğunluk sınıfını tahmin eden trivial model yüksek accuracy alır. Üç-sınıf up/down/stable probleminde "stable" baskınsa, her şeye stable diyen model yanıltıcı biçimde başarılı görünür.

**Metrik tercihleri.** Chicco & Jurman (2020, BMC Genomics 21:6, DOI 10.1186/s12864-019-6413-7): MCC yalnızca dört konfüzyon-matrisi kategorisinin (TP, TN, FP, FN) tümünde iyi sonuç alındığında yüksek skor verir ve dengesiz verilerde accuracy/F1'in *"tehlikeli biçimde aşırı-iyimser şişirilmiş sonuçlar"* verebildiği durumlarda daha güvenilirdir. Macro-F1 her sınıfa eşit ağırlık verdiği için dengesizliğe dayanıklıdır; balanced accuracy sınıf-başı recall ortalamasıdır. Chicco, Tötsch & Jurman (2021) MCC'nin balanced accuracy, bookmaker informedness ve markedness'tan da daha güvenilir olduğunu göstermiştir.

**İstatistiksel–ekonomik kopukluk.** Pagliaro (2025, Electronics, DOI 10.3390/electronics14091721): istatistiksel metrikler (directional accuracy, precision/recall) sınıflandırma yeteneğini gösterir ama işlem maliyeti, market impact ve slippage sonrası ekonomik değere çevrilmez; "istatistiksel anlamlılık gösteren birçok model ekonomik değer üretemez". LQ45 (2016-2025) çalışması yön doğruluğu %49-54, AUC ~0.50-0.53 bulmuş, her stratejinin Buy&Hold'un altında kaldığını raporlamıştır. Moosa & Burns (2016) FX'te RMSE'de random walk'u yenmenin zor ama yön doğruluğu/kârlılıkta mümkün olduğunu — yani metrik seçiminin sonucu tersine çevirebildiğini — göstermiştir.

> **Projeye Uygulanabilirlik:** Birincil metrik MCC veya macro-F1 olmalı; accuracy yalnızca ikincil/tanımlayıcı olarak raporlanmalı. Araç piyasasında "ekonomik anlamlılık" = kararın (alım zamanlaması, fiyatlama, stok) gerçek maliyet/fayda karşılığıdır; yüksek MCC bile bir işlem-maliyeti/karar-fayda analizi olmadan tek başına "değerli model" anlamına gelmez. Bu ayrım finansal literatürden **yüksek aktarılabilirlikle** gelir.

### 6. Rejim Değişimi ve Dağılım Kayması (Concept Drift)

**Problem.** Finansal seriler durağan değildir; eğitim-test dağılım farkı (concept drift / regime change) modeli çökertir. Cavalcante & Oliveira; Gama vd. drift'in tahmin doğruluğunu negatif etkilediğini gösterir. Backtest-overfitting literatürü (Arian vd. 2024) finansal serilerin non-stationarity, autocorrelation, heteroskedasticity ve regime-shift ile karakterize olduğunu vurgular.

**Tespit ve adaptasyon.** Lu vd. (2019, "Learning under Concept Drift: A Review") üç adaptasyon ailesi tanımlar: (a) basit retraining (drift tespit edilince yeni model), (b) ensemble retraining (SEA, AWE, DWM, Adaptive Random Forest), (c) model ayarlama (CVFDT). Drift tespiti: DDM, ECDD, ADWIN, Page-Hinkley. Sliding-window retraining: eski veriyi "unutup" güncel pencereyle model güncelleme.

**Araç piyasasına birebir karşılık (bu bağlantıyı özellikle vurguluyoruz).** Araç piyasasında drift kaynakları doğrudandır ve gözlemlenebilir:
- **Ani (abrupt) drift:** kur şoku, ÖTV/vergi değişikliği, ithalat kısıtı → dağılımda kesikli sıçrama.
- **Tedrijî (gradual) drift:** enflasyon trendi, faiz döngüsü, ikinci-el arz normalizasyonu.
- **Tekrarlayan (recurring) drift:** mevsimsel talep örüntüleri.
Bu, finansal serilerdeki soyut "rejim" kavramının araç piyasasında ölçülebilir dış değişkenlere bağlanabildiği anlamına gelir — finansal literatürün gizli/latent rejim tespiti (HMM, Baum-Welch) yaklaşımlarına kıyasla avantajlıdır.

**Aktarılamayan kısım (negatif bulgu).** Yüksek-frekanslı drift-detection algoritmalarının çoğu (intraday, tick-level, VFDT/CVFDT gibi hızlı akış madenciliği) aylık ufka **aktarılamaz**: aylık veride yılda yalnızca 12 gözlem olduğundan istatistiksel drift-detection testleri (pencere-tabanlı) yeterli güç bulamaz. Araç piyasasında drift, algoritmik tespitten çok **dışsal olay-tabanlı** (kur/vergi takvimi) izlenmelidir.

> **Projeye Uygulanabilirlik:** (i) Eğitim-test ayrımı mutlaka kronolojik olmalı (rastgele değil — bkz. Bölüm 7). (ii) Model periyodik olarak yeniden eğitilmeli (sliding/expanding window); retraining sıklığı aylık ufka uygun seçilmeli. (iii) Bilinen dışsal şoklar (kur, ÖTV) drift göstergesi olarak izlenmeli; şok sonrası performans düşüşü beklenmelidir. (iv) Backtest/validasyon protokol *tasarımı* (purged CV, walk-forward detayı) ayrı bir fazın konusudur; burada yalnızca "kronolojik ayrım şart, rejim-farkında değerlendirme gerekli" genel uyarısı verilir.

### 7. Reprodüksiyon Krizi ve Güvenilmemesi Gereken İddialar

Bu bölüm baseline kurarken hangi iddialara güvenilmemesi gerektiğine dair somut uyarılar içerir.

**Leakage sistemiktir.** Kapoor & Narayanan (2023, Patterns 4(9):100804, DOI 10.1016/j.patter.2023.100804): 17 bilimsel alanda leakage kaynaklı tekrarlanamazlık (hakemli Patterns sürümünde 294 makale; erken arXiv 2207.07048 sürümünde 329 rakamı verilir — fark sürümler arasıdır); 8 tipten oluşan bir leakage taksonomisi (*"eight types of leakage, ranging from textbook errors to open research problems"*: gelecek-türevli özellikler, train-test kontaminasyonu, ön-işlemenin tüm-örneklem üzerinden yapılması, vb.). "Data leakage en büyük tekrarlanamazlık nedenidir."

**Çoklu test / p-hacking / factor zoo.** Harvey, Liu & Zhu (2016, RFS 29(1):5-68, DOI 10.1093/rfs/hhv059): en az 316 faktör test edildiğinden yeni bir faktörün t-istatistik eşiği 2.0 değil **3.0** olmalı — birebir: *"a newly discovered factor needs to clear a much higher hurdle, with a t-ratio greater than 3.0... we argue that most claimed research findings in financial economics are likely false."* Hou, Xue & Zhang (2020, "Replicating Anomalies", RFS 33(5):2019-2133, DOI 10.1093/rfs/hhy131): NYSE breakpoint + değer-ağırlıklı getirilerle 452 anomalinin **%65'i** tekli-test eşiği |t|=1.96'yı bile geçemez; çoklu-test eşiği 2.78'de başarısızlık oranı **%82'ye** çıkar — birebir: *"65% of the 452 anomalies... cannot clear the single test hurdle of the absolute t-value of 1.96. Imposing the higher multiple test hurdle of 2.78 at the 5% significance level raises the failure rate to 82%... capital markets are more efficient than previously recognized."* McLean & Pontiff (2016): yayınlanan faktörler yayın sonrası performanslarını kaybeder.

**Backtest overfitting.** Bailey, Borwein, López de Prado & Zhu (2014, "Pseudo-Mathematics and Financial Charlatanism") ve Bailey & López de Prado (2014, "The Deflated Sharpe Ratio", JPM 40(5):94-107): çoklu deneme Sharpe oranını matematiksel olarak şişirir; standart hold-out/OOS validasyon backtest overfitting'i yakalayamaz; Deflated Sharpe Ratio deneme sayısı, skewness ve kurtosis için düzeltir. López de Prado ("The 10 Reasons Most Machine Learning Funds Fail", JPM 2018): ML algoritmaları sinyal olmasa bile her zaman bir örüntü bulur.

**Spurious predictability (subagent bulgusu, entegre).** Nikolopoulos (2026, arXiv 2604.15531 [q-fin.ST], University of Peloponnese, tek yazarlı, hakem-öncesi preprint): "spurious predictability" bir "Cascade of Spuriousness" ile ortaya çıkar — leakage yapay sinyal yaratır, seleksiyon/spesifikasyon-arama biası bunu büyütür, spesifikasyon hatası risk-primini alpha sanır. Formel sonuç: optimize edilmiş in-sample kazanan istatistik Global Null altında ≈√(2 ln(2K)) büyür (K≈100 bile şansa dayalı anlamlılık üretir); doğru, ayrık, kronolojik walk-forward değerlendirme aynı null altında O_p(1) sınırlı kalır. Yazar Bergmeir vd. (2018)'e atıfla "rastgele cross-validation zamansal sırayı bozar ve look-ahead bias üretir" der. Ana mesaj (birebir): *"in weak-signal, temporally ordered data, reported performance is not credible unless it survives (i) temporally causal validation, (ii) falsification under structured nulls, and (iii) explicit adjustment for adaptive specification search."* Somut uyarılar: in-sample/backtest Sharpe/t-istatistik/R²'ye güvenme; zaman-serisinde rastgele/shuffled CV kullanma; brüt getiriyi alpha sanma (faktör-düzeltmesi yap); tüm pipeline'ı sentetik null'lar üzerinde çalıştırıp "sinyal halüsinasyonu" yapıp yapmadığını test et.

> **Projeye Uygulanabilirlik:** Baseline kurarken (i) yüksek accuracy iddia eden hazır çalışmaları *referans hedef* olarak alma — büyük kısmı leakage taşır; (ii) çok sayıda model/hiperparametre denenip en iyisi raporlanacaksa çoklu-test farkındalığı şart (naif t-istatistik/accuracy güvenilmez); (iii) rastgele k-fold CV kullanma, kronolojik ayrım zorunlu; (iv) mümkünse pipeline'ı bir "null" (karıştırılmış hedef / rastgele-yürüyüş) verisinde çalıştırıp yapay sinyal üretip üretmediğini kontrol et (falsifikasyon audit'i). Backtest protokol detayı ayrı fazın konusudur; buradaki uyarılar kavramsaldır.

### 8. AKTARILABİLİRLİK MATRİSİ

| Finansal Literatür Bulgusu | Dayandığı Piyasa Özelliği | Araç Piyasasında Karşılığı Var mı? | Aktarılabilirlik | Gerekçe | Uyarlama Gerekiyorsa Nasıl |
|---|---|---|---|---|---|
| Gerçekçi yön doğruluğu %50-58 bandındadır (arXiv 2603.16886) | Yüksek etkinlik, yüksek frekans, martingale-fark getiriler | Kısmen; araç daha az etkin ama örneklem az | Orta | Düşük etkinlik lehine ama aylık ufuk örneklem sayısını düşürür; üst sınır belirsizleşir | Hedefi "naif baseline üzeri MCC iyileşmesi" olarak tanımla, mutlak % hedefleme |
| Öngörülebilirlik zamana/koşula göre değişir (AMH, Lo 2004; Kim vd. 2011) | Piyasa etkinliğinin zaman-değişkenliği | Evet, güçlü | Yüksek | Araç piyasasında da öngörülebilirlik rejime bağlı değişir | Rejim-farkında değerlendirme; dönemsel performans raporla |
| Düşük etkinlik → daha yüksek öngörülebilirlik (Urquhart & Hudson) | Etkinlik derecesi | Evet | Yüksek (lehte argüman) | Araç piyasası yapısal olarak az etkin | Bir hipotez olarak test et, garanti sayma |
| SMOTE/agresif oversampling (imbalance çözümü) | i.i.d. büyük veri, dengesiz sınıf | Sınırlı; kalibrasyonu bozar | Düşük | SMOTE kalibrasyonu bozar, AUC iyileştirmez, yanlış-alarm şişirir (van den Goorbergh vd. 2022; IJCT) | Kullanma; class weighting + threshold-moving + post-hoc kalibrasyon tercih et |
| Class weighting / cost-sensitive loss | Dengesiz sınıf, bilinen maliyet | Evet | Yüksek | Doğal dağılımı korur, kalibrasyon bozmaz | Maliyet matrisi araç piyasası karar-faydasına göre tanımla |
| Focal loss (zor örneğe odak) | Aşırı dengesizlik (ör. sahtekârlık) | Kısmen | Orta | Aşırı dengesizlik araç piyasasında olmayabilir (stable bandına bağlı) | Ancak "stable" çok baskınsa dene; değilse gereksiz karmaşıklık |
| MCC / macro-F1 accuracy'den üstün (Chicco & Jurman 2020) | Sınıf dengesizliği (alan-bağımsız) | Evet | Yüksek | Metrik matematiği piyasadan bağımsızdır | Birincil metrik MCC/macro-F1; accuracy ikincil |
| İstatistiksel ≠ ekonomik anlamlılık (Pagliaro 2025) | Yüksek işlem maliyeti, trading getirisi | Evet | Yüksek | Araç piyasasında da yüksek doğruluk ≠ karar-faydası | "Ekonomik anlamlılık" = karar maliyet/fayda; ayrı raporla |
| Concept drift performansı çökertir; sliding-window retraining (Lu vd. 2019) | Non-stationarity, rejim değişimi | Evet, birebir (kur/vergi/arz) | Yüksek | Araç piyasasında drift dışsal olaylarla ölçülebilir | Periyodik retraining; dışsal şok izleme |
| Yüksek-frekanslı drift-detection (VFDT/CVFDT, ADWIN intraday) | Tick/dakikalık akış, çok gözlem | Hayır | Düşük/Yok | Aylık veride yılda ~12 gözlem; testler güçsüz | Algoritmik tespit yerine olay-takvimi tabanlı izleme |
| Rastgele k-fold CV | i.i.d. veri varsayımı | Hayır (zaman-serisi) | Yok | Zamansal sırayı bozar, look-ahead/leakage üretir (Bergmeir vd. 2018; Nikolopoulos 2026) | Kronolojik ayrım; walk-forward (detay ayrı faz) |
| Çoklu-test t-eşiği 3.0, Deflated Sharpe (Harvey vd. 2016; Bailey & LdP 2014) | Binlerce strateji/faktör denemesi | Evet | Yüksek (kavramsal) | Çok model denenirse şişme kaçınılmaz | Denenen model sayısını raporla, naif anlamlılığa güvenme |
| Yüksek accuracy iddiaları (%85-96, RF/SVM çalışmaları) | Tekil hisse, günlük, sızıntı riski | Hayır | Yok/Düşük | Büyük kısmı leakage/overfitting (Kapoor & Narayanan 2023) | Referans hedef alma; kendi sızıntısız baseline'ını kur |
| Latent rejim tespiti (HMM, Baum-Welch) | Gözlemlenemeyen piyasa durumları | Kısmen | Orta | Araç piyasasında rejim çoğu zaman gözlemlenebilir (dışsal) | Latent model yerine dışsal-değişken tabanlı rejim tercih et |

### 9. Açık Sorular / Literatürde Net Olmayanlar

- **Düşük frekans + düşük etkinlik kombinasyonunun net üst sınırı literatürde net değil.** Finansal literatür ya yüksek-frekans/yüksek-etkinlik ya da düşük-frekans/emtia üzerine yoğunlaşmış; araç piyasasının tam profiline (aylık, ilan-tabanlı, segment-düzeyi) doğrudan karşılık gelen sızıntısız benchmark bulunamadı.
- **Üç-sınıf (up/down/stable) yön tahmininde MCC'nin çok-sınıflı davranışı** ikili duruma kıyasla daha az çalışılmış; multiclass MCC güvenilir ama optimal eşik-belirleme literatürü ikili kadar olgun değil.
- **AMH'nin araç piyasası gibi finansal-olmayan varlık piyasalarına genişletilmesi** doğrudan test edilmemiş; çıkarım analojiktir, ampirik doğrulama projeye aittir.
- **SMOTE'un kalibrasyon hasarının büyüklüğü** literatürde çelişkilidir: klinik literatür (van den Goorbergh vd. 2022) "kaçının, hatta kötüleştirebilir" derken, tree-ensemble çalışması (arXiv 2606.29720) "küçük, rekalibrasyonla giderilir" der. Bu çelişki açıkça işaretlenmiştir; araç piyasası bağlamında ampirik test gerekir.
- **Aylık ufukta drift-detection'ın hangi minimum gözlem sayısıyla güç kazandığı** net değildir; literatür yüksek-frekans odaklıdır.

## Recommendations

**Aşama 1 — Baseline ve değerlendirme çerçevesi (hemen):**
- Birincil metrik olarak **MCC** ve **macro-F1** kullan; accuracy'yi yalnızca tanımlayıcı olarak raporla.
- **Kronolojik train-test ayrımı** zorunlu; rastgele k-fold CV kesinlikle kullanma.
- Naif/persistence baseline (bir önceki dönemin yönü) ve "her şeye stable" trivial baseline'ı referans al; model bunları MCC'de anlamlı biçimde geçmiyorsa "sinyal yok" sonucu raporlanmalı (değerli negatif bulgu).

**Aşama 2 — Sınıf dengesizliği (Faz 1 label tasarımı netleştikten sonra):**
- SMOTE/oversampling'e otomatik başvurma. Önce **class weighting + threshold-moving** dene.
- Olasılık çıktıları karar-desteği için kullanılacaksa **post-hoc kalibrasyon** (Platt/isotonic) uygula ve kalibrasyonu diskriminasyonla birlikte raporla.

**Aşama 3 — Rejim/drift yönetimi:**
- **Periyodik retraining** (sliding/expanding window) protokolü kur.
- Bilinen dışsal şokları (kur, ÖTV/vergi, arz) drift göstergesi olarak izle; şok sonrası dönemleri ayrı değerlendir.

**Aşama 4 — Güvenilirlik audit'i:**
- Denenen model/hiperparametre sayısını kayıt altına al; çok sayıda deneme varsa çoklu-test farkındalığıyla raporla.
- Pipeline'ı bir **null veri** (karıştırılmış hedef veya rastgele-yürüyüş) üzerinde çalıştır; "yapay sinyal" üretiyorsa workflow'da leakage var demektir.

**Eşik/benchmark ne zaman kararı değiştirir:**
- Model MCC'de naif baseline'ı geçemiyorsa → mimari değiştirmek yerine özellik/veri sorununu araştır.
- Kronolojik OOS performansı in-sample'dan dramatik düşükse → leakage veya overfitting; validasyon protokolünü ayrı fazda yeniden tasarla.
- Kur/vergi şoku sonrası performans çöküyorsa → retraining sıklığını artır veya rejim-değişkeni ekle.

## Caveats

- Bu faz **metodolojik dersler** fazıdır; bilinçli olarak model-mimari karşılaştırması, label tasarımı, araç-piyasası iktisadi dinamikleri ve backtest protokol detayı KAPSAM DIŞIDIR (ilgili fazlara bırakılmıştır).
- Finansal literatürün büyük kısmı araç piyasasından farklı bir piyasa profilinde üretilmiştir; aktarılabilirlik değerlendirmeleri analojik akıl yürütmeye dayanır ve projede ampirik doğrulama gerektirir.
- Bazı kaynaklar (özellikle Nikolopoulos 2026) hakem-öncesi preprint'tir; bulguları bağımsız olarak tekrarlanmamıştır ve buna göre işaretlenmiştir.
- Yüksek-doğruluk iddia eden çalışmalar bilinçli olarak "hedef" değil "uyarı örneği" olarak kullanılmıştır; puan tablosu üretilmemiştir (kapsam kuralı gereği).
- Faz 1 ile potansiyel bağ: "stable" bandının genişliği sınıf dengesizliği oranını doğrudan belirler; bu fazın imbalance önerileri Faz 1 label kararlarıyla birlikte okunmalıdır (çapraz-referans). İki faz arasında açık bir çelişki tespit edilmemiştir.

## Kaynakça

- **Lo, A. W. (2004). "The Adaptive Markets Hypothesis." Journal of Portfolio Management 30(5):15-29.** — Öngörülebilirliğin zaman-değişkenliği; araç piyasasının düşük etkinliği lehine temel teorik dayanak.
- **Kim, J. H., Shamsuddin, A. & Lim, K.-P. (2011). "Stock return predictability and the adaptive markets hypothesis." Journal of Empirical Finance.** — DJIA 1900-2009; öngörülebilirliğin kriz dönemlerinde yükseldiği ampirik kanıtı.
- **Urquhart, A. & Hudson, R. — Adaptive market hypothesis stock return predictability.** — Az etkin piyasalarda öngörülebilirliğin daha yüksek olduğu bulgusu.
- **Chicco, D. & Jurman, G. (2020). "The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy." BMC Genomics 21:6. DOI 10.1186/s12864-019-6413-7.** — MCC'nin dengesiz sınıflarda üstünlüğü; metrik seçimi için birincil kaynak.
- **Chicco, D., Tötsch, N. & Jurman, G. (2021). "The MCC is more reliable than balanced accuracy, bookmaker informedness, and markedness." BioData Mining 14. DOI 10.1186/s13040-021-00244-z.** — MCC'nin diğer dengeli metriklere üstünlüğü.
- **Pagliaro, A. (2025). "Artificial Intelligence vs. Efficient Markets." Electronics 14(9):1721. DOI 10.3390/electronics14091721.** — İstatistiksel vs ekonomik anlamlılık ayrımı; kritik derleme.
- **Kapoor, S. & Narayanan, A. (2023). "Leakage and the reproducibility crisis in machine-learning-based science." Patterns 4(9):100804. DOI 10.1016/j.patter.2023.100804.** — Leakage taksonomisi (8 tip, 294 makale/17 alan); yüksek doğruluk iddialarına güvensizlik gerekçesi.
- **Harvey, C. R., Liu, Y. & Zhu, H. (2016). "…and the Cross-Section of Expected Returns." Review of Financial Studies 29(1):5-68. DOI 10.1093/rfs/hhv059.** — Çoklu-test, t-eşiği 3.0, factor zoo; ≥316 faktör.
- **Hou, K., Xue, C. & Zhang, L. (2020). "Replicating Anomalies." Review of Financial Studies 33(5):2019-2133. DOI 10.1093/rfs/hhy131.** — 452 anomalinin %65'i |t|=1.96'yı, %82'si çoklu-test eşiği 2.78'i geçemez.
- **Bailey, D. H. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." Journal of Portfolio Management 40(5):94-107.** — Seleksiyon biası ve backtest overfitting düzeltmesi.
- **Bailey, Borwein, López de Prado & Zhu (2014). "Pseudo-Mathematics and Financial Charlatanism." Notices of the AMS 61(5):458-471.** — Backtest overfitting'in OOS performansına etkisi.
- **López de Prado, M. (2018). "The 10 Reasons Most Machine Learning Funds Fail." Journal of Portfolio Management 44(6):120-133.** — ML'in her zaman örüntü bulması; finansal ML tuzakları.
- **Lu, J. vd. (2019). "Learning under Concept Drift: A Review." (arXiv 2004.05785 / IEEE TKDE).** — Drift tespit ve adaptasyon taksonomisi.
- **Arian, H. R., Norouzi M. D. & Seco, L. A. (2024). "Backtest Overfitting in the Machine Learning Era." (SSRN 4686376 / Knowledge-Based Systems).** — Finansal serilerin non-stationarity/regime-shift karakteri; OOS test yöntemleri.
- **Nikolopoulos, S. D. (2026). "Spurious Predictability in Financial Machine Learning." arXiv 2604.15531 [q-fin.ST].** — "Cascade of Spuriousness"; falsifikasyon audit'i; hakem-öncesi preprint (işaretli).
- **van den Goorbergh, R., van Smeden, M., Timmerman, D. & Van Calster, B. (2022). "The harm of class imbalance corrections for risk prediction models." JAMIA 29(9):1525-1534. DOI 10.1093/jamia/ocac093.** — Imbalance düzeltmelerinin kalibrasyon hasarı; SMOTE'a karşı birincil kritik kaynak.
- **Liu, Z. (2026). "The Hidden Cost of Resampling." arXiv 2606.29720.** — SMOTE kalibrasyon hasarı küçük, rekalibrasyonla giderilir (karşı-bulgu, çelişki işaretli).
- **"Empirical Evidence of Posterior Probability Bias Under SMOTE." IJCT.** — SMOTE'un yanlış-alarmı 165 kat şişirdiği (35→5.775) kredi-kartı örneği.
- **PT-bagging (2016). arXiv 1606.08698.** — Threshold-moving ile iyi kalibre olasılıklar.
- **"A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting." arXiv 2603.16886.** — 918 deney; ortalama yön doğruluğu %50.08.
- **Moosa, I. & Burns, K. (2016). "The random walk as a forecasting benchmark: drift or no drift?" Applied Economics 48(43):4131-4142.** — Metrik seçiminin (RMSE vs yön doğruluğu) sonucu tersine çevirmesi.
- **Han, Linton, Oka & Whang — "Directional Predictability of Daily Stock Returns."** — Günlük işaretin istatistiksel öngörülebilirliği ve ekonomik anlamlılık.
- **Bergmeir, C., Hyndman, R. J. & Koo, B. (2018). "A note on the validity of cross-validation for evaluating autoregressive time series prediction." Computational Statistics & Data Analysis 120:70-83.** — Zaman-serisinde rastgele CV'nin geçersizliği.
- **Khaidem, L. vd. (2016). "Predicting the direction of stock market prices using random forest." arXiv 1605.00003.** — Yüksek doğruluk (%85-95) iddiası; uyarı örneği olarak (leakage riski) kullanıldı.
- **Doğan, S. & Büyükkör, Y. (2022). "Makine Öğrenmesi ile Finansal Zaman Serisi Tahminleme." Ankara HBV Üniv. İİBF Dergisi 24(3):1205-1230. DOI 10.26745/ahbvuibfd.1191080.** — Türkçe literatür; finansal zaman serisi ML tahmini genel çerçevesi.

## Kullanılan Nihai Arama Sorguları

İngilizce: "stock price direction prediction accuracy realistic upper bound"; "financial machine learning backtest overfitting multiple testing"; "concept drift regime change financial time series classification"; "class imbalance cost sensitive learning financial prediction focal loss"; "Matthews correlation coefficient macro F1 imbalanced classification evaluation"; "market efficiency predictability directional forecasting economic significance transaction costs"; "reproducibility crisis machine learning finance data leakage Kapoor Narayanan"; "Harvey Liu Zhu cross-section expected returns factor zoo multiple testing t-stat"; "low frequency monthly commodity price direction forecasting machine learning"; "adaptive market hypothesis Lo time-varying predictability"; "concept drift adaptation retraining sliding window ensemble time series"; "random walk hard to beat directional forecasting benchmark naive"; "deflated Sharpe ratio Bailey Lopez de Prado selection bias"; "SMOTE oversampling criticism probability calibration threshold moving imbalanced"; "stock direction prediction survey systematic review accuracy inflated data leakage López de Prado ten reasons machine learning funds fail".

Türkçe: "finansal zaman serisi yön tahmini makine öğrenmesi"; "piyasa etkinliği öngörülebilirlik".

Subagent (hedefli): "Spurious Predictability in Financial Machine Learning" (arXiv 2604.15531) — yazar, tez, kantitatif bulgu ve pratik öneriler.