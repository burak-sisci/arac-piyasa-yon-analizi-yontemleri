---
dokuman_tipi: karar_kaydi
proje: "Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması"
tarih: 2026-07-13
revizyon: v7 (N12 eklendi — Faz 7 bulguları sonrası)
iliskili_dokuman: 00_master_plan_literatur_taramasi.md
durum: onaylandi
---

# Karar Kaydı — Master Plan Açık Noktaları ve Faz Bulguları

Bu kararlar tüm faz promptlarına ve dökümanlarına bağlayıcıdır. Yeni fazlardan
çıkan bulgular yeni karar/not maddesi doğurabilir; her ekleme revizyon notuyla
işaretlenir.

## A. Kapsam Kararları (K)

**K1 — Tahmin ufku:** Faz 1 gerekçeli olarak **aylık ufku** önerdi (ikincil:
2-3 aylık proxy ufuk denenmeli — Label Horizon Paradox). Durum: aylık ufuk
çalışma varsayımıdır; geliştirici ekibin iş tarafı beklentisiyle teyit edilecektir.

**K2 — "Stable" bandı:** Faz 1 bulgusu: sabit yüzde eşiği yerine
**oynaklık-uyarlamalı bant** (segment bazlı, ±0.5σ–1σ taranarak) birincil
öneridir; quantile/tercile tabanlı bölme yedek seçenektir. Neutral sınıf oranı
%60'ı aşarsa quantile'a geçilir.

**K3 — İkinci el / yeni araç kapsamı:** Tarama İKİNCİ EL piyasası odaklıdır.
Yeni araç yalnızca Faz 2'de, ikinci eli etkileyen dışsal faktör (sıfır araç
zamları, kampanya yoğunluğu, arz kıtlığı) olarak ele alınır.

**K4 — Coğrafi kapsam (hibrit):** Metodoloji fazları (1, 3, 5, 6, 7, 8)
uluslararası literatürü tarar. Faz 2 Türkiye odaklıdır. Faz 4 uluslararasıdır,
Türkiye çalışmaları öncelikli raporlanır.

**K5 — Şirket bilgisi sınırı:** Çalışma Arabam.com'dan bağımsız, tamamen kamuya
açık kaynaklarla yürütülür; çıktılar sonra şirketteki geliştirici ekibe
sunulacaktır. Repo public'tir. Hiçbir faz dökümanına şirket içi veri, rapor,
metrik veya yayınlanmamış bilgi giremez.

**K6 — Kaynak türü kapsamı:** Geniş kapsam: peer-reviewed literatür + gri
literatür (arXiv/SSRN, tez) + resmi kurum yayınları (TÜİK, TCMB, ODMD, OSD,
Resmî Gazete) + nitelikli endüstri kaynakları. Sektör beyanları ve basın
haberleri kullanılabilir ancak dökümanda "düşük kanıt gücü" olarak işaretlenir.

**K7 — Faz çıktı uzunluğu:** Üst sınır yoktur. Derinlik hedef kaynak sayısıyla,
disiplin kalite kontrol listesiyle sağlanır.

**K8 — Model hedefi: İLAN FİYATI (Faz 2 bulgusu).** Türkiye'de kamuya açık tüm
ikinci el fiyat serileri **ilan (asking) fiyatıdır**; gerçekleşen işlem fiyatı
kamuya açık değildir (noter devir verisi yalnızca adet içerir).

KARAR: Projenin tahmin hedefi **ilan fiyatının yönü**dür (up/down/stable).
Bu bilinçli ve belgelenmiş bir tasarım tercihidir.
- Tüm dökümanlar "ilan fiyatı yönü" terminolojisini kullanır; "piyasa fiyatı"
  veya "işlem fiyatı" ifadeleri kullanılmaz.
- İlan–işlem farkı (pazarlık marjı) bir belirsizlik kaynağı olarak sentezde
  açıkça raporlanır; sıfır varsayılmaz.
- İlan verisinin yapısal sorunları (seçilim yanlılığı, ölü/tekrarlanan ilanlar,
  fiyat düşürme davranışı) Faz 4 ve Faz 8'de ele alınır.

## B. Faz Bulgularından Doğan Bağlayıcı Notlar (N)

**N1 (Faz 2) — Kompozisyon düzeltmesi modelin işidir.** Kamuya açık Türk
endeksleri (BETAM sahibindex, arabam.com) karma/kilometre/hedonik düzeltmesizdir.
Model kompozisyon düzeltmesini kendi içinde yapmalıdır. → Faz 5'te çözüldü (N10).

