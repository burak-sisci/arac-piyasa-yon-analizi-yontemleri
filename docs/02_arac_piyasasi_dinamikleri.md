---
faz_no: 02
faz_adi: "Araç Piyasası Dinamikleri (Türkiye Odaklı)"
tarih: 2026-07-13
kapsam_ozeti: "İkinci el araç fiyatlarını sürükleyen makro, politika, arz-talep ve mikro yapı faktörlerinin modellenebilir değişkenler olarak haritalanması"
bagimli_oldugu_fazlar: [01]
durum: tamamlandi 
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: 24
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-13
---

# Faz 2 — Türkiye İkinci El Araç Piyasası Dinamiklerinin Modellenebilir Değişken Haritası

## TL;DR

- Türkiye'de ikinci el araç fiyatlarının **baskın (dominant) modellenebilir sürücüsü döviz kuru (özellikle USD/TRY)**; sektör içindeki en tutarlı gözlemlenen ilişki budur (VavaCars Ticari Grup Başkanı Serdıl Gözelekli: "fiyatların döviz kuru özellikle dolar ile olan güçlü korelasyonu"). Kur, enflasyon, faiz/taşıt kredisi ve ÖTV politikası aylık frekansta gözlemlenebilir ve TCMB/TÜİK/Resmî Gazete'den ücretsiz erişilebilir. Bunlar aylık tahmin ufkuna en uygun değişkenlerdir.
- **Aylık ölçekte doğrudan gözlemlenebilir iki kamuya açık ikinci el fiyat serisi vardır:** BETAM "sahibindex" (sahibinden.com verisiyle, aylık, ilanda kalma süresi + talep endeksi dahil) ve arabam.com "Aylık Fiyat Endeksi" (ilan fiyatı ortalaması, aylık). **Ancak ikisi de Manheim tarzı karma/kilometre/hedonik düzeltmeli DEĞİL — segment kırılımlı ham ilan ortalamalarıdır**; bu, kompozisyon (mix) kaymalarına açık oldukları anlamına gelir ve modelleme açısından kritik bir kısıttır.
- **Arz şoku kanalı (sıfır araç kıtlığı → ikinci el primi) 2021–2023'te güçlü biçimde gözlemlendi ama tersine döndü:** 2026'da sıfır araç kampanyaları/agresif fiyatlama ikinci eli baskılıyor. Bu, "sıfır araç fiyatı/kampanya yoğunluğu" değişkeninin **çift yönlü** ve rejime bağlı olduğunu gösterir. EV değer kaybı ve TOGG gibi yerli EV dinamikleri ise Türkiye özelinde literatürde net değildir; anekdotsal ve çelişkilidir.

## Key Findings

1. **Döviz kuru geçişkenliği, ikinci el fiyatlarının en güçlü tek değişkenli açıklayıcısıdır.** TCMB working paper literatürü (Kara & Öğünç 2005; Yılmazkuday 2020 gibi çalışmalara atıfla) tüketici fiyatlarına 1 yıllık kümülatif kur geçişkenliğini yaklaşık %15–26 aralığında bulur; TCMB blogu otomobili "doğrudan ithal edilen" bir tüketim sepeti kalemi olarak açıkça sayar. İkinci el kanalında etki iki mekanizmayla gelir: (a) ithal sıfır araç ve yedek parça maliyeti, (b) sıfır araç fiyatının ikinci ele referans (çapa) olması. Sektör verisi bu bağı aylık düzeyde teyit eder.

