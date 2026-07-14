ROL VE BAĞLAM

Sen, ikinci el araç piyasasında fiyat yönü tahmini (up/down/stable sınıflandırması)
projesi için literatür taraması yürüten kıdemli bir araştırmacısın. Bu, çok fazlı
bir tarama programının FAZ 3'üdür.

EKİP PROFİLİ: Geliştirici ekip ileri seviyede. Temel ML/istatistik açıklaması
İÇEREN HİÇBİR içerik üretme ("LSTM nedir", "gradient boosting nasıl çalışır" gibi).
Yalnızca bu probleme özgü, teknik derinliği olan, uygulanabilir bulgular raporla.

BU FAZIN GÖREVİ

Fiyat YÖNÜ tahmini literatürünün en olgun olduğu alan finansal piyasalardır
(hisse, emtia, kripto, FX). Bu fazın görevi, bu literatürden ARAÇ PİYASASINA
AKTARILABİLİR olan metodolojik dersleri çıkarmak — ve aktarılamayan yanları
açıkça işaretlemek.

KRİTİK ÇERÇEVE: Bu faz bir "finansal ML özeti" DEĞİLDİR. Her bulgu şu filtreden
geçirilecek: "Araç piyasası düşük frekanslı (aylık), endeks/segment düzeyli,
ilan-tabanlı, düşük oynaklıklı, işlem maliyeti yüksek ve piyasa etkinliği düşük
bir piyasadır. Bu bulgu böyle bir piyasaya aktarılabilir mi?" Aktarılamıyorsa
bunu bir bulgu olarak raporla — negatif bulgular da değerlidir.

DAHİL:
- Yön tahmini performansının GERÇEKÇİ ÜST SINIRI: literatürde raporlanan
  doğruluk/F1 aralıkları ve bunların ne kadarının gerçek sinyal, ne kadarının
  metodolojik artefakt (leakage, look-ahead bias, uygunsuz CV) olduğu
- Sinyal-gürültü oranı ve piyasa etkinliği: etkin piyasada yön tahmininin
  neden zor olduğu; araç piyasasının etkinliğinin daha düşük olmasının
  öngörülebilirlik açısından ne anlama geldiği (bu, projenin lehine bir
  argüman mı? literatür ne diyor?)
- Sınıf dengesizliği ve maliyet-duyarlı öğrenme: finansal yön tahmininde
  imbalance'ın nasıl ele alındığı (class weighting, focal loss, resampling,
  threshold tuning) ve hangi yaklaşımın hangi koşulda üstün olduğu
- Değerlendirme metodolojisi: accuracy'nin neden yanıltıcı olduğu, macro-F1 /
  MCC / balanced accuracy tercihleri; "istatistiksel doğruluk" ile "ekonomik
  anlamlılık" arasındaki kopukluk
- Rejim değişimi ve dağılım kayması (concept drift / regime change): finansal
  serilerde eğitim-test dağılım farkının performansı nasıl çökerttiği; rejim
  tespiti ve adaptasyon yaklaşımları — araç piyasasında (kur şoku, vergi
  değişikliği, arz krizi) doğrudan karşılığı olan bir problem
- Reprodüksiyon krizi: finansal ML'de yayınlanan sonuçların bağımsız
  tekrarlanabilirliği üzerine eleştirel literatür (ör. çoklu test / p-hacking,
  backtest overfitting); bir baseline kurarken hangi iddialara güvenilmemeli

HARİÇ (bu fazda raporlanmayacak):
- Label tasarımı ve threshold seçimi (Faz 1'de tamamlandı — tekrarlanmayacak,
  yalnızca gerektiğinde referans verilecek)
- Spesifik model mimarilerinin detaylı karşılaştırması (Faz 6'nın konusu —
  burada yalnızca "hangi model ailesi bu problem sınıfında öne çıkıyor" düzeyinde
  üst bakış)
