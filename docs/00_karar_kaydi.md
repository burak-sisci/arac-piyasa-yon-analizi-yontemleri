---
dokuman_tipi: karar_kaydi
proje: "Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması"
tarih: 2026-07-13
revizyon: v3 (N4–N8 eklendi — Faz 3 bulguları sonrası)
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
→ Faz 5'in somut görevi.

**N2 (Faz 2) — Arz değişkeni rejime bağlı çift yönlüdür.** Kıtlık → ikinci el
primi yukarı; kampanya/bolluk → aşağı. Sabit katsayı varsayımı dönem
geçişlerinde hatalıdır. → Faz 6 ve 7 dikkate alır.

**N3 (Faz 1) — Etiketleme literatüründe boşluk vardır.** Yön etiketleme
metodolojisi sürekli işlem verisi için geliştirilmiştir; düşük frekanslı,
ilan-tabanlı piyasalar için doğrudan ampirik doğrulama YOKTUR. Projeye özgü
deney gerektirir.

**N4 (Faz 3) — SMOTE ve resampling KULLANILMAYACAKTIR.** Hakemli kanıt
(van den Goorbergh, van Smeden, Timmerman & Van Calster, 2022, JAMIA 29(9):
1525-1534): imbalance düzeltmeleri kötü kalibrasyon üretir (azınlık sınıfı
olasılığının güçlü aşırı-tahmini), ROC-AUC'yi iyileştirmez, ve aynı
sensitivite/spesifisite kazanımı yalnızca karar eşiğini kaydırarak elde edilir.

ZORUNLU SIRALAMA: (1) class weighting → (2) threshold-moving → (3) post-hoc
kalibrasyon (Platt / isotonic). Olasılık çıktıları karar-desteği olarak
kullanılacaksa kalibrasyon, diskriminasyonla birlikte raporlanır.
Not: Bu bulguya karşı-bulgu mevcuttur (tree-ensemble bağlamında hasarın küçük ve
rekalibrasyonla giderilebilir olduğu); çelişki işaretlidir, ampirik test önerilir.
→ Faz 6 ve 7 esas alır.

**N5 (Faz 3) — Metrik ve validasyon zorunlulukları.**
- Birincil metrik: **MCC** ve **macro-F1**. Accuracy yalnızca tanımlayıcı olarak
  raporlanır; tek başına başarı ölçütü değildir (Chicco & Jurman 2020).
- **Rastgele k-fold CV YASAKTIR.** Zamansal sırayı bozar, look-ahead/leakage
  üretir (Bergmeir vd. 2018). Kronolojik ayrım zorunludur.
→ Faz 7 protokol detayını tasarlar.

**N6 (Faz 3) — Başarı kriteri: naif baseline üzeri iyileşme.** Hedef mutlak
doğruluk değildir. Referans baseline'lar: (a) persistence (bir önceki dönemin
yönü), (b) "her şeye stable" trivial model. Model bunları MCC'de anlamlı biçimde
geçemiyorsa sonuç "sinyal yok"tur ve DEĞERLİ BİR NEGATİF BULGU olarak raporlanır.
Literatürdeki %70+ doğruluk iddiaları hedef alınmaz; büyük kısmı leakage
kaynaklıdır (Kapoor & Narayanan 2023).

**N7 (Faz 3) — Falsifikasyon audit'i zorunludur.** Pipeline, null veri
(karıştırılmış hedef veya rastgele-yürüyüş) üzerinde çalıştırılacak; yapay sinyal
üretiyorsa iş akışında leakage var demektir. Ayrıca denenen model/hiperparametre
sayısı kayıt altına alınır ve çoklu-test farkındalığıyla raporlanır (Harvey, Liu
& Zhu 2016; Bailey & López de Prado 2014). → Faz 7'nin görevi.

**N8 (Faz 3) — Rejim izleme dışsal olay-tabanlıdır.** Araç piyasasında drift
kaynakları gözlemlenebilir (kur şoku, ÖTV değişikliği = ani drift; enflasyon
trendi = tedrici drift). Yüksek-frekanslı algoritmik drift-detection
(VFDT/CVFDT, intraday ADWIN) aylık ufka AKTARILAMAZ — yılda ~12 gözlem testleri
güçsüz bırakır. Latent rejim modelleri (HMM) yerine dışsal-değişken tabanlı
rejim tercih edilir. → Faz 6 ve 7 dikkate alır.

## C. Yapısal Kararlar (Y)

**Y1:** Sentez dökümanı `docs/09_sentez_ve_karar_dokumani.md` olarak numaralı
seride tutulur. Sunum kaynak dosyaları `docs/sentez/` altında kalır.

**Y2:** Faz dökümanlarının metadata bloğu master plandaki genişletilmiş YAML
şemasıdır (bkz. `docs/standards.md`).

**Y3:** Faz dökümanlarının yapısı Faz 1'de oluşan genişletilmiş şablonu izler:
TL;DR → Key Findings → Details (faz-özel iskelet) → Recommendations → Caveats →
Kaynakça → Kullanılan Arama Sorguları. Kaynakça tek listedir; düşük kanıt gücü
taşıyan kaynaklar (sektör beyanı, basın, hakem-öncesi preprint) giriş içinde
işaretlenir.
