---
faz_no: 05
faz_adi: "Feature Engineering ve Alternatif Veri Kaynakları"
tarih: 2026-07-13
kapsam_ozeti: "Yön sınıflandırması için feature türleri, kompozisyon düzeltmesi, segment tasarımı ve alternatif veri"
bagimli_oldugu_fazlar: [01, 02, 03, 04]
durum: tamamlandi
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 24
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-15
---

# Faz 5 — Feature Engineering ve Alternatif Veri Kaynakları

## TL;DR

- **Kompozisyon düzeltmesi (N1) çözülebilir ve merkezi olmalı:** Ham segment-ortalama ilan fiyatını yön etiketi/feature üretiminde doğrudan kullanmak mix kaymasıyla sahte sinyal üretir. Literatürde iki uygulanabilir çözüm var: (a) Manheim tarzı sabit-kompozisyon (24-aylık yuvarlanan ağırlıklı, mileage-regresyonlu) ağırlıklandırma ve (b) hedonik reziduel/hedonic imputation yöntemi (BLS, OECD Handbook). Öneri: hedonik reziduel yaklaşımını birincil, sabit-kompozisyon ağırlıklandırmayı doğrulama katmanı olarak kur.
- **Makro feature'lar lag'li kullanılmalı ve lag ampirik seçilmeli:** Türkiye için USD/TRY→TÜFE geçişkenliğinin ~%40'ı ilk çeyrekte, ~%80'i üç çeyrekte tamamlanıyor; çekirdek mal (otomobil dahil) geçişi daha hızlı ve büyük (~%25, 3-4 çeyrek). Lag seçimi cross-correlation + Granger-tipi ön eleme ile yapılmalı; aynı-dönem (t) makro değerleri leakage riski taşır.
- **Alternatif/öncü veriler seçici kanıtla destekleniyor:** Google Trends araç satışında sınırlı ama gerçek prediktif güç gösteriyor (bir Massey Üniversitesi tez çalışmasında yeni araç satışı varyansının %10,8'ini açıklıyor); days-on-market / arz-talep oranları sektör pratiğinde fiyat yönünün öncüsü kabul ediliyor. Teknik göstergelerin (RSI/MACD) körü körüne kopyalanması ZORLAMADIR; yalnızca momentum ve oynaklık soyutlamaları aylık ufukta anlamlıdır.

## Key Findings

1. **N1 doğrudan çözülüyor.** Kamuya açık Türk endeksleri (BETAM, arabam.com) mix düzeltmesizdir; ancak resmi istatistik kurumları ve Manheim tam olarak bu problemi çözer. Manheim endeksi ham ortalama değildir: sabit market-class ağırlıkları (24-aylık yuvarlanan satış ortalaması), mileage için market-class bazlı doğrusal regresyon düzeltmesi ve outlier kırpma (fiyat VE km birlikte 2,6 SD dışı) içerir. BLS used cars endeksi ise matched-model + depreciation (bir model yılı genç muadille fiyat oranı) + kalite düzeltmesi kullanır. Bu, projede hedef değişkenin (yön etiketi) mix'ten arındırılmış bir seriden üretilmesi gerektiğini gösterir.
2. **Hedonik reziduel yöntem en uygulanabilir çözüm.** Bir hedonik regresyon (log fiyat ~ yaş + km + marka/model + motor + yakıt + şanzıman + donanım) her ay/segment için tahmin edilir; sabit karakteristik setine göre "quality-adjusted" endeks (hedonic imputation, time-dummy veya çift-imputation) türetilir. Yön etiketi bu düzeltilmiş seriden hesaplanır. Bu N9'daki öznitelik setini doğrudan kullanır.
3. **Makro lag yapısı ampirik seçilmeli.** Cross-correlation fonksiyonu + Granger-tipi ön eleme (pairwise, çoklu lag; grangersearch benzeri sistematik lag taraması) literatürde standart. Türkiye ERPT kanıtı somut lag başlangıç değerleri veriyor: 1, 3, 6, 12 aylık kur lag'leri makul aday penceredir.
4. **Zaman serisi feature aileleri aylık ufka uygun:** lag'ler, hareketli ortalamalar, değişim oranları (MoM/YoY), momentum ve oynaklık (rolling std). Finansal teknik göstergelerin birebir kopyalanması (RSI eşikleri 30/70, MACD 12/26/9) araç piyasasında zorlamadır — bunlar günlük, likit, yüksek-frekanslı, hacim-bilgili piyasalar için kalibre edilmiştir; aylık, düşük-frekanslı, hacimsiz segment serisinde parametreleri anlamsızdır. Ancak altında yatan momentum ve oynaklık kavramları jenerik feature olarak değerlidir.
5. **Segment granülerliği trade-off içeriyor:** marka-model-yaş hücresi en yüksek prediktif çözünürlüğü verir ama sparse cell sorunu doğurur. Çözüm: hiyerarşik backoff (model→marka→segment→genel) ve shrinkage/smoothing (empirical Bayes) — istatistik kurumu ve high-cardinality encoding literatüründen devşirilebilir.
6. **Leakage-safe encoding zorunlu:** high-cardinality kategorikler (marka-model) için target encoding ancak fold-dışı / ordered (CatBoost tarzı expanding-mean) hesaplanırsa leakage üretmez. Zaman serisinde ek olarak encoding istatistikleri yalnızca geçmiş verilerden hesaplanmalı.

## Details

### 1. Giriş: Faz 2 Sürücü Haritasından Feature'a Geçiş Çerçevesi

Bu faz, Faz 2 sürücü haritasındaki her değişkeni prediktif bir feature'a çevirir. Çerçeve dört soruyla ilerler: (i) hangi türetme (lag/rolling/oran/reziduel); (ii) aylık ufka uygunluk; (iii) leakage riski; (iv) beklenen sinyal türü. Sürücü haritası ham girdi, N9 öznitelik seti ilan-düzeyi çekirdek, N1 ise hedef/feature üretiminin merkezi kısıtıdır. N2 (arz rejim çift-yönlülüğü) bir etkileşim feature'ı olarak ele alınır.

Metodolojik dayanak olarak feature-tabanlı zaman serisi sınıflandırmasının state-of-the-art TSC algoritmalarıyla yarışabildiği ampirik olarak gösterilmiştir (Renault, Bondu, Lemaire & Gay, "Automatic Feature Engineering for Time Series Classification", arXiv:2308.01071, 2023; 11 feature aracı × 9 sınıflandırıcı × 112 veri seti, 10.000'den fazla öğrenme deneyi). Bu, feature engineering'e yatırımın modelleme fazından bağımsız olarak getiri sağladığını doğrular.

*Projeye Uygulanabilirlik:* Feature üretimi hem hedef (mix-düzeltilmiş yön) hem girdi tarafını kapsar; bu fazın çıktısı doğrudan Bölüm 8 tablosudur.

### 2. Zaman Serisi Feature'ları (lag, momentum, oynaklık) ve Araç Piyasasına Uygunluk

Standart zaman serisi feature aileleri — lag'ler, rolling mean/std, değişim oranları, autocorrelation — aylık segment serilerine doğrudan uygulanabilir (Christ, Braun, Neuffer & Kempa-Liehr, "tsfresh", Neurocomputing 307:72-77, 2018, doi:10.1016/j.neucom.2018.03.067; tsfresh 63 karakterizasyon yöntemiyle ~800 feature üretir ve FRESH filtresiyle — Fisher's exact, Kolmogorov-Smirnov, Kendall rank testleri + Benjamini-Yekutieli FDR kontrolü — alakasızları eler). tsfresh gibi otomatik çıkarımlar aday feature havuzu üretmede kullanılabilir; ancak aylık, kısa serilerde overfitting riskine karşı FRESH tipi hipotez-testli filtreleme şarttır.

**RSI/MACD analojisi — zorlama mı, anlamlı mı?** Ayrım net yapılmalıdır:
- **Zorlama olan kısım:** RSI'nin 30/70 aşırı-alım/satım eşikleri, MACD'nin 12/26/9 gün parametreleri günlük likit finansal serilere kalibre edilmiştir. Bunlar tanımı gereği lagging (gecikmeli) göstergelerdir — geçmiş fiyat hareketine dayanırlar ve gerçek-zamanlı kaymaları her zaman yansıtmazlar (LevelFields, B2Broker teknik-analiz değerlendirmeleri). Teknik analizin kendisi ampirik olarak tartışmalıdır (etkin piyasa hipotezi karşısında; bazı çalışmalar bazı göstergelerin anlamlı, bazılarının başarısız olduğunu gösterir). Aylık, hacimsiz, düşük-frekanslı bir segment-fiyat serisinde bu parametreleri ve eşikleri birebir kopyalamak metodolojik zorlamadır.
- **Anlamlı olan kısım:** Bu göstergelerin *altında yatan soyutlamalar* — kısa vs. uzun hareketli ortalama farkı (momentum), fiyatın kendi oynaklık zarfına göre konumu (normalize edilmiş sapma), değişim hızı (rate-of-change) — jenerik zaman serisi feature'larıdır ve aylık ufukta anlamlıdır. Finansal ML literatüründe momentum/oynaklık/trend feature ailelerinin bilgi taşıdığı gösterilmiştir (BIST 100 yön tahmininde kapsamlı öznitelik mühendisliğinin dışsal değişken olmadan bile yüksek sınıflandırma performansı verdiği; jyasar/DergiPark, 2021). Ancak bu değer soyutlamadadır, spesifik trader parametrelerinde değil.

**Öneri:** Momentum'u (ör. 3-aylık fiyat değişimi, 3ay-MA eksi 6ay-MA) ve oynaklığı (rolling std, değişim oranı dağılımı) türet; RSI/MACD'yi hazır kütüphaneden birebir kopyalama. Aylık ufukta 1, 3, 6, 12 aylık lag ve rolling pencereler uygundur.

*Leakage/ufuk notu:* Rolling ve lag feature'lar yalnızca t'den önceki verilerle hesaplanmalı; pencere sonrası (centered) istatistik leakage üretir. LSTM/dizi çalışmalarında pencere-üretiminin split'ten SONRA yapılmaması RMSE'de %20'ye varan sahte iyileşme (leakage) doğurmuştur (arXiv:2512.06932, 2025) — bu ilke feature türetiminde de geçerlidir.

*Projeye Uygulanabilirlik:* Momentum + oynaklık + lag ailesi düşük maliyetli, yüksek öncelikli; teknik-gösterge kopyası düşük öncelikli/deneysel.

### 3. Makro Feature Lag Seçimi Metodolojisi

Faz 2 sürücülerinin (kur, TÜFE, faiz, güven) fiyata etkisi gecikmelidir; optimal lag ampirik seçilmelidir. Literatürdeki standart:
- **Cross-correlation fonksiyonu (CCF):** sürücü ile hedef arasında farklı lag'lerde korelasyon; en yüksek anlamlı lag aday.
- **Granger-tipi ön eleme:** pairwise Granger nedensellik testleri çoklu lag'de (F-testi), lag başına p-değeri taranarak (grangersearch tarzı sistematik lag taraması, arXiv:2601.01604). Uyarı: Granger nedensellik gerçek nedensellik değil, lag'li tahmin gücüdür — feature ön elemesi için tam da bu istenir. CCF ve Granger sonuçlarının güçlü korele olmadığı (bir gösterge Granger'da anlamlı ama CCF'de değil olabilir) not edilmeli; ikisi tamamlayıcı kullanılmalı.
- **Regularizasyonlu seçim:** yüksek boyutlu makro-blok için Granger-Lasso, çoğu vakada tahmin hatasını (MAFE) düşürür (arXiv:1508.02846).

**Türkiye-özgü lag kanıtı (ERPT):** USD/TRY→fiyat geçişkenliğinin lag profili somut başlangıç değerleri verir:
- Leigh & Rossi (IMF WP 02/204, 2002): kur etkisi "yaklaşık bir yılda biter ama çoğunlukla ilk dört ayda hissedilir" (*"the impact of the exchange rate on prices is over after about a year, but is mostly felt in the first four months"*); WPI geçişi CPI'den daha belirgin.
- Özmen & Topaloğlu (TCMB Çalışma Tebliği 17/08, 2017; 2005q2–2015q2, 152 CPI alt-bileşeni, 0,5 USD + 0,5 EUR sepeti): geçişin *"approximately 40 percent of the pass-through is completed in the first quarter and 80 percent is completed in three quarters"*; CPI'ye 2-yıllık kümülatif geçiş ~%17 (%17,4, robustluk aralığı %15,7–18,5).
- Çekirdek mal (otomobil dahil) geçişi daha hızlı ve büyük: *"the exchange rate pass-through to core goods prices is around 25% and it is completed much faster compared to import prices, in about 3-4 quarters"* (Özmen & Topaloğlu, 2017). Otomobiller çekirdek malın arketipi olarak kullanılır: *"the majority of the core goods, i.e., automobiles, are imported"*; import-price geçişi ~%17 ve ~6 çeyrekte tamamlanır.
- State-dependence/asimetri: geçiş ısınma dönemlerinde ~%25, soğuma dönemlerinde <%10 (Kara, Öğünç, Özmen & Sarıkaya, "Exchange Rate Pass-Through: Is There a Magical Coefficient?", TCMB Blog, 2017); depreciation ve yüksek-enflasyon rejiminde daha güçlü — üst rejimde pozitif (depreciation) şoklar negatif şoklardan daha etkili (Kal, Arslaner & Arslaner, TCMB WP 15/30, 2015, threshold VAR, aylık veri). Kara & Öğünç'ün (2005) daha düşük ölçülen geçişkenliği kısmen şokların tek-yönlü olmamasına bağladığı da not edilmeli.

**Feature'a çevirme (iktisadi gerekçe tekrar edilmeden):** Kur için 1, 3, 6, 12 aylık lag'leri aday havuza koy; CCF/Granger ile ele. Otomobilin çekirdek-mal davranışı nedeniyle kısa lag'ler (1-3 ay) muhtemelen daha güçlü — bu bir ön hipotez, veriyle test edilmeli. Rejim etkileşimi (kur × ısınma/soğuma göstergesi) N2 ile tutarlı bir feature olarak eklenebilir.

*Leakage/ufuk notu:* Aynı-dönem (t) makro değeri kullanmak look-ahead bias'tır — çoğu makro seri gecikmeli yayımlanır (TÜFE ay sonu + gecikme). Yalnızca tahmin anında YAYIMLANMIŞ değerler kullanılmalı (yayım gecikmesi lag'e eklenmeli). Lag seçimi de sadece eğitim döneminde yapılmalı, tüm seride değil.

