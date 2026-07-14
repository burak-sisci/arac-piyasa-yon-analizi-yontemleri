---
faz_no: 04
faz_adi: "Araç Fiyat Tahmini Akademik Literatürü"
tarih: 2026-07-13
kapsam_ozeti: "Mevcut araç fiyat tahmini literatürünün kapsamı, sınırları ve yön sınıflandırmasına adaptasyon boşluğunun belgelenmesi"
bagimli_oldugu_fazlar: [01]
durum: tamamlandi
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 24
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-15
---

# FAZ 04 — Araç Fiyat Tahmini Akademik Literatürü ve Yön Sınıflandırmasına Adaptasyon Boşluğu

## TL;DR

- **Merkezi bulgu doğrulandı:** Araç fiyat tahmini literatürünün neredeyse tamamı KESİTSEL (cross-sectional) bir REGRESYON problemi çözüyor — tek bir aracın fiyatını, o aracın statik özelliklerinden (marka, model, yaş, km, donanım) tahmin ediyor. Bizim problemimiz (bir segment/piyasa fiyat seviyesinin ZAMAN İÇİNDEKİ YÖNÜNÜ up/down/stable olarak sınıflamak) literatürde doğrudan karşılığı OLMAYAN bir problemdir.
- **Bize en yakın dal "residual value forecasting" (artık değer öngörüsü):** Leasing/filo sektörünün artık değer literatürü (Lessmann & Voß 2017; Dress et al. 2018; Rashed et al. 2019) gelecekteki bir fiyatı öngördüğü için zaman boyutu içerir; ancak hâlâ nokta-tahmin (regresyon) yapar ve sözleşme başındaki araç özniteliklerine dayanır — piyasa seviyesi bir yön sınıflaması değildir. Yine de asimetrik maliyet, model heterojenliği ve "özel bilgi" bulguları devşirilebilirdir.
- **Belgelenen boşluk bir teslimattır:** Bağımsız aramalar, kümüle bir kullanılmış-araç fiyat ENDEKSİNİ zaman serisi olarak öngören veya piyasa fiyat yönünü up/down/stable sınıflayan hakemli hiçbir çalışma bulamadı. Geliştirici ekip bu noktada "hazır reçete yok, öncü çalışma yapıyoruz" diyebilir; bu novelty iddiası literatürle desteklenmektedir.

## Key Findings

1. **Kesitsel regresyon hâkimiyeti.** Kullanılmış araç fiyat tahmini yayınlarının ezici çoğunluğu, tek aracın fiyatını statik özniteliklerden tahmin eden regresyon çalışmalarıdır; ağaç-tabanlı ensemble (Random Forest, gradient boosting) yöntemleri baskın kazanan model ailesidir (Lessmann & Voß 2017, *Int. J. Forecasting* 33(4):864-877; çok sayıda Kaggle/ML çalışması). Bu literatür "hangi özellik prediktif" sorusuna cevap verir ama "fiyat seviyesi ne yöne gidecek" sorusuna cevap vermez.

2. **Prediktif özniteliklerde güçlü uzlaşı.** Çalışmalar arası tutarlı olarak en güçlü fiyat belirleyicileri: model yılı/yaş, kilometre, marka/model, motor gücü/hacmi, yakıt tipi ve şanzıman tipidir (Lessmann & Voß 2017; Erdem & Şentürk 2009; Daştan 2016). Yaş ve km negatif; performans/donanım pozitif etkilidir.

3. **Hedonik fiyatlama = özniteliklerin gölge fiyatları.** Rosen (1974) temelli hedonik model, fiyatı bileşen niteliklerin örtük fiyatlarına ayrıştırır; yarı-logaritmik (semi-log) form standarttır ve katsayılar yaklaşık yüzde etkisi verir (İstanbul: Akay et al. 2018; Türkiye: Erdem & Şentürk 2009, Daştan 2016). Hedonik modeller açıklayıcıdır ama tahmin doğruluğu ensemble'lardan düşüktür (Shmueli & Koppius çerçevesi).

4. **Residual value (artık değer) literatürü zaman boyutu içeren tek olgun daldır.** Leasing sözleşmesi başında, sözleşme sonundaki (gelecekteki) yeniden satış fiyatı öngörülür. Random Forest en etkili yöntemdir; Lessmann & Voß (2017) doğrudan şunu bulur: *"random forest regression is particularly effective for resale price forecasting. It is also shown that the use of linear regression, the prevailing method in previous work, should be avoided."* Kritik metodolojik katkılar: asimetrik hata maliyeti (fazla tahmin, eksik tahminden daha pahalı — Dress et al. 2018), çok-görevli öğrenme ile yardımcı hedefler (gerçekleşen km, hasar — Rashed et al. 2019), ve satıcının "özel bilgi" avantajı.

5. **Değer kaybı (depreciation) eğrileri geometrik/üstel biçimlidir ve segment-bağımlıdır.** Storchmann (2004, *Transportation* 31(4):371-408): 30 ülkeden 54 araç modeli örneğinde *"geometric depreciation appears to be a good approximation to real depreciation rates"* ve *"The average depreciation in OECD countries is 31%, whereas in non-OECD countries it is about 15%."* Schloter (2022, *Transport Policy* 126:268-279): 24.000 kullanılmış araç satışı verisiyle *"electric vehicles have a substantially higher depreciation of 1.16% per month (13.9% per annum) compared to gasoline vehicles with 0.87% per month (10.4% per annum)"* ve araçların yaşa göre *"degressive depreciation"* (azalan hızda değer kaybı) sergilediğini bulur. Bu eğriler zamanla ilgilidir ama bir aracın yaşı boyunca değer kaybını modeller, piyasanın takvim-zamanı boyunca hareketini değil.

