---
faz_no: 07
faz_adi: "Validasyon, Metrik Seçimi ve Backtest Metodolojisi"
tarih: 2026-07-13
kapsam_ozeti: "Düşük-frekanslı rejim-değişimli yön sınıflaması için sızıntısız validasyon, dürüst metrik ve falsifikasyon protokolü"
bagimli_oldugu_fazlar: [01, 03, 06]
durum: tamamlandi
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 26
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-15
---

# FAZ 7 — Validasyon, Metrik Seçimi ve Backtest Metodolojisi

## TL;DR

- **Az-gözlem + kronoloji + rejim değişimi üçlüsü, "çok-fold" tekniklerini elemektedir**: aylık segment-düzeyi veride toplam gözlem onlarla/yüzlerle ölçüldüğü için önerilen omurga, **genişleyen-pencere (expanding-window) walk-forward** artı, örneklem izin veriyorsa **purged + embargoed** blok-CV'dir; gerçekçi test dönemi sayısı **tipik olarak 6–24 aylık adım** aralığındadır, "50–100 fold" önerileri bu problemde geçersizdir. Nested CV çoğu zaman uygulanamaz; yerine tek bir tam-dışsal (hold-out) son dönem + sıkı bütçelenmiş hiperparametre araması önerilir (Bergmeir & Benítez 2012; López de Prado 2018; Vabalas ve ark. 2019).
- **N7 (falsifikasyon) bu fazın kalbi ve somutlaştırılabilir**: hedefi karıştıran **permütasyon/shuffle testi** (Ojala & Garriga 2010), **random-walk/persistence benchmark'ı** ve **denenen model sayısının kaydı → deflated/düzeltilmiş metrik** (Bailey & López de Prado 2014; Fabozzi & López de Prado 2018) birlikte "pipeline sahte sinyal üretiyor mu?" sorusunu ölçülebilir hale getirir. **"Sinyal yok" sonucu (N6) bu protokolde geçerli ve raporlanabilir bir çıktıdır.**
- **Dürüstlük sözleşmesi = raporlama seti**: birincil metrik olarak **çok-sınıflı MCC (Gorodkin 2004) + per-class precision/recall + blok-bootstrap güven aralığı**, baseline'lara karşı **Pesaran–Timmermann (2009) serisel-korelasyona dayanıklı yön testi**, **rejim-ayrık raporlama** (kur şoku/ÖTV sonrası), ve **denenen kombinasyon sayısı** raporlanmazsa sonuç güvenilmez sayılmalıdır (Bölüm 9 kontrol listesi bu sözleşmenin somut halidir).

## Key Findings

1. **CV yöntemi seçimi az-gözlemde bir bütçe problemidir, doğruluk problemi değildir.** Bergmeir & Hyndman geleneği, zaman serisinde kronolojik out-of-sample değerlendirmenin zorunluluğunu; López de Prado (2018) ise etiketlerin zaman-örtüşmesi olduğunda **purging + embargo** olmadan k-fold'un iyimser yanlılık ürettiğini gösterir. N5'in "rastgele k-fold YASAK, kronolojik ayrım zorunlu" kararı literatürle **büyük ölçüde tutarlıdır** (bir gerilim noktası Bölüm 1'de işaretlendi).
2. **Leakage'ın en sinsi biçimi bu problemde makro değişkenlerin vintage/yayın-gecikmesi sorunudur.** Bir makro göstergenin *referans dönemi* ile *ilk yayım tarihi* arasında haftalar-aylar fark vardır; "en son revize seri" ile eğitim, gelecekten bilgi sızdırır (Croushore & Stark; ECB now-casting literatürü). Kapoor & Narayanan (2023) bunu "L3.1 temporal leakage" olarak taksonomize eder.
3. **MCC bu 3-sınıflı dengesiz problem için doğru birincil metriktir** (Chicco & Jurman 2020); ancak çok-sınıflı halinin **Gorodkin (2004) R_K formülü** ile hesaplanması ve micro-averaged MCC'nin accuracy'ye dejenere olmaması gözetilmelidir.
4. **Güven aralığı zaman serisinde i.i.d.-bootstrap ile değil, blok-bootstrap ile üretilmelidir** (Künsch 1989; Politis & Romano); blok uzunluğu ~n^(1/3) mertebesinde, ama az-gözlemde blok sayısı kritik biçimde azalır — bu bir sınırlamadır, gizlenmemelidir.
5. **Anlamlılık testi yön-bağlamına uyarlanmalıdır.** Diebold–Mariano (1995) + Harvey–Leybourne–Newbold (1997) küçük-örneklem düzeltmesi puan-tahmini için; **yön doğruluğu için Pesaran–Timmermann (2009)** serisel-korelasyona ve çok-kategoriye dayanıklı testtir. Küçük örneklemde PT testleri **over-sized**'dır (N≈75'te bile PT2009 hâlâ oversized) — bu nedenle **bootstrap-tabanlı** anlamlılık önerilir.
6. **Çoklu-test farkındalığı (N7) için MinBTL ve deflated metrikler operasyoneldir.** Bailey, Borwein, López de Prado & Zhu (2014): MinBTL ≈ 2·ln(N)/E[max]², yani denenen bağımsız model sayısı N arttıkça gereken minimum out-of-sample uzunluğu artar; kaynaktaki somut örnek — **beş yıllık günlük veriyle en fazla ~45 bağımsız konfigürasyon** test edilmelidir — az-gözlemde **denenecek model sayısını sert biçimde sınırlamayı** zorunlu kılar.
7. **Rejim-farkında değerlendirme (N8/N2) bir "keşfedilecek sonuç" değil, önceden ilan edilen bir rapor kesitidir.** Bilinen şok tarihleri (kur şoku, ÖTV değişikliği) etrafında ayrı MCC raporu + şok-öncesi/sonrası performans farkı, N2'nin "rejim geçişinde düşüş beklenir" hipotezini doğrudan test eder.

## Details

### 1. Giriş: Az-Gözlem + Kronoloji + Rejim Değişimi Kısıtları

Bu faz, projenin **"sonuçlara güvenilebilir mi?"** sorusunu güvence altına alır. Üç kısıt aynı anda geçerlidir ve birbirini şiddetlendirir:

