---
faz_no: 08
faz_adi: "Başarısızlık Modları, Tuzaklar ve Kırmızı Takım"
tarih: 2026-07-13
kapsam_ozeti: "Baseline'ın başarısızlık modlarının mekanizma + erken-uyarı + azaltıcı önlem olarak haritalanması"
bagimli_oldugu_fazlar: [01, 02, 03, 04, 05, 06, 07]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 30
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-13
---

# FAZ 8 — Başarısızlık Modları, Tuzaklar ve Kırmızı Takım Raporu

## TL;DR

- **Projenin en kırılgan varsayımı (K8+N9) literatürce doğrudan çürütülebilir durumdadır:** İlan-fiyatı ile gerçekleşen-fiyat arasındaki pazarlık marjı sabit değildir. Anenberg & Laufer (2017, *Review of Economics and Statistics* 99(4):722-734) verbatim olarak şunu bulmuştur: "The sale-to-list price ratio fluctuates within a band of several percentage points, and the variation appears to be correlated with the house price cycle, in violation of the assumptions of our simple list-price index. Periods of rising prices tend to have high sale-to-list price ratios." Yani ilan-tabanlı yön sinyali tam da döngü dönüm noktalarında (yükselişte gücü abartma, düşüşte zayıflığı hafife alma) sapar — bu bir "olabilir" değil, benzer piyasalarda ölçülmüş bir olgudur.
- **En yüksek olasılık × en yüksek etki taşıyan üç günlük tuzak:** (1) gizli veri sızıntısı (leakage) nedeniyle iyimser değerlendirme; (2) naif baseline'ı (persistence/random walk) yenememe durumunun raporda gizlenmesi; (3) "stable" bandının keyfî seçimiyle etiket dengesizliği/anlamsızlaşması. Üçü de önceden tespit edilebilir ve azaltıcı önlemleri mevcuttur.
- **Bu proje için "sinyal yok" (N6) meşru ve olası bir sonuçtur.** Rapor, projenin ne zaman TERK/yeniden-çerçeveleneceğine dair somut, önceden-ilan-edilen (pre-registered) eşikler önermektedir; bu eşikler karşılanmazsa devam etmek kaynak israfı ve yanlış-pozitif üretme riskidir.

## Key Findings

1. **K8+N9 kritik varsayımı ampirik olarak test edilmemiştir ve literatür onun aleyhinedir.** Anenberg & Laufer (2017), sale-to-list oranı varyasyonunun "basit ilan-fiyatı endeksinin varsayımlarını ihlal ederek" konut fiyat döngüsüyle korelasyonlu olduğunu belirtir. Bu, projenin baseline'ının döngü dönümlerinde sistematik olarak yanılacağı anlamına gelir.
2. **Dolaylı test mümkündür.** Doğrudan işlem verisi olmadan; days-on-market (DOM), fiyat-düşürme oranı ve satış-dönüşüm oranı proxy'leri sapmanın erken-uyarı sinyalleridir. Trojanek, Hartigan, Pfeifer & Steurer (2025, CAMA WP 2025-45 / Graz Economics Papers 2025-13) verbatim bulguları: "list-price indices consistently lead transaction-price indices by one to two months, with the strongest relationship in Warsaw's larger, more liquid market."
3. **Türkiye-özgü rejim riski yüksek ve günceldir.** 24 Temmuz 2025 tarihli Resmî Gazete düzenlemesi (7555 sayılı kanun değişikliği + 10115 sayılı Cumhurbaşkanı Kararı, 25 Temmuz 2025 yürürlük) binek otomobilde en düşük ÖTV oranını %80'e, en yüksek dilimi %220'ye, elektriklide taban oranı %10'dan %25'e çıkardı. Bu, arz/talep değişkenini rejime bağlı çift yönlü kılar (N2); sabit-katsayı baseline'ı dönem geçişinde çöker.
4. **Değerlendirme kaynaklı başarısızlıklar en sinsi olanlardır.** Kapoor & Narayanan (2023, *Patterns* 4(9):100804): leakage "17 fields where leakage has been found, collectively affecting 294 papers"; iç savaş tahmini örneğinde "When the errors are corrected, complex ML models do not perform substantively better than decades-old LR [logistic regression] models." Bu, projenin baseline'ının naif modeli yenmesinin bir artefakt olabileceğine dair en güçlü uyarıdır.
5. **Sessiz bozulma (silent drift) izlenmezse fark edilmez.** Saf konsept kayması hiçbir denetimsiz proxy ile yakalanamaz; bu yüzden etiketli periyodik denetim ve champion/challenger mimarisi şarttır.

## Details

### 1. Giriş: Kırmızı Takım Çerçevesi ve Risk Derecelendirme Yöntemi

Bu faz yapıcı kötümserlik ilkesiyle çalışır: amaç projeyi durdurmak değil, baseline'ın **nerede ve neden** başarısız olacağını önceden avlamak ve her risk için azaltıcı önlem tanımlamaktır. Yeni metodoloji önermek bu fazın kapsamı dışındadır (o, Faz 02-05'in işiydi); bu faz yalnızca risk haritalar ve ilgili fazlara eleştirel geri-referans verir.