6. **Piyasa/endeks düzeyinde zaman serisi çalışması akademik literatürde YOK.** Manheim Used Vehicle Value Index (MUVVI) gibi kümüle endeksler yalnızca endüstri (Cox Automotive) tarafından üretilir ve öngörülür; hakemli bir kullanılmış-araç fiyat endeksi zaman serisi öngörüsü bulunamadı. En yakın istisna Asilkan & Irmak (2009): model-bazında ortalama fiyat zaman serisini YSA ile öngörür — ama endeks değil, regresyondur.

7. **İlan verisi metodolojik tuzaklarla doludur.** İlan (asking) fiyatı ≠ gerçekleşen (transaction) fiyat; aradaki pazarlık marjı ve satılmayan ilanların yarattığı seçilim yanlılığı temel sorunlardır. Web-scrape veri seti gürültülüdür (serbest-metin alanlar, aykırı değerler, tekrarlı/ölü ilanlar). Bu, neredeyse tüm scraping-tabanlı çalışmaların ortak zaafıdır.

8. **Türkiye piyasası üzerine sağlam bir hedonik ve ML külliyatı var — ama tamamı kesitsel.** Erdem & Şentürk (2009), Akay et al. (2018, İstanbul), Daştan (2016, N=1000, sahibinden+arabam), Ecer (2013, hedonik vs YSA) ve çok sayıda tez. Hepsi belirli bir zaman kesitinde fiyat seviyesini/belirleyicilerini modeller; hiçbiri fiyat yönünü zaman içinde sınıflamaz.

## Details

### 1. Giriş: Literatürün Konumu ve Problem Uyuşmazlığı

Araç fiyat tahmini literatürü olgun ve kalabalıktır, ancak baskın problem tanımı bizimkinden yapısal olarak farklıdır. Standart kurulum şudur: veri kümesi = araçlar (satır), öznitelikler = statik araç karakteristikleri (marka, model, yaş, km, motor, donanım), hedef = o aracın fiyatı (sürekli değişken). Bu bir **kesitsel regresyon** problemidir. Amaç, "bu özelliklere sahip bir araç ne kadar eder?" sorusudur.

Bizim problemimiz ise: veri kümesi = zaman noktaları veya (segment × zaman) hücreleri, hedef = bir segment/piyasa fiyat seviyesinin bir sonraki dönemde **yukarı/aşağı/yatay** hareket edeceği (kategorik). Bu bir **zaman serisi sınıflandırma** problemidir. İki problem arasındaki fark yalnızca "regresyon vs sınıflandırma" değil; analiz düzeyi (araç vs piyasa/segment) ve zaman boyutunun varlığıdır. Literatür bu üç eksende de bizimkinden ayrışır.

Bu fazın ana tezi doğrulanmıştır: mevcut literatür "hangi araç ne kadar eder"i çözer; "piyasa ne yöne gidiyor"u çözmez. Aşağıdaki bölümler bu boşluğu titizlikle haritalar ve devşirilebilir olanı ayıklar.

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Kesitsel literatürün problem kurgusu bize doğrudan aktarılamaz. Ancak öznitelik-fiyat ilişkileri bilgisi, segment tanımı için (hangi araç grupları homojen fiyat davranışı gösterir) girdi olabilir. Literatürün asıl değeri "yöntem şablonu" değil, "hangi değişkenler fiyatı sürüyor" bilgisidir.

### 2. Kesitsel Araç Fiyat Tahmini Literatürü

Bu dal, "hangi özellikler prediktif çıkıyor" sorusunda güçlü bir uzlaşı üretir. Lessmann & Voß'un (2017, *International Journal of Forecasting* 33(4):864-877) 6 araç modeli ve ~450.000 örnek üzerinde 19 yöntemi kıyaslayan kapsamlı çalışması, **Random Forest regresyonunun** özellikle etkili olduğunu ve önceki çalışmalarda hâkim olan **doğrusal regresyondan kaçınılması gerektiğini** gösterir. Aynı çalışma iki önemli ek bulgu sunar: (a) yeniden satış fiyatı tahmininde **heterojenlik** vardır (bazı araç modelleri diğerlerinden çok daha zor modellenir) ve otomatik olarak bunu aşan yöntemler tanımlanır; (b) araç **satıcıları, piyasa araştırma ajanslarına kıyasla enformasyonel avantaja** sahiptir — çalışmanın kendi ifadesiyle: *"the study confirms that the sellers of used cars possess informational advantages over market research agencies, which enable them to forecast resale prices more accurately. This implies that sellers have an incentive to invest in in-house forecasting solutions, instead of basing their pricing decisions on externally generated residual value estimates."*

Feature importance bulguları çalışmalar arası tutarlıdır: yaş/model yılı ve kilometre neredeyse her çalışmada en güçlü iki belirleyicidir; ardından marka/model, motor gücü/hacmi, yakıt tipi, şanzıman gelir. Renk, donanım kalemleri ikincil ama ölçülebilir etkilidir.

**Metrik okuma uyarısı:** Bu çalışmalarda raporlanan R² (%80-99) ve RMSE değerleri **veri setine, segmente ve fiyat aralığına şiddetle bağlıdır** ve çalışmalar arası doğrudan kıyaslanamaz. Örneğin dar bir segment (tek marka) veya sentetik Kaggle verisinde R² şişer. Bu sayıları bir "sıralama tablosu" olarak okumak metodolojik hatadır; yalnızca "bu veri kümesinde bu öznitelikler bu kadar sinyal taşıyor" olarak yorumlanmalıdır.

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Bu dalın feature seti bize kısmen aktarılabilir — ama dikkatle. Kesitsel öznitelikler (marka, yaş, km) bir aracın *seviyesini* belirler; bizim hedefimiz seviye değil, seviyenin *değişim yönüdür*. Sabit bir aracın markası zaman içinde değişmediğinden, kesitsel öznitelikler yön sinyali taşımaz. Devşirilebilir olan: hangi segmentlerin (ör. lüks vs ekonomi, EV vs ICE) sistematik olarak farklı fiyat davranışı gösterdiği bilgisi — bu, segment-bazlı yön modellemesinde stratifikasyon için kullanılabilir. Random Forest/GBM'in tablo verisinde üstünlüğü de taşınabilir bir gözlemdir, ancak model mimarisi bu fazın kapsamı dışındadır.