- **Az-gözlem**: Aylık, segment-düzeyi yön etiketi → toplam gözlem onlarla/yüzlerle ölçülür. Bu, validasyon tasarımının merkezi kısıtıdır (N5). Vabalas ve ark. (2019, *PLOS ONE* 14(11):e0224365) küçük örneklemde standart k-fold'un sistematik iyimser yanlılık ürettiğini şu verbatim ifadeyle gösterir: *"K-fold Cross-Validation (CV) produces strongly biased performance estimates with small sample sizes, and the bias is still evident with sample size of 1000. Nested CV and train/test split approaches produce robust and unbiased performance estimates regardless of sample size."* Aynı çalışma, **feature selection'ın havuzlanmış (pooled) veride yapılmasının** yanlılığa hiperparametre ayarından bile **daha fazla** katkıda bulunduğunu belirtir (*"feature selection if performed on pooled training and testing data is contributing to bias considerably more than parameter tuning"*) — bu, Bölüm 3'teki L1.3 kuralının önceliğini doğrudan destekler.
- **Kronoloji**: N5 gereği rastgele k-fold yasaktır. Bergmeir & Benítez (2012, *Information Sciences* 191:192–213) ve Bergmeir, Hyndman & Koo (2018, *CSDA* 120:70–83) zaman serisinde CV'nin ancak model artıkları korelasyonsuzsa geçerli olabileceğini gösterir.
- **Rejim değişimi**: N8/N2 gereği dışsal şoklar (kur şoku, ÖTV) koşullu dağılımı (P(y|X)) değiştirir — literatürde **concept drift** (Gama ve ark. 2014). N2, arz değişkeni rejime bağlı olduğu için rejim geçişlerinde performans düşüşü öngörür; bu düşüş ölçülmelidir.

**N5/N6/N7/N8 ile tutarlılık kontrolü ve AÇIK ÇELİŞKİ İŞARETİ**: López de Prado (2018) ve Arnott, Harvey & Markowitz (2019) tam da "az veri + kronoloji + non-stationarity" koşullarını hedef alır; bu yönüyle çelişki yoktur. **Ancak** Bergmeir & Benítez (2012), belirli koşullarda (durağan seri, korelasyonsuz artık) **bloke-CV'yi standart olarak önerir** — verbatim: *"the use of a blocked form of cross-validation for time series evaluation became the standard procedure, thus using all available information and circumventing the theoretical problems."* Bu, N5'in katı "kronolojik ayrım zorunlu, tek-yönlü" kuralıyla **gerilim** yaratır. Bu fazın kararı: **rejim değişimi + non-stationarity nedeniyle N5 korunur** (bloke-CV durağanlık varsayar, bu problemde ihlal edilir); bloke-CV yalnızca purge+embargo ile ve **yardımcı/ikincil** tahmin olarak kullanılabilir. Bu bir açık işaretlenmiş çelişkidir; kör biçimde bloke-CV'ye geçilmemelidir.

**Projeye Uygulanabilirlik**: Toplam gözlem sayısı ilk iş olarak sayılmalı; N < ~50 ise hiçbir istatistiksel iddia "güvenilir" ilan edilmemeli, yalnızca "keşifsel/negatif bulgu" statüsü verilmelidir.

### 2. Zaman Serisi CV Yöntemleri ve Az-Gözlemde Seçim

**(a) Walk-forward (expanding vs sliding).** Genişleyen pencere (anchored) tüm geçmişi kullanarak her adımda büyür; kayan pencere sabit uzunlukta ilerler (Hyndman & Athanasopoulos, *FPP*; walk-forward "rolling-origin" olarak deployment'ı taklit eder, lookahead bias'ı önler). Az-gözlemde **genişleyen pencere tercih edilir**, çünkü kayan pencere zaten kıt olan eğitim verisini daha da küçültür. Kayan pencere yalnızca rejim değişiminin eski veriyi "zararlı" hale getirdiği durumda (concept drift) gerekçelendirilebilir — ama bu az-gözlemle çelişir, dolayısıyla **her ikisi de raporlanıp karşılaştırılmalı**, tek başına birine güvenilmemelidir.

**(b) Purged + embargoed CV (López de Prado 2018, *Advances in Financial Machine Learning*, s. 105–109).** Etiket, gelecekteki bir olaya bağlıysa (aylık yön, önceki döneme referansla hesaplanır → örtüşme vardır) eğitim ve test arasında **purging** (etiket-zamanı test aralığıyla kesişen eğitim gözlemlerini silmek) ve **embargo** (test sonrası tampon dönem) zorunludur. Aylık veride embargo tipik olarak **1–2 ay** olmalıdır (feature pencereleri ve otokorelasyon dikkate alınarak).

**(c) Combinatorial Purged CV (CPCV).** Çoklu backtest yolu üretir ve tek-yollu walk-forward'ın "tek tarihsel senaryoya bağımlılık / yüksek varyans" zaafını giderir; sonuç bir out-of-sample **dağılımıdır** (skfolio/mlfinlab uygulamaları). Ancak yol sayısı N (grup) ve k (test grubu) ile faktöriyel büyür; tipik N=5–10 kullanılır. **Az-gözlem gerçekçiliği**: 60 gözlemle N=6 grup → grup başına 10 gözlem; bu, test folülarının istatistiksel olarak anlamsız hale gelmesi riskini taşır (bir kaynak yol başına <100 gözlemde performans dağılımlarının "unstable and noisy" olduğunu belirtir). CPCV bu projede **ancak gözlem ≥ ~120 ise** ve o zaman bile küçük N ile denenmelidir; aksi halde tek-yollu walk-forward yeterlidir. CPCV'nin karmaşıklığı ek bir risktir: purging/indeksleme hataları sessizce (crash olmadan) leakage geri getirebilir.

**Kaç fold/test dönemi GERÇEKÇİ?** Somut öneri:
- **N ≈ 40–80 gözlem**: Tek genişleyen-pencere walk-forward, **6–12 adımlı** test dönemi (son 6–12 ay). Her adım 1 aylık ufuk. Fold "sayısı" = test dönemi sayısı = 6–12.
- **N ≈ 80–150 gözlem**: 12–24 adımlı walk-forward; purge+embargo eklenir; opsiyonel küçük-N CPCV (N=5, k=2 → 10 yol) yardımcı olarak.
- **N > ~150**: CPCV daha güvenilir bir out-of-sample dağılımı verir.
- **"50–100 fold walk-forward" bu problemde YASAK**: her fold'a ~1 gözlem düşer, hiçbir metrik stabil olmaz.