**Risk derecelendirme yöntemi (olasılık × etki):** Her başarısızlık modu iki eksende derecelendirilir:
- **Olasılık:** Düşük (özel koşullar gerektirir) / Orta (belirli rejimlerde beklenir) / Yüksek (varsayılan olarak, önlem alınmazsa gerçekleşir).
- **Etki:** Düşük (metrikte küçük sapma) / Orta (yanlış model seçimi) / Yüksek (baseline'ın tüm sonuçlarını geçersiz kılar veya yanlış iş kararına yol açar).

Kritik ayrım: **düşük-olasılıklı felaket senaryoları** (ör. tam kur çöküşü, piyasa donması) ile **yüksek-olasılıklı günlük tuzaklar** (ör. leakage, naif baseline'ı yenememe) açıkça ayrılır. Enerji ve dikkat öncelikle yüksek×yüksek hücrelere yönlendirilmelidir.

### 2. Veri/Hedef Kaynaklı Başarısızlıklar (K8 kritik varsayımı derinlemesine)

#### 2.1 K8+N9: İlan-yönü ≠ İşlem-yönü sapması (PROJENİN EN KIRILGAN VARSAYIMI)

**Mekanizma.** Baseline, ilan-fiyatı yönünün gerçekleşen-fiyat yönüyle örtüştüğünü varsayar. Ancak pazarlık marjı (ilan − gerçekleşen) piyasa rejimine göre değişir. Konut arama-eşleşme literatürü bunu doğrudan ve nicel olarak belgeler:
- **Anenberg & Laufer (2017, *Review of Economics and Statistics* 99(4)):** verbatim, "The sale-to-list price ratio fluctuates within a band of several percentage points, and the variation appears to be correlated with the house price cycle... Periods of rising prices tend to have high sale-to-list price ratios." Yani yükselişte marj daralır (fiyat ilana yakın/üstünde), düşüşte marj genişler (alıcı pazarlık gücü artar).
- **Anenberg (2016, *International Economic Review* 57(4)) "crossing pattern":** Satıcılar ilan fiyatını **bayat (yüksek) emsallere** çıpalar; işlem fiyatı düşmeye devam ederken ilan fiyatı yapışkan kalır — böylece düşüş piyasasında marj mekanik olarak genişler. Değer kaybı oranındaki %1 artış ilan fiyatını yaklaşık %0.57 artırır.
- **Han & Strange (2016, *Journal of Urban Economics* 93):** "Bir boom'da liste-altı satışlar daha az, ilan fiyatına eşit ve üstü işlemler daha çoktur." Bust'ta tersi.
- **Carrillo, de Wit & Larson (2015, *Real Estate Economics* 43(3)):** Satıcı pazarlık gücü döngüyle hareket eder (Fairfax'te 2000'de hızlanma, 2005 zirve, kriz sonrası çöküş); bu "tightness/heat index" değişkeni gelecekteki fiyat artışını haber verir ve dışlandığında RMSE %30'a kadar (bazı ufuklarda ~%35) kötüleşir.

**Türkiye bağlamına uygulanması:** Düşen/durgun bir TL piyasasında ilan fiyatları yapışkan kalıp gerçekleşen fiyatlar daha hızlı düşerse, ilan-tabanlı sinyal "stable/up" derken piyasa gerçekte "down" olur. 24 Temmuz 2025 ÖTV düzenlemesi sonrası talep ertelemesi dönemlerinde (satıcıların beklemeye geçtiği) bu sapma özellikle büyür.

**Erken-uyarı işareti.** (a) DOM'un (ilanın piyasada kalma süresi) sistematik uzaması; (b) fiyat-düşürme (price-reduction) oranının artması; (c) satış-dönüşüm (conversion) oranının düşmesi. Trojanek vd. (2025) bu proxy'lerin işlem endeksini "one to two months" öncesinden haber verdiğini gösterir; ayrıca "The predictive advantage is greatest when incorporating list-price data from the first or second month of the quarter, as third-month data introduce forward-looking noise" — yani proxy'lerin zamanlaması dikkatli seçilmelidir.

**Azaltıcı önlem (SOMUT İZLEME/TEST TASARIMI — A maddesi):**
1. **Proxy-tabanlı dolaylı validasyon paneli:** DOM medyanı, aktif ilanlarda fiyat-düşüş yapan ilanların oranı ve (varsa) delisting/satış-dönüşüm oranını aylık izle. Bu üç seri, ilan-fiyatı yön sinyaliyle **aynı yönde hareket etmiyorsa** (ör. ilan "up" derken DOM uzuyor + düşüşler artıyorsa) sapma alarmı ver.
2. **Rejim-koşullu tutarlılık testi:** Örneklemi yükselen/düşen alt-dönemlere böl; ilan-yön sinyalinin bir sonraki dönem proxy'lerini öngörme gücünün rejimler arası **kararlı** olup olmadığını test et. Kararsızsa, K8 çökmüştür.
3. **Vekil hedef triangülasyonu:** Kamuya açık işlem-tabanlı seriler (TÜİK ikinci el fiyat serileri, sahibindex/BETAM görünümleri) ile ilan-tabanlı serinin yönsel uyumunu (directional agreement / confusion matrix) periyodik ölç. Uyum belirli bir eşiğin altına düşerse sinyal geçersiz sayılır. Not: Anenberg & Laufer (2017) seçilim uyarısı da geçerlidir — "delistings that result in closings are a selected group of delistings that tend to have lower list prices" — yani satılanların örneklemi rasgele değildir.
4. Kalıcı çözüm için Heckman-tipi seçim düzeltmesi veya sale-to-list oranını ayrı durum değişkeni olarak modele katma **Faz 04'ün işiydi**; bu faz yalnızca test/izleme tasarımını dayatır.

**Literatür dayanağı:** Güçlü (Anenberg & Laufer 2017; Anenberg 2016; Han & Strange 2016; Carrillo vd. 2015; Trojanek vd. 2025).
**Olasılık: Yüksek | Etki: Yüksek.**

#### 2.2 Kompozisyon (mix) kayması (N1)

**Mekanizma.** Satılan/ilan edilen araçların bileşimi dönemden döneme değişir; pahalı segment ağırlığı artarsa ortalama/medyan ilan fiyatı, tek bir araç bile değer değiştirmese de yükselir. Emlak fiyat endeksi literatürü bunu klasik bir yanlılık kaynağı olarak belgeler (IMF *RPPI Handbook*, Bölüm 4; Case & Shiller 1987): "cari dönemde orantısız sayıda yüksek fiyatlı ev satıldıysa, tek bir ev bile değer kazanmasa da ortalama/medyan fiyat yükselir."

**Erken-uyarı işareti.** Segment/marka/yaş/km dağılımında dönemsel PSI kayması; düzeltilmiş ve ham fiyat serilerinin ayrışması.

**Azaltıcı önlem.** Stratifikasyon/mix-adjustment veya hedonik kalite düzeltmesi (Faz 02/04'ün işiydi); bu fazda önlem = kompozisyon PSI'sini feature'lardan bağımsız izlemek ve düzeltilmemiş seride yön sinyali üretmeyi yasaklamak.
**Literatür dayanağı:** Güçlü (IMF RPPI Handbook, Bölüm 4). **Olasılık: Yüksek | Etki: Orta-Yüksek.**

#### 2.3 Seçilim yanlılığı: satılmayan ilanların model dışı kalması

**Mekanizma.** Yalnızca satılan/kapanan ilanlar gözlemlenirse, örneklem satıcı davranışı ve fiyat açısından temsili olmaz. Sanat müzayedesi verisiyle Heckman-tipi çalışmalar (art-auction selection modelleri, *PMC*) yalnızca satılanların yayımlanmasının forecast hatasını **hafife aldırdığını** gösterir: "Relying on the published data leads to underestimating the forecast error of the pre-sale estimates." Anenberg & Laufer (2017) de kapanan ilanların düşük ilan fiyatlı seçili bir grup olduğunu belgeler.

**Erken-uyarı işareti.** Satılan-vs-satılmayan ilanların özellik dağılımlarının ayrışması; conversion oranının segment bazında büyük farklılık göstermesi.

**Azaltıcı önlem.** Heckman iki-aşamalı düzeltme / inverse Mills ratio veya survival/censoring çerçevesi (tasarım Faz 04'ün işiydi); bu fazda önlem = satılmayan ilanları da veri hattında tutmak ve "yalnızca-satılan" örneklem üzerinde yön etiketi üretmeyi bir leakage/selection riski olarak işaretlemek.
**Literatür dayanağı:** Güçlü (Heckman 1979; art-auction selection literatürü). **Olasılık: Orta-Yüksek | Etki: Yüksek.**

#### 2.4 Ölü/tekrarlı ilanlar

**Mekanizma.** Aynı aracın birden çok kez/tekrar listelenmesi (relisting) veya hiç güncellenmeyen ölü ilanlar, hem hedef değişkeni hem de DOM proxy'sini kirletir; ayrıca train/test'e aynı aracın sızması bir duplicate-leakage türüdür (Kapoor & Narayanan taksonomisinde L1.4).

**Erken-uyarı işareti.** Aynı VIN/ilan-kimliği veya birebir aynı feature vektörünün birden çok kayıtta görünmesi; anormal derecede pürüzsüz öğrenme eğrileri.

**Azaltıcı önlem.** İlan-kimliği bazında dedup; cumulative-DOM hesabı; split'lerin araç-kimliği (grup) bazında yapılması (temizlik Faz 01/03'ün işiydi, ama grup-bazlı split zorunluluğu burada bir değerlendirme kuralı olarak dayatılır).
**Literatür dayanağı:** Güçlü (Kapoor & Narayanan 2023). **Olasılık: Orta | Etki: Orta.**

#### 2.5 Fiyat-düşürme davranışının hedef değişkeni kirletmesi

**Mekanizma.** Satıcının kendi ilan fiyatını indirmesi, piyasa yönünden bağımsız bir mikro-davranıştır (Merlo & Ortalo-Magné 2004: fiyat düşüşleri DOM arttıkça olasıdır, "piyasa koşulları değişmese bile"). Bu indirimler aylık yön etiketine gürültü veya sahte "down" sinyali enjekte eder.

**Erken-uyarı işareti.** Yön etiketlerinin bireysel ilan fiyat-düşüşleriyle yüksek korelasyonu; etiketin piyasa-geneli hareketten çok ilan-içi düzeltmeleri yansıtması.

**Azaltıcı önlem.** Yön etiketini bireysel ilan bazında değil, kompozisyon-düzeltilmiş piyasa-geneli agregada tanımlamak; ilan-içi fiyat revizyonlarını ayrı feature/kontrol olarak ele almak (etiket tanımı Faz 02'nin işiydi).
**Literatür dayanağı:** Orta (Merlo & Ortalo-Magné 2004). **Olasılık: Orta | Etki: Orta.**

### 3. Etiketleme Kaynaklı Başarısızlıklar

#### 3.1 Threshold/ufuk seçiminin dengesizlik veya gürültü üretmesi

**Mekanizma.** Aylık yön (up/down/stable) eşiği ve tahmin ufku keyfî seçilirse, sınıf dağılımı ciddi dengesizleşir veya etiketler ölçüm gürültüsünü yansıtır. Küçük eşik → gürültüyü sinyal sayma; büyük ufuk → gözlem sayısında düşüş.

**Erken-uyarı işareti.** Sınıf oranlarının aşırı çarpık olması; eşik/ufka küçük değişikliklerde etiketlerin büyük oranda değişmesi (etiket kararsızlığı).

**Azaltıcı önlem.** Eşik ve ufku önceden-ilan et (pre-register); duyarlılık analizi olarak birkaç makul eşikte sonuç kararlılığını raporla; enflasyon/kur nedeniyle nominal serilerde eşiği reel/deflate edilmiş bazda tanımla (tasarım Faz 02'nin işiydi).
**Literatür dayanağı:** Kısmi ("literatürde net değil" — ilan-tabanlı düşük-frekanslı yön etiketlemesi için doğrudan literatür yoktur, N3). **Olasılık: Yüksek | Etki: Orta-Yüksek.**

#### 3.2 "Stable" bandının anlamsızlaşması

**Mekanizma.** "Stable" bandı çok genişse çoğu ay "stable" olur → model çoğunluk sınıfını tahmin ederek yüksek doğruluk gösterir ama bilgisizdir; çok darsa "stable" pratikte yok olur → problem ikili yön tahminine döner ve gürültü artar.

**Erken-uyarı işareti.** "Stable" sınıfının frekansının %70+ veya %5- olması; naif "hep stable" tahmincisinin modeli yenmesi.

**Azaltıcı önlem.** Band genişliğini serinin tarihsel volatilitesine (ör. ±0.5σ) bağlamak, keyfî sabit yüzde yerine; her band seçiminde naif-çoğunluk baseline'ını raporlamak.
**Literatür dayanağı:** "Literatürde net değil" (proje-özgü). **Olasılık: Orta-Yüksek | Etki: Orta.**

### 4. Rejim/Non-Stationarity Kaynaklı Başarısızlıklar

#### 4.1 Kur/ÖTV/arz şoklarında model çöküşü (N2)

**Mekanizma.** Ekonometrik forecast-failure literatürü (Hendry; Economics Observatory) sistematik forecast başarısızlığının başlıca kaynağının "equilibrium mean/trend" kaymaları — yani location shift'ler — olduğunu gösterir: "modeller kayma-öncesi ortalamayı/trendi tahmin etmeye devam eder ve sistematik olarak yanılır." Türkiye'de bu şoklar somut ve günceldir: 24 Temmuz 2025 Resmî Gazete düzenlemesi (7555 sayılı değişiklik + 10115 sayılı Cumhurbaşkanı Kararı) ile binek otomobilde en düşük ÖTV %80'e, en yüksek dilim %220'ye, elektriklide taban %10'dan %25'e çıktı; örneğin Togg T10X standart menzil 1.505.000 TL'den ~1.710.226 TL'ye yükselirken, bazı yüksek matrahlı modeller (ör. Tesla Model Y Long Range) düzenlemeden farklı yönde etkilendi. Bu segment-bazlı çift-yönlü etki, arz değişkeninin rejime bağlılığını (N2: kıtlık→prim yukarı; kampanya→aşağı) doğrudan örnekler; sabit katsayı geçişte çöker.

**Erken-uyarı işareti.** Politika/kur şoku takvimiyle çakışan ani hata artışı; katsayı kararsızlığı; şok dönemlerinde tüm modellerin (benchmark dahil) bozulması.

**Azaltıcı önlem.** Bilinen şok tarihlerinde (ÖTV düzenlemesi, büyük kur hareketi) intercept-correction / rejim kukla değişkeni ile "location shift" düzeltmesi; şok sonrası hızlı yeniden-eğitim; şok dönemlerini ayrı değerlendirme dilimi olarak raporlama (rejim modellemesi Faz 05'in işiydi; burada önlem = şok takvimi izleme ve şok-dönemi ayrı raporlama).
**Literatür dayanağı:** Güçlü (Hendry forecast-failure literatürü; Türkiye ÖTV/kur kaynakları). **Olasılık: Yüksek | Etki: Yüksek.**

#### 4.2 Eğitim döneminin gelecekteki rejimi temsil etmemesi

**Mekanizma.** "Who Saw It Coming?" (2026, arXiv) çalışması 2021 enflasyon sürprizini analiz ederek forecast hatalarının "fonksiyonel form yanlış-belirlemesinden çok örneklem kompozisyonundan" kaynaklandığını gösterir: nadir ama ekonomik açıdan önemli rejimleri az-ağırlıklayan örneklemler normal-rejim parametrelerine yakınsar. İkinci el araç serisi kısaysa ve tek bir rejimi kapsıyorsa, model gelecekteki farklı rejimde kör olur.

**Erken-uyarı işareti.** Eğitim penceresinin tek bir makro rejimi kapsaması; out-of-sample dönemin makro göstergelerinin eğitim aralığı dışına çıkması.

**Azaltıcı önlem.** Mümkün olan en uzun tarihsel pencereyi kullanmak; farklı rejimleri (yükseliş/düşüş/durgun) kapsayan dönemlerde ayrı ayrı değerlendirmek; rejim kapsamını açıkça raporlamak (veri toplama Faz 01'in işiydi).
**Literatür dayanağı:** Güçlü ("Who Saw It Coming?" 2026). **Olasılık: Yüksek | Etki: Yüksek.**

#### 4.3 "Sessiz" (yavaş, fark edilmeyen) dağılım kayması

**Mekanizma.** Model hata fırlatmadan yavaşça bozulur ("silent decay"). Kritik bulgu: **saf konsept kayması** (P(Y|X) değişirken P(X) korunuyorsa) hiçbir denetimsiz proxy ile yakalanamaz (Label-Free Detection... 2026, arXiv): "saf konsept kayması tüm pencerelerde tam olarak sıfır delta üretir."

**Erken-uyarı işareti.** Feature PSI artışı (>0.10 incele, >0.25 yeniden-eğit); ama performans düşüşü PSI olmadan da olabilir — bu yüzden etiketli denetim şart.

**Azaltıcı önlem.** Katmanlı izleme (veri kalitesi → drift sinyalleri → performans sinyalleri); periyodik **etiketli** denetim ve champion/challenger mimarisi (saf konsept kaymasının tek yakalanma yolu); PSI eşikli otomatik alarm.
**Literatür dayanağı:** Güçlü (drift-monitoring literatürü; Label-Free Detection 2026). **Olasılık: Orta-Yüksek | Etki: Yüksek.**

### 5. Model Kaynaklı Başarısızlıklar

#### 5.1 Aşırı uyum/overfitting (az-gözlemde ciddi risk)

**Mekanizma.** Aylık düşük-frekanslı seri → az gözlem. Yüksek-boyut/küçük-örneklem rejiminde overfitting başlıca tehlikedir; Simon vd.'nin gösterdiği gibi (NCBI Bookshelf), hiç sinyal olmayan veride bile yanlış feature-seçim prosedürleri sahte genelleme performansı üretebilir.

**Erken-uyarı işareti.** Train-validation aralığının >5% açılması; öğrenme eğrilerinde validation hatasının yükselmesi; model karmaşıklığının gözlem sayısına oranla yüksekliği.

**Azaltıcı önlem.** Basit/düzenlileştirilmiş modeller tercih etmek; nested/time-series cross-validation; feature seçimini CV döngüsü içinde yapmak; parsimony (model seçimi Faz 05'in işiydi; burada önlem = az-gözlem uyarısı ve karmaşıklık tavanı dayatmak).
**Literatür dayanağı:** Güçlü (NCBI overfitting bölümü; Simon vd.). **Olasılık: Yüksek | Etki: Yüksek.**

#### 5.2 Yanlış kalibrasyon

**Mekanizma.** Sınıflandırıcı olasılıkları gerçek frekansları yansıtmazsa, karar eşikleri (up/down/stable) optimal olmaz. Sınıf oranı eğitim ile dağıtım arasında değişirse (label drift), sabit-eşikli karar kuralı yanlış olur (Flach kalibrasyon survey'i, 2023).

**Erken-uyarı işareti.** Reliability diagram sapması; yüksek ECE; sınıf-önselleri kaydıkça bozulan kararlar.

**Azaltıcı önlem.** Ayrı validasyon setinde kalibrasyon (Platt/isotonic); sınıf-önseli değiştikçe eşiği r/(r+r') kuralıyla ayarlamak; karar-teorik kalibrasyon hatası (CDL) izlemek (kalibrasyon tasarımı Faz 05'in işiydi).
**Literatür dayanağı:** Güçlü (Flach kalibrasyon survey'i; Calibration Error for Decision Making 2024). **Olasılık: Orta | Etki: Orta-Yüksek.**

#### 5.3 Ordinal yapının ihmal edilmesi

**Mekanizma.** up/down/stable doğal olarak sıralıdır (down < stable < up). Standart nominal sınıflandırma MAP kriteri sırayı yok sayar; "low"u "high" tahmin etmek "medium" tahmin etmekten daha ağır bir hatadır ama nominal kayıp bunu ayırt etmez (Ord-MAP 2025; cost-sensitive ordinal literatürü).

**Erken-uyarı işareti.** Karışıklık matrisinde down↔up (komşu-olmayan) hatalarının yüksekliği; nominal accuracy yüksek ama MAE/QWK kötü.

**Azaltıcı önlem.** Ordinal-farkındalıklı kayıp/karar kuralı (Ord-MAP, cumulative-probability); değerlendirmede MAE/quadratic-weighted-kappa gibi sıra-duyarlı metrikler (ordinal model seçimi Faz 05'in işiydi; burada önlem = sıra-duyarlı metrik raporlama zorunluluğu).
**Literatür dayanağı:** Güçlü (Ord-MAP 2025; cost-sensitive ordinal). **Olasılık: Orta | Etki: Orta.**

#### 5.4 Ensemble'ın yanlış/aşırı güven vermesi

**Mekanizma.** Ensemble'lar (özellikle boosted ağaçlar) yüksek doğrulukla birlikte kötü kalibre olabilir (Niculescu-Mizil & Caruana 2005); aşırı-güvenli olasılıklar karar-vericiyi yanıltır.

**Erken-uyarı işareti.** Aşırı yüksek güven skorlarının yanlış tahminlere eşlik etmesi; ensemble güveninin gerçek doğrulukla uyuşmaması.

**Azaltıcı önlem.** Ensemble çıktısını kalibre etmek; güven-eşikli abstain/fallback mekanizması; belirsizlik sinyalini karar-vericiye açıkça iletmek.
**Literatür dayanağı:** Güçlü (kalibrasyon literatürü). **Olasılık: Orta | Etki: Orta.**

### 6. Değerlendirme Kaynaklı Başarısızlıklar

#### 6.1 Gizli leakage (YÜKSEK×YÜKSEK)

**Mekanizma.** Kapoor & Narayanan (2023, *Patterns* 4(9):100804) leakage'ın ML-tabanlı bilimde yaygın bir başarısızlık modu olduğunu, "17 fields where leakage has been found, collectively affecting 294 papers" ifadesiyle belgeler; sekiz-türlü taksonomi (train/test ayrımı eksikliği, tüm veride ön-işleme, duplicate'ler, meşru-olmayan feature'lar, temporal leakage, örneklem-bağımlılığı, dağıtım-dışı test seti). Bu projede en olası türler: (a) temporal leakage (geleceği gören feature/hedef), (b) tüm veride ön-işleme/ölçekleme, (c) araç-kimliği bazında bölünmemiş split (relisting duplicate'leri). Kritik uyarı: İç savaş tahmini örneğinde "When the errors are corrected, complex ML models do not perform substantively better than decades-old LR models" — yani leakage düzeltilince karmaşık modelin üstünlüğü kaybolabilir.

**Erken-uyarı işareti.** Gerçekçi-olmayan yüksek doğruluk; aşırı pürüzsüz öğrenme eğrileri; naif baseline ile arasında şüpheli büyük fark; canlı ortamda çöküş.

**Azaltıcı önlem.** Kesin temporal split (train tarihleri < test tarihleri); ön-işlemeyi yalnızca train'e fit edip pipeline içinde uygulamak; grup (araç-kimliği) bazlı split; Kapoor & Narayanan "model info sheet"ini doldurmak; N7 gereği her aşamada leakage denetimi.
**Literatür dayanağı:** Güçlü (Kapoor & Narayanan 2023). **Olasılık: Yüksek | Etki: Yüksek.**

#### 6.2 Çoklu-test şişmesi

**Mekanizma.** Çok sayıda model/feature/eşik/dönem denenip yalnızca "işleyen" raporlanırsa, şans eseri anlamlılık ("garden of forking paths", p-hacking) kaçınılmazdır. Finansal backtest literatürü (Chordia vd., "p-Hacking: Evidence from Two Million Trading Strategies") bunu belgeler; düşük t-eşiği (1.8+) veya çoklu-test düzeltmesi önerilir.

**Erken-uyarı işareti.** Çok sayıda konfigürasyon denenmesi; yalnızca en iyi sonucun raporlanması; out-of-sample'da kaybolan üstünlük.

**Azaltıcı önlem.** Analiz planını önceden-ilan et; denenen tüm konfigürasyonları raporla; çoklu-test düzeltmesi (Bonferroni/deflated Sharpe benzeri); nihai onayı ayrı, dokunulmamış holdout'ta yap.
**Literatür dayanağı:** Güçlü (p-hacking / multiple-comparisons literatürü). **Olasılık: Yüksek | Etki: Yüksek.**

#### 6.3 Güven aralığı olmadan raporlama

**Mekanizma.** Az gözlemli aylık seride nokta-tahmin metrikleri (accuracy) geniş belirsizlik taşır; güven aralığı olmadan raporlanan bir "iyileşme" gürültü olabilir.

**Erken-uyarı işareti.** Tek sayı olarak raporlanan metrikler; küçük test setinde büyük görünen farklar.

**Azaltıcı önlem.** Bootstrap/blok-bootstrap güven aralıkları; Diebold-Mariano benzeri forecast-karşılaştırma testleri; metrikleri her zaman belirsizlik bandıyla raporlamak.
**Literatür dayanağı:** Güçlü (kalibrasyon/forecast-değerlendirme literatürü). **Olasılık: Yüksek | Etki: Orta-Yüksek.**

#### 6.4 Naif baseline'ı yenememe durumunun gizlenmesi (YÜKSEK×YÜKSEK)

**Mekanizma.** Forecasting literatürünün merkezî bulgusu: naif/persistence/random-walk baseline'ı yenmek şaşırtıcı derecede zordur (M-competitions; Hyndman; Moosa). "Modeliniz naif baseline'ı yenemiyorsa kullanmaya değmez." Kapoor & Narayanan (2023) iç savaş tahmininde leakage düzeltildiğinde karmaşık ML'in eski lojistik regresyona üstünlüğünün kaybolduğunu gösterir — bu, "gizli başarı"nın çoğu zaman gizli leakage olduğuna dair en somut kanıttır.

**Erken-uyarı işareti.** MASE ≥ 1; naif "hep-stable" veya "hep-son-yön" tahmincisinin model kadar iyi olması; baseline karşılaştırmasının raporda eksikliği.

**Azaltıcı önlem.** En az iki naif baseline (persistence + çoğunluk-sınıfı) zorunlu; tüm metrikleri baseline-göreli (MASE, skill score) raporla; naifi yenemiyorsa bunu açıkça N6 kapsamında "sinyal yok" olarak raporla, gizleme.
**Literatür dayanağı:** Güçlü (M-competitions; Hyndman; Moosa; Kapoor & Narayanan 2023). **Olasılık: Yüksek | Etki: Yüksek.**

### 7. Dağıtım/Operasyon Kaynaklı Başarısızlıklar

#### 7.1 Veri yayın gecikmesi (vintage / real-time revizyon)

**Mekanizma.** Real-time-data literatürü (Croushore & Stark; Koenig, Dolmas & Piger 2003, *REStat* 85(3); Faust vd.) gösterir ki nihai (revize) veriyle kurulan modeller gerçek-zamanda mevcut olmayan bilgiyi kullanır ve forecast performansını abartır: nihai veriyle kurulan döviz modelleri, revize-öncesi veriyle kurulanların üstünlüğünün yaklaşık üçte birini geri alır. İlan verisinde de agregatların sonradan revize edilmesi/gecikmeli yayımı aynı tuzağı doğurur. Trojanek vd. (2025) ilan verisinde bu noktayı somutlaştırır: çeyreğin üçüncü ayının verisi "forward-looking noise" ekler.

**Erken-uyarı işareti.** Model kurgusunda "as-of" tarihi ihmali; backtest'te yalnızca son-vintage veri kullanımı; canlıda düşen performans.

**Azaltıcı önlem.** Point-in-time / vintage veri tabanı kurmak; her forecast'i yalnızca o tarihte mevcut veriyle üretmek; değerlendirmeyi real-time vintage'larla yapmak.
**Literatür dayanağı:** Güçlü (Croushore & Stark; Koenig vd. 2003; Faust vd.; Trojanek vd. 2025). **Olasılık: Orta-Yüksek | Etki: Yüksek.**

#### 7.2 Feature'ın canlı/gerçek-zamanlı ortamda mevcut olmaması

**Mekanizma.** Eğitimde kullanılan bir feature canlıda tahmin anında mevcut değilse (ör. sonradan hesaplanan agregat), training-serving skew oluşur; model kâğıt üzerinde çalışır, üretimde çöker.

**Erken-uyarı işareti.** Feature'ların üretim gecikmesinin denetlenmemiş olması; training-serving skew testinin yokluğu; üretimde null-oranı artışı (>1% alarm).

**Azaltıcı önlem.** Her feature için "tahmin anında mevcut mu?" denetimi; modelin gördüğü gerçek vektörü loglamak; training-serving skew izleme.
**Literatür dayanağı:** Güçlü (production-ML güvenilirlik literatürü). **Olasılık: Orta | Etki: Yüksek.**

#### 7.3 Modelin bakım/yeniden-eğitim ihmali & concept drift'in izlenmemesi

**Mekanizma.** Dağıtılan model dünya değiştikçe bozulur; izlenmezse "stale intelligence" sessizce değer kaybettirir. Uzun süre dokunulmayan modellerde hata oranının belirgin arttığı raporlanır.

**Erken-uyarı işareti.** İzleme/alarm altyapısının yokluğu; yeniden-eğitim tetikleyicisinin tanımsızlığı; sahiplik (ownership) belirsizliği.

**Azaltıcı önlem.** PSI/KS eşikli otomatik alarm + yeniden-eğitim tetikleyicisi; net sahiplik/paging; fallback (kural-tabanlı/eski sürüm/belirsizlik sinyali) mekanizması.
**Literatür dayanağı:** Güçlü (drift-monitoring / MLOps literatürü). **Olasılık: Orta-Yüksek | Etki: Orta-Yüksek.**

### 8. Yorumlama/Karar Kaynaklı Başarısızlıklar

#### 8.1 İstatistiksel sinyalin ekonomik/karar-faydasına çevrilememesi

**Mekanizma.** İstatistiksel olarak anlamlı bir yön-doğruluğu, işlem maliyetleri/karar frictions altında ekonomik fayda üretmeyebilir. Naive-forecast literatürü (MPANF, arXiv:2406.14469) açıkça uyarır: bu iyileşmeler mütevazı ve bağlam-bağımlı olabilir; işlem maliyetleri, slippage ve piyasa frictions dikkate alındığında ekonomik kazanca dönüşmeyebilir.

**Erken-uyarı işareti.** Yalnızca accuracy raporlanması, karar-faydası (regret/expected payoff) hesaplanmaması; küçük ama "anlamlı" edge'in maliyet sonrası kaybolması.

**Azaltıcı önlem.** Karar-teorik değerlendirme (beklenen fayda/regret, CDL); yön sinyalinin gerçek iş kararındaki değerini maliyetlerle birlikte simüle etmek.
**Literatür dayanağı:** Güçlü (MPANF 2024; Calibration Error for Decision Making 2024). **Olasılık: Orta | Etki: Yüksek.**

#### 8.2 Yön tahmininin yanlış bir iş kararına bağlanması

**Mekanizma.** Aylık up/down/stable sinyali, karşılık gelmediği bir aksiyona (ör. bireysel araç fiyatlama, envanter kararı) bağlanırsa, doğru sinyal bile yanlış sonuç üretir; sinyal piyasa-geneli iken karar birim-düzeyinde olabilir.

**Erken-uyarı işareti.** Sinyalin kapsamı (agrega) ile kararın kapsamı (birim) arasındaki uyumsuzluk; kararın sinyalin belirsizliğini yok sayması.

**Azaltıcı önlem.** Sinyalin kapsamını ve sınırlarını açıkça belgelemek; kararı sinyal belirsizlik bandıyla eşleştirmek; kullanım-amacı dokümantasyonu.
**Literatür dayanağı:** "Literatürde net değil" (proje-özgü karar bağlamı). **Olasılık: Orta | Etki: Yüksek.**

### 9. BAŞARISIZLIK MODU REGİSTRİ (Ana Teslimat)

En kritik satırlar **kalın** (yüksek olasılık × yüksek etki).

| # | Başarısızlık Modu | Mekanizma | Olasılık | Etki | Erken-Uyarı İşareti | Azaltıcı Önlem | Sorumlu Faz/Referans |
|---|---|---|---|---|---|---|---|
| **1** | **K8+N9: İlan-yönü ≠ İşlem-yönü sapması** | **Pazarlık marjı rejime göre pro-döngüsel değişir; düşüşte genişler, yükselişte daralır** | **Yüksek** | **Yüksek** | **DOM uzaması + fiyat-düşürme oranı artışı + conversion düşüşü sinyalle ters yönde** | **Proxy izleme paneli + rejim-koşullu tutarlılık testi + işlem serisiyle yönsel uyum ölçümü** | **Faz 04 (düzeltme); test tasarımı bu faz — Anenberg & Laufer 2017; Anenberg 2016; Han & Strange 2016; Carrillo vd. 2015** |
| 2 | Seçilim yanlılığı (satılmayanlar dışarıda) | Yalnızca satılan ilanlar temsili değil; forecast hatası hafife alınır | Orta-Yüksek | Yüksek | Satılan/satılmayan feature dağılımı ayrışması | Heckman/IMR veya censoring; satılmayanları veri hattında tutmak | Faz 04 — Heckman 1979; art-auction selection lit. |
| 3 | Kompozisyon (mix) kayması (N1) | Segment ağırlığı değişince ham fiyat serisi sahte yön üretir | Yüksek | Orta-Yüksek | Segment/yaş/km PSI kayması; ham-vs-düzeltilmiş ayrışması | Stratifikasyon/hedonik düzeltme; mix PSI izleme | Faz 02/04 — IMF RPPI Handbook; Case & Shiller 1987 |
| **4** | **Gizli leakage** | **Temporal/duplicate/ön-işleme sızıntısı iyimser değerlendirme** | **Yüksek** | **Yüksek** | **Gerçekçi-olmayan doğruluk; pürüzsüz eğriler; naifle şüpheli fark** | **Temporal+grup split; pipeline'da fit; model info sheet** | **Faz 03/06; N7 — Kapoor & Narayanan 2023 (294 makale)** |
| **5** | **Naif baseline'ı yenememenin gizlenmesi** | **Persistence/random-walk yenilmesi zor; edge yok** | **Yüksek** | **Yüksek** | **MASE ≥ 1; naif çoğunluk modeli yeniyor** | **≥2 naif baseline zorunlu; baseline-göreli metrik; N6'yı dürüstçe raporla** | **Faz 06; N6 — M-competitions; Hyndman; Kapoor & Narayanan 2023** |
| 6 | Çoklu-test şişmesi | Çok konfigürasyon → şans eseri anlamlılık | Yüksek | Yüksek | Çok deneme, tek raporlama; OOS'ta kaybolan üstünlük | Pre-registration; tüm denemeleri raporla; çoklu-test düzeltmesi; dokunulmamış holdout | Faz 06 — p-hacking / forking-paths lit. |
| 7 | "Stable" bandının anlamsızlaşması | Çok geniş→çoğunluk; çok dar→gürültü | Orta-Yüksek | Orta | Stable frekansı %70+ veya %5-; naif band'ı yeniyor | Band'ı volatiliteye (±σ) bağla; her band'da naif baseline raporla | Faz 02 — "literatürde net değil" |
| 8 | Threshold/ufuk keyfîliği (dengesizlik/gürültü) | Keyfî eşik/ufuk dengesizlik veya gürültü etiketi | Yüksek | Orta-Yüksek | Aşırı çarpık sınıflar; eşiğe etiket kararsızlığı | Pre-register eşik/ufuk; duyarlılık analizi; reel bazda tanımla | Faz 02; N3 — "literatürde net değil" |
| **9** | **Kur/ÖTV/arz şoklarında çöküş (N2)** | **Location shift'te sabit-katsayı model kayma-öncesi trendi tahmin eder** | **Yüksek** | **Yüksek** | **Şok takvimiyle çakışan hata artışı; katsayı kararsızlığı** | **Intercept-correction/rejim kuklası; hızlı yeniden-eğitim; şok-dönemi ayrı raporlama** | **Faz 05; N2 — Hendry forecast-failure; TR 24 Temmuz 2025 ÖTV düzenlemesi** |
| 10 | Eğitim döneminin gelecek rejimi temsil etmemesi | Kısa/tek-rejim örneklem gelecekte kör | Yüksek | Yüksek | Tek makro rejim kapsama; OOS makro göstergeleri aralık dışı | En uzun pencere; rejim-bazlı ayrı değerlendirme; kapsam raporu | Faz 01 — "Who Saw It Coming?" 2026 |
| 11 | Sessiz drift / saf konsept kayması | Hata fırlatmadan bozulma; P(Y\|X) değişimi proxy'lerle görünmez | Orta-Yüksek | Yüksek | PSI artışı; ama saf konsept kayması sıfır-delta | Katmanlı izleme + periyodik etiketli denetim + champion/challenger | Faz 06 — drift-monitoring; Label-Free Detection 2026 |
| 12 | Overfitting (az-gözlem) | Küçük örneklemde gürültüyü öğrenme | Yüksek | Yüksek | Train-val açığı >5%; val hatası yükseliyor | Regülarizasyon/parsimony; nested TS-CV; CV içi feature seçimi | Faz 05 — NCBI overfitting; Simon vd. |
| 13 | Yanlış kalibrasyon / label drift | Olasılıklar gerçek frekansı yansıtmaz; eşik optimal değil | Orta | Orta-Yüksek | Reliability sapması; yüksek ECE | Platt/isotonic; r/(r+r') eşik ayarı; CDL izleme | Faz 05 — Flach survey; CDL 2024 |
| 14 | Ordinal yapının ihmali | down↔up hataları medium hatasıyla eşit sayılır | Orta | Orta | Komşu-olmayan hata yüksekliği; nominal iyi, MAE kötü | Ord-MAP/cumulative karar; MAE/QWK metrik | Faz 05 — Ord-MAP 2025 |
| 15 | Vintage / real-time revizyon | Nihai veriyle kurulan model gerçek-zamanda yok bilgiyi kullanır | Orta-Yüksek | Yüksek | "as-of" ihmali; yalnız son-vintage backtest | Point-in-time veri tabanı; real-time vintage değerlendirme | Faz 06 — Croushore & Stark; Koenig vd. 2003; Trojanek vd. 2025 |
| 16 | Feature canlıda mevcut değil (training-serving skew) | Tahmin anında olmayan feature | Orta | Yüksek | Feature gecikmesi denetlenmemiş; null artışı | "Tahmin anında mevcut mu?" denetimi; skew izleme | Faz 06 — production-ML lit. |
| 17 | İstatistik sinyalin ekonomik faydaya çevrilememesi | Anlamlı edge maliyet sonrası kaybolur | Orta | Yüksek | Yalnız accuracy; karar-faydası hesapsız | Karar-teorik değerlendirme (regret/CDL); maliyetli simülasyon | Faz 07 — MPANF 2024; CDL 2024 |
| 18 | Yön tahmininin yanlış karara bağlanması | Agrega sinyal birim-düzey karara bağlanır | Orta | Yüksek | Sinyal-karar kapsam uyumsuzluğu | Kapsam/sınır dokümantasyonu; belirsizlik bandıyla eşleştirme | Faz 07 — "literatürde net değil" |
| 19 | Ölü/tekrarlı ilanlar | Relisting/ölü ilan hedefi ve DOM'u kirletir; duplicate-leakage | Orta | Orta | Aynı kimlik/vektör çoklu kayıt; pürüzsüz eğri | İlan-kimliği dedup; cumulative-DOM; grup-split | Faz 01/03 — Kapoor & Narayanan 2023 |
| 20 | Fiyat-düşürme davranışı hedefi kirletir | İlan-içi indirim piyasadan bağımsız gürültü | Orta | Orta | Etiketin ilan-içi indirimlerle korelasyonu | Etiketi agrega-piyasa bazında tanımla; revizyonu ayrı feature | Faz 02 — Merlo & Ortalo-Magné 2004 |

### 10. Projenin Terk/Yeniden-Çerçeveleme Kriterleri (N6 Uzantısı)

N6 gereği "sinyal yok" meşru bir sonuçtur. Aşağıdaki **önceden-ilan-edilen (pre-registered)** eşikler karşılanmazsa proje mevcut haliyle TERK edilmeli veya yeniden-çerçevelenmelidir. Bu, iyimserlik değil dürüstlük gereğidir; negatif sonucun gizlenmesi (publication bias / positive-outcome bias) bilimsel ve operasyonel bir hatadır ("Embracing Negative Results in Machine Learning", ICML 2024, arXiv:2406.03980).

**TERK/yeniden-çerçeveleme tetikleyicileri:**
1. **Naif baseline kriteri:** Model, dokunulmamış holdout'ta iki naif baseline'ı (persistence + çoğunluk-sınıfı) güven aralığı örtüşmeden **yenemiyorsa** → sinyal yok; terk veya yeniden-çerçevele.
2. **K8 uyum kriteri:** İlan-tabanlı yön sinyalinin bağımsız işlem-tabanlı seriyle yönsel uyumu (directional agreement) önceden belirlenen eşiğin (ör. şansın anlamlı üstü) altındaysa ve rejimler arası kararsızsa → hedef geçersiz; yeniden-çerçevele (ilan-fiyatı yönünü kendi başına bir hedef olarak tanımla, işlem-fiyatı vekili olarak değil).
3. **Rejim kararlılığı kriteri:** Performans yalnızca tek bir rejimde pozitif, diğerlerinde baseline-altı ise → genellenebilir sinyal yok.
4. **Ekonomik fayda kriteri:** İstatistiksel edge, işlem maliyetleri/karar frictions altında pozitif beklenen fayda üretmiyorsa → karar-faydası yok; yeniden-çerçevele.
5. **Leakage-düzeltme kriteri:** Leakage denetimi sonrası performans naif baseline seviyesine düşüyorsa (Kapoor & Narayanan iç-savaş örneğindeki gibi) → önceki sonuçlar artefakttı; terk.

**Yeniden-çerçeveleme (terk yerine) seçenekleri (yalnızca not, yeni metodoloji önerisi değildir):** hedefi işlem-vekili olmaktan çıkarıp doğrudan ilan-davranışı (DOM/fiyat-düşürme) tahminine kaydırmak; frekansı/agregasyon düzeyini değiştirmek; "sinyal yok" bulgusunu dürüst bir negatif-sonuç raporu olarak yayımlamak.

### 11. Açık Sorular / Literatürde Net Olmayanlar

- **İlan-tabanlı düşük-frekanslı yön-etiketleme (N3):** Doğrudan bir yön-etiketleme literatürü yoktur; proje finansal-piyasa ve emlak-endeksi analojileriyle çalışır. Bu analojilerin ikinci el araç piyasasına transfer edilebilirliği **ampirik olarak doğrulanmamıştır**.
- **"Stable" band genişliğinin optimal seçimi:** Proje-özgü; literatürde net değil.
- **Threshold/ufuk seçiminin optimal kuralı:** Literatürde net değil (N3'ün uzantısı).
- **Türkiye ikinci el araç piyasasında sale-to-list marjının döngüsel davranışının nicel büyüklüğü:** Konut literatüründen güçlü analoji var (Anenberg & Laufer 2017; Trojanek vd. 2025 — list index'ler transaction index'i 1-2 ay önden gösteriyor), ama TR araç piyasası için doğrudan yayımlanmış nicel ölçüm bulunamadı — dolaylı proxy izlemeyle test edilmesi gerekir.
- **Yön sinyalinin doğru iş kararına eşlenmesi:** Karar bağlamı proje-özgü; literatürde net değil.

## Recommendations

**Aşama 1 (hemen, değerlendirme kilitlenmeden önce):**
- Temporal + araç-kimliği (grup) bazlı split'i ve pipeline-içi ön-işlemeyi zorunlu kıl; Kapoor & Narayanan model info sheet'ini doldur (leakage — #4).
- En az iki naif baseline'ı (persistence + çoğunluk-sınıfı) ve baseline-göreli metrikleri (MASE, skill score) zorunlu raporlama kuralı koy (#5).
- Analiz planını (eşik, ufuk, band, denenecek modeller, birincil metrik) **önceden-ilan et**; çoklu-test düzeltmesi tanımla (#6, #8).

**Aşama 2 (K8 test tasarımı — kritik):**
- DOM medyanı, fiyat-düşürme oranı, conversion oranını aylık izleyen proxy panelini kur; bu serileri ilan-yön sinyaliyle karşılaştıran sapma-alarmı tanımla. Trojanek vd. (2025) uyarısı gereği proxy verisini çeyreğin ilk-ikinci ayından al, üçüncü-ay verisi "forward-looking noise" ekler (#1).
- Bağımsız işlem-tabanlı kamu serileriyle (TÜİK, sahibindex/BETAM) periyodik yönsel-uyum ölçümü yap; uyum eşiğini önceden belirle (#1, terk kriteri 2).
- Rejim-koşullu tutarlılık testini örneklemi yükseliş/düşüş dilimlerine bölerek uygula (#1, #9, #10).

**Aşama 3 (operasyon):**
- Point-in-time/vintage veri tabanı kur; real-time vintage değerlendirmesi yap (#15).
- PSI/KS eşikli drift alarmı (>0.10 incele, >0.25 yeniden-eğit) + periyodik etiketli denetim + champion/challenger; net sahiplik ve fallback tanımla (#11, #16).

**Kararı değiştirecek eşikler:** Bölüm 10'daki beş pre-registered tetikleyiciden herhangi biri karşılanırsa, projeyi mevcut haliyle sürdürmek yerine terk/yeniden-çerçeveleme kararı verilmelidir. Naif baseline'ı güven aralığı örtüşmeden yenmek ve K8 yönsel-uyum eşiğini rejimler arası kararlı biçimde geçmek, devam için asgari koşuldur.

## Caveats

- Bu rapor **risk avlar, yeni metodoloji önermez**; azaltıcı önlemlerin çoğunun tasarımı önceki fazların (02-06) işiydi ve buraya yalnızca kritik geri-referansla getirilmiştir.
- K8+N9 için başvurulan nicel kanıt ağırlıklı olarak **konut piyasası** literatüründendir (Anenberg & Laufer 2017; Anenberg 2016; Han & Strange 2016; Carrillo vd. 2015; Trojanek vd. 2025); ikinci el araç piyasasına transfer güçlü bir analoji olsa da doğrudan araç-piyasası ölçümüyle doğrulanmamıştır — bu yüzden dolaylı proxy testi zorunludur.
- Bazı web kaynakları (blog, satıcı-tavsiye siteleri) birincil değildir; bunlar yalnızca mekanizma örneklemesi için kullanılmış, nicel iddialar hakemli/kurumsal kaynaklara bağlanmıştır.
- "Literatürde net değil" olarak işaretlenen noktalar tahmin edilmemiş, açıkça belirsiz bırakılmıştır (N3, N6 ilkesi).
- Olasılık × etki dereceleri bu projenin bağlamına göre uzman-yargısıdır; farklı veri/rejim koşullarında güncellenmelidir.
- Türkiye ÖTV rakamları (24 Temmuz 2025 / 7555 sayılı değişiklik + 10115 sayılı Karar) ikincil haber/ticari kaynaklardan derlenmiştir; kesin oran ve matrah dilimleri için Resmî Gazete birincil metni esas alınmalıdır.

## Kaynakça

1. Anenberg, E. & Laufer, S. (2017). "A More Timely House Price Index." *Review of Economics and Statistics*, 99(4):722-734. (FEDS WP 2014-16)
2. Anenberg, E. (2016). "Information Frictions and Housing Market Dynamics." *International Economic Review*, 57(4):1449-1479. (FEDS WP 2012-48)
3. Han, L. & Strange, W. C. (2016). "What is the role of the asking price for a house?" *Journal of Urban Economics*, 93:115-130.
4. Carrillo, P. E., de Wit, E. R. & Larson, W. (2015). "Can Tightness in the Housing Market Help Predict Subsequent Home Price Appreciation?" *Real Estate Economics*, 43(3):609-651. (IIEP-WP-2012-11)
5. Merlo, A. & Ortalo-Magné, F. (2004). "Bargaining over Residential Real Estate: Evidence from England." *Journal of Urban Economics*, 56(2):192-216.
6. Trojanek, R., Hartigan, L., Pfeifer, P. & Steurer, M. (2025). "Nowcasting Transaction-Based House Price Indices Using Web-Scraped Listings and MIDAS Regression." CAMA WP 2025-45 / Graz Economics Papers 2025-13.
7. Kapoor, S. & Narayanan, A. (2023). "Leakage and the reproducibility crisis in machine-learning-based science." *Patterns*, 4(9):100804.
8. IMF (Eurostat et al.). *Handbook on Residential Property Prices (RPPIs)*, Bölüm 4: Stratification/Mix Adjustment; Case & Shiller (1987).
9. Heckman, J. (1979). "Sample Selection Bias as a Specification Error." *Econometrica*.
10. "How Well Do Selection Models Perform? Assessing the Accuracy of Art Auction Pre-Sale Estimates." *PMC*.
11. Hendry, D. F. — Forecast-failure literature; Economics Observatory, "Why can economic forecasts go wrong?"
12. "Who Saw It Coming? Historical Experience and the 2021 Inflation Forecast Failure." arXiv (2026).
13. "Label-Free Detection of Governance Evidence Degradation in Risk Decision Systems." arXiv (2026).
14. NCBI Bookshelf: "Overfitting, Underfitting and General Model Overconfidence and Under-Performance Pitfalls and Best Practices in ML and AI."
15. Flach, P. et al. (2023). "Classifier calibration: a survey." *Machine Learning* (Springer).
16. "Calibration Error for Decision Making." arXiv:2404.13503.
17. Delgado, R. (2025). "Ord-MAP criterion: Extending MAP for ordinal classification." *Knowledge-Based Systems* (ScienceDirect).
18. Chordia, T., Goyal, A. & Saretto, A. "p-Hacking: Evidence from Two Million Trading Strategies."
19. Makridakis et al. — M-Competitions; Hyndman, R. J., "Benchmarks for forecasting"; Moosa — random-walk / naive benchmark literature.
20. "Movement-Prediction-Adjusted Naïve Forecast (MPANF): Is the Naive Baseline Unbeatable?" arXiv:2406.14469.
21. Croushore, D. & Stark, T.; Koenig, Dolmas & Piger (2003), "The Use and Abuse of Real-Time Data in Economic Forecasting," *REStat* 85(3); Faust et al. — real-time/vintage forecasting literature.
22. Production-ML reliability & drift-monitoring practitioner literature (Hex "ML Failure Modes"; Microsoft "Failure Modes in ML"; RAND AI-project failure study).
23. "Position: Embracing Negative Results in Machine Learning." ICML 2024 (arXiv:2406.03980).
24. Niculescu-Mizil, A. & Caruana, R. (2005) — ensemble kalibrasyonu.
25. Türkiye bağlamı: TÜİK Motorlu Kara Taşıtları verileri; BETAM sahibindex Otomobil Piyasası Görünümü; 24 Temmuz 2025 Resmî Gazete (7555 sayılı değişiklik + 10115 sayılı Cumhurbaşkanı Kararı); ikincil kaynaklar (WAT Mobilite, Voltify, Otomobilhaber, arabam.com).

## Kullanılan Nihai Arama Sorguları

**İngilizce:** machine learning failure modes production · forecasting model failure regime change · selection bias unsold listings survival analysis · listing price asking price sold price gap used cars negotiation · composition effect quality mix bias house price index · calibration failure classifier decision making probability · silent model degradation drift monitoring PSI concept drift · data leakage machine learning evaluation pitfalls reproducibility · real-time data revision vintage forecasting pitfalls · overfitting small sample warning signs machine learning generalization · multiple hypothesis testing p-hacking forecasting spurious predictability · forecast baseline random walk naive benchmark hard to beat · days on market price reduction probability of sale listing signal · ordinal classification ignoring order cost sensitive up down stable · list price transaction price ratio market conditions housing bargaining power · knowing when to stop machine learning project negative results publication · sample selection bias Heckman asking price only sold observed

**Türkçe:** Türkiye ikinci el araç piyasası fiyat ÖTV kur 2024 2025 · makine öğrenmesi başarısızlık nedenleri (kapsam) · model çöküşü rejim değişimi (kapsam) · ilan fiyatı yanlılık ikinci el (kapsam)

**Subagent hedefli araştırması:** K8+N9 bargaining margin regime evidence — Carrillo/de Wit/Larson, Anenberg & Laufer (2017), Anenberg (2016), Merlo & Ortalo-Magné (2004), Han & Strange (2016), Haurin vd. (2013), Trojanek vd. (2025).