### 3. Hedonik Fiyatlama ve Nitelik Ayrıştırması

Hedonik yaklaşım (Rosen 1974, *Journal of Political Economy* 82(1):34-55) fiyatı, ürünün oluşturucu niteliklerinin örtük ("gölge") fiyatlarının toplamı olarak modeller. Araç piyasasında standart form yarı-logaritmiktir (bağımlı değişken ln(fiyat)), çünkü bu form katsayıları yaklaşık yüzde etkisi olarak yorumlanabilir kılar (Halvorsen & Palmquist 1980 kuralı dummy değişkenler için).

Bulgular: İngiltere piyasası için hedonik analizde (2008-19 verisi) performans ve araç boyutu ana fiyat sürücüleridir ve etki, fiyat arttıkça güçlenir; alternatif yakıtlı araçlar karakteristik değişimlerine daha duyarlıdır ve fiyat artışının ~%65'i yalnızca araç kalitesindeki iyileşmeden kaynaklanır (kalite-ayarlı hedonik endeks). Prieto, Caracciolo & Baltas (2015, *Journal of Retailing and Consumer Services*) hedonik modeli prospect teorisiyle birleştirir: güvenilirlik beklenen referans değerin altındayken tüketiciler risk-arayan, üstündeyken risk-kaçınan davranır — güvenilirliğin fiyat üzerindeki etkisi asimetrik ve doğrusal-olmayandır.

Hedonik modellerin bilinen zaafı: OLS aykırı değerlere duyarlıdır; İstanbul çalışması (Akay et al. 2018) bu yüzden robust/resistant tahmin yöntemleri kullanır.

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Hedonik modelin katsayıları statik gölge fiyatlardır; bir niteliğin gölge fiyatının zaman içinde nasıl kaydığı (ör. dizel priminin daralması, EV priminin erimesi) teorik olarak yön sinyali taşır. Ancak standart hedonik literatür bunu tek kesitte dondurur; zaman-değişken katsayı (time-varying hedonic index) çalışmaları enderdir ve araç piyasası için pratikte yalnızca kalite-ayarlı endeks üretiminde kullanılır — yön sınıflaması için değil. Devşirilebilir fikir: ardışık kesitlerde hedonik katsayıların farkı, bir segmentin göreli değer kayması için özellik (feature) üretebilir. Bu, literatürde hazır bulunmayan, bizim inşa etmemiz gereken bir köprüdür.

### 4. Değer Kaybı ve Artık Değer (Residual Value) Tahmini — Zaman Boyutlu Literatür

Bu, problemimize **en yakın** olgun literatür dalıdır ve bu yüzden ayrıntılı incelenmiştir. Leasing bağlamında sözleşme, aracın gelecekteki (sözleşme sonu) artık değerine göre fiyatlanır: leasing oranı = liste fiyatı − artık değer. Dolayısıyla artık değer öngörüsü gerçek bir **gelecek-zaman** öngörüsüdür.

**Yöntem ve bulgular:**
- **Lessmann & Voß (2017):** RF en etkili; doğrusal regresyondan kaçınılmalı; heterojenlik ve satıcı özel-bilgisi kritik.
- **Dress, Lessmann & von Mettenheim (2018, arXiv:1707.02736; *Int. J. Forecasting*):** Öngörü hatalarının maliyeti **asimetriktir**. Artık değeri fazla tahmin etmek (overestimate), araç iadede beklenenden ucuza satıldığında doğrudan zarar/kâr kaybı yaratır; eksik tahmin ise fırsat maliyeti (daha düşük leasing oranıyla daha çok satış yapılabilirdi). Fazla-tahmin maliyeti eksik-tahminin iki katı varsayıldığında, asimetriyi model kurgusuna gömmek karar maliyetini ~%8 azaltır. Asimetriyi *model tahmini sırasında* hesaba katmak, tahminleri *sonradan düzeltmekten* üstündür.
- **Rashed et al. (2019, ECML; Volkswagen Financial Services, ~270k sözleşme):** Çok-görevli derin öğrenme. Ana hedef artık değer; yardımcı hedefler gerçekleşen km, hasar maliyeti, satışa kadar geçen gün, iade tarihi. Yardımcı hedefler (sözleşme başında bilinmeyen, dinamik büyüklükler) paylaşımlı temsili zenginleştirir ve tek-görev regresyonu anlamlı biçimde geçer. Veri kronolojik olarak train/test'e bölünür (2002-2014 → 2015-2019 vb.).
- **Amortisman eğrileri:** Storchmann (2004) geometrik amortismanın iyi bir yaklaşım olduğunu; gelişmiş ülkelerde (~%31) gelişmekte olanlardan (~%15) daha hızlı değer kaybı olduğunu gösterir. Aynı çalışma gelir etkisini de nicelleştirir: *"an income increase by $1000 is likely to increase the annual depreciation rate by 2.7% in OECD countries and 3.6% in non-OECD countries."* Schloter (2022) EV'lerin (%13,9/yıl) benzinlilerden (%10,4/yıl) daha hızlı değer kaybettiğini; değer kaybının araç yaşıyla azalan (degressive) bir ilişki izlediğini web-scrape 9 marka verisiyle bulur.

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Bu dal bize üç güçlü, doğrudan devşirilebilir metodolojik ders verir. (1) **Asimetrik maliyet:** Bizim up/down/stable sınıflamamızda da hata maliyetleri asimetrik olabilir (ör. "up derken down çıkması" ile "stable derken up çıkması" farklı maliyetli); Dress et al.'ın çerçevesi sınıf-ağırlıklı kayıp fonksiyonuna doğrudan çevrilebilir. (2) **Kronolojik train/test bölme:** Rashed et al.'ın disiplini bizim için zorunludur (ama leakage/backtesting ayrı fazın konusu). (3) **Çok-görevli öğrenme:** Yönü ana hedef, fiyat değişim büyüklüğünü yardımcı hedef yapmak makul bir mimari fikirdir. ÇEVRİLEMEYEN kısım: tüm bu literatür hâlâ **tek aracın** gelecekteki fiyatını **nokta olarak** öngörür (regresyon) ve sözleşme-başı araç özniteliklerine dayanır; **piyasa/segment seviyesinde bir yön** öngörmez. Amortisman eğrileri de araç-yaşı ekseninde tanımlıdır (bir aracın ömrü boyunca), takvim-zamanı ekseninde piyasa hareketini değil — bu ikisini karıştırmak kavramsal hatadır.