**N2 (Faz 2) — Arz değişkeni rejime bağlı çift yönlüdür.** Kıtlık → prim yukarı;
kampanya/bolluk → aşağı. Sabit katsayı dönem geçişlerinde hatalıdır. → Faz 5'te
rejim etkileşim feature'ı; Faz 6'da GBM split/etkileşim ile ele alındı.

**N3 (Faz 1) — Etiketleme literatüründe boşluk vardır.** Düşük frekanslı,
ilan-tabanlı piyasalar için doğrudan ampirik doğrulama YOKTUR. Projeye özgü
deney gerektirir.

**N4 (Faz 3) — SMOTE ve resampling KULLANILMAYACAKTIR.** (van den Goorbergh vd.
2022, JAMIA). ZORUNLU SIRALAMA: (1) class weighting → (2) threshold-moving →
(3) post-hoc kalibrasyon. Karşı-bulgu işaretli. → Faz 6'da uygulandı.

**N5 (Faz 3) — Metrik ve validasyon zorunlulukları.** Birincil metrik: MCC ve
macro-F1; accuracy tanımlayıcı. Rastgele k-fold CV YASAKTIR; kronolojik ayrım
zorunludur. → Faz 7'de protokole çevrildi (N12).

**N6 (Faz 3) — Başarı kriteri: naif baseline üzeri iyileşme.** Referans:
persistence + "her şeye stable". Geçilemezse "sinyal yok" değerli negatif
bulgudur. %70+ iddiaları hedef alınmaz. → Faz 7'de baseline seti + anlamlılık
testi olarak somutlaştı (N12).

**N7 (Faz 3) — Falsifikasyon audit'i zorunludur.** Null veri üzerinde pipeline
testi; denenen model sayısı kayıt + çoklu-test farkındalığı. → Faz 7'de somut
protokole çevrildi (N12: blok-permütasyon null + pozitif kontrol + deneme günlüğü).

**N8 (Faz 3) — Rejim izleme dışsal olay-tabanlıdır.** Yüksek-frekanslı algoritmik
drift-detection aylık ufka AKTARILAMAZ. Latent HMM yerine dışsal-değişken tabanlı
rejim. → Faz 6'da öznitelik olarak modele girdi; Faz 7'de rejim-ayrık değerlendirme
protokolü oldu (N12).

**N9 (Faz 4) — Projenin novelty konumu belgelendi.** Kümüle ilan-fiyat endeksinin
zaman serisi YÖN sınıflaması hakemli literatürde YOKTUR (en yakın Bukvić vd. 2022
kesitsel). Devşirilebilir çekirdek: prediktif öznitelik seti, residual value
asimetrik-maliyet çerçevesi (→ sınıf-ağırlıklı kayıp), Kaggle veri-temizlik.
Kritik varsayım (N9+K8): ilan-yönü ↔ gerçekleşen-yön ilişkisi pazarlık marjı
rejime göre değişirse bozulur. → Faz 8 ve sentez.

**N10 (Faz 5) — Kompozisyon düzeltmesi ve feature üretimi reçeteye bağlandı.**
(1) BİRİNCİL: aylık hedonik imputation (log-fiyat ~ N9 seti), yön etiketi
mix-düzeltilmiş Δα_t'den. (2) DOĞRULAMA: Manheim-tarzı sabit-ağırlık endeksi;
diverjans = mix kayması teşhisi. (3) FEATURE: hedonik reziduel ε. Makro lag
ampirik (CCF + Granger, eğitim-içi); kur 1/3/6/12 ay, kısa lag'ler öncelikli
hipotez. Çift leakage kısıtı: yalnızca-geçmiş + fold-dışı. Teknik göstergeler
soyutlama düzeyinde (momentum/oynaklık); RSI/MACD kopyalanmaz. → Faz 6, 7 girdisi.

**N11 (Faz 6) — Model baseline kararı.** Birincil baseline: segment kimliği +
dışsal rejim değişkenlerini (N8) öznitelik alan, **class-weighted tek global
gradient boosting** (küçük segment → CatBoost / sıkı-düzenlileştirilmiş XGBoost;
büyük veri → LightGBM). N4 sırası uygulanır; post-hoc kalibrasyon az-gözlemde
**Platt/temperature scaling** (izotonik DEĞİL — overfit riski). Başarı ölçütü
naif baseline üzeri MCC (N6).

