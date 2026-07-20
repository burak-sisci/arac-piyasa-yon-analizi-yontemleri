---
faz_no: 09
faz_adi: "Sentez ve Karar Dökümanı"
tarih: 2026-07-18
kapsam_ozeti: "Faz 1-8 bulgularının ve karar kaydının (K1-K8, N1-N13) tek karar-odaklı anlatıda birleştirilmesi; yeni tarama içermez"
bagimli_oldugu_fazlar: [01, 02, 03, 04, 05, 06, 07, 08]
durum: taslak
hedef_kaynak_sayisi: 0
gerceklesen_kaynak_sayisi: 0
kaynak_arac: "Claude Code (sentez)"
son_guncelleme: 2026-07-18
---

# Faz 09 — Sentez ve Karar Dökümanı

**Bu dökümanın rolü:** Sekiz tarama fazının bulgularını ve karar kaydındaki bağlayıcı
kararları (K1–K8, N1–N13) tek bir karar-odaklı anlatıda birleştirmek. Bu döküman
fazların yerine geçmez; onları birbirine bağlar. Her bölüm ilgili fazın ana
teslimatını özetler ve detay için o faza işaret eder. Yeni literatür taraması
yapılmamıştır; buradaki her iddia bir faz dökümanına veya karar kaydına dayanır.

**Revizyon notu:** Bu, dökümanın ikinci üretimidir. İlk üretim sırasında
`docs/08_basarisizlik_modlari_tuzaklar.md` repoya henüz eklenmemişti; Bölüm B8 ve
D o zaman yalnızca karar kaydındaki N13 özetine dayanıyordu. Bu sürüm, Faz 8'in
tam metnini (20 maddelik başarısızlık registrisi + 7 kategori + kendi Açık
Sorular bölümü) okuyarak yeniden yazılmıştır.

**Okuma kılavuzu:** Bölüm A yönetici/mentor özetidir (teknik olmayan okuyucu için).
Bölüm B teknik gövdedir (geliştirici ekip için). Bölüm C fazlar arası karar
zincirlerini, Bölüm D bilinen belirsizlikleri, Bölüm E kilit kaynakları toplar.

---

## A. Yönetici / Mentor Özeti

**Proje nedir?** Türkiye ikinci el araç piyasasında, segment düzeyinde (örn.
marka/model/yaş grubu) fiyatların bir sonraki ay **yukarı mı, aşağı mı, yatay mı**
(up/down/stable) hareket edeceğini tahmin edecek bir makine öğrenmesi sistemi için,
geliştirici ekibin "gelmiş geçmiş en iyi baseline" ile işe başlamasını sağlayacak
literatür temelli bilgi tabanı. Sekiz fazlık tarama tamamlandı; tüm bağlayıcı
kararlar `00_karar_kaydi.md` dosyasında numaralı (K/N) maddeler halinde kayıtlıdır.