### 5. Piyasa/Endeks Düzeyinde Zaman Serisi Çalışmaları

**Bu bölüm büyük ölçüde bir boşluk raporudur.** Bağımsız aramalar sonucunda, kümüle bir kullanılmış-araç fiyat ENDEKSİNİ (ör. MUVVI benzeri) ARIMA/VAR/LSTM gibi zaman serisi yöntemleriyle öngören **hakemli hiçbir akademik çalışma bulunamadı** ("literatürde yok").

Kümüle endeksler pratikte yalnızca endüstri tarafından üretilir: Manheim Used Vehicle Value Index (Cox Automotive), karma/kilometre/mevsimsellik-ayarlı toptan fiyat endeksidir ve Cox tarafından öngörülür. Cox Automotive'in 8 Temmuz 2026 tarihli Q2 raporuna göre baş ekonomist Jeremy Robb: *"the company's year-end outlook remains unchanged with expectations the Manheim Used Vehicle Value Index will finish the year approximately 2% higher than year-end 2025 levels, consistent with long-term historical norms."* (Haziran 2026 MUVVI = 212,9, yıllık +%2,1; 2025 kapanışı yıllık +%0,4 ile uzun-dönem ortalaması %2,3'ün altındaydı.) Bu bir *öngörüdür*, gerçekleşme değil. ACT Research (kamyon), S&P Global (liste fiyatı 12 yıl ileri projeksiyon) benzer ticari ürünler sunar. Bunlar hakemli değildir ve metodolojileri şeffaf değildir.

En yakın akademik istisna **Asilkan & Irmak (2009, *SDÜ İİBF Dergisi* 14(2):375-391)**: 2005-2007 aylık ortalama fiyat serisiyle 2008-2009 fiyatlarını YSA ile öngörür ve zaman serisi analiziyle kıyaslar. Ancak bu (a) model-bazında ortalama fiyattır, kümüle endeks değildir; (b) fiyat *seviyesini* öngören regresyondur, yön sınıflaması değildir.

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Bu boşluk bizim için hem risk hem fırsattır. Devşirilebilir hazır şablon YOKTUR. Genel finansal/emtia zaman serisi ve enflasyon-dezagregasyon literatüründen (ör. disaggregate price index forecasting) metodolojik ilham alınabilir, ancak bunlar araç-piyasasına özgü değildir ve finansal ML metodolojisi ayrı fazın konusudur. Somut çıkarım: piyasa-seviyesi yön modeli, araç literatüründen değil, zaman serisi sınıflama literatüründen beslenmek zorundadır — bu, ekibin öncü çalışma yaptığı noktadır.

### 6. İlan Verisiyle Çalışmanın Metodolojik Sorunları

Neredeyse tüm erişilebilir veri (ve muhtemelen bizim verimiz) ilan (listing) verisidir. Temel sorunlar:

- **İlan fiyatı ≠ gerçekleşen fiyat.** İlan fiyatı satıcının *umduğu* fiyattır; gerçekleşen fiyat pazarlık sonrası oluşur. Alman online platform verisiyle yapılan çalışmalar (ör. VW emisyon skandalı sorting çalışması) alıcı-satıcının ilan fiyatından *sapan* bir işlem fiyatında anlaştığını açıkça belgeler. Sektör kaynakları (IBTimes/Cox) "yayınlanmış fiyat piyasa değeri değildir; niyet sinyalidir, talep kanıtı değildir" der.
- **Seçilim yanlılığı (satılmayan ilanlar).** Scrape edilen ilanların bir kısmı hiç satılmaz; yalnızca gözlemlenen ilanlar üzerinden çıkarım, satılan/satılmayan ayrımını ihmal eder. Born, Kovachka, Lessmann & Seow (2018) bu yüzden **survival analysis** (satışa kadar geçen süre) ile fiyat yönetimini modeller.
- **Gürültü ve veri temizliği.** Serbest-metin/validasyonsuz formlar aşırı gürültü üretir (km alanında "çok" gibi metinler, aykırı değerler, boş alanlar). Standart uygulama: 99. persentilde aykırı-değer kırpma, kategorik seviyeleri azaltma (ör. yüzlerce renk adını temel renklere eşleme).
- **Tekrarlı/ölü ilanlar.** Aynı araç birden çok kez veya yeniden listelenebilir; deduplication yapılmazsa popüler/uzun-yayında kalan araçlar aşırı-temsil edilir.
- **Pazarlık marjı ve kanal farkı.** Bayi fiyatı ile bireysel satıcı fiyatı sistematik farklıdır (KBB çoklu tahmin sunar).

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Bu sorunlar bizim problemimizde biçim değiştirir ama kaybolmaz — hatta bazıları hafifler. Yön sınıflaması için mutlak seviye doğruluğu değil, *seviyenin dönemler arası değişimi* önemlidir; ilan fiyatı ile gerçekleşen fiyat arasındaki marj *sabit* kaldığı sürece, ilan-fiyatı-endeksinin YÖNÜ gerçekleşen-fiyat-endeksinin yönünü izleyebilir. KRİTİK RİSK: bu marj zamanla değişirse (ör. talep düşerken pazarlık payı genişler), ilan verisi yön sinyalini saptırır — bu, ekibin özellikle test etmesi gereken bir varsayımdır. Seçilim yanlılığı (satılmayanlar) da yön-bağımlı olabilir: düşen piyasada ilanlar daha uzun kalır, bu da endeks kompozisyonunu kaydırır. Bu köprü kurma işi literatürde hazır DEĞİLDİR.