2. **Türkiye'de aylık, kamuya açık iki ikinci el fiyat göstergesi mevcuttur, ancak metodolojik olarak Manheim'dan zayıftır.** BETAM sahibindex (Aralık 2023'ten beri aylık, sahibinden.com havuzu) ve arabam.com Aylık Fiyat Endeksi (ilan bazlı) — her ikisi de "ortalama ilan/satılık fiyat" raporlar, hedonik/karma düzeltme kamuya açık metinlerde belgelenmemiştir. Manheim Used Vehicle Value Index ise ABD'de karma (mix), kilometre ve mevsimsellik düzeltmeli, yılda 5 milyondan fazla işlem üzerine kurulu ve genellikle takip eden ayın 5. iş gününde yayımlanır — Türkiye'de birebir eşdeğeri yoktur.

3. **ÖTV matrah/oran değişiklikleri ikinci ele hızlı (haftalar içinde) ve ölçülebilir biçimde geçer, ama etki yönü koşullara bağlıdır.** 12 Ağustos 2021 matrah düzenlemesi sonrası ikinci el fiyatları Ağustos'ta aylık ~%10 düştü (MASFED/sektör); 24 Temmuz 2025 düzenlemesi EV'lerde en düşük ÖTV'yi %10'dan %25'e çıkardı ve Togg T10X standart menzil fiyatını 1.505.000 TL'den 1.710.226 TL'ye yükseltti. Resmî Gazete tarihleri kesin "event" değişkeni sağlar.

4. **Sıfır araç arz kısıtı ikinci el primini 2021–2023'te yukarı, 2025–2026'da aşağı itti.** Çip krizi döneminde ikinci el ilan fiyatları haftada ~%10 arttı (Hürriyet/Cardata); ABD karşılaştırmasında kullanılmış araç TÜFE'si Mayıs 2021'e kadar 12 ayda neredeyse %30 arttı ve toplam aylık TÜFE artışının yaklaşık üçte birini oluşturdu (Cleveland Fed Economic Commentary 2021-17). 2026'da tersine, sıfır araç kampanyaları 0–5 yaş ikinci eli baskılıyor (arabam.com). Değişken: sıfır araç satış/teslimat + kampanya yoğunluğu, ODMD'den aylık.

5. **Piyasa mikro yapısı göstergeleri Türkiye'de aylık kamuya açık olarak izlenebilir.** BETAM "ilanda kalma süresi" (Haziran 2026: 23,8 gün), "satılan/satılık ilan oranı" (Haziran 2026: %19,4) ve "talep endeksi" yayımlar. İlan-işlem farkı için: arabam.com bireysel satıcıların fiyat düşürme oranının kurumsallardan %17,08 puan yüksek olduğunu raporlar; noter devir verisi (TÜİK, aylık) gerçekleşen işlem hacmini verir.

6. **EV değer kaybı Türkiye için literatürde net değildir; uluslararası bulgular çelişkili ve aktarılabilirliği sınırlıdır.** Uluslararası çalışmalar EV'lerin 3 yılda %38–42 (Cox Automotive EU, 2025 sonu) değer kaybettiğini gösterir; iSeeCars'tan Karl Brauer'a göre EV'ler beş yıllık dönemde genel piyasadan yaklaşık 13 puan daha fazla değer kaybeder (CNBC, 20 Ekim 2025). Türkiye'de TOGG için ise anekdotsal ve çelişkili veriler var: bazı kaynaklar "değer kaybı yok/sıfıra yakın" derken, diğerleri sıfır faizli kampanyaların ikinci el TOGG'u sattırmadığını söylüyor.

7. **Mevsimsellik Türkiye'de sektör anlatısında güçlü ama nicel olarak doğrulanmamıştır.** Uzmanlar Şubat–Mart, yaz başı ve Ekim–Aralık'ta hareketlilik, bayram/tatil etkisi belirtir; ancak 2026'da beklenen yaz canlanması gerçekleşmedi (arabam.com). Manheim ABD'de Census X-13 ile mevsimsel düzeltme uygular — Türkiye endekslerinde açık mevsimsel düzeltme belgelenmemiştir.

## Details

### 1. Giriş ve Kapsam

Bu doküman, çok fazlı araştırma programının Faz 2'sidir. Amaç, Türkiye ikinci el araç fiyatlarını sürükleyen iktisadi/piyasa dinamiklerini **modellenebilir değişkenler** olarak haritalamaktır: her dinamik için (a) gözlemlenebilir gösterge, (b) frekans + kaynak, (c) fiyata etkisinin gecikmesi (lag), (d) ampirik kanıtın gücü değerlendirilir. Faz 1'de tahmin ufkunun büyük olasılıkla **aylık** olacağı belirlendiği için her dinamik bu ufka göre süzülmüştür.

Kapsam dışı (bu fazda işlenmez): yeni araç fiyat tahmini literatürü (yeni araç yalnızca dışsal faktör), model mimarileri/ML teknikleri, label tasarımı/threshold seçimi, genel feature engineering. Yeni araç yalnızca ikinci eli etkileyen dışsal bir referans/çapa değişkeni olarak ele alınır.

Coğrafya kuralı: Türkiye odaklı. Uluslararası çalışmalar yalnızca (a) Türkiye'de karşılığı olan mekanizmayı açıklıyorsa veya (b) Türkiye'de eşdeğeri olmayan bir ölçüm metodolojisi sunuyorsa dahil edilmiştir ve aktarılabilirlik sınırı açıkça belirtilmiştir.

### 2. Makro Sürücüler (kur, enflasyon, faiz, kredi)

**Döviz kuru (USD/TRY, EUR/TRY).** Türkiye'de ikinci el fiyatının en tutarlı gözlemlenen açıklayıcısıdır. Mekanizma: (i) ithal sıfır araç ve yedek parça maliyeti kanalı, (ii) sıfır araç fiyatının ikinci ele referans olması. TCMB literatürü kur geçişkenliğinin tüketici fiyatlarına yaklaşık %15 (1 yıl kümülatif; TCMB blogu) ile %26 (Kara & Öğünç tipi tahminler) aralığında olduğunu, otomobilin doğrudan ithal tüketim malı olarak yüksek geçişkenlik grubunda yer aldığını belirtir. Pierros, Rodousakis & Soklis (2024, Applied Economics Letters 31(1):24–30) arz-kullanım modeliyle genel fiyat düzeyine geçişkenliği 0,61 birim bulur. Sektör verisi aylık teyit sağlar: VavaCars Mart 2026'da "dolar bazında fiyat hareketi neredeyse yatay" diyerek TL fiyatının dolarla güçlü korelasyonunu vurgular; Ocak 2026'da yatay seyreden fiyatların dolar hareketiyle yeniden artışa geçtiğini raporlar. **Lag:** kısa — haftalar; sektör anlatısında ilan fiyatları kur hareketine günler-haftalar içinde tepki verir (çip krizi döneminde "bir haftada %10"). **Kanıt gücü:** geçişkenlik teorisi için güçlü (hakemli, TCMB working paper); ikinci el özelinde orta (sektör raporu + teori).

**Enflasyon (TÜFE/ÜFE).** İki rol: (i) nominal fiyatların genel seviye artışıyla yukarı çekilmesi, (ii) reel fiyat hesaplamasında deflatör. 2026'nın ilk yarısında ikinci el nominal fiyatlar TÜFE'nin belirgin altında kaldı: VavaCars ilk yarı +%5 nominal, aynı dönem enflasyon %17,7; BETAM Haziran 2026 reel yıllık -%7,9. Bu, ikinci el fiyatının **reel olarak gerilediğini** ama nominal olarak arttığını gösterir — modelde nominal/reel ayrımı kritik. **Frekans:** aylık (TÜİK, ayın 3'ü). **Lag:** eşzamanlı-kısa. **Kanıt gücü:** orta-güçlü.

**Faiz oranları ve taşıt kredisi koşulları.** Taşıt kredisi faizi talep kanalını doğrudan etkiler; yüksek faiz talebi erteler ("finansmana erişim koşullarının sınırlı kalması... talebin daha seçici olması" — VavaCars). BDDK kredilendirme oranları (kasko değeri dilimlerine göre azami vade: 400.000 TL altı 48 ay, 400.000–800.000 TL 36 ay, 800.000–1.200.000 TL 24 ay, 1.200.000–2.000.000 TL 12 ay, 2.000.000 TL üstü kredi kullandırılmaz) ikinci el için yapısal bir talep kısıtı oluşturur. Hesapkurdu 10.07.2026'da ortalama taşıt kredisi faizini aylık %3,70 raporlar. **Kaynak:** TCMB EVDS "Kredi Faiz Oranları — Taşıt" serisi (aylık/haftalık ağırlıklı ortalama, ücretsiz). **Lag:** faiz değişimi → talep → fiyat için 1–3 ay makul; literatürde Türkiye ikinci el özelinde nicel lag **net değil**. **Kanıt gücü:** orta (teorik olarak güçlü, Türkiye ikinci el için nicelleştirilmemiş).

**Hanehalkı satın alma gücü.** Reel ücret, tüketici güven endeksi (TÜİK/TCMB, aylık) talep göstergesi olarak kullanılabilir. Sektör 2026'da "fiyat hassasiyeti" ve "seçici talep" anlatısıyla bunu destekler; ancak ikinci el fiyatına doğrudan nicel katkı **literatürde net değil**.

> **Projeye Uygulanabilirlik (Bölüm 2):** Kur (USD/TRY), TÜFE, taşıt kredisi faizi ve tüketici güveni — dördü de aylık, ücretsiz, uzun geçmişli (TCMB EVDS/TÜİK). Kur en yüksek öncelikli değişkendir; nominal/reel dönüşüm için TÜFE zorunludur. Faiz ve güven endeksinin lag yapısı Türkiye ikinci el özelinde ampirik olarak kalibre edilmemiştir, bu nedenle model içi lag taraması gereklidir.

### 3. Politika ve Regülasyon Kanalı (ÖTV, matrah, ithalat)

**ÖTV matrah/oran değişiklikleri.** Sıfır araç nihai fiyatını doğrudan belirler; ikinci ele referans (çapa) kanalıyla geçer. Spesifik tarihli örnekler:
- **12 Ağustos 2021** Cumhurbaşkanı Kararı (matrah dilimi değişimi): sıfır araçlarda %3,3–16,6 (30.000–80.000 TL) düşüş; ikinci el Ağustos 2021'i bir önceki aya göre ortalama ~%10 düşüşle kapattı (MASFED Başkanı Aydın Erkoç, sektör).
- **24 Kasım 2022** (6417 sayılı karar): matrah dilimleri güncellendi.
- **24 Temmuz 2025** düzenlemesi (Resmî Gazete): EV'lerde en düşük ÖTV %10→%25; Togg T10X standart menzil 1.505.000 TL→1.710.226 TL (%11,36 artış); EV matrah eşiği 1.450.000→1.650.000 TL. Etki: vergisel avantajlı B/C segmenti ve 1.6 altı ICE'de ikinci el talebinde hareketlenme beklentisi (arabam.com CEO'su Önder Oğuzhan).

**Etki yönü koşullu:** ÖTV düşüşü → sıfır ucuzlar → ikinci el aşağı çekilir; ancak sıfırda arz sıkıntısı varsa ikinci el yüksek kalır (2021 çift senaryosu). **Frekans:** olay-bazlı (event); kesin tarih Resmî Gazete'den. **Lag:** haftalar (ilan fiyatları günler içinde revize edilir). **Kanıt gücü:** orta (tutarlı sektör gözlemi, hakemli çalışma yok).

**İthalat düzenlemeleri ve idari önlemler.** Ticaret Bakanlığı'nın "6 ay / 6.000 km" düzenlemesi (sıfırın hızla ikinci ele yüksek fiyatla aktarılmasını sınırlar; 2026 ortasına dek uzatıldığı belirtiliyor) ve e-Devlet onaylı "doğrulanmış ilan" sistemi (Nisan 2025) fiyat köpüğü/sahte ilanı hedefler. Ticaret Bakanı Ömer Bolat (2023) ikinci el fiyatlarında %10–15 düşüş bildirdi. **Kaynak:** Resmî Gazete, Ticaret Bakanlığı duyuruları (olay-bazlı). **Kanıt gücü:** zayıf-orta (idari beyan, bağımsız ölçüm sınırlı).

**Hurda teşviki / "İlk Arabam" programı.** Tarihsel olarak 2003 ve 2019'da uygulanmış; 2025–2026'da "İlk Arabam Yerli Otomobil Aile Destek Programı" ve 25 yaş üstü hurda→yerli ÖTV muafiyeti teklifi gündemde ama **Temmuz 2026 itibarıyla yasalaşmamış / Resmî Gazete'de yayımlanmamıştır**. Otomobilde 70.000 TL'ye varan ÖTV indirimi taslakta geçiyor. Yasalaşırsa eski/yüksek yaş segmentinde arzı azaltıp fiyat etkisi yaratabilir; **şu an modellenebilir bir olay değil, izleme değişkenidir.**

> **Projeye Uygulanabilirlik (Bölüm 3):** ÖTV değişiklikleri kesin tarihli dummy/event değişkeni olarak modele girmelidir (Resmî Gazete tarihleri kesin). Bunlar aylık ufka uygundur çünkü geçiş haftalar içinde tamamlanır. Hurda teşviki henüz spekülatif; yasalaşma tarihi bir tetikleyici olarak izlenmeli.

### 4. Arz Yönlü Şoklar ve Yeni Araç Piyasasının Yansıması

**2021–2023 çip krizi.** Türkiye'de Oyak Renault (15–22 Mart 2021), Toyota, Ford Otosan üretime ara verdi. Sıfır araç kıtlığı talebi ikinci ele kaydırdı; ikinci el ilan fiyatları "bir haftada %10" arttı, 24 saatte ~45.000 ilan fiyatı değişti (Hürriyet/Cardata). MASFED matrah indirimine rağmen "bayilerde araç yok → ikinci ele yönelme" mekanizmasını doğruladı. Karşılaştırma (aktarılabilirlik sınırı: **ABD toptan/perakende verisidir, Türkiye ilan-tabanlı perakende piyasa için doğrulanmamıştır**): Cleveland Fed Economic Commentary 2021-17'ye (Krolikowski & Naggert, 8 Temmuz 2021) göre ABD kullanılmış araç TÜFE'si Mayıs 2021'e kadar 12 ayda neredeyse %30 arttı ve toplam aylık TÜFE artışının yaklaşık üçte birini oluşturdu; bazı perakende ölçümlerinde tepe noktasında ~%45.

**2025–2026 tersine dönüş.** Arz normalleşti; şimdi sıfır araç **kampanyaları/agresif fiyatlama** ikinci eli baskılıyor. arabam.com Haziran 2026: sıfır kampanyaları özellikle 0–5 yaş ikinci el talebini yavaşlattı, bazı sıfır araçlar liste fiyatı altında satışa sunuldu. Bu, arz değişkeninin **rejime bağlı çift yönlü** olduğunu gösterir: kıtlık → prim yukarı; kampanya/bolluk → ikinci el aşağı. (ABD tarafında karşılaştırma: Cox Automotive'e göre MUVVI 2025'i yıllık +%0,4 ile, uzun dönem ortalaması %2,3'ün belirgin altında kapattı — kriz sonrası normalleşmenin toptan piyasada da sürdüğünü gösterir.)

**Gözlemlenebilir göstergeler:** ODMD aylık sıfır otomobil + hafif ticari satışları; OSD üretim/ihracat; TÜİK trafiğe kayıt (aylık). Teslimat süreleri kamuya açık sistematik seri olarak **mevcut değil** (anekdotsal: "sıfırda bekleme 6 aya çıktı").

> **Projeye Uygulanabilirlik (Bölüm 4):** ODMD sıfır araç satışı ve TÜİK trafiğe kayıt aylık ve ücretsizdir; "sıfır/ikinci el satış oranı" bir arz-baskısı proxy'si olarak kullanılabilir (2021: 1 sıfıra ~11 ikinci el). Sıfır araç kampanya yoğunluğu için sistematik kamuya açık seri yoktur — bu bir ölçüm boşluğudur. Arz değişkeninin etki yönü rejime bağlı olduğundan sabit katsayı varsayımı hatalı olabilir.

### 5. Talep Yönlü ve Yapısal Faktörler (mevsimsellik, EV geçişi)

**Mevsimsellik.** Sektör anlatısı güçlü: Şubat–Mart canlı, yaz başı (tatil/bayram) hareketli, Ekim–Aralık ikinci dalga, rent-a-car filo yenileme (Erol Şahin, sektör). Ancak nicel doğrulama zayıf: 2026'da beklenen yaz canlanması gerçekleşmedi (arabam.com "yaprak kımıldamıyor"; Temmuz ilk hafta durgun). Bayram tarihleri hicri takvimle kaydığından takvim etkisi yıldan yıla değişir. **Kanıt gücü:** zayıf-orta (anlatı güçlü, nicel doğrulanmamış; mevsimsel düzeltilmiş Türkiye serisi kamuya açık değil).

**Model yılı geçişleri.** BETAM verisi model yılı grubuna göre fiyat kırılımı verir; en yeni model yılı araçların fiyatı yıl sonu/yeni model gelişiyle tipik olarak düzeltilir (ör. Kasım 2024: en yeni 2023 model aya göre -%2). Yılbaşı model yılı geçişi öngörülebilir bir takvim etkisidir. **Kanıt gücü:** orta.

**EV geçişi ve değer kaybı.** TÜİK Ocak–Mayıs 2026: trafiğe kaydı yapılan otomobillerde hibrit %32,2, elektrikli %18,4 — sıfır tarafında EV payı hızla artıyor; ancak ikinci el havuzunda EV hâlâ dar (arabam.com Haziran 2026: elektrikli %1,6, hibrit %2,4 ilan payı). Uluslararası EV değer kaybı literatürü (aktarılabilirlik sınırı: **ağırlıkla ABD/AB perakende ve lease piyasası; Türkiye için doğrulanmamıştır**):
- Cox Automotive EU (2025 sonu): EV 3 yılda %38–42, benzin %35–40 değer kaybı — makasın kapandığı yönünde.
- iSeeCars (Karl Brauer, CNBC 20 Ekim 2025): EV'ler beş yıllık dönemde genel piyasadan yaklaşık 13 puan daha fazla değer kaybeder; ana sebeplerden biri EV'lerin benzinli araçların yaklaşık iki katı teşvik/sübvansiyon almış olması ve menzil teknolojisinin hızlı ilerlemesiyle eski modellerin çabuk eskimesidir.
- MDPI (2024/2025): lease dönüşü EV'lerin 2027'de ortalama %53 değer koruması beklentisi (2023'te %41'den iyileşme).
- Ana belirleyiciler: batarya sağlığı/garanti, menzil, teknolojik eskime, sıfır araç sübvansiyon/kampanyası.

**TOGG (Türkiye'ye özgü) — çelişkili:** Bazı kaynaklar ikinci el TOGG'un sıfıra çok yakın fiyatla satıldığını, "değer kaybı yaşamadığını" söylüyor (Yeni Şafak, Aksam); ikinci el ilan/sıfır farkı bazı versiyonlarda ~44.000–311.000 TL. Diğer kaynaklar sıfır faizli kampanyaların (700.000–800.000 TL sıfır faiz) ikinci el TOGG'u sattırmadığını, likidite sorunu yarattığını belirtiyor. **Bu iki anlatı çelişkilidir ve Türkiye EV ikinci el değer kaybı literatürde net değildir.**

> **Projeye Uygulanabilirlik (Bölüm 5):** Mevsimsellik için takvim/ay-dummy değişkenleri eklenebilir ama Türkiye'de mevsimsel örüntü zayıf/istikrarsız olduğundan güçlü prior verilmemeli. EV segmenti ayrı modellenmelidir: ikinci el EV havuzu hâlâ ince (istatistiksel güç düşük) ve fiyat dinamiği sıfır EV kampanyası + ÖTV rejimine aşırı duyarlı. TOGG özelinde kamuya açık, tutarlı bir değer-kaybı serisi yoktur.

### 6. Piyasa Mikro Yapısı (ilan vs işlem fiyatı, days-on-market, stok)

**İlan vs gerçekleşen işlem fiyatı (pazarlık payı).** Her iki Türk endeksi de **ilan (asking) fiyatına** dayanır — gerçekleşen işlem fiyatı değil. arabam.com açıkça belirtir: "ilan fiyatı satıcının talep ettiği tutar; gerçekleşen satış pazarlıkla altına inebilir." Ölçülebilir proxy: arabam.com Haziran 2026'da bireysel satıcıların fiyat düşürme oranının kurumsallardan %17,08 puan yüksek olduğunu raporlar (bireysel likidite arayışı vs kurumsal maliyet direnci). Gerçekleşen fiyat için tek kamuya açık kaynak noter devir verisidir ama **fiyat içermez, yalnızca adet**.

**İlanda kalma süresi (days-on-market).** BETAM "kapatılan ilan yaşı" olarak yayımlar (Haziran 2026: 23,8 gün, aya göre +1,5 gün). Yükselen days-on-market genelde zayıflayan talep/fiyat baskısıyla ilişkilidir. Sektör: fiyatı doğru araç ~33 günde, yanlış fiyatlı araç çok daha geç satılıyor; 2025'te ortalama satış süresi 44–48 güne uzadı (sektör beyanı — BETAM'ın ~20-24 gün rakamıyla farklı, çünkü farklı tanım/havuz).

**Stok/likidite göstergeleri.** BETAM "satılan/satılık ilan oranı" (Haziran 2026: %19,4) ve "talep endeksi" (Haziran 2026 aya göre -%2,8, yıllık -%16,2); satılık ilan sayısı (Mayıs 2026: 904.741). TÜİK noter devir adedi aylık likidite ölçer (2025'te 11M+ devir).

> **Projeye Uygulanabilirlik (Bölüm 6):** BETAM days-on-market, satılan/satılık oranı ve talep endeksi aylık, ücretsizdir ve öncü (leading) talep göstergesi olarak değerlidir. Kritik uyarı: **model, hedef olarak ilan fiyatını mı yoksa işlem fiyatını mı tahmin ettiğine karar vermelidir** — kamuya açık tüm seriler ilan fiyatıdır; gerçekleşen işlem fiyatı kamuya açık değildir. Bireysel/kurumsal indirim farkı segment değişkeni olarak faydalıdır.

### 7. Mevcut Fiyat Endeksleri ve Ölçüm Metodolojileri

**BETAM sahibindex Otomobil Piyasası Görünümü.** Yayıncı: Bahçeşehir Üniversitesi Ekonomik ve Toplumsal Araştırmalar Merkezi. Veri: sahibinden.com havuzu. Frekans: aylık (Aralık 2023'ten beri). Metrikler: ortalama cari fiyat, reel fiyat (enflasyondan arındırılmış), araç sınıfı/model yılı/yakıt kırılımı, talep endeksi, satılan/satılık oranı, ilanda kalma süresi. **Metodolojik sınır:** kamuya açık metinlerde ortalamanın basit aritmetik mi yoksa karma (mix)/hedonik düzeltmeli mi olduğu **belgelenmemiştir**; ayrıntı indirilemeyen .docx eklerinde olabilir. Talep endeksinin formülü de kamuya açık değildir. Erişim: kamuya açık-ücretsiz.

**arabam.com Aylık Fiyat Endeksi.** İlan fiyatı bazlı ortalama (Haziran 2026: 914.918 TL). Reel fiyat da hesaplanır. Marka/model/yakıt/fiyat bandı/yaş kırılımı verir. **Metodolojik sınır:** karma/kilometre düzeltmesi basın bültenlerinde belirtilmez — ham ilan ortalaması izlenimi verir (kesin doğrulanamadı). Not: arabam.com'un ayrı "Arabam Kaç Para?" bireysel değerleme aracı aykırı-değer temizliği yapar ("gerçekçi olmayan çok yüksek ve çok düşük bedelli olanları hesaplama dışında tutar"), ama bu endeks metodolojisi değildir. Erişim: kamuya açık-ücretsiz (basın bültenleri).

**VavaCars VavaAI Fiyat Endeksi.** Kamuya açık verilerin AI ile analizi; aylık nominal/reel değişim + segment (A/B/C/D) kırılımı. Metodoloji ayrıntısı kamuya açık değildir. Erişim: kamuya açık-ücretsiz (basın bültenleri).

**Diğer:** Otoendeks, sahibinden Oto360 değerleme, Türkiye Sigortalar Birliği (TSB) Kasko Değer Listesi — kasko değeri, taşıt kredisi kredilendirmesinin de tabanı olduğu için önemli bir referans fiyat kaynağıdır.

**Uluslararası metodoloji referansı — Manheim Used Vehicle Value Index (Cox Automotive).** ABD toptan (wholesale) müzayede işlemleri; yılda 5 milyondan fazla işlem; J.D. Power'ın 20 pazar sınıfı. **Karma (mix), kilometre ve mevsimsellik düzeltmeli.** Aykırı değerler fiyat ve kilometrede 2,6 standart sapma dışında elenir. Kilometre düzeltmesi: her pazar sınıfı için cari ay fiyat-kilometre basit doğrusal regresyonu; kullanılan kilometre farkı = cari ay ortalama km − son 24 ay ortalama km. Ağırlıklandırma: son 24 ay satışlarının hareketli ortalaması. Mevsimsel düzeltme: Census X-13. Yayın: genellikle takip eden ayın 5. iş günü; Ocak 1997=100 (Ocak 2023'te yeniden bazlandı; Mart 2026'da endekste EV ağırlığı rekor %3,9'a çıktı). **Aktarılabilirlik sınırı: Bu ABD toptan müzayede verisidir; Türkiye'nin ilan-tabanlı perakende piyasası için doğrulanmamıştır — ama metodolojik şablon (karma+km+mevsimsel düzeltme + aykırı değer eleme) Türkiye'de eksik olan kalite kontrolünü gösterir.**

**Akademik hedonik referans — Türkiye.** Erdem & Şentürk (2009, International Journal of Economic Perspectives, 3(2):141–149): 1.074 araçlık veri setiyle Türkiye ikinci el fiyatının hedonik analizi (semi-log, log-linear, Box-Cox). **Fiyatı pozitif etkileyen:** dizel motor, siyah/gri renk, otomatik şanzıman, sunroof, menşe (Japonya/Almanya/Kore/ABD), üretim yılı, motor silindiri. **Negatif:** yetkili servis sayısı, İstanbul'da satış. Bu, hedonik değişken setinin Türkiye'de anlamlı olduğunu kanıtlar (ama tek çalışma, eski veri).

> **Projeye Uygulanabilirlik (Bölüm 7):** Türkiye'de aylık, kamuya açık, kalite-düzeltmeli bir "Manheim eşdeğeri" YOKTUR. Mevcut endeksler ham/segment-kırılımlı ilan ortalamalarıdır ve kompozisyon kaymasına açıktır (ör. pahalı segmentin havuzda payı artınca ortalama şişer). Model, dış endeksi doğrulama/çapa olarak kullanabilir ama kompozisyon düzeltmesini kendi içinde (hedonik/mix) yapmalıdır. Erdem & Şentürk değişken seti hedonik kontrol için başlangıç noktasıdır.

### 8. SÜRÜCÜ DEĞİŞKEN HARİTASI

| Sürücü | Gözlemlenebilir Gösterge | Kaynak | Frekans | Beklenen Lag | Etki Yönü | Ampirik Kanıt Gücü | Erişilebilirlik | Araç Piyasasına Notlar |
|---|---|---|---|---|---|---|---|---|
| Döviz kuru | USD/TRY, EUR/TRY nominal kur | TCMB EVDS | Günlük/Aylık | Günler–haftalar (kısa) | (+) TL fiyatı | Güçlü (teori); Orta (ikinci el özelinde) | Kamuya açık-ücretsiz | En baskın sürücü; ithal araç+parça+sıfır çapa kanalı |
| Enflasyon (TÜFE) | Aylık/yıllık TÜFE | TÜİK | Aylık (ayın 3'ü) | Eşzamanlı-kısa | (+) nominal; deflatör | Orta-güçlü | Kamuya açık-ücretsiz | Nominal/reel ayrımı zorunlu; 2026'da ikinci el reel gerileme |
| Üretici fiyatları (ÜFE) | Aylık ÜFE | TÜİK | Aylık | Kısa | (+) maliyet | Orta | Kamuya açık-ücretsiz | Yedek parça/onarım maliyeti kanalı |
| Taşıt kredisi faizi | Taşıt kredisi ağırlıklı ort. faiz | TCMB EVDS | Haftalık/Aylık | 1–3 ay (talep kanalı) | (−) talep→fiyat | Orta (Türkiye ikinci el için nicelleşmemiş) | Kamuya açık-ücretsiz | BDDK vade/kredilendirme dilimleri yapısal kısıt |
| Hanehalkı satın alma gücü | Tüketici güven endeksi, reel ücret | TÜİK/TCMB | Aylık | 1–3 ay | (−) düşükse talep zayıf | Zayıf-orta | Kamuya açık-ücretsiz | "Fiyat hassasiyeti/seçici talep" anlatısı |
| ÖTV matrah/oran | Resmî Gazete karar tarihi (event dummy) | Resmî Gazete | Olay-bazlı | Haftalar | Koşullu (±) | Orta | Kamuya açık-ücretsiz | 12.08.2021 → −%10; 24.07.2025 EV %10→%25 |
| İdari önlemler | 6ay/6binkm, doğrulanmış ilan tarihleri | Ticaret Bakanlığı/Resmî Gazete | Olay-bazlı | Haftalar-aylar | (−) köpük azaltıcı | Zayıf-orta | Kamuya açık-ücretsiz | Fiyat köpüğü/spekülasyon sınırlama |
| Hurda teşviki | Yasa/karar tarihi (henüz yok) | Resmî Gazete | Olay-bazlı | Belirsiz | (−) eski segment arzı (potansiyel) | Zayıf (henüz yasalaşmadı) | Kamuya açık-ücretsiz | İzleme değişkeni; 2026 itibarıyla spekülatif |
| Sıfır araç arzı | ODMD sıfır otomobil+HTA satışı | ODMD | Aylık | 1–2 ay | Rejime bağlı (±) | Orta | Kamuya açık-ücretsiz | Kıtlık→prim yukarı; kampanya→aşağı |
| Sıfır/ikinci el satış oranı | ODMD + TÜİK devir | ODMD/TÜİK | Aylık | 1–2 ay | Arz baskısı proxy | Orta | Kamuya açık-ücretsiz | 2021: 1 sıfıra ~11 ikinci el |
| Sıfır araç kampanya yoğunluğu | Sistematik kamuya açık seri YOK | — | — | Haftalar | (−) ikinci el | Zayıf (anekdot) | Erişilemez (sistematik) | 2026'da 0–5 yaş ikinci eli baskılıyor |
| Üretim/ithalat hacmi | OSD üretim; TÜİK trafiğe kayıt | OSD/TÜİK | Aylık | 1–3 ay | Arz kanalı | Orta | Kamuya açık-ücretsiz | Çip krizi üretim durdurma etkisi |
| İşlem hacmi/likidite | Noter devir adedi | TÜİK | Aylık | Eşzamanlı | Likidite göstergesi | Güçlü (idari kayıt) | Kamuya açık-ücretsiz | 2025'te 11M+ devir; fiyat içermez |
| İlanda kalma süresi | Kapatılan ilan yaşı (gün) | BETAM/sahibindex | Aylık | Öncü (leading) | Uzarsa (−) baskı | Orta | Kamuya açık-ücretsiz | Haziran 2026: 23,8 gün |
| Satılan/satılık oranı | Talep endeksi + oran | BETAM/sahibindex | Aylık | Öncü | Düşerse (−) | Orta | Kamuya açık-ücretsiz | Haziran 2026: %19,4 |
| İlan vs işlem farkı | Bireysel/kurumsal indirim oranı | arabam.com | Aylık | Eşzamanlı | Pazarlık payı | Zayıf-orta | Kamuya açık-ücretsiz | Haz 2026: bireysel %17,08 puan daha fazla indirim |
| Mevsimsellik | Ay/takvim (bayram kayması) | Takvim | Aylık | Takvim-eşzamanlı | Belirsiz (±) | Zayıf (nicel doğrulanmamış) | Kamuya açık-ücretsiz | 2026 yaz canlanması gerçekleşmedi |
| Model yılı geçişi | Model yılı grubu fiyatı | BETAM | Aylık/Yıllık | Yıl sonu | (−) en yeni model yılı | Orta | Kamuya açık-ücretsiz | Yeni model yılı gelince eski düzeltilir |
| EV geçişi (segment payı) | Yakıt türü ilan/kayıt payı | TÜİK/arabam.com | Aylık | Yapısal (yavaş) | Belirsiz (±) | Zayıf-orta | Kamuya açık-ücretsiz | İkinci el EV havuzu hâlâ ince (%1,6 ilan payı) |
| EV değer kaybı | Sıfır-ikinci el fiyat farkı (EV) | Sektör/uluslararası | Aylık | — | Türkiye'de net değil | Zayıf (çelişkili) | Kamuya açık-ücretsiz | TOGG için çelişkili anlatı |
| Yakıt fiyatı | Akaryakıt fiyatı | EPDK/piyasa | Günlük/Aylık | 1–2 ay | LPG/EV tercihine (±) | Zayıf-orta | Kamuya açık-ücretsiz | LPG ilan payı Haz 2026 +1,8 puan →%19,7 |

### 9. Açık Sorular / Literatürde Net Olmayanlar

- **Kur geçişkenliğinin ikinci el özelinde nicel lag'i ve büyüklüğü** hakemli çalışmayla ölçülmemiştir (genel TÜFE geçişkenliği ölçülmüştür; ikinci el araç alt-kalemi ayrıştırılmamıştır).
- **Taşıt kredisi faizi → ikinci el talep → fiyat lag'i** Türkiye için nicelleştirilmemiştir.
- **Türk endekslerinin (BETAM, arabam.com) kompozisyon düzeltmesi yapıp yapmadığı** kamuya açık dokümanlardan kesin doğrulanamamıştır — büyük olasılıkla ham/segment ortalamasıdır.
- **Mevsimsellik** sektör anlatısında güçlü ama nicel ve istikrarlı bir örüntü kamuya açık veriyle doğrulanmamıştır (bayram takvimi kayması komplikasyon yaratır).
- **Türkiye'de EV/TOGG ikinci el değer kaybı** literatürde net değildir; anekdotsal kaynaklar çelişkilidir.
- **Sıfır araç kampanya yoğunluğu** için sistematik, kamuya açık, aylık bir seri yoktur (önemli ölçüm boşluğu).
- **Teslimat/bekleme süreleri** kamuya açık sistematik seri olarak mevcut değildir.

## Recommendations

**Aşama 1 (temel model — hemen):** Baz değişken setini kur (USD/TRY, TCMB EVDS), TÜFE (TÜİK), taşıt kredisi faizi (TCMB EVDS), ODMD sıfır araç satışı ve TÜİK noter devir adedi ile kurun. Bunların hepsi aylık, ücretsiz, uzun geçmişli ve aylık ufka uygundur. Kuru en yüksek öncelikli değişken olarak alın; nominal ve reel hedefi ayrı ayrı test edin.

**Aşama 2 (politika + mikro yapı):** ÖTV değişikliklerini kesin Resmî Gazete tarihleriyle event/dummy değişkeni olarak ekleyin (12.08.2021, 24.11.2022, 24.07.2025). BETAM days-on-market, satılan/satılık oranı ve talep endeksini öncü talep göstergesi olarak dahil edin. arabam.com bireysel/kurumsal indirim farkını segment değişkeni olarak deneyin.

**Aşama 3 (segment ayrıştırma):** EV/hibrit segmentini ayrı modelleyin (havuz ince olduğundan ayrı belirsizlik bandı). Erdem & Şentürk (2009) hedonik değişken setini (yakıt, vites, renk, menşe, yaş, motor) kompozisyon kontrolü için kullanın — çünkü kamuya açık endeksler mix-düzeltmesiz.

**Eşik/tetikleyiciler (kararı değiştirecek benchmarklar):**
- Hurda teşviki Resmî Gazete'de yayımlanırsa → eski segment arz şoku değişkenini aktive edin.
- Sıfır araç kampanya yoğunluğu için kamuya açık sistematik seri yayımlanırsa (ör. ODMD/OYDER) → çift yönlü arz değişkenini güçlendirin.
- İkinci el EV ilan payı %5'i geçerse → EV segment modelinin istatistiksel gücü anlamlı hale gelir, ayrı model önceliklendirilebilir.
- Kur aylık %5'i aşan tek yönlü hareket yaparsa → geçişkenlik doğrusal olmayabilir (Yılmaz & Yücel 2021: geçişkenlik depresiasyon büyüklüğüne bağlı); doğrusal-olmayan spesifikasyon test edin.

## Caveats

- **Tüm kamuya açık Türk fiyat serileri ilan (asking) fiyatıdır**, gerçekleşen işlem fiyatı değil. Noter devir verisi adet içerir, fiyat içermez. Model hedefinin ilan mı işlem fiyatı mı olduğu net tanımlanmalıdır.
- **Türk endeksleri kalite/karma düzeltmeli değildir** (kesin doğrulanamadı ama muhtemel); kompozisyon kayması sistematik yanlılık yaratabilir. Manheim tarzı metodoloji Türkiye'de mevcut değildir.
- **Uluslararası bulgular (Manheim, ABD/AB EV değer kaybı, ABD çip krizi fiyat artışları) toptan/farklı piyasa yapısına aittir**; Türkiye'nin ilan-tabanlı perakende piyasası için doğrulanmamıştır ve doğrudan katsayı olarak kullanılmamalıdır.
- **Sektör beyanları (CEO/dernek başkanı açıklamaları) hakemli kanıt değildir**; yön göstergesi olarak kullanılmış, kesin büyüklük olarak alınmamıştır.
- **Arz değişkeninin etki yönü rejime bağlıdır** (kıtlık vs kampanya); sabit katsayı varsayımı dönem geçişlerinde hatalı olabilir.
- **Hurda teşviki ve "İlk Arabam" programı Temmuz 2026 itibarıyla yasalaşmamıştır**; gelecek zamanlı/spekülatif haberler olgu olarak sunulmamıştır.
- **Bazı sektör rakamları kaynaklar arası tutarsızdır** (ör. ortalama satış süresi BETAM ~20-24 gün vs sektör 44-48 gün — farklı tanım/havuz); bu tutarsızlıklar işaretlenmiştir.

## Kaynakça

- **TCMB — Kara & Öğünç, "Exchange Rate Pass-Through in Turkey: It is Slow, but is it Really Low?" (Working Paper 0510, 2005).** Türkiye kur geçişkenliği teorisinin temel hakemli referansı; otomobil ithal malı kanalını açıklar.
- **TCMB Blog, "Exchange Rate Pass-Through: Is There a Magical Number?"** 1 yıllık kümülatif geçişkenliği ~%15 verir; otomobili doğrudan ithal tüketim malı sayar.
- **Pierros, Rodousakis & Soklis (2024), "Exchange-rate pass-through in Turkey with a supply and use model", Applied Economics Letters 31(1):24–30.** Genel fiyat düzeyine geçişkenliği 0,61 birim bulur (sektörel).
- **Yılmaz & Yücel (2021), "Exchange Rate Pass-Through to Consumer Prices in Turkey: Nonparametric Kernel Estimation Evidence" (MPRA 105895).** Geçişkenliğin depresiasyon büyüklüğüne bağlı (doğrusal olmayan) olduğunu gösterir.
- **BETAM (Bahçeşehir Üni.), "sahibindex Otomobil Piyasası Görünümü" (aylık, Aralık 2023–).** Türkiye'nin aylık kamuya açık ikinci el gösterge seti; fiyat, reel fiyat, talep endeksi, days-on-market.
- **arabam.com "Aylık Fiyat Endeksi" (basın bültenleri, AA/Motor1).** İlan fiyatı bazlı aylık ortalama; bireysel/kurumsal indirim farkı.
- **VavaCars "VavaAI Fiyat Endeksi" (basın bültenleri, AA/Hürriyet).** Kamuya açık veri + AI; dolar korelasyonu vurgusu; segment kırılımı.
- **Cox Automotive / Manheim, "Summary Methodology for Manheim Used Vehicle Value Index" ve aylık bültenler.** Karma+kilometre+mevsimsel düzeltmeli, aykırı değer elemeli toptan endeks metodolojisi — Türkiye'de eşdeğeri olmayan ölçüm şablonu.
- **Erdem & Şentürk (2009), "A Hedonic Analysis of Used Car Prices in Turkey", International Journal of Economic Perspectives 3(2):141–149.** Türkiye ikinci el hedonik değişken seti (1.074 araç).
- **Cleveland Fed Economic Commentary 2021-17 — Krolikowski & Naggert (2021), "Semiconductor Shortages and Vehicle Production and Prices".** ABD kullanılmış araç TÜFE'si Mayıs 2021'e kadar neredeyse %30 arttı, aylık TÜFE artışının ~1/3'ü — çip krizi mekanizması karşılaştırması.
- **Cox Automotive EU (2025), "EV vs. ICE: Depreciation and residual values explained".** EV 3 yılda %38–42 vs benzin %35–40; makas kapanıyor.
- **iSeeCars / Karl Brauer (CNBC, 20 Ekim 2025).** EV'ler 5 yılda genel piyasadan ~13 puan fazla değer kaybı; teşvik ve menzil eskimesi ana sebep.
- **MDPI (2024/2025), "The Second-Hand Market in the Electric Vehicle Transition".** EV değer kaybı belirleyicileri (batarya, sübvansiyon, teknolojik eskime).
- **TÜİK "Motorlu Kara Taşıtları" (aylık).** Trafiğe kayıt, devir adedi, yakıt türü dağılımı — arz/likidite göstergesi.
- **ODMD "Otomobil ve Hafif Ticari Araç Pazarı" ve "İkinci El Online Sektör Raporu".** Sıfır araç satış verisi (aylık).
- **NTV/Hürriyet (2021–2022), çip krizi ve ÖTV sektör röportajları (MASFED, Cardata).** 12.08.2021 sonrası ~%10 düşüş; çip krizi ikinci el primi.
- **arabam.com Blog + Teknotalk (Temmuz 2025), ÖTV matrah düzenlemesi.** 24.07.2025 EV %10→%25; Togg T10X fiyat değişimi.
- **Cumhuriyet/Tamindir/Aksam/Karar (2025–2026), TOGG ikinci el.** Çelişkili değer kaybı anlatıları.
- **TCMB EVDS "Kredi Faiz Oranları — Taşıt" metaveri.** Aylık/haftalık ağırlıklı ortalama taşıt kredisi faizi kaynağı.
- **Hesapkurdu/ENUYGUN/BDDK kredilendirme dilimleri.** Taşıt kredisi vade/oran yapısal kısıtları.
- **Hesapkurdu/Allianz/Yeni Şafak (2026), hurda teşviki.** "İlk Arabam" ve hurda teşviki henüz yasalaşmamış durum.

## Kullanılan Nihai Arama Sorguları

- ikinci el araç fiyat endeksi Türkiye
- ÖTV matrah değişikliği ikinci el araç fiyatları
- taşıt kredisi ikinci el otomobil talebi faiz
- sahibindex otomobil metodoloji hedonik BETAM
- çip krizi ikinci el araç fiyat primi 2021 2022 Türkiye
- Manheim Used Vehicle Value Index methodology mix adjustment
- EV depreciation residual value used market study
- exchange rate pass-through automobile prices Turkey
- ODMD ikinci el otomobil pazarı ötelenmiş talep rapor
- TÜİK motorlu kara taşıtları devir istatistikleri aylık
- TOGG ikinci el fiyat değer kaybı satış
- hurda teşviki ÖTV indirimi araç yenileme programı Türkiye
- semiconductor shortage used car prices spike 2021 percent increase
- hedonic regression used car price index methodology
- arabam.com ikinci el otomobil fiyat endeksi rapor aylık
- ikinci el araç piyasası mevsimsellik yaz aylık hareketlilik
- TCMB taşıt kredisi faiz oranı EVDS tüketici kredileri

*Not (arama stratejisi şeffaflığı): Başlangıç sorgu listesinden genişletilen sorgular — "sahibindex ... hedonik BETAM", "TCMB taşıt kredisi faiz oranı EVDS" ve "Manheim ... methodology mix adjustment" — Türkiye kamuya açık endekslerinin metodolojisini ve resmi veri kaynaklarını (TCMB EVDS, TÜİK, BETAM) hedeflemek için eklenmiştir. Tek bir alt-araştırma (subagent) çağrısı, BETAM/arabam.com metodoloji belgelenebilirliği ve Erdem & Şentürk hedonik makale künyesini doğrulamak için kullanılmıştır.*