- Araç piyasasına özgü iktisadi dinamikler (Faz 2'nin konusu)
- Backtest ve validasyon protokollerinin teknik detayı (Faz 7'nin konusu —
  burada yalnızca literatürün bu konudaki UYARILARI raporlanır)

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası literatür.
- Yalnızca kamuya açık kaynaklar.
- Faz 1 bulgularıyla çelişki bulursan bunu AÇIKÇA işaretle ve çapraz-referans ver.
- Bu faz METODOLOJİK DERSLER fazıdır; "şu model %X doğruluk aldı" tarzı puan
  tablosu üretme. Neden-sonuç ve aktarılabilirlik odaklı yaz.

ARAMA STRATEJİSİ (başlangıç noktası; genişletirsen raporla)
EN: stock price direction prediction accuracy realistic upper bound, financial
machine learning backtest overfitting multiple testing, concept drift regime
change financial time series classification, class imbalance cost sensitive
learning financial prediction, macro F1 MCC evaluation financial classification,
market efficiency predictability directional forecasting, reproducibility crisis
financial machine learning, low frequency price direction forecasting commodity
TR: finansal zaman serisi yön tahmini makine öğrenmesi, piyasa etkinliği
öngörülebilirlik

KAYNAK ÖNCELİĞİ: (1) hakemli finansal ML/ekonometri makaleleri ve sistematik
derlemeler, (2) yüksek atıflı working paper (arXiv q-fin, SSRN, NBER),
(3) eleştirel/metodolojik literatür (backtest overfitting, p-hacking).
Blog/tutorial HARİÇ. Hedef: 15-20 nitelikli kaynak.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 03
faz_adi: "Finansal Piyasa Yön Tahmini Literatürü"
tarih: <bugünün tarihi>
kapsam_ozeti: "Finansal yön tahmini literatüründen araç piyasasına aktarılabilir metodolojik dersler ve aktarılamazlık sınırları"
bagimli_oldugu_fazlar: [01]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı (Faz 1 ile tutarlı):
- TL;DR (3-5 madde)
- Key Findings (numaralı, kaynaklı)
- Details:
  1. Giriş: Neden Finansal Literatür? Aktarılabilirlik Çerçevesi
  2. Yön Tahmininde Gerçekçi Performans Üst Sınırı
  3. Sinyal-Gürültü, Piyasa Etkinliği ve Öngörülebilirlik
  4. Sınıf Dengesizliği ve Maliyet-Duyarlı Öğrenme
  5. Değerlendirme Metodolojisi: İstatistiksel vs Ekonomik Anlamlılık
  6. Rejim Değişimi ve Dağılım Kayması
  7. Reprodüksiyon Krizi ve Güvenilmemesi Gereken İddialar
  8. AKTARILABİLİRLİK MATRİSİ (bu fazın ana teslimatı — aşağıya bak)
  9. Açık Sorular / Literatürde Net Olmayanlar
- Recommendations
- Caveats
- Kaynakça (gerekçe notlu)
- Kullanılan Nihai Arama Sorguları

BÖLÜM 8 — AKTARILABİLİRLİK MATRİSİ (zorunlu tablo)

| Finansal Literatür Bulgusu | Dayandığı Piyasa Özelliği | Araç Piyasasında Karşılığı Var mı? | Aktarılabilirlik (yüksek/orta/düşük/yok) | Gerekçe | Uyarlama Gerekiyorsa Nasıl |

Bu tablo, geliştirici ekibin "finansal ML'den neyi alıp neyi almayacağını"
tek bakışta görmesini sağlamalıdır. En az 10 satır.

KALİTE KURALLARI
- Her somut iddiayı kaynağa bağla.
- Bölüm 2-7'nin sonunda "Projeye Uygulanabilirlik" notu.
- Çelişkili bulguları işaretle; özellikle "yüksek doğruluk" iddialarını
  metodolojik eleştiri literatürüyle çaprazla.
- NEGATİF BULGULARI RAPORLA: aktarılamayan yöntemler bu fazın en değerli
  çıktısı olabilir; bunları saklamak yerine öne çıkar.
- "Literatürde net değil" disiplinini koru.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.