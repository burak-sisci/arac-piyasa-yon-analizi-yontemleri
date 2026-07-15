---
dokuman_tipi: karar_kaydi
proje: "Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması"
tarih: 2026-07-13
revizyon: v5 (N10 eklendi — Faz 5 bulguları sonrası)
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
endeksleri (BETAM sahibindex, arabam.com) karma/kilometre/hedonik düzeltmesizdir;
mix kaymasına açıktırlar. Model kompozisyon düzeltmesini kendi içinde yapmalıdır.
→ Faz 5'te çözüldü (bkz. N10).

**N2 (Faz 2) — Arz değişkeni rejime bağlı çift yönlüdür.** Kıtlık → ikinci el
primi yukarı; kampanya/bolluk → aşağı. Sabit katsayı varsayımı dönem
geçişlerinde hatalıdır. → Faz 6 ve 7 dikkate alır; Faz 5'te rejim etkileşim
feature'ı olarak ele alındı.

**N3 (Faz 1) — Etiketleme literatüründe boşluk vardır.** Yön etiketleme
metodolojisi sürekli işlem verisi için geliştirilmiştir; düşük frekanslı,
ilan-tabanlı piyasalar için doğrudan ampirik doğrulama YOKTUR. Projeye özgü
deney gerektirir.

**N4 (Faz 3) — SMOTE ve resampling KULLANILMAYACAKTIR.** Hakemli kanıt
(van den Goorbergh, van Smeden, Timmerman & Van Calster, 2022, JAMIA 29(9):
1525-1534): imbalance düzeltmeleri kötü kalibrasyon üretir, ROC-AUC'yi
iyileştirmez, ve aynı sensitivite/spesifisite kazanımı yalnızca karar eşiğini
kaydırarak elde edilir. ZORUNLU SIRALAMA: (1) class weighting → (2)
threshold-moving → (3) post-hoc kalibrasyon (Platt / isotonic). Karşı-bulgu
işaretli; ampirik test önerilir. → Faz 6 ve 7 esas alır.

**N5 (Faz 3) — Metrik ve validasyon zorunlulukları.** Birincil metrik: MCC ve
macro-F1; accuracy tanımlayıcı (Chicco & Jurman 2020). Rastgele k-fold CV
YASAKTIR; kronolojik ayrım zorunludur (Bergmeir vd. 2018). → Faz 7 protokole çevirir.

**N6 (Faz 3) — Başarı kriteri: naif baseline üzeri iyileşme.** Referans:
persistence + "her şeye stable". Model bunları MCC'de anlamlı geçemiyorsa sonuç
"sinyal yok"tur ve DEĞERLİ NEGATİF BULGU olarak raporlanır. %70+ iddiaları hedef
alınmaz (leakage; Kapoor & Narayanan 2023).

**N7 (Faz 3) — Falsifikasyon audit'i zorunludur.** Pipeline null veri
(karıştırılmış hedef/rastgele-yürüyüş) üzerinde test edilir. Denenen
model/hiperparametre sayısı kayıt + çoklu-test farkındalığı (Harvey vd. 2016;
Bailey & López de Prado 2014). → Faz 7'nin görevi.

**N8 (Faz 3) — Rejim izleme dışsal olay-tabanlıdır.** Yüksek-frekanslı algoritmik
drift-detection (VFDT/CVFDT, intraday ADWIN) aylık ufka AKTARILAMAZ. Latent rejim
(HMM) yerine dışsal-değişken tabanlı rejim. → Faz 6 ve 7 dikkate alır.

**N9 (Faz 4) — Projenin novelty konumu belgelendi.** Kümüle ilan-fiyat endeksinin
zaman serisi YÖN sınıflaması (up/down/stable) hakemli literatürde YOKTUR; en yakın
(Bukvić et al. 2022) dahi kesitseldir. Devşirilebilir çekirdek: prediktif öznitelik
seti (→ Faz 5), residual value asimetrik-maliyet çerçevesi (→ sınıf-ağırlıklı kayıp,
N4 uyumlu), Kaggle veri-temizlik pratikleri. Piyasa/segment yön köprüsü literatürde
hazır DEĞİLDİR, projede inşa edilir.

Kritik geçerlilik varsayımı (N9 + K8): İlan-fiyatı endeksinin YÖNÜ, gerçekleşen-
fiyat yönünü izler — ANCAK pazarlık marjı rejime göre değişirse ilişki bozulur.
Projenin en kritik test edilecek varsayımıdır. → Faz 8 ve sentez ele alır.

**N10 (Faz 5) — Kompozisyon düzeltmesi ve feature üretimi reçeteye bağlandı.**
N1'in çözümü:
1. BİRİNCİL: Aylık hedonik imputation. log(P_it) = α_t + Σβ_k·x_k,it + ε_it,
   x_k = N9 seti (yaş, km, marka/model, motor, yakıt, şanzıman, donanım). Yön
   etiketi mix-düzeltilmiş Δα_t'den hesaplanır (log geri-çevirmede bias düzeltmesi).
2. DOĞRULAMA: Manheim-tarzı sabit-ağırlık endeksi (24-ay yuvarlanan ağırlık +
   km regresyon düzeltmesi + outlier kırpma). İki serinin diverjansı = mix
   kayması teşhisi.
3. FEATURE BONUSU: hedonik reziduel ε (segment ucuz/pahalı sapması).

Makro lag ailesi ampirik seçilir: CCF + pairwise Granger (çoklu lag), EĞİTİM-İÇİ.
Kur için 1/3/6/12 ay aday havuzu; ERPT kanıtıyla (geçişin ~%40'ı ilk çeyrek,
çekirdek mal/otomobil daha hızlı) kısa lag'ler öncelikli hipotez — veriyle test.

Çift leakage kısıtı TÜM feature'larda: (a) yalnızca-geçmiş (t öncesi; makroda
yayım gecikmesi lag'e eklenir), (b) fold-dışı hesaplama. Aynı-dönem büyüklükler
(days-on-market, ilan hacmi) t-1'e çekilir. High-cardinality kategorik
(marka-model) için ordered/expanding-mean target encoding + hiyerarşik backoff.

Teknik göstergeler soyutlama düzeyinde alınır: momentum + oynaklık türetilir;
RSI/MACD hazır parametrelerle KOPYALANMAZ (zorlama). → Faz 6 ve 7 girdisi.

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