### 7. Türkiye Piyasası Üzerine Çalışmalar (ÖNCELİKLİ)

Türkiye, yüksek hacimli kullanılmış-araç piyasası ve zengin online ilan verisi (sahibinden.com, arabam.com) nedeniyle görece sağlam bir akademik külliyata sahiptir. Ancak tamamı kesitseldir:

- **Erdem & Şentürk (2009), *International Journal of Economic Perspectives* 3(2):141-149:** 1074 araçlık benzersiz veri; semi-log, log-linear ve Box-Cox dönüşümleriyle hedonik regresyon. Dizel motor, siyah/gri renk, otomatik şanzıman, sunroof, üretim yeri (Japonya/Almanya/Kore/ABD), model yılı ve motor silindiri POZİTİF; resmi servis sayısı ve İstanbul'da satış NEGATİF etkili.
- **Daştan (2016), *Gazi Üniversitesi İİBF Dergisi* 18(1):303-327:** Ekim 2015'te sahibinden+arabam'dan scrape edilen yatay-kesit veri; 323.189 ilandan N=1000 örnek; 118 aday değişken; EViews'te OLS ile linear/semi-log/log-log; en iyi model semi-log (düzeltilmiş R²=0,91). POZİTİF: net ağırlık, benzin yakıt, tork, genişlik, ABS (~+%11), hardtop (~+%58), panoramik cam tavan, ısıtmalı direksiyon, start/stop, geri görüş kamerası, belirli marka dummy'leri (Audi A6 ~+%34). NEGATİF: yaş (~−%5/yıl), manuel vites (~−%12), önden çekiş (~−%22), **kilometre (negatif, %1'de anlamlı)**, gri renk, boyalı/değişen parça sayısı. NOT: Bazı sonraki Türkçe makaleler Daştan'ın km bulgusunu yanlış aktarıyor; birincil kaynak km etkisinin NEGATİF olduğunu doğruluyor.
- **Akay, Bölükbaşı & Bekar (2018), *International Journal of Economics and Financial Issues* 8(1):39-47:** İstanbul, 1032 gözlem; OLS aykırı-değere duyarlı olduğu için robust/resistant yöntemler. Anlamlı: kilometre, yakıt tipi, çekiş tipi, kasa tipi, motor silindir hacmi, şanzıman, hız sabitleyici, sunroof, yol bilgisayarı, yağmur sensörü, değişen parçalar.
- **Ecer (2013), *Anadolu Üniversitesi Sosyal Bilimler Dergisi* 13(4):101-112:** Hedonik model ile YSA'yı kıyaslar; hedonik fonksiyondaki potansiyel doğrusal-olmama nedeniyle YSA'nın daha iyi alternatif olabileceğini bulur.
- **"What is happening to used car prices in Turkey?" (Selçuk Üniv. SBE Dergisi 46/2021):** Mayıs 2020 ve Mart 2021 (iki ayrı kesit) için Renault Megane ve VW Passat'a kesitsel doğrusal regresyon; donanım, yıl, km, şanzıman, yakıt anlamlı. İki tarihi *ayrı ayrı* analiz eder — yani gerçek bir zaman serisi/yön modeli değil, iki bağımsız kesittir.
- **COVID dönemi CART çalışması (KSÜ SBD 2021):** Pandemide fiyatı en çok etkileyen değişken düşük km; ardından yaş, marka, vites, yakıt. Pandemi öncesi/sırası kıyaslar ve karar kriterlerinin değiştiğini bulur.
- Ayrıca çok sayıda lisansüstü tez ve mühendislik makalesi: Ticaret Üniv. tezi (makine öğrenmesiyle ikinci el araç fiyat tahmini), KTÜN tezi (Volkswagen odaklı, web-scrape), Sakarya Üniv. tezi (web kazıma + ML), Konya Journal of Engineering Sciences vaka çalışması (ML vs doğrusal regresyon).

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Türkiye literatürü bize iki değerli şey verir: (1) Türkiye'ye özgü prediktif öznitelik seti ve bunların etki yönü/büyüklüğü (segmentleme ve feature mühendisliği için doğrudan girdi); (2) veri kaynağı doğrulaması (sahibinden/arabam scrape'inin akademik olarak kabul gören standart olması). ÇEVRİLEMEYEN: hiçbir Türkiye çalışması fiyat yönünü zaman içinde sınıflamaz; 2021 Selçuk çalışması "iki kesit" yaklaşımıyla en yakınıdır ama yön modeli değildir. Türkiye piyasasında yön sınıflaması literatürde YOKTUR.

### 8. Endüstri ve Kaggle Kaynakları (güvenilirlik uyarısıyla)