İLERİ DENEMELER (her biri GBM baseline'ı geçme eşiğiyle — N6):
- Frank & Hall (2001) ordinal 2-ikili-model ayrıştırması; QWK/MCC'de nominal'i
  geçerse benimse. 3 sınıfta kazanç garanti değil (literatürde net değil).
- Focal loss veya ordinal-farkında kuadratik maliyet matrisi (N9 asimetrik
  maliyet; reversal > off-by-one cezası).
- Hiyerarşik / partial-pooling (segment az ve heterojense).
- Çok-küçük veride TabPFN; gözlem büyür + global/cross-learning kurulursa DL.

DEEP LEARNING BASELINE DEĞİLDİR. Saf segment-başı lokal modeller önerilmez
(az-gözlem gürültüsü). → Faz 7 ve Faz 8 esas alır.

**N12 (Faz 7) — Validasyon ve raporlama protokolü.** Bir deneyin "güvenilir"
ilan edilmesi için 24-maddelik kontrol listesi (Faz 7 Bölüm 9) bağlayıcı
güvenilirlik sözleşmesidir. Çekirdek kararlar:

- OMURGA: genişleyen-pencere walk-forward + 1 ay ufuk + 1-2 ay purge/embargo;
  test dönemi gözlem bütçesine göre 6-24. "50-100 fold" YASAK (her fold'a ~1
  gözlem düşer). Eşik: N<50 → yalnızca keşifsel/negatif-bulgu; N≥80 → tam
  protokol; N≥150 → CPCV opsiyonel.
- AS-OF DATE MİMARİSİ: Tek merkezî bilgi-kesim tarihi; kronoloji (N5) + makro
  vintage/yayın-gecikmesi (en kritik leakage riski) tek noktadan garanti.
  Vintage yoksa pseudo-real-time +1/+2 ay lag. Ön-işleme/encoding/feature-
  selection fold-İÇİNDE fit.
- METRİK: macro-MCC (Gorodkin R_K, micro-MCC değil) + macro-F1 + per-class
  P/R/support; hepsine blok-bootstrap %95 CI (B≥1000, blok ~n^(1/3), seed
  raporlu). Accuracy tanımlayıcı.
- BASELINE + ANLAMLILIK: persistence, mevsimsel-naif, hep-stable, prior-oran;
  yön-anlamlılığı bootstrap-PT (Pesaran-Timmermann 2009 ruhu; asimptotik PT
  N<75'te over-sized). Fark CI'ı sıfırı içeriyorsa → "sinyal yok" (N6, geçerli).
- FALSİFİKASYON (BLOKE EDİCİ GEÇİT): blok-permütasyon hedef-shuffle null
  (B≥1000, tam pipeline); null ortalaması ≈0 DEĞİLSE DUR — leakage var. Ayrıca
  sentetik-sinyal pozitif kontrolü + random-walk benchmark.
- ÇOKLU-TEST: deneme günlüğü (her run kaydı) + denenen N raporu + permütasyon
  max-istatistik / FDR düzeltmesi + MinBTL kontrolü. Nested CV yerine katı
  hiperparametre bütçesi + kilitli hold-out (az-gözlem gerçekçiliği).
- REJİM-FARKINDALIK: şok takvimi ÖNCEDEN sabit (veriden keşfetme); rejim-ayrık
  MCC (sakin vs şok-sonrası); dağılım-kayması (covariate/temporal vs concept
  drift) ayrıştırılır.

İşaretli çelişki: Bergmeir & Benítez (2012) belirli koşulda blocked-CV'yi
standart önerir; ancak durağanlık varsayar, bu problemde rejim değişimi
nedeniyle ihlal edilir → N5 korunur, blocked-CV yalnızca purge+embargo ile
ikincil/yardımcı tahmin olarak. Boşluk: "deflated MCC" standart formülü yok;
permütasyon max-istatistik null'u muadil olarak kullanılır.

→ Faz 8 protokolün kaçırabileceği riskleri avlar.

## C. Yapısal Kararlar (Y)

**Y1:** Sentez dökümanı `docs/09_sentez_ve_karar_dokumani.md` olarak numaralı
seride tutulur. Sunum kaynak dosyaları `docs/sentez/` altında kalır.

**Y2:** Faz dökümanlarının metadata bloğu master plandaki genişletilmiş YAML
şemasıdır (bkz. `docs/standards.md`).

**Y3:** Faz dökümanlarının yapısı Faz 1'de oluşan genişletilmiş şablonu izler:
TL;DR → Key Findings → Details (faz-özel iskelet) → Recommendations → Caveats →
Kaynakça → Kullanılan Arama Sorguları. Kaynakça tek listedir; düşük kanıt gücü
taşıyan kaynaklar (sektör beyanı, basın, hakem-öncesi preprint, endüstri/hakemsiz)
giriş içinde işaretlenir.