**Projeye Uygulanabilirlik**: Omurga = genişleyen-pencere walk-forward + 1 ay ufuk + 1–2 ay embargo; test dönemi sayısı gözlem bütçesine göre 6–24. CPCV yalnızca gözlem izin verirse.

### 3. Leakage Taksonomisi ve Önleme (vintage/real-time dahil)

Kapoor & Narayanan (2023, *Patterns* 4(9):100804, DOI 10.1016/j.patter.2023.100804) 8-tipli leakage taksonomisi verir; yayımlanmış Patterns sürümünün resmi rakamıyla **17 bilimsel alanda 294 makalenin** leakage nedeniyle geçersizleştiğini raporlar (verbatim: *"we find 17 fields where leakage has been found, collectively affecting 294 papers and, in some cases, leading to wildly overoptimistic conclusions"*; arXiv ön-baskısında rakam 329 idi). Bu proje için kritik tipler ve önleme protokolü:

- **L1.2 — Ön-işlemenin tüm veride yapılması**: Scaling, encoding, imputation **fold içinde, yalnızca eğitim kısmında** fit edilmeli, teste transform olarak uygulanmalı. Aksi halde test istatistikleri eğitime sızar.
- **L1.3 — Feature selection'ın tüm veride yapılması**: Değişken seçimi walk-forward'ın her adımında yeniden yapılmalı. Vabalas ve ark. (2019) bunun **hiperparametre ayarından bile daha büyük** yanlılık kaynağı olduğunu gösterir (yukarıda verbatim).
- **Target encoding leakage**: Kategorik değişkenlerin hedef-ortalamasıyla kodlanması, hedef bilgisini feature'a sızdırır — bu Faz'da yeniden teorik olarak tartışılmaz (feature türetimi başka fazın konusu); **protokol kuralı**: target encoding varsa fold-içi ve zaman-nedensel (yalnızca geçmiş) hesaplanmalı, aksi halde yasaklanmalıdır.
- **L3.1 — Temporal leakage / vintage sorunu (BU PROBLEMİN EN KRİTİK RİSKİ)**: Makro göstergeler (enflasyon, kur, faiz, ÖTV kararları) *referans döneminden* haftalar-aylar sonra yayımlanır ve sonradan revize edilir. Croushore & Stark'ın Philadelphia Fed **Real-Time Data Set for Macroeconomists** ve ALFRED (St. Louis Fed) vintage arşivi bu sorunu çözmek için kurulmuştur; ECB now-casting literatürü (Bańbura ve ark.) "ragged edge" ve yayın-gecikmesi problemini modeller (tipik yayın-gecikmeleri günlerden aylara uzanır; bazı serilerde >2 ay). **Protokol kuralı**: Her makro feature için "bu değer, tahmin origin tarihinde GERÇEKTEN yayımlanmış mıydı?" sorusu yanıtlanmalı; yalnızca **o tarihte bilinen vintage** kullanılmalı, en-son-revize seri KULLANILMAMALIDIR. Vintage veri yoksa, **gerçekçi bir yayın-gecikmesi (ör. makro için +1 ila +2 ay lag)** yapay olarak uygulanmalıdır (pseudo-real-time).

**Projeye Uygulanabilirlik**: Pipeline'da tek bir "as-of date" (bilgi kesim tarihi) parametresi merkezî olmalı; tüm feature'lar bu tarihten önceki bilgiyle sınırlanmalı. Bu, hem N5 kronolojisini hem vintage kuralını tek noktadan garanti eder.

### 4. Metrik Protokolü ve Güven Aralığı

**Birincil metrik (N5 bağlayıcı): MCC / macro-F1.** Chicco & Jurman (2020, *BMC Genomics* 21:6, DOI 10.1186/s12864-019-6413-7) MCC'nin dört confusion-matrix kategorisini dengeli birleştirdiğini şu verbatim ifadeyle vurgular: MCC *"produces a high score only if the prediction obtained good results in all of the four confusion matrix categories (true positives, false negatives, true negatives, and false positives)"*; buna karşılık accuracy ve F1 *"can dangerously show overoptimistic inflated results, especially on imbalanced datasets."* "Hep stable" gibi trivial bir sınıflayıcı yüksek accuracy alabilir ama MCC ≈ 0 verir — bu tam da N6'nın istediği ayrımdır.

**Çok-sınıflı MCC doğru hesaplama**: 3-sınıf (up/down/stable) için **Gorodkin (2004, *Computational Biology and Chemistry* 28(5):367–374) R_K istatistiği** kullanılmalıdır (K×K confusion matrisi üzerinden; scikit-learn `matthews_corrcoef` ve torchmetrics `MulticlassMatthewsCorrCoef` bunu uygular). **Uyarı**: "micro-averaged MCC" diyagonal elemanlara indirgenir ve accuracy ile orantılı hale gelir, MCC'nin avantajını kaybeder (arXiv 2503.06450, "Statistical Inference of the MCC for Multiclass Classification"); dolayısıyla **Gorodkin global R_K veya macro-averaged MCC** raporlanmalı, micro-MCC birincil metrik yapılmamalıdır.

**Per-class raporlama standardı**: Her sınıf için precision/recall/support ayrı ayrı verilmeli (özellikle "stable" sınıfının baskın olması beklendiğinden, azınlık up/down sınıflarındaki recall kritik). Sadece global metrik güvenilmez sayılmalıdır.

**Güven aralığı — blok-bootstrap**: Zaman serisinde i.i.d. bootstrap otokorelasyonu yok sayar ve **standart hataları sistematik olarak küçük gösterir**. Bunun yerine **moving block bootstrap** (Künsch 1989; Politis & Romano) kullanılmalı; blok uzunluğu ~n^(1/3) mertebesinde (Patton, Politis & White 2009 veri-uyarlı seçici; ampirik uygulamalarda ör. 3-aylık blok + B=1000 resample yaygındır). **Az-gözlem uyarısı**: 60 gözlemde blok uzunluğu ~4 → ~15 etkin blok; bootstrap CI'ları geniş ve gürültülü olur. Bu bir zayıflık değil, dürüst raporlamanın parçasıdır: CI genişliği açıkça belirtilmelidir.

**Projeye Uygulanabilirlik**: Rapor tablosu = {macro-MCC (Gorodkin), macro-F1, per-class P/R/support, her biri için %95 moving-block-bootstrap CI, B≥1000, blok uzunluğu ve seed açıkça}. Accuracy yalnızca tanımlayıcı olarak (N5).