> **GÜVENİLİRLİK UYARISI:** Bu bölümdeki kaynaklar hakemli DEĞİLDİR. Kaggle çözümleri çoğunlukla SENTETİK veri (bir sinir ağının gerçek veriden ürettiği) üzerinde çalışır; endüstri raporları pazarlama amaçlı ve metodolojisi kapalıdır. Bu kaynaklar yalnızca *mühendislik pratiği* ipuçları için, akademik bulgulardan AYRI güvenilirlik düzeyinde değerlendirilmelidir.

- **Kaggle Playground S4E9 "Regression of Used Car Prices" (2024):** Sentetik veri. Kazanan yaklaşımlar: gradient-boosted ağaç ensemble'ları ve dikkat çekici biçimde RAPIDS LASSO. Feature mühendisliği ipuçları: serbest-metin motor/model alanlarını regex ile parse etme, kategorik seviyeleri azaltma (model adını ilk kelimeye indirme, yüzlerce renk adını temel renklere eşleme), hedef değişkende log-dönüşüm (sağa çarpık dağılım için).
- **CatBoost tercihi:** Kategorik değişkenleri ön-işleme olmadan doğal ele aldığı için sık kazanır (GitHub 4. sıra çözümü). Türetilen özellikler: birleşik üretim yılı, 99. persentil kırpma, boolean bayraklar (ör. yetkili serviste bakım).
- **Endüstri artık-değer sistemleri:** statworx (merkezi ML artık-değer aracı, yorumlanabilirlik için ağırlıklı doğrusal modeller), Oliver Wyman (geleneksel RV modellerinin EV/dizel krizi/WLTP karşısında yetersizleştiği tespiti), J.D. Power/ALG (ticari RV öngörü ürünü).
- **Manheim MUVVI / ACT / S&P Global:** piyasa-seviyesi endeks ve öngörü ürünleri (Bölüm 5).

**Regresyondan Sınıflandırmaya Adaptasyon Notu:** Kaggle'ın feature mühendisliği pratikleri (metin parse, kategorik indirgeme, log-dönüşüm, aykırı-değer kırpma) veri hazırlıkta doğrudan uygulanabilir ve düşük riskle taşınır. Ancak sentetik-veri sonuçlarının gerçek piyasaya genellenebilirliği ŞÜPHELİDİR ve model-seçim iddiaları (CatBoost/LASSO kazandı) veri-bağımlıdır — bunlar akademik bulgu gibi sunulamaz. Endüstri RV sistemleri yorumlanabilirlik-doğruluk dengesini hatırlatır. Hiçbiri yön sınıflaması yapmaz.

### 9. LİTERATÜR BOŞLUĞU HARİTASI

#### (A) Literatür Dallarının Problemimize Denk Düşme Tablosu

| Literatür Dalı | Problem Tipi | Zaman Boyutu Var mı? | Analiz Düzeyi | Bizim Probleme Uzaklık | Devşirilebilir Olan |
|---|---|---|---|---|---|
| Kesitsel ML fiyat tahmini | Regresyon | Hayır | Araç | Uzak | Prediktif öznitelik seti; ağaç-ensemble üstünlüğü |
| Hedonik fiyatlama | Regresyon (açıklayıcı) | Hayır (tek kesit) | Araç | Uzak | Nitelik gölge fiyatları; semi-log form; kalite-ayarlı endeks fikri |
| Residual value forecasting | Regresyon (nokta tahmin) | EVET (gelecek-zaman) | Araç | Orta (en yakın olgun dal) | Asimetrik maliyet; kronolojik bölme; çok-görevli öğrenme; satıcı özel-bilgisi |
| Amortisman/değer kaybı eğrileri | Parametrik eğri uydurma | EVET (araç-yaşı ekseni) | Araç/segment | Orta-uzak | Geometrik/üstel form; segment-bağımlı hız; EV vs ICE farkı |
| Piyasa/endeks zaman serisi (akademik) | — | — | — | — | YOK (literatürde bulunamadı) |
| Piyasa endeksi (endüstri: MUVVI vb.) | Öngörü (kapalı metodoloji) | EVET | Piyasa | Yakın (düzey/hedef) ama hakemsiz | Endeks kurgusu (karma/km/mevsim ayarı) fikri |
| İlan verisi metodolojisi | Veri kalitesi/ekonometri | Kısmen | Araç/piyasa | Orta | İlan≠işlem; seçilim yanlılığı; survival analysis; deduplication |
| Türkiye kesitsel çalışmalar | Regresyon | Hayır | Araç | Uzak | TR-özgü öznitelikler; veri kaynağı doğrulaması |
| Sıralı açık artırma fiyat anomalileri | Ekonometri (auction) | Kısmen (satış sırası) | İşlem | Uzak | Fiyat trajektorisi düşer/yükselir tartışması (kavramsal) |

#### (B) Açık Boşluklar — "Literatürde YOK" Olarak İşaretlenenler

Aşağıdaki bileşenler için literatürde **doğrudan hiçbir hakemli kaynak bulunamadı**. Bunlar ekibin öncü çalışma yaptığı noktalardır:

1. **Kümüle kullanılmış-araç fiyat ENDEKSİNİN zaman serisi öngörüsü (akademik).** Hakemli literatürde YOK. Yalnızca endüstri ürünleri (MUVVI) mevcut, metodolojisi kapalı.
2. **Piyasa/segment fiyat YÖNÜNÜN up/down/stable olarak SINIFLANDIRILMASI.** Zaman serisi yönü sınıflaması olarak YOK. En yakın (Bukvić et al. 2022, *Sustainability* 14(24):17034) hâlâ kesitsel araç-bazlı trend sınıflamasıdır, takvim-zamanı piyasa yönü değildir; kendi ifadesiyle *"predict price trends based on available attributes"* — yani araç özniteliklerine dayalı, zaman-eksenli piyasa yönü değil.
3. **Segment-seviyesinde (araç değil) fiyat dinamiği modeli.** Literatür ezici çoğunlukla araç-seviyesindedir; segment-agregasyonu bir yön hedefi olarak modellenmemiştir.
4. **İlan-fiyatı marjının zaman-değişkenliğinin yön sinyaline etkisi.** İlan≠işlem farkı bilinir (statik), ama bu marjın piyasa yönüne göre nasıl değiştiği ve yön tahminini nasıl saptırdığı modellenmemiştir — YOK.
5. **Yön sınıflaması için asimetrik sınıf-maliyeti kurgusu (araç piyasası bağlamında).** Asimetrik maliyet regresyonda vardır (Dress et al. 2018) ama up/down/stable sınıflama maliyet matrisi araç bağlamında YOK.