**Neyi tahmin ediyoruz — ve neden?** Hedef, **ilan fiyatının yönüdür** [K8].
Türkiye'de kamuya açık tüm ikinci el fiyat serileri ilan (asking) fiyatıdır;
gerçekleşen satış fiyatı kamuya açık değildir (noter devir verisi yalnızca adet
içerir). Bu bilinçli ve belgelenmiş bir tasarım tercihidir: ilan fiyatı ile satış
fiyatı arasındaki pazarlık payı sıfır varsayılmaz, ayrıca izlenir (aşağıda "en
kritik risk").

**Literatürdeki yerimiz:** Bu problemin hazır bir reçetesi **yoktur** [N9]. Araç
fiyatı literatürünün neredeyse tamamı "bu özelliklerdeki araç bugün ne eder?"
sorusunu çözer (tek araç, tek an, fiyat seviyesi); "piyasa/segment fiyatı gelecek
ay ne yöne gider?" sorusunu çözen hakemli çalışma bulunamamıştır (Faz 4). Bu
boşluk projenin gerekçesidir: ekip öncü bir baseline kuruyor. Boşluğun iki yüzü
var — hazır şablon yok (risk), ama katkı/yayın fırsatı var.

**Önerilen sistemin özü (tek paragraf):** Ham ilan ortalamaları kompozisyon
kaymasına açık olduğundan (bir ay ucuz araç ilanları artınca ortalama, gerçek
fiyat hareketi olmadan düşer), önce karma-düzeltilmiş bir fiyat serisi kurulur
[N1→N10]; yön etiketi bu temiz seriden, her segmentin kendi oynaklığına
uyarlanmış bantlarla üretilir [K2], tahmin ufku aylıktır [K1]. Girdiler: döviz
kuru başta olmak üzere gecikmeli makro göstergeler, ÖTV değişiklik tarihleri,
ilan piyasası arz-talep göstergeleri [N10]. Model: tüm segmentleri birlikte
öğrenen tek bir gradient boosting sınıflandırıcısı [N11] — bu veri rejiminde
derin öğrenme baseline olarak uygun bulunmamıştır. Tüm deney süreci, veri
sızıntısını ve kendini kandırmayı engelleyen 24 maddelik bir güvenilirlik
protokolüne bağlıdır [N12].

**Başarı neye benziyor?** Mutlak yüksek doğruluk değil [N6]. Literatürdeki "%70+
doğruluk" iddialarının büyük kısmı metodolojik hata (veri sızıntısı) ürünüdür ve
hedef alınmaz (Faz 3). Başarı ölçütü: modelin, iki naif referansı — "geçen ayın
yönü bu ay da sürer" (persistence) ve "her şey yatay" — şansa göre düzeltilmiş
bir metrikte (MCC) istatistiksel güvenle geçmesidir. Geçemiyorsa sonuç "sinyal
yok"tur ve bu, dürüstçe raporlanan **değerli bir negatif bulgudur** — projenin
kabul edilmiş olası sonuçlarından biridir.

**En kritik risk ve sigortası [N13]:** Projenin temel varsayımı, ilan
fiyatlarının yönünün gerçekleşen satış fiyatlarının yönünü izlediğidir [K8+N9].
Faz 8'in kırmızı-takım denetimi bu varsayımı 20 maddelik bir başarısızlık
registrisinin **en tepesine** koyar: konut piyasası literatüründen hakemli kanıt
(Anenberg & Laufer 2017; Anenberg 2016; Han & Strange 2016; Carrillo vd. 2015),
pazarlık payının **dönüm noktalarında sistematik olarak** saptığını gösteriyor —
piyasa yükselirken daralıyor, düşerken genişliyor. Yani sinyal tam da en kritik
anlarda (piyasa yön değiştirirken) yanılabilir. Bu yüzden Faz 8, dolaylı
doğrulama testlerini (ilanda kalma süresi, fiyat indirme oranı, satılan/satılık
oranı panelleri; bağımsız işlem-tabanlı serilerle yön uyumu) **zorunlu** kılar
ve **beş önceden ilan edilmiş terk/yeniden-çerçeveleme eşiği** tanımlar. Bu
eşiklerden biri karşılanırsa proje mevcut haliyle sürdürülmez; hedef ya yeniden
çerçevelenir (örn. doğrudan ilan-davranışı tahmini) ya da "sinyal yok" raporu
yayımlanır.

**Yöneticiye net mesaj:** Bu, "kesin kazanç" vaat eden bir model projesi değil;
başarı ve başarısızlık kriterleri **önceden tanımlanmış**, falsifiye edilebilir,
disiplinli bir deney programıdır. Karar noktaları (devam / yeniden çerçevele /
terk et) baştan bellidir ve veriye bakmadan sabitlenmiştir. Faz 8'in 20 maddelik
registrisi, bu kararların hangi somut erken-uyarı işaretine ve azaltıcı önleme
dayandığını tek tek belgeler (Bölüm B8).

---

## B. Teknik Gövde

### B1. Problem tanımı ve hedef — Faz 1 (+ K1, K2, K8)

Yön etiketlemesinde tek "doğru" yaklaşım yoktur; sınıf sayısı, threshold türü ve
tahmin ufku class balance'ı ve sinyal-gürültü oranını birlikte belirler (Faz 1).
Faz 1'in karar matrisi (Faz 1, Bölüm 7) seçenekleri araç piyasası bağlamında
tartar ve şu kararlara varır:

- **Aylık ufuk** [K1]: günlük/haftalık ufuk ilan verisinde gürültü baskındır;
  aylık ufuk Manheim benzeri endekslerin de yayın frekansıdır. İkincil deney:
  eğitim etiketi için 2–3 aylık proxy ufuk ("Label Horizon Paradox", Song et al.
  2026 — optimal eğitim ufku çıkarım ufkuyla aynı olmayabilir).
- **Oynaklık-uyarlamalı 3-sınıf etiket** [K2]: stable bandı sabit yüzde değil,
  segment bazlı ±0.5σ–1σ taramasıyla belirlenir; neutral oranı %60'ı aşarsa
  quantile/tercile yedeğine geçilir. 3. sınıf (stable) bir abstention/gürültü
  filtresi işlevi görür (Chalkidis & Savani 2021).
- **Hedef: ilan fiyatı yönü** [K8] — Faz 2'nin veri gerçekliği bulgusundan doğan
  kapsam kararı; tüm dökümanlarda terminoloji buna göredir.
- Finansal ML'nin olgun etiketleme araçları (triple-barrier, meta-labeling)
  yol-bağımlı sürekli işlem verisi için tasarlanmıştır; ilan-tabanlı aylık seriye
  doğrudan aktarılamaz, erken evrede kullanılmaz (Faz 1). Trend-scanning ikinci
  görüş/değerlendirme aracı olarak saklanır.

Kritik boşluk [N3]: düşük frekanslı, ilan-tabanlı piyasalar için yön etiketleme
metodolojisinin ampirik doğrulaması literatürde yoktur — etiket tasarımı projeye
özgü deney gerektirir. Detay: `01_problem_cerceveleme_label_tasarimi.md`.

### B2. Veri gerçekliği ve fiyat sürücüleri — Faz 2 (+ N1, N2)

Faz 2'nin sürücü değişken haritası (Faz 2, Bölüm 8) ~20 sürücüyü gösterge,
kaynak, frekans, lag, etki yönü ve kanıt gücüyle listeler. Sentez düzeyinde üç
yapısal bulgu belirleyicidir:

1. **Kur (USD/TRY) en baskın modellenebilir sürücüdür**; TCMB/TÜİK/Resmî Gazete
   kaynakları aylık ufka uygun, ücretsiz ve uzun geçmişlidir. ÖTV değişiklikleri
   kesin tarihli event değişkeni sağlar.
2. **Kamuya açık Türk endeksleri (BETAM sahibindex, arabam.com) karma/hedonik
   düzeltmesizdir** [N1]: ham ilan ortalamaları kompozisyon (mix) kaymasına
   açıktır. Sonuç: kompozisyon düzeltmesi modelin işidir — bu, Faz 5'te reçeteye
   bağlanmıştır (bkz. B5 ve C1 zinciri).
3. **Arz değişkeni rejime bağlı çift yönlüdür** [N2]: sıfır araç kıtlığı ikinci
   el primini yukarı iter (2021–2023), kampanya/bolluk aşağı baskılar
   (2025–2026). Sabit katsayı varsayımı dönem geçişlerinde hatalıdır — bu bulgu
   Faz 5 (etkileşim feature), Faz 6 (model) ve Faz 7 (rejim-ayrık değerlendirme)
   boyunca taşınır (bkz. C4 zinciri).

Faz 2'nin işaretli çelişkileri sentezde de korunur: Türkiye'de EV/TOGG ikinci el
değer kaybı anlatıları çelişkilidir; mevsimsellik sektör anlatısında güçlü ama
nicel doğrulanmamıştır; ortalama satış süresi ölçümleri kaynaklar arası tutarsızdır
(farklı tanım/havuz). Detay: `02_arac_piyasasi_dinamikleri.md`.

### B3. Metodolojik duruş: finansal literatürden ne alındı, ne reddedildi — Faz 3 (+ N4–N8)

Faz 3'ün tezi: finansal yön tahmini literatürünün **pozitif** bulguları (model X
şu doğruluğu aldı) çoğunlukla aktarılamaz; **negatif ve metodolojik** bulguları
yüksek oranda aktarılabilir. Aktarılabilirlik matrisi (Faz 3, Bölüm 8) her bulguyu
tek tek değerlendirir. Karar kaydına geçen beş bağlayıcı sonuç:

- **[N4] SMOTE/resampling kullanılmayacak.** Hakemli kanıt (van den Goorbergh vd.
  2022): imbalance düzeltmeleri kalibrasyonu bozar, AUC'yi iyileştirmez; aynı
  kazanım karar eşiği kaydırılarak elde edilir. Zorunlu sıralama: class weighting
  → threshold-moving → post-hoc kalibrasyon. **İşaretli karşı-bulgu:**
  tree-ensemble bağlamında hasarın küçük ve rekalibrasyonla giderilebilir olduğu
  yönünde çalışma vardır (arXiv 2606.29720); çelişki düzleştirilmemiş, ampirik
  test önerilmiştir.
- **[N5] Birincil metrik MCC + macro-F1; accuracy tanımlayıcı. Rastgele k-fold
  yasak, kronolojik ayrım zorunlu** (Chicco & Jurman 2020; Bergmeir vd. 2018).
- **[N6] Başarı = naif baseline üzeri iyileşme.** Sızıntısız çalışmalarda gerçekçi
  yön doğruluğu %50–58 bandındadır; %70+ iddiaların büyük kısmı leakage ürünüdür
  (Kapoor & Narayanan 2023). "Sinyal yok" geçerli ve değerli bir sonuçtur.
- **[N7] Falsifikasyon audit'i zorunlu:** pipeline null veri üzerinde test edilir;
  denenen model sayısı kaydedilir, çoklu-test farkındalığıyla raporlanır (Harvey
  vd. 2016; Bailey & López de Prado 2014).
- **[N8] Rejim izleme dışsal olay-tabanlıdır:** araç piyasasında drift kaynakları
  gözlemlenebilir (kur şoku, ÖTV = ani; enflasyon = tedrici). Yüksek-frekanslı
  algoritmik drift-detection aylık ufka aktarılamaz; latent rejim (HMM) yerine
  dışsal değişken tabanlı rejim tercih edilir.

Lehte tek teorik argüman: Adaptive Market Hypothesis (Lo 2004) çerçevesinde araç
piyasasının düşük etkinliği öngörülebilirlik ihtimalini artırır — ancak bu bir
garanti değil, test edilecek hipotezdir. Detay: `03_finansal_piyasa_yon_tahmini.md`.

### B4. Literatür boşluğu ve devşirilen çekirdek — Faz 4 (+ N9)

Faz 4'ün boşluk haritası (Faz 4, Bölüm 9) literatür dallarını probleme uzaklığına
göre dizer ve beş bileşeni "literatürde YOK" olarak belgeler — en önemlisi:
kümüle ilan-fiyat endeksinin zaman serisi yön sınıflaması hiçbir hakemli çalışmada
yoktur; en yakın çalışma (Bukvić vd. 2022) dahi kesitsel araç-bazlıdır [N9].

Devşirilen çekirdek (Faz 4 → sonraki fazlara girdi):
- **Prediktif öznitelik seti** (yaş, km, marka/model, motor, yakıt, şanzıman,
  donanım; Türkiye doğrulaması: Erdem & Şentürk 2009, Daştan 2016) → Faz 5'te
  hedonik regresyonun ve segmentlemenin girdisi oldu.
- **Asimetrik maliyet çerçevesi** (residual value dalı; Dress vd. 2018) →
  Faz 6'da sınıf-ağırlıklı/maliyet-matrisli kayba çevrildi (N4 ile uyumlu).
- **Kaggle veri-temizlik pratikleri** (metin parse, kategorik indirgeme, 99p
  kırpma, deduplication) → veri hattı standardı.
- Residual value dalından ayrıca: kronolojik train/test disiplini ve çok-görevli
  öğrenme fikri (yön ana hedef, değişim büyüklüğü yardımcı hedef).

Faz 4 ayrıca projenin **kritik geçerlilik varsayımını** ilk kez formüle etti
[N9+K8]: ilan-fiyat endeksinin yönü, gerçekleşen-fiyat yönünü ancak pazarlık
marjı stabil kaldığı sürece izler. Bu varsayımın riski Faz 8'de hakemli kanıtla
değerlendirilip test tasarımına bağlanmıştır (bkz. B8 ve C2 zinciri).
Detay: `04_arac_fiyat_akademik_literatur.md`.

### B5. Veri hazırlık ve feature reçetesi — Faz 5 (+ N10)

Faz 5, N1 problemini teoriden reçeteye çevirir [N10] ve feature üretim tablosunu
(Faz 5, Bölüm 8: ~18 feature ailesi × türetim × leakage riski × öncelik) teslim
eder. Çekirdek kararlar:

1. **Kompozisyon düzeltmesi (bloke edici ilk adım):** Birincil yöntem aylık
   hedonik imputation — log(P_it) = α_t + Σβ_k·x_k,it + ε_it, x_k = N9 öznitelik
   seti; yön etiketi mix-düzeltilmiş Δα_t'den hesaplanır (log geri-çevirmede bias
   düzeltmesiyle). Doğrulama katmanı: Manheim-tarzı sabit-ağırlık endeksi (24 ay
   yuvarlanan ağırlık + km regresyon düzeltmesi + outlier kırpma); iki serinin
   diverjansı mix kayması teşhisidir. Bonus: hedonik reziduel ε, segment
   ucuz/pahalı sapması feature'ı olur. **Bu yapılmadan üretilen hiçbir etikete
   güvenilmez** (Faz 5, Öneri 1).