*Projeye Uygulanabilirlik:* Kur lag ailesi en yüksek öncelikli (en baskın sürücü); lag seçim prosedürü eğitim-içi, leakage'sız kurulmalı.

### 4. Kompozisyon Düzeltmesi (N1 Çözümü — Kritik Bölüm)

**Problem (N1):** BETAM sahibindex ve arabam.com endeksleri ham segment-ortalama ilan fiyatıdır, mix düzeltmesizdir. Aynı segmentte bile ayın ilan kompozisyonu (daha yeni/az km'li araçların payı) değiştiğinde ortalama fiyat gerçek fiyat hareketi olmadan kayar. BLS bile Manheim için "Manheim depreciation veya kalite değişimi için düzeltme YAPMAZ ve endeksi aylık yayımlar" notunu düşer — yani ham ortalama endeksin sınırı resmi olarak kabul edilir. Model bu düzeltmeyi kendi içinde yapmalıdır.

**Uygulanabilir çözümler (üç yaklaşım, artan sağlamlık):**

**(A) Sabit-kompozisyon / ağırlıklandırma (Laspeyres/Manheim tarzı) — birincil doğrulama katmanı.**
Manheim metodolojisi somut şablondur (Manheim / Cox Automotive, "Summary Methodology for Manheim Used Vehicle Value Index", 2023; endeks J.D. Power sınıflandırmasına göre 20 market-class üzerinden, yılda 5 milyondan fazla tamamlanmış satıştan kurulur):
1. Outlier kırpma: her model-yılı/marka/gövde için ortalama fiyat ve km; *"Outliers are defined as those where both price and mileage are outside of 2.6 standard deviations"* (fiyat VE km birlikte 2,6 SD dışıysa at).
2. Market-class bazında ortalama fiyat.
3. Mileage düzeltmesi: her market-class için fiyat~km doğrusal regresyonu; *"current month's average mileage by market class minus average mileage for that market class over the past 24 months"* farkıyla düzelt.
4. Sabit ağırlıklandırma: *"the Index is weighted based on a 24-month rolling average of past sales by market class"* — market-class'ları 24-aylık yuvarlanan satış payına göre ağırlıkla; sabit ağırlık mix kaymasını nötralize eder. Sonuç endeks mix-, mileage- ve mevsimsel-düzeltilmiş olup *"independent of underlying shifts in the characteristics of vehicles being sold"* niteliğindedir.
Bu yaklaşım projeye çevrildiğinde: her segment-yaş hücresini sabit ağırlıkla topla; hücre içi km'yi regresyonla düzelt. Basit, şeffaf, açıklanabilir; ancak yalnızca gözlenen hücre ağırlığını sabitler, hücre-içi kalite kaymasını tam çözmez.

**(B) Hedonik reziduel / hedonic imputation — ÖNERİLEN BİRİNCİL YÖNTEM.**
Log fiyatı N9 özniteliklerine regresyon et:

    log(P_it) = α_t + Σ β_k · x_k,it + ε_it

Burada x_k = {yaş, km, marka/model, motor, yakıt, şanzıman, donanım}. İki kullanım:
- **Time-dummy hedonik:** α_t katsayıları (dönem kuklaları) sabit-kalite fiyat endeksini verir; yön etiketi Δα_t'den hesaplanır. Not: log katsayıları geri çevirirken bias düzeltmesi gerekir (Wooldridge tarzı, normallik varsaymayan düzeltme; IAEE 2021 hedonik araç çalışması bu düzeltmeyi açıkça uygular).
- **Hedonic imputation / çift-imputation:** her dönem için sabit karakteristik setine göre fiyat tahmin edilip endeks kurulur (OECD, "Handbook on Hedonic Indexes and Quality Adjustments in Price Indexes", 2006; ONS'nin Price Index of Private Rents'te kullandığı "hedonic double imputation", Eurostat residential property price handbook Ch.5'e dayanır — uluslararası kabul görmüş yöntem).
Reziduel yaklaşımın feature değeri: ε_it (bir aracın hedonik-beklenen fiyattan sapması) segment "pahalılık/ucuzluk" sinyali olarak da feature'laştırılabilir. Türkiye used-car hedonik çalışmaları bu regresyonun uygulanabilirliğini doğrular (Erdem & Şentürk, "A Hedonic Analysis of Used Car Prices in Turkey"; ScienceDirect S0969698914001210 prospect-theory hedonik used-car çalışması — fiyat varyasyonunun çoğu gözlenen karakteristiklerle: motor gücü, yaş, ekstralar, motor tipi ile açıklanır).

**(C) Matched-model / depreciation-adjusted — hedef serisi için ek sağlamlık.**
BLS used cars metodolojisi: fiyat oranı, örneklenen araç (vintage v) ile bir model yılı genç muadili (v+1) arasında hesaplanıp depreciation düzeltmesi yapılır; kalite düzeltmesi yeni-araç düzeltmesinin depreciate edilmiş halidir (BLS, "Measuring Price Change in the CPI: Used Cars and Trucks", güncelleme 20 Mayıs 2026; örnek 2–7 yaş araçlar, J.D. Power JDPIN'den olasılık-orantılı 480 araç). Matched-model uyarısı: hızlı ürün devrinde "unmatched" modelleri atmak endeksi aşağı yanlı yapabilir (IMF CPI Manual Ch.7; OECD Handbook 2006) — Türkiye'de model devri hızlıysa bu bias izlenmeli. Chain-drift riski için yüksek-frekans zincirleme + compounding kullanılabilir ama chain-drift bias'a dikkat (arXiv:2305.00044, "Hedonic Prices and Quality Adjusted Price Indices").

**Somut reçete (projeye):**
1. Birincil: aylık hedonik regresyon (B); yön etiketini Δα_t (mix-düzeltilmiş) üzerinden hesapla.
2. Doğrulama: Manheim-tarzı sabit-ağırlık endeksi (A) ile karşılaştır; iki seri diverjans gösterirse mix kayması teşhis edilmiş demektir.
3. Feature bonusu: hedonik reziduel (ε) ve segment-bazlı reziduel ortalaması ek feature.

*Projeye Uygulanabilirlik:* Bu, N1'in doğrudan çözümüdür — teori değil reçete. Hedonik regresyon N9 setini tam kullanır; sabit-ağırlık yöntemi düşük maliyetli çapraz-kontrol sağlar.

### 5. Segment Tasarımı ve Sparse Cell Yönetimi

**Granülerlik trade-off'u:** Daha ince hücre (marka-model-yaş) daha yüksek prediktif çözünürlük ama daha az gözlem/daha gürültülü yön etiketi. Daha kaba hücre (segment) istatistiksel güç ama sinyal seyreltme. Literatürde net tek bir optimal granülerlik yok (**literatürde net değil**); veriyle hücre başına minimum gözlem eşiği belirlenerek seçilmeli.

**Sparse cell çözümleri (devşirilebilir):**
- **Hiyerarşik backoff:** seyrek model-yaş hücresini üst düzeye (marka-yaş → segment-yaş → genel) geri çek; n-gram dil modellerindeki backoff/interpolasyon mantığı (Chen & Goodman tarzı hiyerarşik smoothing) doğrudan uyarlanabilir.
- **Shrinkage / empirical Bayes:** hücre istatistiğini global ortalamaya doğru, hücredeki gözlem sayısıyla kontrol edilen bir katsayıyla çek. Micci-Barreca'nın high-cardinality smoothing formülü: (n·μ_hücre + m·μ_global)/(n+m), burada m priora ağırlık veren düzeltme sabiti. Bu hem kompozisyon hücre ortalamalarında hem target encoding'de kullanılır.
- **Hiyerarşik gruplama/kümeleme:** benzer segmentleri veri-temelli grupla (shrinkage estimator + hash-tabanlı seviye sıkıştırma pratikleri).

*Leakage/ufuk notu:* Hücre ağırlıkları/smoothing parametreleri yalnızca eğitim döneminden; hücre-bazlı hedef istatistikleri gelecek dönem gözlemi içermemeli.

*Projeye Uygulanabilirlik:* Segment-yaş hücresi + backoff + shrinkage önerilir; hücre başına gözlem eşiği bir hiperparametre olarak eğitim-içi belirlenmeli.

### 6. Alternatif/Öncü Veri Kaynakları

**Google Trends / arama trendi:** Araç piyasasında sınırlı ama gerçek prediktif güç. Kanıtlar karışık ama pozitife yakınsıyor: erken çalışmalar (Barreira vd. 2013; Fantazzini & Toktamysiva 2015) zayıf; Geva, Oestreicher-Singer, Efron & Shimshoni (MIS Quarterly 41(1):65-82, 2017) forum+arama kombinasyonuyla başarılı; von Graevenitz, Helmers, Millot & Turnbull (Almanya/UK, CGR Working Paper, 2016) "satın-alma niyeti" içeren aramaların satışı öngördüğünü, salt marka aramasının zayıf öngörücü olduğunu bulur. Bir Massey Üniversitesi tez çalışması (Google Trends as complementary tool for new car sales forecasting; Hindistan/Güney Kore) Google Trends'in yeni araç satışı varyansının %10,8'ini açıkladığını, ABD'de ilişkilerin %63'ünün anlamlı (R²≈0,282), Almanya'da %46'sının anlamlı (R²≈0,226) olduğunu raporlar. Wijnhoven & Plant (ICIS 2017) sosyal medya sentiment'inin zayıf, Google Trends + mention hacminin anlamlı olduğunu bulur. ECB (Nymand-Andersen & Pantelidis, ECB Statistics Paper, 2018) euro-alanı araç satışını Google ile nowcast eder. Kritik nokta: bu kanıtların çoğu SATIŞ/ADET tahminine dairdir; İLAN FİYAT YÖNÜ tahminine doğrudan katkısı **literatürde net değil** — feature olarak denenmeli ama abartılı beklenti kurulmamalı. Ayrıca Google Trends'i ekonomik değişkenlerle birleştirmenin out-of-sample performansı her zaman iyileştirmediği (yalnızca 12-ay lag'li CPI'nin katkı verdiği) da raporlanmıştır (Annals CSIS, 2019).

**Days-on-market / arz-talep oranı / talep endeksi (Faz 2: BETAM):** Sektör pratiğinde güçlü öncü. Market Day Supply (MDS = envanter/günlük satış hızı) düşükse fiyat yukarı, yüksekse aşağı baskı (Cox Automotive/vAuto pratiği; Laser Appraiser MDS kılavuzu: "Vehicles with high MDS may require price cuts or incentives, whereas models with lower MDS can sustain higher pricing"). Cox Automotive verileri days-on-market artışının fiyat yumuşamasıyla eş-hareket ettiğini gösterir (S&P Global Ocak 2026: "days advertised before sale increased... indicating that listings are taking longer to convert" ile eş zamanlı fiyat yumuşaması); Cox'un wholesale days'-supply serisi de mevsimsel bir referans verir (pandemi öncesi Şubat sonu ~31 gün). Bu, N2 (arz rejimi) ile tutarlı ve BETAM days-on-market / satılan-satılık oranı / talep endeksinin doğrudan feature olacağını destekler. Akademik peer-reviewed kanıt used-car fiyat YÖNÜ için sınırlı (**literatürde net değil**), ancak mekanizma ve endüstri kanıtı güçlü.

**İlan hacmi/akışı:** arz proxy'si; ani ilan artışı arz şoku (kampanya rejimi, N2) sinyali olabilir.

*Leakage/ufuk notu:* Days-on-market ve ilan hacmi aynı-dönem gerçekleşen büyüklüklerdir; t dönemi feature'ı olarak kullanılırsa look-ahead riski var — yalnızca t-1 ve öncesi kullanılmalı. Google Trends gerçek-zamanlı yayımlandığından görece güvenli ama yine lag'lenmeli.

*Projeye Uygulanabilirlik:* Days-on-market/arz-talep oranı yüksek öncelikli öncü feature; Google Trends orta öncelikli deneysel; her ikisi de lag'li.

### 7. Kategorik/Metin Feature ve Leakage-Safe Kodlama

**Metin/donanım alanları (N9 + Kaggle pratikleri):** İlan metni ve donanım alanlarından binary/sayısal feature çıkarımı (parse: "otomatik", "hasarsız", "LPG'li", donanım paketleri; sayısal parse: km, yaş). Kaggle used-car pratikleri (cars.com/Craigslist veri setleri; ör. taeefnajib/cars.com 4009 satır, marka-model-yıl-km-yakıt-motor alanları) metin parse, kategorik indirgeme, aykırı-değer kırpma, deduplication ve türetilmiş feature (car age, fuel-economy score) üretimini standartlaştırır. Bu N9'un devşirilebilir çekirdeğidir.

**High-cardinality kategorikler (marka-model) — leakage-safe target encoding:**
- **Problem:** Naif target encoding (tüm veriyle grup ortalaması) hedef sızıntısı yaratır; özellikle seyrek kategoride (ör. tek gözlemli kategori %100 koşullu olasılık verir) encoding hedefi ele verir (Micci-Barreca, "A Preprocessing Scheme for High-Cardinality Categorical Attributes in Classification and Prediction Problems", ACM SIGKDD Explorations, 2001).
- **Çözümler:** (a) fold-dışı (out-of-fold) hesaplama — encoding her CV fold'unda yalnızca eğitim fold'undan hesaplanmalı; (b) smoothing (yukarıdaki shrinkage formülü); (c) CatBoost ordered target statistics / expanding-mean — sadece o satırdan önceki gözlemleri kullanır, zaman serisi validasyonunu taklit eder (Prokhorenkova vd., "CatBoost: unbiased boosting with categorical features", NeurIPS 2018). Regularized target encoding geleneksel yöntemleri high-cardinality'de geçer (Pargent vd., Computational Statistics, 2022, doi:10.1007/s00180-022-01207-6).
- **Hiyerarşik target encoding:** marka-model gibi implicit hiyerarşi varsa backoff'lu encoding (Micci-Barreca'nın orijinal makalesinde önerdiği ama çoğu uygulamanın atladığı hiyerarşik varyant) — Bölüm 5 ile birleşir.

*Leakage/ufuk notu:* Zaman serisinde çift kısıt: encoding hem fold-dışı hem sadece-geçmiş olmalı. Ordered/expanding-mean bu iki kısıtı doğal karşılar — bu proje için tercih edilmeli. Standart k-fold target encoding zamansal sıra korunmazsa gelecek bilgisi sızdırır; LOO encoding ise ikili sınıflandırmada iki-değerli encoding üreterek doğrudan hedefi ele verebilir.

*Projeye Uygulanabilirlik:* marka-model için ordered/expanding-mean target encoding + hiyerarşik backoff; metin parse feature'ları düşük leakage, yüksek öncelik.

### 8. FEATURE ÜRETİM TABLOSU

| Feature Ailesi | Kaynak Değişken (Faz 2/N9) | Türetim Yöntemi | Aylık Ufka Uygunluk | Leakage Riski | Beklenen Sinyal Türü | Öncelik |
|---|---|---|---|---|---|---|
| Kur lag'leri | USD/TRY (Faz 2, baskın sürücü) | 1/3/6/12 ay lag; CCF+Granger ile seç | Yüksek (ERPT ~%40 ilk çeyrek) | Düşük — yayımlanmış geçmiş değer; t kullanılmazsa | Yön: kur↑→fiyat↑ gecikmeli | Çok yüksek |
| Kur momentum/oynaklık | USD/TRY | 3ay değişim; rolling std | Yüksek | Düşük — sadece geçmiş pencere | Hızlanan depreciation → yukarı baskı | Yüksek |
| Enflasyon lag | TÜFE (Faz 2) | MoM/YoY, 1-6 ay lag | Yüksek | Orta — yayım gecikmesi lag'e eklenmezse leakage | Nominal yukarı taban | Yüksek |
| Faiz lag | Taşıt kredisi faizi (Faz 2) | Seviye + değişim, 1-3 ay lag | Orta-Yüksek | Düşük — geçmiş değer | Faiz↑→talep↓→aşağı | Orta |
| Tüketici güveni | Tüketici güven endeksi (Faz 2) | Lag + değişim | Orta | Düşük | Öncü talep sinyali | Orta |
| ÖTV event | ÖTV Resmî Gazete tarihleri (Faz 2) | Event dummy + t-since-event | Yüksek | Düşük — tarih önceden bilinir | Rejim kırılma sinyali | Yüksek |
| Arz rejim etkileşimi | ODMD sıfır satış/kampanya (Faz 2, N2) | Kur × arz-rejim göstergesi etkileşimi | Orta | Orta — aynı-dönem arz t-1'e çekilmeli | Çift-yönlü (kıtlık→↑, kampanya→↓) | Yüksek |
| Days-on-market | BETAM DOM (Faz 2) | Seviye + değişim, t-1 lag | Yüksek | Yüksek — aynı-dönem büyüklük; lag zorunlu | DOM↑→aşağı baskı (öncü) | Yüksek |
| Arz-talep oranı | BETAM satılan/satılık, talep endeksi | Oran + momentum, lag'li | Yüksek | Yüksek — lag'lenmezse look-ahead | Düşük oran→yukarı | Yüksek |
| İlan hacmi/akışı | İlan sayısı (arz proxy) | Akış + değişim, lag'li | Orta | Yüksek — aynı-dönem; lag zorunlu | Arz şoku sinyali | Orta |
| İndirim farkı | arabam.com bireysel-kurumsal indirim (Faz 2) | Fark seviyesi + değişim | Orta | Orta | Piyasa gevşekliği sinyali | Orta |
| Google Trends | Arama trendi (dışsal) | Model/segment sorgu hacmi, lag'li | Orta — aylık toplanır | Düşük-Orta — gerçek-zamanlı; yine lag'le | Zayıf öncü talep | Düşük-Orta (deneysel) |
| Hedonik reziduel | Fiyat + N9 öznitelikleri | log-fiyat hedonik reg. rezidueli (ε) | Yüksek | Orta — reg. eğitim-içi fit; leakage'a dikkat | Segment ucuz/pahalı sapması | Yüksek |
| Segment lag/momentum | Mix-düzeltilmiş segment fiyatı (N1, Δα_t) | Δα_t lag; 3ay momentum; rolling std | Yüksek | Orta — yön etiketiyle örtüşmemeli | Otokorelasyon/momentum | Yüksek |
| Marka-model encoding | Marka/model (N9, high-card.) | Ordered/expanding-mean target enc. + backoff | Yüksek | Orta — naif ise yüksek; ordered ile düşer | Kategori-bazlı seviye | Orta-Yüksek |
| Metin/donanım parse | İlan metni/donanım (N9) | Binary/sayısal parse (LPG, hasar, paket) | Yüksek | Düşük | Statik kalite sinyali | Orta |
| Yakıt/LPG payı | Yakıt türü payları, LPG payı (Faz 2) | Segment içi pay + değişim | Orta | Orta | Kompozisyon/talep kayması | Orta |
| Mevsimsellik | Takvim | Ay/çeyrek dummy, Fourier terimleri | Yüksek | Düşük | Mevsimsel yön (ör. yıl sonu) | Orta |

### 9. Açık Sorular / Literatürde Net Olmayanlar

- **Optimal segment granülerliği:** marka-model-yaş vs. segment-yaş için tek bir literatür-onaylı optimal yok; veriyle belirlenecek (**literatürde net değil**).
- **Google Trends → ilan fiyat YÖNÜ:** kanıtların neredeyse tümü satış/adet tahmini içindir; fiyat yönü tahminine katkı doğrudan gösterilmemiştir (**literatürde net değil**).
- **Days-on-market'ın fiyat yönü öncüsü olarak akademik doğrulaması:** sektör pratiği güçlü, peer-reviewed used-car fiyat-yönü kanıtı sınırlı (**literatürde net değil**).
- **Türkiye ERPT'nin AY-bazlı profili:** çalışmaların çoğu çeyreklik; ay-bazlı ağırlıklar interpolasyondur (Özmen & Topaloğlu 2017 uyarısı).
- **Otomobile-özgü ERPT katsayısı:** temiz, istatistiksel anlamlı otomobil-tek katsayısı kimliklendirilememiş (item-düzeyi güven aralıkları geniş); çekirdek-mal ~%25 proxy olarak kullanılıyor.
- **Hedonik model devri bias'ı:** Türkiye'de hızlı model devrinde matched-model aşağı yanlılığının büyüklüğü ölçülmeli (**literatürde net değil**).

## Recommendations

1. **Önce N1'i çöz (bloke edici):** Aylık hedonik regresyon (log fiyat ~ N9 seti) kur, yön etiketini mix-düzeltilmiş Δα_t'den üret. Manheim-tarzı sabit-ağırlık endeksiyle çapraz-doğrula. Bu yapılmadan hiçbir zaman serisi feature'ına güvenilmemeli — ham ortalama üzerinden üretilen etiket sahte sinyal taşır. *Eşik:* iki seri arasında sistematik diverjans varsa mix düzeltmesi kritik demektir; yoksa sabit-ağırlık yeterli olabilir.
2. **Makro lag ailesini ampirik kur:** Kur için 1/3/6/12 ay aday havuzu; CCF + pairwise Granger (çoklu lag) ile eğitim-içi seç. Yayım gecikmelerini lag'e ekle. *Eşik:* Granger p<0,05 ve CCF tepe lag'i tutarlıysa feature'ı sabitle; ikisi çelişirse ikisini de aday tut.
3. **Öncü arz/talep feature'larını önceliklendir:** BETAM days-on-market, satılan/satılık oranı, talep endeksi — hepsi t-1 lag'li. N2 rejim etkileşimini (kur × arz-rejim) ekle.
4. **Leakage-safe encoding'i standartlaştır:** marka-model için ordered/expanding-mean target encoding (CatBoost tarzı) + hiyerarşik backoff; k-fold yerine zamansal-sıra korumalı hesaplama.
5. **Teknik göstergeleri soyutlama düzeyinde al:** momentum + oynaklık türet; RSI/MACD'yi hazır parametrelerle birebir kopyalama. Deneysel/düşük öncelik.
6. **Google Trends'i deneysel tut:** ekle ama düşük ağırlık/beklenti; katkısı fiyat yönü için kanıtlanmamış.
7. **Aşamalı feature genişletme:** Önce yüksek-öncelik ailesi (kur lag, hedonik reziduel, segment momentum, days-on-market, ÖTV event); sonra orta-öncelik; en son deneyseller. *Eşik:* bir feature ailesi eğitim-içi önem/istikrar göstermezse (ör. cross-fold önem sıralaması Spearman <0,8 istikrarsız) çıkar.

## Caveats

- Bu faz feature *üretimini* kapsar; model mimarisi, validasyon/backtest protokol detayı, label/threshold tasarımı ve makro dinamiklerin iktisadi açıklaması KAPSAM DIŞIDIR ve önceki/sonraki fazlara aittir.
- Leakage'a yalnızca "feature seçimi leakage üretmemeli" ilkesi düzeyinde değinildi; teknik validasyon protokolü tasarlanmadı.
- Türkiye ERPT sayıları çeyreklik çalışmalardan; ay-bazlı kullanımda interpolasyon varsayımı var. Ayrıca ERPT büyüklüğü zamanla ve rejime göre değişir ("magical coefficient" yoktur); tek bir sabit katsayı varsayılmamalı.
- Endüstri kaynakları (Cox/Manheim/Kaggle blogları) akademik kaynaklardan ayrı güvenilirlik düzeyinde sunuldu; mekanizma göstergesi olarak değerli ama peer-reviewed kanıt değiller. Cox/Manheim rakamları ABD wholesale piyasasına aittir; Türkiye ilan (retail asking) piyasasına doğrudan aktarılmamalı, yalnızca metodoloji/mekanizma örneği olarak kullanılmalı.
- Kompozisyon düzeltmesi reçetesi Manheim/BLS/OECD/ONS metodolojisinden uyarlanmıştır; Türk ilan verisinin km/donanım alanı eksikliği veya gürültüsü hedonik regresyonun gücünü sınırlayabilir — veri kalitesi ön-kontrol edilmeli.

## Kaynakça

1. Renault, Bondu, Lemaire & Gay (2023), "Automatic Feature Engineering for Time Series Classification: Evaluation and Discussion", arXiv:2308.01071.
2. Christ, Braun, Neuffer & Kempa-Liehr (2018), "Time Series FeatuRe Extraction on basis of Scalable Hypothesis tests (tsfresh — A Python package)", Neurocomputing 307:72-77, doi:10.1016/j.neucom.2018.03.067.
3. Manheim / Cox Automotive (2023), "Summary Methodology for Manheim Used Vehicle Value Index".
4. U.S. Bureau of Labor Statistics (2026), "Measuring Price Change in the CPI: Used Cars and Trucks".
5. U.S. Bureau of Labor Statistics (2019), "A New Vehicles Transaction Price Index", Research Paper ec190040.
6. OECD (2006), "Handbook on Hedonic Indexes and Quality Adjustments in Price Indexes", ISBN 92-64-02814-5.
7. ONS (2024), "Price Index of Private Rents detailed methodology" (hedonic double imputation).
8. IMF, "Consumer Price Index Manual", Ch.7 "Adjusting for Quality Change".
9. "Hedonic Prices and Quality Adjusted Price Indices", arXiv:2305.00044 (2023).
10. Erdem & Şentürk, "A Hedonic Analysis of Used Car Prices in Turkey".
11. ScienceDirect S0969698914001210, hedonic price model / prospect theory, used cars.
12. IAEE (2021), "Hedonic Pricing of Vehicle Characteristics, Safety and Equipment".
13. Leigh & Rossi (2002), "Exchange Rate Pass-Through in Turkey", IMF Working Paper WP/02/204.
14. Özmen & Topaloğlu (2017), "Disaggregated Evidence for Exchange Rate and Import Price Pass-through...", TCMB Çalışma Tebliği 17/08.
15. Kara, Öğünç, Özmen & Sarıkaya (2017), "Exchange Rate Pass-Through: Is There a Magical Coefficient?", TCMB Blog.
16. Kal, Arslaner & Arslaner (2015), "Sources of Asymmetry and Non-linearity in Pass-Through of Exchange Rate and Import Price...", TCMB Çalışma Tebliği 15/30.
17. Micci-Barreca (2001), "A Preprocessing Scheme for High-Cardinality Categorical Attributes in Classification and Prediction Problems", ACM SIGKDD Explorations.
18. Prokhorenkova, Gusev, Vorobev, Dorogush & Gulin (2018), "CatBoost: unbiased boosting with categorical features", NeurIPS.
19. Pargent, Pfisterer, Thomas & Bischl (2022), "Regularized target encoding outperforms traditional methods in supervised machine learning with high cardinality features", Computational Statistics, doi:10.1007/s00180-022-01207-6.
20. von Graevenitz, Helmers, Millot & Turnbull (2016), "Does Online Search Predict Sales? Evidence from Big Data for Car Markets in Germany and the UK", CGR Working Paper.
21. Geva, Oestreicher-Singer, Efron & Shimshoni (2017), "Using forum and search data for sales prediction of high-involvement products", MIS Quarterly 41(1):65-82.
22. Nymand-Andersen & Pantelidis (2018), "Google econometrics: nowcasting euro area car sales and big data quality requirements", ECB Statistics Paper.
23. Wijnhoven & Plant (2017), "Sentiment Analysis and Google Trends Data for Predicting Car Sales", ICIS 2017 Proceedings.
24. "Hidden Leaks in Time Series Forecasting: How Data Leakage Affects LSTM Evaluation...", arXiv:2512.06932 (2025).

Ek/destekleyici kaynaklar: grangersearch R paketi (arXiv:2601.01604); Granger-Lasso yüksek boyutlu seçim (arXiv:1508.02846); "Öznitelik Mühendisliği ile Makine Öğrenmesi Yöntemleri Kullanılarak BIST 100 Endeksi..." (jyasar/DergiPark, 2021); Massey Üniversitesi tezi "Google trends as complementary tool for new car sales forecasting"; Cox Automotive / S&P Global / Laser Appraiser MDS endüstri kaynakları (mekanizma göstergesi).

## Kullanılan Nihai Arama Sorguları

1. feature engineering time series classification methods
2. mix adjustment composition bias used car price index
3. target encoding leakage time series cross-validation
4. macroeconomic lag selection forecasting cross-correlation Granger
5. Google Trends nowcasting car sales prices predictive
6. hedonic residual price index construction used cars
7. technical indicators RSI MACD applicability non-financial time series critique
8. sparse category hierarchical smoothing backoff high cardinality encoding
9. days on market inventory leading indicator used car price forecast
10. matched-model price index methodology Eurostat ONS handbook
11. time series feature engineering financial technical indicators forecasting empirical value
12. used car listing text NLP feature extraction description Kaggle price prediction
13. tsfresh automated feature extraction time series
14. öncü gösterge fiyat tahmini zaman serisi öznitelik mühendisliği
15. exchange rate pass-through consumer prices lag months emerging market
16. CatBoost ordered target encoding leave-one-out prevent leakage
17. (subagent) Turkey exchange rate pass-through consumer prices lag structure automobiles state-dependent asymmetric — TCMB/IMF sources