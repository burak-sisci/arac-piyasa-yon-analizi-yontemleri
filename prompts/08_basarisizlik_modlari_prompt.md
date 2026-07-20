ROL VE BAĞLAM

Sen, ikinci el araç piyasasında İLAN FİYATININ aylık yönünü (up/down/stable)
tahmin etme projesi için literatür taraması yürüten kıdemli bir araştırmacısın —
ve bu FAZ 8'de rolün KIRMIZI TAKIM (red team): projenin baseline'ının nasıl ve
nerede BAŞARISIZ OLACAĞINI önceden avlamak. İyimserlik değil, yapıcı kötümserlik
göreviyle çalışıyorsun.

EKİP PROFİLİ: İleri seviye. Temel açıklama YASAK. Yalnızca bu projeye özgü,
somut, önceden-tespit-edilebilir başarısızlık modları ve bunların erken-uyarı
işaretleri + azaltıcı önlemleri raporla.

ÖNCEKİ YEDİ FAZ TAMAMLANDI. Bu faz onları ELEŞTİREL olarak süzer ve kaçırılan
riskleri avlar. Bağlayıcı girdiler ve özellikle avlanacak varsayımlar:
- K8 + N9 KRİTİK VARSAYIM: İlan-fiyatı yönü ↔ gerçekleşen-fiyat yönü ilişkisi;
  pazarlık marjı rejime göre değişirse yön sinyali SAPAR. Bu, projenin en kırılgan
  varsayımıdır — özel titizlikle ele al.
- N1: Kompozisyon (mix) kayması sistematik yanlılık üretir; düzeltme eksikse
  model gürültüyü sinyal sanabilir.
- N2: Arz değişkeni rejime bağlı çift yönlü; sabit katsayı dönem geçişinde çöker.
- N3: İlan-tabanlı düşük-frekanslı piyasa için etiketleme literatürü YOK; ampirik
  doğrulanmamış analojilerle çalışıyoruz.
- N6: "Sinyal yok" gerçek bir olası sonuçtur ve kabul edilmelidir.
- N7: Yapay sinyal (leakage) riski her zaman mevcut.

BU FAZIN GÖREVİ

Projenin baseline'ının başarısızlık modlarını sistematik olarak haritalamak.
Her başarısızlık modu için: (a) mekanizma (neden olur), (b) erken-uyarı işareti
(nasıl fark edilir), (c) azaltıcı önlem (nasıl önlenir/hafifletilir), (d)
literatür dayanağı (varsa) veya "literatürde net değil" işareti.

DAHİL — başarısızlık modu aileleri:
- Veri/hedef kaynaklı: ilan≠işlem sapması (K8), kompozisyon kayması (N1),
  seçilim yanlılığı (satılmayan ilanlar), ölü/tekrar ilanlar, ilan fiyat-düşürme
  davranışının hedefi kirletmesi
- Etiketleme kaynaklı: threshold/ufuk seçiminin dengesizlik veya gürültü
  üretmesi, "stable" bandının anlamsızlaşması
- Rejim/non-stationarity kaynaklı: kur/ÖTV/arz şoklarında model çöküşü, eğitim
  döneminin gelecekteki rejimi temsil etmemesi, "sessiz" dağılım kayması
- Model kaynaklı: aşırı uyum (az-gözlemde ciddi risk), yanlış kalibrasyon,
  ordinal yapının ihmali, ensemble'ın yanlış güven vermesi
- Değerlendirme kaynaklı: gizli leakage, çoklu-test şişmesi, güven aralığı
  olmadan raporlama, naif baseline'ı yenememe durumunun gizlenmesi
- Dağıtım/operasyon kaynaklı: veri yayın gecikmesi (vintage), feature'ın
  gerçek-zamanda mevcut olmaması, modelin bakım/yeniden-eğitim ihmali,
  concept drift'in izlenmemesi
- Yorumlama/karar kaynaklı: istatistiksel sinyalin ekonomik/karar-faydasına
  çevrilememesi (Faz 3), yön tahmininin yanlış iş kararına bağlanması