2. **Makro lag'ler ampirik seçilir:** kur için 1/3/6/12 ay aday havuzu; CCF +
   pairwise Granger taraması **eğitim-içi** yapılır. Türkiye ERPT kanıtı
   (geçişkenliğin ~%40'ı ilk çeyrekte; çekirdek mal/otomobil daha hızlı) kısa
   lag'leri öncelikli hipotez yapar — veriyle test edilir.
3. **Çift leakage kısıtı tüm feature'larda:** (a) yalnızca-geçmiş (makroda yayım
   gecikmesi lag'e eklenir), (b) fold-dışı hesaplama. Aynı-dönem büyüklükler
   (days-on-market, ilan hacmi) t-1'e çekilir.
4. **High-cardinality kategorikler:** ordered/expanding-mean target encoding
   (CatBoost tarzı) + hiyerarşik backoff; sparse hücreler için shrinkage/empirical
   Bayes.
5. **Teknik göstergeler soyutlama düzeyinde:** momentum ve oynaklık türetilir;
   RSI/MACD hazır parametreleriyle kopyalanmaz (zorlama). Google Trends deneysel
   ve düşük beklentiyle tutulur.

Detay: `05_feature_engineering_alternatif_veri.md`.

### B6. Model kararı — Faz 6 (+ N11)

Faz 6'nın model seçim karar ağacı (Faz 6, Bölüm 8) gözlem sayısı × dengesizlik ×
rejim yoğunluğu eksenlerinde koşullu seçim çerçevesi verir. Bağlayıcı karar [N11]:

- **Birincil baseline:** segment kimliği + dışsal rejim değişkenlerini [N8]
  öznitelik olarak alan, **class-weighted tek global gradient boosting** modeli.
  Küçük segment/az gözlem → CatBoost veya sıkı-düzenlileştirilmiş XGBoost; büyük
  veri → LightGBM. Gerekçe: ağaç-ensemble'ların tablo verisindeki üstünlüğü
  (Grinsztajn vd. 2022; McElfresh vd. 2023) + global/cross-learning'in az-gözlemi
  telafi etmesi (Montero-Manso & Hyndman 2021; M5 dersi).
- **N4 sırası uygulanır**; post-hoc kalibrasyon az-gözlemde **Platt/temperature
  scaling** ile (izotonik regresyon değil — küçük kalibrasyon setinde overfit
  eder; Niculescu-Mizil & Caruana 2005).
- **Deep learning baseline DEĞİLDİR**; saf segment-başı lokal modeller önerilmez.
  İleri denemeler (her biri GBM baseline'ı N6 eşiğiyle geçmek zorunda): Frank &
  Hall (2001) ordinal ayrıştırması (3 sınıfta kazanç garanti değil — literatürde
  net değil), focal loss / ordinal-farkında kuadratik maliyet matrisi (N9
  asimetrik maliyetin uygulaması; reversal > off-by-one cezası), hiyerarşik
  partial-pooling, çok-küçük veride TabPFN.

Detay: `06_model_mimarileri_ensemble.md`.

### B7. Güvenilirlik ve değerlendirme protokolü — Faz 7 (+ N12)

Faz 7'nin 24 maddelik protokol kontrol listesi (Faz 7, Bölüm 9) bağlayıcı
"güvenilirlik sözleşmesi"dir [N12]: bir deney, listenin tamamını geçmeden
"güvenilir" ilan edilemez. Sentez düzeyinde omurga:

- **Validasyon:** genişleyen-pencere walk-forward + 1 ay ufuk + 1–2 ay
  purge/embargo; test dönemi sayısı gözlem bütçesine göre 6–24 ("50–100 fold"
  bu problemde geçersiz). Gözlem eşikleri: N<50 → yalnızca keşifsel/negatif-bulgu
  modu; N≥80 → tam protokol; N≥150 → CPCV opsiyonel.
- **As-of date mimarisi:** tek merkezî bilgi-kesim tarihi; kronoloji [N5] ve
  makro vintage/yayın-gecikmesi (bu problemin en kritik leakage riski) tek
  noktadan garanti edilir. Vintage yoksa pseudo-real-time +1/+2 ay lag.
  Ön-işleme/encoding/feature-selection fold-içinde fit edilir.
- **Metrik:** macro-MCC (Gorodkin R_K; micro-MCC değil) + macro-F1 + per-class
  precision/recall/support; hepsine blok-bootstrap %95 CI (B≥1000, blok ~n^(1/3)).
- **Baseline + anlamlılık [N6'nın somutlaşması]:** dört baseline (persistence,
  mevsimsel-naif, hep-stable, prior-oran); yön anlamlılığı bootstrap-PT
  (asimptotik Pesaran–Timmermann küçük örneklemde over-sized). Fark CI'ı sıfırı
  içeriyorsa → "sinyal yok".
- **Falsifikasyon geçidi [N7'nin somutlaşması] (bloke edici):** blok-permütasyon
  hedef-shuffle null testi (B≥1000, tam pipeline) — null ortalaması ≈ 0 değilse
  DUR, leakage var; ayrıca sentetik-sinyal pozitif kontrolü ve random-walk
  benchmark'ı.
- **Çoklu-test:** deneme günlüğü + denenen N raporu + permütasyon max-istatistik
  / FDR düzeltmesi + MinBTL kontrolü; nested CV yerine katı hiperparametre
  bütçesi + kilitli hold-out.
- **Rejim-farkındalık [N8/N2'nin somutlaşması]:** şok takvimi önceden sabitlenir
  (veriden keşfedilmez); rejim-ayrık MCC (sakin vs şok-sonrası); covariate shift
  ile concept drift ayrıştırılır.

**İşaretli gerilim (düzleştirilmedi):** Bergmeir & Benítez (2012) belirli
koşullarda blocked-CV'yi standart önerir; ancak durağanlık varsayar ve bu
problemde rejim değişimi nedeniyle ihlal edilir → N5 korunur, blocked-CV yalnızca
purge+embargo ile ikincil/yardımcı tahmin olarak kullanılabilir. Ayrıca "deflated
MCC" için standart formül yoktur; permütasyon max-istatistik null'u muadil olarak
kullanılır (literatürde net değil). Detay: `07_validasyon_metrik_backtest.md`.

### B8. Riskler ve terk kriterleri — Faz 8 (+ N13)

Faz 8, yeni metodoloji önermeden önceki yedi fazı **"yapıcı kötümserlik"**
ilkesiyle kırmızı-takım gözüyle denetler (Faz 8, Bölüm 1): amaç projeyi
durdurmak değil, baseline'ın *nerede ve neden* başarısız olacağını önceden
avlamak. Her risk **olasılık × etki** ekseninde derecelendirilir. Ana teslimat,
**20 maddelik Başarısızlık Modu Registrisi'dir** (Faz 8, Bölüm 9), yedi kaynak
kategorisinde toplanır: (1) veri/hedef kaynaklı, (2) etiketleme kaynaklı,
(3) rejim/non-stationarity kaynaklı, (4) model kaynaklı, (5) değerlendirme
kaynaklı, (6) dağıtım/operasyon kaynaklı, (7) yorumlama/karar kaynaklı.

**Kritik varsayım derinlemesine test edildi [N13].** Registrinin #1 maddesi ve
Faz 8'in ana bulgusu, K8+N9 varsayımını (ilan-yönü ↔ işlem-yönü) konut piyasası
literatüründen doğrudan nicel kanıtla riskli ilan eder: satış/ilan fiyat oranı
(sale-to-list ratio) piyasa döngüsüyle korelasyonludur ve fiyat yükselirken
daralır, düşerken genişler (Anenberg & Laufer 2017); satıcılar ilanı bayat
emsallere çapalayıp yapışkan tutar, bu da düşüş döneminde marjı mekanik olarak
büyütür — "crossing pattern" (Anenberg 2016); boom'da liste-altı satış azalır,
liste-üstü/liste-eşiti satış artar (Han & Strange 2016); satıcı pazarlık gücünü
temsil eden bir "tightness" değişkeni dışlandığında RMSE bazı ufuklarda %30–35
kötüleşir (Carrillo vd. 2015). Bu literatür ikinci el araç piyasasına doğrudan
ölçülmemiş ama güçlü bir analojidir.

**Somut test tasarımı [N13'ün detayı, Faz 8 §2.1]:** (a) DOM medyanı +
fiyat-düşürme oranı + satış-dönüşüm (conversion) oranından oluşan bir proxy
paneli aylık izlenir — bu üç seri ilan-yön sinyaliyle **ters** hareket ederse
sapma alarmı verilir; Trojanek vd. (2025) ilan-endekslerinin işlem-endekslerini
1–2 ay önden haber verdiğini ama üçüncü-ay verisinin "forward-looking noise"
eklediğini gösterir, bu yüzden proxy verisi çeyreğin ilk-ikinci ayından
alınmalıdır. (b) Bağımsız işlem-tabanlı kamu serileriyle (TÜİK, BETAM/sahibindex)
periyodik yönsel-uyum (directional agreement) ölçümü — uyum eşiğin altına
düşerse sinyal geçersiz sayılır. (c) Rejim-koşullu tutarlılık testi
(yükseliş/düşüş dilimleri ayrı ayrı). Kalıcı çözüm (Heckman-tipi seçim
düzeltmesi veya sale-to-list oranını durum değişkeni olarak modele katmak)
Faz 4'ün alanı olarak işaretlenmiştir; Faz 8 yalnızca izleme/test tasarımını
dayatır — yeni metodoloji önermez.

**Registrinin diğer kategorileri (tam liste Faz 8 §9'da; burada yalnızca
fazlar-arası bağlantı noktaları özetlenir):**
- *Veri/hedef kaynaklı* (#2–5): seçilim yanlılığı — yalnızca satılan ilanlar
  gözlemlenir, forecast hatası hafife alınır (Heckman 1979; art-auction
  selection literatürü); **kompozisyon (mix) kayması, yani N1'in kendisi**
  — Faz 5'in hedonik düzeltmesi (N10) tasarım-zamanı bir çözümdür, Faz 8 bunu
  runtime'da izlenmesi gereken bir risk olarak yeniden değerlendirir (segment
  PSI kayması + ham-vs-düzeltilmiş seri diverjansı erken-uyarı işaretidir — bkz.
  C1 zinciri); ölü/tekrarlı ilanlar (duplicate-leakage, Kapoor & Narayanan
  taksonomisi); ilan-içi fiyat-düşürme davranışının hedefi kirletmesi (Merlo &
  Ortalo-Magné 2004).
- *Etiketleme kaynaklı* (#7–8): "stable" bandının anlamsızlaşması (çok geniş →
  çoğunluk sınıfı, çok dar → gürültü) ve threshold/ufuk keyfîliği — ikisi de N3
  boşluğunun somut sonucudur, "literatürde net değil" işaretlidir; K2'nin
  oynaklık-uyarlamalı bant kararı tam da bu riski azaltmak için seçilmiştir.
- *Rejim/non-stationarity kaynaklı* (#9–11): **kur/ÖTV/arz şoklarında çöküş**
  — N2'nin somutlaşması; Hendry'nin forecast-failure literatürü "location
  shift"leri sistematik başarısızlığın başlıca kaynağı sayar, 24 Temmuz 2025
  ÖTV düzenlemesi (7555 sayılı değişiklik) somut/güncel örnektir; eğitim
  döneminin gelecek rejimi temsil etmemesi ("Who Saw It Coming?" 2026 —
  nadir-ama-önemli rejimleri az-ağırlıklayan örneklem normal-rejim
  parametrelerine yakınsar); sessiz/saf konsept kayması — **denetimsiz
  proxy'lerle (PSI vb.) hiç yakalanamaz**, yalnızca periyodik etiketli denetim
  + champion/challenger mimarisi yakalar.
- *Model kaynaklı* (#12–14): az-gözlemde overfitting (N11'in "basit/düzenlileş-
  tirilmiş model" tercihini destekler); yanlış kalibrasyon (N11'in
  Platt/temperature kararının runtime karşılığı); ordinal yapının ihmali
  (N11'in ordinal-ileri-deneme önerisiyle aynı eksen — bkz. C3 zinciri).
- *Değerlendirme kaynaklı* (#4, #6, #17 + destek maddeler): **gizli leakage**
  ve **naif baseline'ı yenememenin gizlenmesi** iki yüksek×yüksek maddedir;
  ayrıca çoklu-test şişmesi ve güven-aralıksız raporlama — dördü de N7/N12'nin
  protokolüyle doğrudan örtüşür (bkz. C3 zinciri).
- *Dağıtım/operasyon kaynaklı* (#15–16 + bakım maddesi): vintage/real-time
  revizyon — N12'nin as-of-date kuralının **canlı ortamdaki** karşılığı
  (Croushore & Stark; Koenig vd. 2003); training-serving skew (feature'ın
  tahmin anında mevcut olmaması); izlenmeyen drift/bakım ihmali.
- *Yorumlama/karar kaynaklı* (#17–18): istatistiksel sinyalin ekonomik/karar
  faydasına çevrilememesi (işlem maliyeti sonrası edge kaybolabilir — MPANF
  2024); agrega (piyasa-geneli) sinyalin yanlış biçimde birim-düzey bir karara
  bağlanması — ikisi de "literatürde net değil" veya proje-özgü karar
  bağlamına dayanır.

**Beş yüksek×yüksek risk (registri #1, #4, #5, #6, #9 — Faz 8'de kalın
işaretli satırlar):** (1) K8 ilan-yönü sapması, (4) gizli leakage, (5) naif
baseline'ı yenememenin gizlenmesi, (6) çoklu-test şişmesi, (9) kur/ÖTV/arz
şokunda rejim çöküşü. Bu beşi, projenin en fazla dikkat/kaynak ayırması
gereken noktalardır; geri kalan 15 madde orta önceliklidir ama registriden
çıkarılmamıştır (Faz 8, Bölüm 9'daki tam tabloya bakınız).

**Beş önceden-ilan-edilen terk/yeniden-çerçeveleme eşiği (bağlayıcı — Faz 8
§10 = N13):**
1. Model, dokunulmamış holdout'ta iki naif baseline'ı (persistence + çoğunluk)
   güven aralığı örtüşmeden yenemiyorsa → sinyal yok.
2. İlan-yön sinyalinin işlem serisiyle yönsel uyumu şans üstü değilse veya
   rejimler arası kararsızsa → hedef geçersiz; yeniden çerçevele.
3. Performans yalnızca tek rejimde pozitifse → genellenebilir sinyal yok.
4. İstatistiksel edge, işlem maliyeti/karar frictions altında pozitif fayda
   üretmiyorsa → karar-faydası yok.
5. Leakage düzeltmesi sonrası performans naif seviyeye düşüyorsa → önceki
   sonuçlar artefakttı; terk.

Faz 8, bu beş eşiğin "iyimserlik değil dürüstlük gereği" olduğunu vurgular:
negatif sonucun gizlenmesi (publication/positive-outcome bias) bilimsel ve
operasyonel bir hatadır ("Embracing Negative Results in Machine Learning",
ICML 2024).

**Yeniden-çerçeveleme seçeneği:** hedefi işlem-vekili olmaktan çıkarıp doğrudan
ilan-davranışı (DOM / fiyat-düşürme) tahminine kaydırmak; veya "sinyal yok"u
dürüst negatif-sonuç raporu olarak yayımlamak [N6 ile tutarlı]. Detay ve tam
20 maddelik registri: `08_basarisizlik_modlari_tuzaklar.md`.

---

## C. Fazlar Arası Karar Zincirleri (sentezin katma değeri)

Aşağıdaki dört zincir, fazların birbirinden bağımsız dökümanlar değil, tek bir
karar sisteminin parçaları olduğunu gösterir.

**C1. Kompozisyon zinciri: N1 (Faz 2) → N10 (Faz 5) → Faz 8 §2.2 (runtime izleme).**
Faz 2, kamuya açık endekslerin mix-düzeltmesiz olduğunu teşhis etti (problem).
Faz 5 bunu reçeteye bağladı: hedonik imputation birincil, sabit-ağırlık endeksi
doğrulama, reziduel bonus feature (tasarım-zamanı çözüm). Faz 8 bu zincire üçüncü
bir halka ekler: hedonik düzeltme kurulduktan sonra bile kompozisyon kayması bir
**runtime riski** olarak registriye (#3) girer — segment/yaş/km dağılımındaki PSI
kayması ve ham-vs-düzeltilmiş seri diverjansı erken-uyarı işaretidir. Yani "N1
çözüldü" statik bir gerçek değil, sürekli izlenmesi gereken bir taahhüttür.
Zincirin ucu Faz 7'nin falsifikasyon geçidine de bağlanır: etiket sahte sinyal
taşıyorsa null testi bunu yakalamalıdır.

**C2. Varsayım zinciri: K8 (Faz 2) → N9 (Faz 4) → N13 (Faz 8).**
Faz 2 veri gerçekliği nedeniyle hedefi ilan fiyatı olarak sabitledi. Faz 4 bunun
örtük varsayımını formüle etti (ilan-yönü ↔ işlem-yönü) ve literatürde
ölçülmediğini belgeledi. Faz 8 bu varsayımı emlak literatürünün hakemli
kanıtıyla "yüksek olasılık × yüksek etki" olarak derecelendirdi (registri #1),
somut bir üç parçalı dolaylı test paketi (proxy panel + yönsel-uyum ölçümü +
rejim-koşullu tutarlılık testi) tasarladı ve 2 numaralı terk eşiğine bağladı.
Yani projenin en kritik riski, keşfedilmiş, derecelendirilmiş ve
sigortalanmıştır — göz ardı edilmemiştir.

**C3. Dengesizlik ve model-güvenilirliği zinciri: N4 (Faz 3) → N11 (Faz 6) →
N12 (Faz 7) → Faz 8 §5/§6 (risk olarak kapanış).**
Faz 3, SMOTE/resampling'i hakemli kanıtla yasakladı ve class weighting →
threshold-moving → kalibrasyon sırasını koydu. Faz 6 bu sırayı model kararına
gömdü (class-weighted GBM; az-gözlemde Platt/temperature, izotonik değil) ve
ordinal yapıyı (up<stable<down) ileri deneme olarak işaretledi. Faz 7,
kalibrasyon ve threshold kararlarının değerlendirmesini protokole bağladı
(per-class raporlama, olasılık-tabanlı karar eşiği için kalibrasyon ön koşulu).
Faz 8 zinciri iki yönden kapatır: (a) "yanlış kalibrasyon" (registri #13) ve
"ordinal yapının ihmali" (#14) birer izlenecek risk olarak kayda geçer; (b)
"gizli leakage" (#4) ve "naif baseline'ı yenememenin gizlenmesi" (#5) — N7/N12
protokolünün tam da önlemeye çalıştığı iki yüksek×yüksek risktir. SMOTE
karşı-bulgusu zincir boyunca işaretli kaldı; ampirik test kapısı açıktır.

**C4. Rejim zinciri: N2 (Faz 2) → N8 (Faz 3) → N11 (Faz 6) → N12 (Faz 7) →
N13 (Faz 8, registri #9).**
Faz 2, arz değişkeninin rejime bağlı çift yönlü olduğunu buldu. Faz 3, rejim
izlemenin aylık ufukta algoritmik değil dışsal olay-tabanlı olması gerektiğini
ekledi. Faz 6, rejim değişkenlerini latent model yerine gözlemlenebilir
öznitelik olarak modele soktu (GBM etkileşimleri + açık etkileşim feature'ları).
Faz 7, şok takvimini önceden sabitleyip rejim-ayrık MCC raporlamasını zorunlu
kıldı. Faz 8, zincirin son halkasını ekler: bu riski somut ve **güncel** bir
örnekle (24 Temmuz 2025 ÖTV düzenlemesi) derecelendirir (Yüksek×Yüksek, registri
#9), Hendry'nin "location shift" forecast-failure çerçevesini bağlar ve
azaltıcı önlem olarak intercept-correction/rejim kuklası + hızlı yeniden-eğitim
+ şok-dönemi ayrı raporlamayı önerir. 3 numaralı terk eşiği (tek-rejim
performansı) bu zincirin nihai denetim noktasıdır.

---

## D. Bilinen Belirsizlikler (fazlardan konsolide)

Aşağıdaki maddeler fazların "Açık Sorular / Literatürde Net Olmayanlar"
bölümlerinden derlenmiştir; sentez bunları çözmez, görünür kılar.

**Etiket ve hedef tasarımı (Faz 1, Faz 4, Faz 8):**
- İlan-tabanlı, düşük frekanslı piyasalar için yön etiketleme literatürü yoktur
  [N3]; tüm etiket tasarımı projeye özgü deneyle doğrulanacaktır.
- Aynı veri/model üzerinde temiz bir 2-sınıf vs 3-sınıf F1 kıyaslaması literatürde
  yoktur; stable bandının optimal genişliği için önceden belirlenmiş değer yoktur
  (Faz 1, Faz 8 §11 bu belirsizliği ayrıca risk olarak da tekrarlar).
- Threshold/ufuk seçiminin optimal kuralı literatürde net değildir — N3'ün
  doğrudan uzantısıdır (Faz 8 §11).
- İlan-endeksi yönü ile gerçekleşen-fiyat yönünün örtüşme derecesi ölçülmemiştir
  (Faz 4). **Türkiye'ye özgü olarak:** sale-to-list marjının döngüsel
  davranışının nicel büyüklüğü de ölçülmemiştir — konut literatüründen güçlü
  analoji var (Anenberg & Laufer 2017; Trojanek vd. 2025: ilan-endeksleri
  işlem-endekslerini 1–2 ay önden gösteriyor) ama Türkiye araç piyasası için
  doğrudan yayımlanmış bir ölçüm yok; bu, Faz 8'in dolaylı proxy test paketiyle
  projede ölçülecektir.
- Hangi agregasyon düzeyinin (marka/segment/piyasa) yön açısından en öngörülebilir
  olduğu literatürde test edilmemiştir (Faz 4).

**Domain dinamikleri (Faz 2):**
- Kur geçişkenliğinin ikinci el araç özelindeki nicel lag'i ve büyüklüğü hakemli
  olarak ölçülmemiştir; taşıt kredisi faizi → talep → fiyat lag'i Türkiye için
  nicelleştirilmemiştir.
- BETAM/arabam.com endekslerinin kompozisyon düzeltmesi yapıp yapmadığı kamuya
  açık dokümanlardan kesin doğrulanamamıştır.
- Mevsimsellik nicel olarak doğrulanmamıştır; Türkiye EV/TOGG değer kaybı
  anlatıları çelişkilidir; sıfır araç kampanya yoğunluğu için sistematik seri
  yoktur (ölçüm boşluğu).

**Feature katmanı (Faz 5):**
- Optimal segment granülerliği literatürde yoktur; hücre başına gözlem eşiği
  veriyle belirlenecektir.
- Google Trends'in fiyat YÖNÜ tahminine katkısı gösterilmemiştir (kanıt
  satış/adet tahminine dairdir); days-on-market'ın fiyat yönü öncülüğünün
  akademik doğrulaması sınırlıdır (sektör kanıtı güçlü).
- Türkiye ERPT profili çeyreklik çalışmalardan gelir; ay-bazlı kullanım
  interpolasyon varsayımı taşır; otomobile-özgü temiz ERPT katsayısı yoktur.

**Model katmanı (Faz 6):**
- 3 sınıfta ordinal yaklaşımın kazancı literatürde net değildir (kazanç 6+
  sınıfta belirginleşir); yalnızca deneysel doğrulanabilir.
- Maliyet matrisi için literatür varsayılan değer vermez; class weight +
  cost-sensitive kayıp + kalibrasyon üçlüsünün birlikte etkileşimi tam
  çözülmemiştir; TabPFN bu problem sınıfında doğrulanmamıştır.

**Protokol katmanı (Faz 7):**
- "Deflated MCC" standart formülü yoktur (permütasyon max-istatistik muadil
  kullanılır); çok küçük N'de nested-CV vs kilitli hold-out sorusunun kesin
  cevabı yoktur; kategorik yön serilerinde blok-permütasyon blok uzunluğu ve
  PT testinin 3-sınıf/küçük-N güç davranışı az çalışılmıştır; CPCV için minimum
  gözlem eşiği kanıta değil pratiğe dayanır.

**Karar/kullanım katmanı (Faz 8):**
- Yön sinyalinin hangi somut iş kararına (fiyatlama, envanter, alım zamanlaması)
  eşleneceği proje-özgüdür; literatürde net değildir — sinyalin kapsamı
  (agrega/piyasa-geneli) ile kararın kapsamı (birim/bireysel) arasındaki uyum
  ayrıca belgelenmelidir (Faz 8 §8.2).

**İşaretli çelişkiler (düzleştirilmedi):**
- SMOTE hasarının büyüklüğü: klinik literatür "kaçının" vs tree-ensemble
  çalışması "küçük, rekalibre edilir" (Faz 3) → ampirik test.
- Blocked-CV: Bergmeir & Benítez standardı vs kronolojik-tek-yön kuralı [N5]
  (Faz 7) → durağanlık ihlali gerekçesiyle N5 korundu, blocked-CV ikincil.
- Trend-scanning'in üstünlüğü: López de Prado geleneği güçlü sunar, AEDL (2025)
  risk-ayarlı metrikte üstün bulmaz (Faz 1).
- TOGG/EV değer kaybı ve satış-süresi ölçümleri (Faz 2) kaynaklar arası
  tutarsızdır.

---

## E. Konsolide Kilit Kaynakça (faz işaretli)

Yeni kaynak eklenmemiştir; aşağıdaki liste fazlarda tam künyesiyle verilen kilit
kaynakların faz işaretli kısa dizinidir. Tam kaynakçalar ilgili faz
dökümanlarındadır.

**Etiketleme (Faz 1):** López de Prado 2018 *AFML* & 2020 *MLAM*; Chalkidis &
Savani 2021 (ICAIF); Wu vd. 2020 (Entropy); Kovačević vd. 2023 (IEEE Access);
Song vd. 2026 (ICML, Label Horizon Paradox); Kang 2025 (arXiv).

**Domain — Türkiye ve araç piyasası (Faz 2):** Kara & Öğünç 2005 (TCMB); Özmen &
Topaloğlu 2017 (TCMB, Faz 5'te de); Erdem & Şentürk 2009; BETAM sahibindex ve
arabam.com endeks yayınları; Manheim/Cox Automotive metodoloji dökümanı (Faz 5'te
de); Cleveland Fed 2021-17 (çip krizi).

**Finansal ML metodolojisi (Faz 3, Faz 7):** van den Goorbergh vd. 2022 (JAMIA)
[N4'ün kaynağı]; Chicco & Jurman 2020 (BMC Genomics) [N5]; Kapoor & Narayanan
2023 (Patterns) [ayrıca Faz 8'in gizli-leakage riskinin (#4) temel kaynağı];
Harvey, Liu & Zhu 2016 (RFS); Bailey & López de Prado 2014 (Deflated Sharpe);
Bailey, Borwein, López de Prado & Zhu 2014 (MinBTL); Lo 2004 (AMH); Bergmeir &
Benítez 2012, Bergmeir vd. 2018 (zaman serisi CV).

**Araç fiyat literatürü (Faz 4):** Rosen 1974; Lessmann & Voß 2017 (IJF); Dress
vd. 2018 (asimetrik maliyet); Rashed vd. 2019 (ECML); Storchmann 2004; Schloter
2022; Daştan 2016; Bukvić vd. 2022 (en yakın çalışma).

**Feature/endeks metodolojisi (Faz 5):** OECD 2006 Hedonic Handbook; BLS used
cars metodolojisi; Micci-Barreca 2001 (target encoding); Prokhorenkova vd. 2018
(CatBoost); Pargent vd. 2022; tsfresh (Christ vd. 2018).

**Model (Faz 6):** Grinsztajn vd. 2022; McElfresh vd. 2023; Shwartz-Ziv & Armon
2022; Montero-Manso & Hyndman 2021; Makridakis vd. 2022 (M5); Frank & Hall 2001
(ordinal); Hollmann vd. 2025 (TabPFN, Nature); Niculescu-Mizil & Caruana 2005
(kalibrasyon) [Faz 8'de ensemble aşırı-güven riskinin de kaynağı]; Mukhoti vd.
2020 (focal loss).

**Protokol (Faz 7):** Gorodkin 2004 (çok-sınıflı MCC); Pesaran & Timmermann
1992/2009; Blaskowitz & Herwartz 2014; Ojala & Garriga 2010 (permütasyon testi);
Künsch 1989 / Politis & Romano (blok-bootstrap); Vabalas vd. 2019; Cawley &
Talbot 2010; Fabozzi & López de Prado 2018; Arnott, Harvey & Markowitz 2019.

**Kritik varsayım ve kırmızı-takım (Faz 8 / N13):** Anenberg & Laufer 2017
(REStat 99(4):722-734); Anenberg 2016 (IER 57(4)); Han & Strange 2016 (JUE 93);
Carrillo, de Wit & Larson 2015 (Real Estate Economics 43(3)); Trojanek vd. 2025
(CAMA WP 2025-45); Merlo & Ortalo-Magné 2004 (seçilim/fiyat-düşürme davranışı);
Heckman 1979 (seçilim yanlılığı düzeltmesi); Hendry — forecast-failure /
location-shift literatürü; "Who Saw It Coming? Historical Experience and the
2021 Inflation Forecast Failure" (2026, arXiv); NCBI Bookshelf overfitting
bölümü; Flach 2023 (kalibrasyon survey'i); "Embracing Negative Results in
Machine Learning" (ICML 2024, arXiv:2406.03980) [terk kriterlerinin dürüstlük
gerekçesi].

---

*Not: Bu sentez dökümanı yeni arama yapmamıştır; "Kullanılan Arama Sorguları"
bölümü bu nedenle yoktur. Kalite kontrolü için `docs/standards.md` Bölüm 4
listesi, "yeni kaynak yok / faz atıfları esas" kuralı çerçevesinde uygulanır.*