### 5. Baseline Tasarımı ve Anlamlılık Testi

**Baseline seti (N6 bağlayıcı — model bunları MCC'de geçmelidir):**
1. **Persistence / naif**: bir önceki dönemin yönü bu dönem de sürecek.
2. **Mevsimsel-naif**: 12 ay önceki yön (mevsimsellik varsa).
3. **"Hep stable" (trivial/majority)**: en sık sınıfı her zaman tahmin — accuracy'yi şişirir ama MCC≈0 verir; N6'nın kilit karşılaştırması.
4. **Prior-oran (stratified random)**: sınıf öncül dağılımından rastgele çekiliş.

**Anlamlılık testi — yön bağlamına uyarlama:**
- **Puan-tahmini karşılaştırması**: Diebold–Mariano (1995, *JBES*) iki tahminin kayıp farkını test eder; **Harvey, Leybourne & Newbold (1997) küçük-örneklem düzeltmesi** az-gözlemde zorunludur.
- **Yön doğruluğu karşılaştırması (asıl ilgi)**: Pesaran–Timmermann (1992, *JBES* 10(4):461–465, DOI 10.1080/07350015.1992.10509922) market-timing testi, tahmin edilen ve gerçekleşen yönün bağımsızlığını test eder (H0: bağımsız → yön becerisi yok; S_n → N(0,1)). **Ancak 1992 testi serisel bağımsızlık varsayar** ve otokorelasyonlu yön serilerinde over-size eder. Bu proje için doğru araç **Pesaran–Timmermann (2009, *JASA* 104(485):325–337, DOI 10.1198/jasa.2009.0113)**: çok-kategorili (up/down/stable ↔ 2×2'nin ötesi) ve serisel-korelasyona dayanıklı (kanonik korelasyon + dinamik-augmented reduced-rank regresyon ile) bir bağımsızlık testidir. Verbatim (2009 özeti): *"there are no tests that account for serial dependencies... This paper proposes a new test of independence based on the maximum canonical correlation between pairs of discrete variables... in order to account for serial dependence."*
- **KÜÇÜK ÖRNEKLEM UYARISI (kritik)**: Blaskowitz & Herwartz (2014, *International Journal of Forecasting* 30(1):30–42) ve *Applied Economics* (2024) Monte-Carlo bulguları — serisel-korelasyonlu yön serilerinde **N≈50'de tüm kontenjans-tablosu testleri, N≈75'te bile PT2009 hâlâ over-sized**'dır; yalnızca dinamik-lojistik-regresyon-tabanlı test N=50'de doğru boyutludur. Dolayısıyla asimptotik PT p-değerine ham haliyle güvenilmemeli; **bootstrap-tabanlı PT (Blaskowitz–Herwartz)** veya dinamik-lojistik-regresyon alternatifi kullanılmalıdır. Bu eşikler simülasyon-tabanlıdır ve DGP'ye bağlıdır.

**Projeye Uygulanabilirlik**: Model, dört baseline'ın hepsini blok-bootstrap CI üzerinde MCC olarak geçmeli; "model > persistence" ve "model > hep-stable" farkları **bootstrap-PT** ile test edilmeli. Fark CI'ı sıfırı içeriyorsa → "sinyal yok" (N6'ya göre geçerli negatif bulgu).

### 6. Falsifikasyon Audit'i (N7 somut protokol)

Bu, fazın merkezî teslimatlarından biridir. Amaç: **pipeline'ın yapay/sahte sinyal üretip üretmediğini sistematik kontrol etmek.**

**(a) Hedef-karıştırma (permütasyon/shuffle) testi — Ojala & Garriga (2010, *JMLR* 11).** Hedef etiketler kronolojiyi bozmayacak şekilde (blok-permütasyon ile, çünkü basit permütasyon otokorelasyonu yok eder) B≥1000 kez karıştırılır; **tüm pipeline** (ön-işleme, feature, model, CV dahil) her karıştırmada yeniden çalıştırılır ve MCC'nin null dağılımı üretilir. Eğer gerçek MCC bu null dağılımının içindeyse (p büyük), **pipeline sinyal bulmuyor** demektir. Eğer null dağılımının ortalaması 0'dan belirgin biçimde yüksekse → **pipeline'da leakage var** (karıştırılmış hedefte bile "başarı" üretiyor); bu bir kırmızı bayraktır ve durdurucudur. (scikit-learn `permutation_test_score` bu mantığı i.i.d. için uygular; bu projede blok-permütasyona uyarlanmalıdır.)

**(b) Random-walk / persistence benchmark'ı**: Yön serisi bir rastgele yürüyüşün işaret değişimiyse, hiçbir model persistence'ı anlamlı geçemez. Random-walk null'u, "predictable by construction" tuzağına (temporal aggregate'lerde sahte yön öngörülebilirliği; *Applied Economics* 2025 — random-walk null altında period-average öngörülerinde >20 puanlık sahte Sharpe kazanımları belgelenmiştir) karşı koruma sağlar.

**(c) Sentetik sinyal enjeksiyon testi (pozitif kontrol)**: Bilinen, yapay bir sinyal veriye eklenip pipeline'ın onu **bulabildiği** doğrulanır. Bu, (a)'nın tersidir: (a) "yokken bulmamalı", (c) "varken bulmalı" der. İkisi birlikte pipeline'ın kalibrasyonunu gösterir.

**Prosedür (adım adım)**:
1. Gerçek veri üzerinde tam pipeline'ı çalıştır → gerçek MCC.
2. Blok-permütasyon ile hedefi B=1000 kez karıştır, her seferinde tam pipeline → null MCC dağılımı.
3. p = (null ≥ gerçek sayısı + 1)/(B+1).
4. Null dağılımının ortalaması ≈ 0 mı? (leakage kontrolü). Değilse pipeline'ı düzelt.
5. Sentetik sinyal enjekte et → pipeline bulmalı (pozitif kontrol).
6. Random-walk benchmark'ı ile karşılaştır.

**N6 ile tutarlılık**: Bu prosedür "sinyal yok" sonucunu **değerli ve geçerli** kılar; p büyükse bu bir başarısızlık değil, dürüst bir negatif bulgudur.

**Projeye Uygulanabilirlik**: Permütasyon testi **blok-permütasyon** olmalı (basit shuffle N5'i ihlal eder ve otokorelasyonu yok eder). B ve blok uzunluğu raporlanmalı.

### 7. Çoklu-Test ve Araştırmacı Serbestliğinin Kontrolü

N7'nin ikinci ayağı: **denenen model-hiperparametre kombinasyonu sayısının kaydı + çoklu-test düzeltmesi.**

- **Denenen kombinasyon sayısını kaydet (N)**: Fabozzi & López de Prado (2018, *JPM* 45(1):141–147) "Being Honest in Backtest Reporting" — denenen tüm testlerin sayısı açıklanmazsa seçilen sonuç bir "false discovery" olabilir. Her denenen model/hiperparametre/feature-set kombinasyonu bir logda tutulmalıdır.
- **Deflated/düzeltilmiş metrik**: Bailey & López de Prado (2014, *JPM* 40(5):94–107) Deflated Sharpe Ratio — N deneme arasından seçilen en iyi metriğin şişkinliğini, deneme sayısı ve dağılım momentleriyle (skewness/kurtosis) düzeltir. Sharpe yerine bu projede MCC kullanıldığından, **doğrudan Deflated Sharpe uygulanamaz**; ancak muadili **permütasyon-null + çoklu-karşılaştırma düzeltmesi** (ör. denenen N model için Bonferroni/BH-FDR ya da max-statistic null) uygulanmalıdır. *Literatürde net değil*: MCC için hazır bir "deflated MCC" formülü standartlaşmamıştır; bu nedenle çoklu-test kontrolü permütasyon-tabanlı max-istatistik null'u ile yapılmalıdır.
- **Minimum Backtest Length (MinBTL)** — Bailey, Borwein, López de Prado & Zhu (2014, *Notices of the AMS* 61(5):458–471): **MinBTL ≈ 2·ln(N)/E[max]²** (yıl cinsinden), yani denenen bağımsız model sayısı N arttıkça gereken minimum out-of-sample uzunluğu logaritmik büyür. Kaynaktaki somut örnek: **beş yıllık günlük borsa verisiyle overfit'i önlemek için en fazla ~45 bağımsız strateji varyasyonu** test edilmelidir; aksi halde gerçek OOS becerisi sıfır olsa bile IS Sharpe≈1 üreten bir strateji "keşfetmek" neredeyse kaçınılmazdır (*"The higher the number of configurations tried, the greater is the probability that the backtest is overfit."*). **Az-gözlem sonucu**: bu proje denenecek model sayısını **sert biçimde ve önceden** sınırlamalıdır.
- **Nested CV az-gözlemde uygulanabilir mi?** Cawley & Talbot (2010, *JMLR* 11:2079–2107) model-seçim yanlılığına karşı nested-CV önerir; Vabalas ve ark. (2019) küçük örneklemde nested-CV'nin yanlılığı giderdiğini ama **varyansı artırdığını** gösterir. **Bu projedeki karar**: aylık, onlarca-gözlemli, kronolojik veride tam nested walk-forward çoğu zaman **pratik değildir** (iç döngüye yeterli gözlem kalmaz). Yerine: (i) hiperparametre uzayını küçük ve önceden belirle; (ii) tek bir son dönem "kilitli" hold-out ayır; (iii) denenen N'i logla ve deflate et. *Literatürde net değil*: çok küçük N'de nested-CV mı yoksa tek hold-out + katı bütçe mi üstün — Wainer & Cawley (2018, arXiv:1809.09446) birçok pratik durumda nested-CV'nin "aşırı" olduğunu savunur, bu da tek hold-out lehine bir argümandır.

**Projeye Uygulanabilirlik**: Bir "deneme günlüğü" (her run: model, hiperparametre, feature-set, CV konfigürasyonu, MCC) zorunlu; nihai raporda N açıkça verilmeli ve p-değerleri N'e göre düzeltilmeli.

### 8. Rejim-Farkında Değerlendirme (N8/N2)

**Şok tarihleri önceden ve dışsal olarak tanımlanır** (kur şoku, ÖTV değişikliği gibi bilinen makro-politika olayları) — bunlar veriden "keşfedilmez", çünkü keşif çoklu-test problemini geri getirir. Protokol:

1. **Şok takvimi**: Bilinen şok tarihleri listesi önceden sabitlenir (ör. büyük kur hareketleri, ÖTV/vergi düzenlemeleri).
2. **Rejim-ayrık raporlama**: Genel MCC'ye ek olarak, {şok-öncesi, şok-sonrası N ay} pencereleri için **ayrı MCC + per-class raporu**. N2'nin öngörüsü: şok-sonrası dönemde MCC düşer; bu düşüş **ölçülür ve raporlanır**.
3. **Dağılım-kayması ölçümü**: Şok-öncesi vs sonrası feature dağılımlarında kayma (covariate shift / temporal shift: marjinal dağılım değişir) ile koşullu ilişki kayması (concept drift: P(y|X) değişir, Gama ve ark. 2014) ayrıştırılmalı. Performans düşüşünün kaynağının hangisi olduğu (girdi mi değişti, girdi-hedef ilişkisi mi) belirtilmeli; bu ayrım düzeltme stratejisini (yeniden-eğitim mi, normalizasyon mu, yeni feature mi) belirler.
4. **"Predictable by construction" tuzağı**: Şok dönemlerinde yön serisi çok kalıcı hale gelebilir (uzun "up" veya "down" serileri), bu da persistence baseline'ını yapay olarak güçlendirir; model iyileşmesi **her rejim için ayrı** persistence'a karşı ölçülmelidir.

**N2 ile tutarlılık**: N2 "rejim geçişinde performans düşüşü beklenir" der; protokol bunu bir hipotez olarak test eder — düşüş **görülmezse** bu da raporlanır (belki model rejim-robust, belki test gücü yetersiz).

**Projeye Uygulanabilirlik**: Nihai rapor en az üç MCC verir: {tüm örneklem, sakin dönem, şok-sonrası dönem}. Şok-sonrası CI'lar çok geniş olacaktır (az gözlem) — bu açıkça belirtilmeli, aşırı yorum yapılmamalı.

### 9. PROTOKOL KONTROL LİSTESİ (ana teslimat)

Bir deney "güvenilir" ilan edilmeden önce **her madde geçilmelidir**. Format: **[Ne] — [Neden] — [Atlanırsa risk]**.

**A. Veri ve Kronoloji**
1. **Gözlem sayısını say ve raporla.** — Tüm istatistiksel gücün üst sınırını belirler. — Atlanırsa: aşırı-iddialı sonuçlar; N<50'de anlamsız CI'lar.
2. **Tek merkezî "as-of date" (bilgi kesim tarihi) uygula.** — Kronoloji + vintage kuralını tek noktadan garanti eder (N5). — Atlanırsa: temporal leakage, sistematik iyimserlik.
3. **Makro feature'larda vintage/yayın-gecikmesi uygula (gerçek vintage veya pseudo-real-time +1/+2 ay lag).** — Gösterge yayımlanmadan "bilinmiş" sayılması sızıntıdır (L3.1). — Atlanırsa: gerçekte imkânsız öngörü, canlıda çöküş.

**B. Validasyon Tasarımı**
4. **Genişleyen-pencere walk-forward + kronolojik ayrım (rastgele k-fold YASAK).** — N5 zorunluluğu; deployment'ı taklit eder. — Atlanırsa: gelecekten geçmişe bilgi akışı.
5. **Purge + embargo (1–2 ay) uygula.** — Etiket zaman-örtüşmesi leakage'ını keser (López de Prado 2018). — Atlanırsa: bitişik dönem sızıntısı, şişik MCC.
6. **Test dönemi sayısını gözlem bütçesine göre gerçekçi seç (6–24; "50–100 fold" YASAK).** — Her fold'a yeterli gözlem düşmeli. — Atlanırsa: stabil olmayan, gürültülü metrikler.
7. **Ön-işleme/feature-selection/encoding fold-İÇİNDE fit edilsin.** — L1.2/L1.3 leakage önleme (Vabalas: feature-selection en büyük yanlılık kaynağı). — Atlanırsa: test istatistikleri eğitime sızar.

**C. Metrik ve Belirsizlik**
8. **Birincil metrik = çok-sınıflı MCC (Gorodkin) + macro-F1; accuracy yalnızca tanımlayıcı.** — N5 zorunluluğu; dengesizlikte doğru sinyal (Chicco & Jurman 2020). — Atlanırsa: "hep stable" trivial çözüm başarılı görünür.
9. **Per-class precision/recall/support raporla.** — Azınlık up/down sınıflarındaki gerçek performansı gösterir. — Atlanırsa: global metrik azınlık başarısızlığını gizler.
10. **Blok-bootstrap %95 CI (B≥1000, blok uzunluğu ~n^(1/3), seed raporlu).** — Otokorelasyon altında dürüst belirsizlik. — Atlanırsa: sahte-dar CI, yanlış anlamlılık.

**D. Baseline ve Anlamlılık**
11. **Dört baseline'a karşı MCC üstünlüğü göster (persistence, mevsimsel-naif, hep-stable, prior-oran).** — N6 başarı tanımı. — Atlanırsa: mutlak MCC yanıltıcı olur.
12. **Yön-anlamlılığı bootstrap-PT (Pesaran–Timmermann 2009 ruhu) ile test et.** — Serisel-korelasyon + çok-kategori altında geçerli. — Atlanırsa: N<75'te over-sized asimptotik test yanlış "anlamlı" verir.

**E. Falsifikasyon (N7)**
13. **Blok-permütasyon (hedef-shuffle) null testi, tam pipeline, B≥1000.** — Pipeline sahte sinyal/leakage üretiyor mu? (Ojala & Garriga 2010). — Atlanırsa: leakage fark edilmez; "keşif" bir artefakttır.
14. **Null dağılımı ortalaması ≈ 0 doğrula.** — Shuffle'da başarı = leakage kanıtı. — Atlanırsa: gizli sızıntı raporlanmaz.
15. **Sentetik sinyal pozitif kontrolü.** — Pipeline gerçek sinyali bulabiliyor mu? — Atlanırsa: pipeline'ın körlüğü fark edilmez.
16. **Random-walk benchmark'ı.** — "Predictable by construction" tuzağı. — Atlanırsa: sahte öngörülebilirlik.

**F. Çoklu-Test (N7)**
17. **Deneme günlüğü tut; denenen N kombinasyonu raporla.** — Fabozzi & López de Prado (2018) dürüstlük şartı. — Atlanırsa: seçim yanlılığı, false discovery.
18. **p-değerlerini N'e göre düzelt (permütasyon max-istatistik / FDR); MinBTL kontrolü.** — Bailey ve ark. (2014); şişik en-iyi metriği düzeltir. — Atlanırsa: overfit strateji "başarılı" ilan edilir.
19. **Nested CV yerine katı hiperparametre bütçesi + kilitli hold-out (az-gözlem gerçekçiliği).** — İç döngüye gözlem kalmaz. — Atlanırsa: ya uygulanamaz ya da yüksek-varyanslı tahmin.

**G. Rejim-Farkındalık (N8/N2)**
20. **Şok takvimini önceden sabitle (kur/ÖTV); veriden keşfetme.** — Post-hoc keşif çoklu-testi geri getirir. — Atlanırsa: cherry-picking.
21. **Rejim-ayrık MCC raporu (sakin vs şok-sonrası) + düşüşü ölç.** — N2/N8 zorunluluğu. — Atlanırsa: canlı rejim değişiminde beklenmedik çöküş.
22. **Dağılım-kaymasını (covariate/temporal shift vs concept drift) ayrıştır.** — Düşüşün kaynağını gösterir. — Atlanırsa: yanlış düzeltme (yeniden-eğitim mi, yeni feature mi?).

**H. Nihai Dürüstlük**
23. **"Sinyal yok" sonucunu geçerli çıktı olarak kabul et (N6).** — Negatif bulgu değerlidir. — Atlanırsa: sonuç zorlanır, overfit'e itilir.
24. **Tüm seed/konfigürasyon/kod-versiyonunu raporla (reprodüksiyon).** — Tekrarlanabilirlik. — Atlanırsa: sonuç doğrulanamaz.

### 10. Açık Sorular / Literatürde Net Olmayanlar

- **"Deflated MCC" yok**: Deflated Sharpe (Bailey & López de Prado 2014) doğrudan MCC'ye uyarlanmış standart bir formül literatürde bulunmuyor. Bu faz, permütasyon max-istatistik null'unu muadil olarak öneriyor; ancak bu, deflated Sharpe kadar oturmuş değildir. *Literatürde net değil.*
- **Çok küçük N'de (ör. <40) nested-CV vs tek hold-out**: Vabalas (2019) nested-CV'yi, Wainer & Cawley (2018) çoğu durumda gereksiz bulur; aylık-yön problemi için kesin bir eşik yok. *Literatürde net değil.*
- **Blok-permütasyonda optimal blok uzunluğu**: Otokorelasyonu koruyacak blok uzunluğunun yön-etiketi (kategorik) serilerinde nasıl seçileceği, sürekli seriler kadar iyi çalışılmamış. *Literatürde net değil.*
- **PT2009'un 3-sınıf + çok-küçük N'de kesin güç davranışı**: Simülasyon bulguları (Applied Economics 2024) N≈75'te bile over-size gösteriyor ama up/down/stable'a özgü kalibrasyon çalışılmamış; bootstrap-PT önerisi bu boşluğu kapatmaya yönelik pragmatik bir seçimdir.
- **CPCV'nin minimum gözlem eşiği**: "En az kaç gözlemle CPCV anlamlı?" için kesin bir literatür eşiği yok; grup başına ~10 gözlem (ve yol başına <100 gözlemde "unstable/noisy" uyarısı) sezgisel bir alt sınır olarak kullanıldı, kanıta değil pratiğe dayanıyor.

## Recommendations

**Aşama 1 — Kurulum (deney öncesi, kod yazmadan):**
- Toplam gözlem sayısını say. **Eşik**: N<50 → yalnızca keşifsel/negatif-bulgu modu; N≥80 → tam protokol; N≥150 → CPCV opsiyonel.
- Şok takvimini ve hiperparametre uzayını **önceden ve yazılı** sabitle (deneme sayısı N'i minimize et — MinBTL gereği; hatırla: 5 yıl günlük veri ↔ ~45 bağımsız konfigürasyon üst sınırı gibi bir sezgiyle ölçekle).
- Tek merkezî "as-of date" mimarisini kur; vintage/lag kuralını kodun çekirdeğine göm.

**Aşama 2 — Validasyon omurgası:**
- Genişleyen-pencere walk-forward + 1 ay ufuk + 1–2 ay embargo + purging. Test dönemi = 6–24 (bütçeye göre).
- Ön-işleme/encoding/feature-selection'ı fold-içine taşı.
- Birincil metrik: macro-MCC (Gorodkin) + macro-F1 + per-class P/R; hepsine blok-bootstrap CI.

**Aşama 3 — Anlamlılık ve baseline:**
- Dört baseline'a karşı MCC farkı + bootstrap-PT anlamlılığı. Fark CI'ı sıfırı içeriyorsa → "sinyal yok" ilan et (N6, geçerli sonuç).

**Aşama 4 — Falsifikasyon (bloke edici geçit):**
- Blok-permütasyon null (B≥1000): null-ortalaması ≠ 0 ise **DUR ve leakage'ı düzelt**. Bu geçit geçilmeden hiçbir sonuç "güvenilir" ilan edilemez.
- Sentetik-sinyal pozitif kontrolü + random-walk benchmark.

**Aşama 5 — Çoklu-test ve raporlama:**
- Deneme günlüğünden N'i raporla; p-değerlerini düzelt (permütasyon max-istatistik/FDR); MinBTL uyumunu kontrol et.
- Rejim-ayrık MCC (sakin vs şok-sonrası) ver; dağılım-kaymasını ayrıştır.
- Bölüm 9 kontrol listesinin 24 maddesini işaretle; eksik madde varsa sonuç "taslak/güvenilmez".

**Kararı değiştirecek eşikler (benchmark'lar):**
- Permütasyon null-ortalaması >0.05 MCC → leakage var, protokol durur.
- Model MCC − persistence MCC CI'ı sıfırı içeriyor → "sinyal yok".
- Şok-sonrası MCC, sakin-dönem MCC'nin belirgin altında ve persistence'ı geçemiyor → model rejim-kırılgan, canlı kullanım için uygun değil.
- Denenen N, MinBTL'in izin verdiğinden büyük → deneme sayısını azalt veya sonucu deflate ederek raporla.

## Caveats

- **Bu faz PROTOKOL kurar; kırmızı-takım/başarısızlık-modu avı ayrı fazın konusudur.** Protokolün kaçırabileceği riskler burada avlanmamıştır (kapsam kuralı).
- **Feature türetimi ve model ailesi seçimi bu fazın kapsamı dışıdır**; yalnızca leakage ve "validasyon model seçimini kısıtlar" bağlantısıyla değinildi.
- **Finans literatürüne dayanma**: López de Prado/Bailey metodolojisi finansal ML için geliştirildi; ikinci-el araç ilan-fiyatı yön problemi farklıdır (Sharpe → MCC uyarlaması gibi noktalarda birebir taşınamaz). Bu, açıkça işaretlendi (deflated-MCC boşluğu).
- **Bazı kaynaklar ikincil/blog niteliğinde** (Medium, Towards AI, Grokipedia, Hudson & Thames) — bunlar yalnızca birincil kaynakları (López de Prado 2018, Gorodkin 2004, Bailey ve ark. 2014) teyit için kullanıldı; hiçbir birincil iddia yalnızca ikincil kaynağa dayandırılmadı.
- **Az-gözlem her yerde belirleyici**: Önerilen tüm CI'lar geniş, tüm testler düşük güçlü olacaktır. Bu bir kusur değil, problemin doğasıdır; dürüst rapor bunu gizlemez, öne çıkarır.
- **Simülasyon-tabanlı eşikler DGP'ye bağlıdır**: PT over-sizing eşikleri (N≈50/75) belirli AR/Markov süreçlerinden gelir; bu projenin gerçek otokorelasyon yapısında farklı olabilir.

## Kaynakça

- Bergmeir, C. & Benítez, J.M. (2012). "On the use of cross-validation for time series predictor evaluation." *Information Sciences* 191:192–213.
- Bergmeir, C., Hyndman, R.J. & Koo, B. (2018). "A note on the validity of cross-validation for evaluating autoregressive time series prediction." *Computational Statistics and Data Analysis* 120:70–83.
- Bergmeir, C., Costantini, M. & Benítez, J.M. (2014). "On the usefulness of cross-validation for directional forecast evaluation." *CSDA* 76:132–143.
- Hyndman, R.J. & Athanasopoulos, G. *Forecasting: Principles and Practice* (FPP), 2. baskı.
- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. (Purged/embargoed CV, CPCV; s. 105–109.)
- Kapoor, S. & Narayanan, A. (2023). "Leakage and the reproducibility crisis in ML-based science." *Patterns* 4(9):100804. DOI 10.1016/j.patter.2023.100804.
- Croushore, D. & Stark, T. "A Real-Time Data Set for Macroeconomists." Federal Reserve Bank of Philadelphia. (Ayrıca ALFRED, St. Louis Fed vintage arşivi.)
- Gorodkin, J. (2004). "Comparing two K-category assignments by a K-category correlation coefficient." *Computational Biology and Chemistry* 28(5):367–374.
- Chicco, D. & Jurman, G. (2020). "The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation." *BMC Genomics* 21:6. DOI 10.1186/s12864-019-6413-7.
- Chicco, D., Tötsch, N. & Jurman, G. (2021). "The MCC is more reliable than balanced accuracy, bookmaker informedness, and markedness in two-class confusion matrix evaluation." *BioData Mining* 14:13.
- "Statistical Inference of the Matthews Correlation Coefficient for Multiclass Classification." (2025). arXiv:2503.06450.
- Künsch, H.R. (1989). "The jackknife and the bootstrap for general stationary observations." *Annals of Statistics* 17(3):1217–1241.
- Politis, D.N. & Romano, J.P. (1994). "The stationary bootstrap." *JASA* 89:1303–1313. (Ayrıca moving block bootstrap literatürü.)
- Patton, A., Politis, D.N. & White, H. (2009). "Correction to Automatic block-length selection for the dependent bootstrap." *Econometric Reviews*.
- Diebold, F.X. & Mariano, R.S. (1995). "Comparing predictive accuracy." *Journal of Business & Economic Statistics* 13:253–263.
- Harvey, D., Leybourne, S. & Newbold, P. (1997). "Testing the equality of prediction mean squared errors." *International Journal of Forecasting* 13:281–291.
- Pesaran, M.H. & Timmermann, A. (1992). "A simple nonparametric test of predictive performance." *JBES* 10(4):461–465. DOI 10.1080/07350015.1992.10509922.
- Pesaran, M.H. & Timmermann, A. (2009). "Testing dependence among serially correlated multicategory variables." *JASA* 104(485):325–337. DOI 10.1198/jasa.2009.0113.
- Blaskowitz, O. & Herwartz, H. (2014). "Testing the value of directional forecasts in the presence of serial correlation." *International Journal of Forecasting* 30(1):30–42. DOI 10.1016/j.ijforecast.2013.06.001.
- "Assessing the accuracy of directional forecasts." (2024). *Applied Economics*. DOI 10.1080/00036846.2024.2393902.
- Ojala, M. & Garriga, G.C. (2010). "Permutation tests for studying classifier performance." *Journal of Machine Learning Research* 11:1833–1863.
- Bailey, D.H. & López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality." *Journal of Portfolio Management* 40(5):94–107.
- Bailey, D.H., Borwein, J.M., López de Prado, M. & Zhu, Q.J. (2014). "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance." *Notices of the AMS* 61(5):458–471. (MinBTL.)
- Bailey, D.H., Borwein, J.M., López de Prado, M. & Zhu, Q.J. (2017). "The Probability of Backtest Overfitting." *Journal of Computational Finance* 20(4):39–70. DOI 10.21314/JCF.2016.322.
- Fabozzi, F.J. & López de Prado, M. (2018). "Being Honest in Backtest Reporting: A Template for Disclosing Multiple Tests." *JPM* 45(1):141–147. DOI 10.3905/jpm.2018.45.1.141.
- Arnott, R., Harvey, C.R. & Markowitz, H. (2019). "A Backtesting Protocol in the Era of Machine Learning." *Journal of Financial Data Science* 1(1):64–74. DOI 10.3905/jfds.2019.1.064.
- Cawley, G.C. & Talbot, N.L.C. (2010). "On over-fitting in model selection and subsequent selection bias in performance evaluation." *JMLR* 11:2079–2107.
- Vabalas, A., Gowen, E., Poliakoff, E. & Casson, A.J. (2019). "Machine learning algorithm validation with a limited sample size." *PLOS ONE* 14(11):e0224365.
- Wainer, J. & Cawley, G. (2018). "Nested cross-validation when selecting classifiers is overzealous for most practical applications." arXiv:1809.09446.
- Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M. & Bouchachia, A. (2014). "A survey on concept drift adaptation." *ACM Computing Surveys* 46(4):44.

## Kullanılan Nihai Arama Sorguları

İngilizce: "walk-forward validation time series forecasting expanding sliding window"; "purged cross-validation embargo Lopez de Prado"; "Bergmeir cross-validation time series evaluation"; "data leakage machine learning taxonomy Kapoor Narayanan reproducibility"; "real-time vintage data macroeconomic forecasting publication lag"; "multiclass Matthews correlation coefficient computation Gorodkin"; "block bootstrap confidence interval time series Politis moving block"; "Diebold-Mariano test directional accuracy Pesaran-Timmermann forecast evaluation"; "deflated Sharpe ratio backtest overfitting multiple testing Bailey Lopez de Prado"; "permutation test target shuffle null model significance machine learning Ojala Garriga"; "concept drift regime shift evaluation distribution shift performance degradation forecasting"; "nested cross-validation small sample overfitting Vabalas Cawley"; "Fabozzi Lopez de Prado being honest backtest reporting template disclosing multiple tests"; "Arnott Harvey Markowitz backtesting protocol machine learning seven principles"; "MCC advantages F1 accuracy imbalanced classification Chicco Jurman"; "combinatorial purged cross-validation number of paths minimum sample requirement"; "used car price prediction machine learning direction classification monthly".
Türkçe: "zaman serisi çapraz doğrulama veri sızıntısı önleme backtest".
Alt-ajan (odaklı) sorguları: Pesaran–Timmermann 1992/2009 test mekaniği ve serisel-korelasyon düzeltmesi; PT testinin küçük-örneklem boyut/güç davranışı; Bailey ve ark. Minimum Backtest Length formülü ve sayısal örneği.

---
*Not: `gerceklesen_kaynak_sayisi` YAML metadata'sındaki 26 değeri, kaynakçadaki farklı birincil/ikincil kaynakların toplamını yansıtır; hedef (18) aşılmıştır.*