### 10. Açık Sorular / Literatürde Net Olmayanlar

- **İlan-endeksi yönü ile gerçekleşen-fiyat yönü ne kadar örtüşür?** Literatürde net değil — ilan≠işlem farkı statik olarak bilinir ama yön-örtüşmesi ölçülmemiştir.
- **Hangi agregasyon düzeyi (marka/segment/piyasa) yön açısından en öngörülebilir?** Literatürde net değil; kesitsel çalışmalar bunu test etmez.
- **Amortisman eğrisi (araç-yaşı) ile piyasa takvim-zamanı hareketi ne ölçüde ayrıştırılabilir?** Literatürde net değil; çoğu çalışma ikisini ayırmaz.
- **Segment heterojenliği (Lessmann & Voß'ın bulduğu) yön tahmininde de geçerli mi?** Literatürde net değil (regresyon bağlamında var, sınıflama bağlamında test edilmemiş).

## Recommendations

**Aşama 1 — Devşirilebilir çekirdeği hemen kullan (düşük risk):**
- Prediktif öznitelik setini (yaş, km, marka/model, motor, yakıt, şanzıman, donanım) ve Türkiye-özgü etki yönlerini (Daştan 2016, Erdem & Şentürk 2009, Akay et al. 2018) segment tanımı ve feature mühendisliğinin temeli olarak al.
- Kaggle veri-temizlik pratiklerini (metin parse, kategorik indirgeme, 99p aykırı-değer kırpma, deduplication) veri hattına uygula.
- Residual value literatürünün asimetrik-maliyet çerçevesini (Dress et al. 2018) sınıf-ağırlıklı kayıp fonksiyonuna çevirerek başlangıç kaybı olarak benimse.

**Aşama 2 — Köprü kur (orta risk, öncü iş):**
- Ardışık kesitlerde hedonik katsayı farklarını veya segment-medyan fiyatını türeterek "segment × zaman" yön hedefi inşa et (literatürde hazır değil).
- İlan-fiyatı marjının zaman-değişkenliğini açıkça test et: ilan-endeksi yönü ile (varsa) gerçekleşen-fiyat proxy'si yönü arasındaki korelasyonun piyasa rejimine göre değişip değişmediğini ölç. Bu, projenin en kritik geçerlilik varsayımıdır.

**Aşama 3 — Boşluğu novelty olarak konumla:**
- Bölüm 9(B)'deki beş boşluğu proje dokümantasyonunda açıkça "hazır reçete yok" olarak belgele; bu hem risk yönetimi hem de yayın/katkı fırsatıdır.

**Eşik/tetikleyiciler:** İlan marjı testinde ilan-yönü ile proxy-gerçekleşen-yönü korelasyonu düşük/rejim-bağımlı çıkarsa (ör. düşen piyasada ayrışıyorsa), yalnızca ilan verisine dayanmak yerine işlem-proxy'si (satışa kadar süre, ilan yaşı, conversion) sinyalleri eklemek zorunlu hale gelir.

## Caveats

- Raporlanan R²/RMSE değerleri veri-setine bağlıdır ve çalışmalar arası kıyaslanamaz; sıralama tablosu olarak okunmamalıdır (bilinçli olarak kaçınıldı).
- "Literatürde YOK" işaretlemeleri, erişilebilir kamuya açık kaynaklar (Google Scholar/arXiv/DergiPark/ResearchGate/MDPI yüzey sonuçları) temellidir; kapalı-erişim veya endeks-dışı çalışmalar gözden kaçmış olabilir. Yine de üç bağımsız arama hattı aynı boşluğu doğrulamıştır.
- Bazı endüstri sayıları (MUVVI 2026 yıl sonu ~%2 artış beklentisi) *tahmindir*, gerçekleşme değil; bu ayrım korunmuştur.
- Bazı Türkçe ikincil kaynaklar Daştan (2016)'in km bulgusunu yanlış aktarır; birincil kaynak km etkisinin negatif olduğunu doğrular.
- Makro dinamikler (kur/ÖTV), label tasarımı, finansal ML metodolojisi ve model mimarisi karşılaştırması bilinçli olarak kapsam dışı bırakılmıştır (ayrı fazlar).

## Kaynakça

- **Rosen, S. (1974).** "Hedonic Prices and Implicit Markets," *Journal of Political Economy* 82(1):34-55. — Hedonik fiyatlamanın kurucu teorik çerçevesi; nitelik-gölge fiyatı ayrıştırmasının temeli.
- **Storchmann, K. (2004).** "On the Depreciation of Automobiles: An International Comparison," *Transportation* 31(4):371-408. — Geometrik amortisman ve ülke-bazlı değer kaybı oranları (OECD %31, OECD-dışı %15); zaman-boyutlu değer kaybı referansı.
- **Lessmann, S. & Voß, S. (2017).** "Car resale price forecasting: The impact of regression method, private information, and heterogeneity on forecast accuracy," *International Journal of Forecasting* 33(4):864-877. — RF üstünlüğü, heterojenlik ve satıcı özel-bilgisi; residual value dalının anahtar çalışması.
- **Dress, K., Lessmann, S. & von Mettenheim, H.-J. (2018).** "Residual Value Forecasting Using Asymmetric Cost Functions," *Int. J. Forecasting* (arXiv:1707.02736). — Asimetrik hata maliyeti; sınıf-maliyeti kurgumuza doğrudan devşirilebilir.
- **Rashed, A., Jawed, S., Rehberg, J., Grabocka, J., Schmidt-Thieme, L. & Hintsches, A. (2019).** "A Deep Multi-Task Approach for Residual Value Forecasting," ECML-PKDD (VW Financial Services). — Çok-görevli öğrenme, yardımcı hedefler, kronolojik bölme.
- **Schloter, L. (2022).** "Empirical analysis of the depreciation of electric vehicles compared to gasoline vehicles," *Transport Policy* 126:268-279. — EV (%13,9/yıl) vs ICE (%10,4/yıl) amortisman farkı; segment-bağımlı değer kaybı.
- **Prieto, M., Caracciolo, B. & Baltas, G. (2015).** "Using a hedonic price model to test prospect theory assertions," *Journal of Retailing and Consumer Services*. — Güvenilirliğin fiyat üzerindeki asimetrik/doğrusal-olmayan etkisi.
- **Erdem, C. & Şentürk, İ. (2009).** "A Hedonic Analysis of Used Car Prices in Turkey," *International Journal of Economic Perspectives* 3(2):141-149. — Türkiye kesitsel hedonik referansı; 1074 araç.
- **Daştan, H. (2016).** "Türkiye'de İkinci El Otomobil Fiyatlarını Etkileyen Faktörlerin Hedonik Fiyat Modeli ile Belirlenmesi," *Gazi Üniv. İİBF Dergisi* 18(1):303-327. — N=1000, semi-log (R²=0,91); TR-özgü öznitelik yönleri.
- **Akay, E.Ç., Bölükbaşı, Ö.F. & Bekar, E. (2018).** "Robust and Resistant Estimations of Hedonic Prices for Second Hand Cars: an Application to the Istanbul Car Market," *IJEFI* 8(1):39-47. — Robust hedonik; aykırı-değer duyarlılığı.
- **Ecer, F. (2013).** "Forecasting of Second-Hand Automobile Prices and Identification of Price Determinants in Turkey," *Anadolu Üniv. Sosyal Bilimler Dergisi* 13(4):101-112. — Hedonik vs YSA.
- **Asilkan, Ö. & Irmak, S. (2009).** "İkinci El Otomobillerin Gelecekteki Fiyatlarının Yapay Sinir Ağları İle Tahmin Edilmesi," *SDÜ İİBF Dergisi* 14(2):375-391. — Nadir zaman-serisi + YSA fiyat öngörüsü (endeks değil).
- **Born, A., Kovachka, N., Lessmann, S. & Seow, H.-V. (2018).** "Price Management in the Used-Car Market: An Evaluation of Survival Analysis," IRTG 1792 DP 2018-065. — Satılmayan ilan/seçilim; survival analysis.
- **Raviv, Y. (2006).** "New Evidence on Price Anomalies in Sequential Auctions: Used Cars in New Jersey," *Journal of Business & Economic Statistics* 24(3):301-312. — Açık artırmada fiyat trajektorisi (kavramsal ilgi).
- **Bukvić, L., Pašagić Škrinjar, J., Fratrović, T. & Abramović, B. (2022).** "Price Prediction and Classification of Used-Vehicles Using Supervised Machine Learning," *Sustainability* 14(24):17034. — Yön sınıflamasına en yakın çalışma (yine de kesitsel).
- **Cox Automotive / Manheim.** Manheim Used Vehicle Value Index raporları (coxautoinc.com). — Piyasa-seviyesi endeks; endüstri, hakemsiz.
- **Oliver Wyman (2019).** "A Better Approach To Residual Value." — Geleneksel RV modellerinin sınırları; endüstri.
- **statworx.** "Forecast of Residual Value for Leased Vehicles" (case study). — Endüstri ML RV uygulaması.
- **Kaggle Playground S4E9 (2024)** ve ilgili notebook/GitHub çözümleri. — Feature mühendisliği pratikleri; sentetik veri, hakemsiz.

## Kullanılan Nihai Arama Sorguları

İngilizce: "used car price prediction machine learning features"; "hedonic price model used vehicles automobile"; "residual value forecasting vehicles leasing"; "used car price index forecasting time series Manheim"; "vehicle depreciation curve model empirical"; "listing price versus transaction price used cars selection bias unsold"; "Schloter depreciation electric vehicles gasoline Transport Policy"; "Storchmann depreciation automobiles international comparison findings"; "Kaggle playground used car price prediction winning solution feature engineering"; "used car price index forecasting neural network wholesale auction time series"; "Lessmann Voß car resale price 19 models random forest comparison"; "forecasting used vehicle price index macroeconomic aggregate market level model"; "Voß Lessmann resale price used car market private information heterogeneity forecast"; "Raviv price anomalies sequential auctions used cars declining price"; "price direction classification up down forecasting real estate index machine learning".

Türkçe: "ikinci el araç fiyat tahmini makine öğrenmesi"; "ikinci el araç fiyat endeksi zaman serisi tahmin Türkiye"; "Erdem Şentürk hedonic used car prices Turkey"; "Ecer forecasting second-hand automobile prices Turkey determinants Anadolu".

Alt-ajan (bağımsız) sorguları: "used car price index time series forecasting ARIMA LSTM"; "forecasting used vehicle price index Manheim ARIMA VAR aggregate market"; Daştan (2016) tam-metin doğrulaması (DergiPark); "used car resale value direction up down classification".