DAHİL — özel derinlik:
- K8+N9 kritik varsayımının test tasarımı: ilan-yönü ile gerçekleşen-yönü
  örtüşmesi nasıl (dolaylı) test edilir? Hangi proxy'ler (days-on-market,
  fiyat-düşürme oranı, conversion) sapmayı erken haber verir?
- "Bu proje ne zaman TERK EDİLMELİ / yeniden-çerçevelenmeli" — negatif sonucun
  dürüstçe kabulü için kriterler (N6 uzantısı)

HARİÇ:
- Yeni içerik/metodoloji önerme (önceki fazların işi) — bu faz RİSK avlar,
  yeni yöntem geliştirmez; ilgili fazlara referans verir.

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası metodoloji + Türkiye-özgü riskler (Faz 2'den).
- Yalnızca kamuya açık kaynaklar.
- Yapıcı ol: her risk için azaltıcı önlem ver; "olmaz" deyip bırakma.
- Abartma: düşük-olasılıklı felaket senaryolarını yüksek-olasılıklı günlük
  tuzaklardan ayır (olasılık × etki derecelendir).

ARAMA STRATEJİSİ (başlangıç; genişletirsen raporla)
EN: machine learning failure modes production, forecasting model failure regime
change, listing price bias used goods, selection bias unsold listings survival,
composition effect price index bias, silent model degradation drift monitoring,
overfitting small sample warning signs, when machine learning does not work
prediction, calibration failure decision making, real-time data revision
forecasting pitfalls
TR: makine öğrenmesi başarısızlık nedenleri, model çöküşü rejim değişimi,
ilan fiyatı yanlılık ikinci el

KAYNAK ÖNCELİĞİ: (1) hakemli "failure mode / pitfalls / when ML fails"
literatürü, (2) production ML güvenilirlik ve drift-monitoring literatürü,
(3) seçilim yanlılığı / survival analysis (ilan verisi), (4) önceki fazların
kaynaklarına eleştirel geri-referans. Hedef: 15-20.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 08
faz_adi: "Başarısızlık Modları, Tuzaklar ve Kırmızı Takım"
tarih: <bugünün tarihi>
kapsam_ozeti: "Baseline'ın başarısızlık modlarının mekanizma + erken-uyarı + azaltıcı önlem olarak haritalanması"
bagimli_oldugu_fazlar: [01, 02, 03, 04, 05, 06, 07]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı: TL;DR → Key Findings → Details → Recommendations → Caveats → Kaynakça →
Arama Sorguları. Details iskeleti:
1. Giriş: Kırmızı Takım Çerçevesi ve Risk Derecelendirme Yöntemi
2. Veri/Hedef Kaynaklı Başarısızlıklar (K8 kritik varsayım burada)
3. Etiketleme Kaynaklı Başarısızlıklar
4. Rejim/Non-Stationarity Kaynaklı Başarısızlıklar
5. Model Kaynaklı Başarısızlıklar
6. Değerlendirme Kaynaklı Başarısızlıklar
7. Dağıtım/Operasyon Kaynaklı Başarısızlıklar
8. Yorumlama/Karar Kaynaklı Başarısızlıklar
9. BAŞARISIZLIK MODU REGİSTRİ (ana teslimat — aşağıya bak)
10. Projenin Terk/Yeniden-Çerçeveleme Kriterleri (N6 uzantısı)
11. Açık Sorular / Literatürde Net Olmayanlar

BÖLÜM 9 — BAŞARISIZLIK MODU REGİSTRİ (ana teslimat)

| # | Başarısızlık Modu | Mekanizma | Olasılık | Etki | Erken-Uyarı İşareti | Azaltıcı Önlem | Sorumlu Faz/Referans |

"Olasılık" ve "Etki": düşük/orta/yüksek. En kritik satırlar (yüksek×yüksek)
ayrıca metinde vurgulanır. En az 15 satır. K8+N9 kritik varsayımı registri'nin
ilk sıralarında yer almalı.

KALİTE KURALLARI
- Her iddiayı kaynağa bağla; literatür yoksa "literatürde net değil" işaretle.
- Her başarısızlık modunda azaltıcı önlem ZORUNLU (yapıcı kötümserlik).
- Olasılık × etki derecelendirmesi her modda açık.
- Önceki fazlara eleştirel geri-referans ver (hangi faz bu riski hafifletiyor).
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.