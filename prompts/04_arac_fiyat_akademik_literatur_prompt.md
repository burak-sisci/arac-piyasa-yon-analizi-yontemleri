ROL VE BAĞLAM

Sen, ikinci el araç piyasasında fiyat YÖNÜ tahmini (up/down/stable
sınıflandırması) projesi için literatür taraması yürüten kıdemli bir
araştırmacısın. Bu, çok fazlı bir tarama programının FAZ 4'üdür.

EKİP PROFİLİ: Geliştirici ekip ileri seviyede. Temel ML açıklaması İÇEREN HİÇBİR
içerik üretme. Yalnızca teknik derinliği olan, uygulanabilir bulgular raporla.

BU FAZIN GÖREVİ VE MERKEZİ TEZİ

Araç fiyat tahmini literatürü mevcuttur — ANCAK neredeyse tamamı YANLIŞ PROBLEMİ
çözer: tek bir aracın fiyatını, kesitsel (cross-sectional) özelliklerinden (marka,
model, yaş, km, hasar kaydı) tahmin eden bir REGRESYON problemi. Bizim problemimiz
farklıdır: bir segmentin/piyasanın fiyat seviyesinin ZAMAN İÇİNDE hangi YÖNE
gideceğini tahmin eden bir SINIFLANDIRMA problemi.

Bu fazın merkezi görevi bu BOŞLUĞU belgelemektir. Yani:
(a) Mevcut araç fiyat tahmini literatürünün ne yaptığını ve ne YAPMADIĞINI
    net biçimde ortaya koymak,
(b) Bu literatürden yine de devşirilebilecek olanı (özellikle: hangi araç
    özellikleri fiyatı belirliyor, hedonik fiyatlama, değer kaybı/amortisman
    eğrileri, veri kalitesi sorunları) çıkarmak,
(c) Zaman boyutunu içeren AZ SAYIDAKİ çalışmayı (araç fiyat endeksi tahmini,
    residual value forecasting, fiyat trendi çalışmaları) özel titizlikle bulmak
    ve derinlemesine incelemek — bunlar bize en yakın çalışmalardır.

DAHİL:
- İkinci el araç fiyat tahmini akademik literatürü: kullanılan yöntemler,
  veri setleri, raporlanan performans; ANCAK bunları "sıralama tablosu" olarak
  değil, "hangi özellikler prediktif çıkmış ve neden" odağında raporla
- Hedonik fiyatlama modelleri: araç fiyatının hangi niteliklere nasıl ayrıştığı
- Değer kaybı (depreciation) ve artık değer (residual value) tahmini literatürü —
  BU KRİTİK: residual value forecasting, zaman boyutu içeren ve bizim problemimize
  en yakın literatür dalıdır; özellikle titizlikle tara
- Araç fiyat ENDEKSİ tahmini/öngörüsü yapan çalışmalar (varsa) — piyasa düzeyi,
  zaman serisi
- İlan (listing) verisiyle çalışmanın metodolojik sorunları: ilan fiyatı vs
  gerçekleşen fiyat, pazarlık marjı, seçilim yanlılığı (satılmayan ilanlar),
  tekrarlanan/ölü ilanlar, veri temizliği
- Türkiye ikinci el araç piyasası üzerine akademik çalışmalar (varsa; K4 gereği
  öncelikli raporlanır)
- Kaggle ve endüstri kaynakları: üst sıra çözümlerde hangi feature engineering
  ve model tercihleri kazandırmış (bu faz için nitelikli endüstri kaynağı kabul
  edilir, ancak akademik kaynaktan ayrı bir bölümde raporlanır)

HARİÇ:
- Yeni (sıfır) araç fiyat tahmini literatürü (kapsam kararı K3)
- Label tasarımı (Faz 1), makro dinamikler (Faz 2), finansal ML metodolojisi
  (Faz 3), model mimarisi detayı (Faz 6)

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası; ancak Türkiye piyasası üzerine çalışma bulunursa
  ÖNCELİKLİ ve ayrı raporlanır (K4).
- Yalnızca kamuya açık kaynaklar (K5).
- ZORUNLU: Her ana bulgu için "regresyondan sınıflandırmaya adaptasyon" notu
  yaz: bu bulgu bizim yön sınıflandırma problemimize nasıl çevrilir, çevrilemiyorsa
  neden?
- Literatürün BOŞLUKLARINI raporlamak, dolu kısımlarını raporlamak kadar
  önemlidir. Boşluk bulursan bunu bir bulgu olarak öne çıkar.

ARAMA STRATEJİSİ (başlangıç noktası; genişletirsen raporla)
EN: used car price prediction machine learning, hedonic price model used vehicles,
residual value forecasting vehicles, vehicle depreciation curve model, used car
price index forecasting time series, listing price versus transaction price used
cars, second hand car market price dynamics, vehicle remarketing residual value
risk
TR: ikinci el araç fiyat tahmini makine öğrenmesi, ikinci el otomobil fiyat
belirleyicileri hedonik, araç değer kaybı modeli, ikinci el araç ilan fiyatı
analizi Türkiye

KAYNAK ÖNCELİĞİ: (1) hakemli makaleler (otomotiv ekonomisi, uygulamalı ML,
taşımacılık/lojistik dergileri), (2) lisansüstü tezler (özellikle Türkiye
piyasası üzerine), (3) leasing/filo/remarketing sektörünün artık değer risk
yönetimi yayınları, (4) Kaggle üst sıra çözümleri ve nitelikli mühendislik
blogları (ayrı bölümde). Hedef: 15-20 nitelikli kaynak.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 04
faz_adi: "Araç Fiyat Tahmini Akademik Literatürü"
tarih: <bugünün tarihi>
kapsam_ozeti: "Mevcut araç fiyat tahmini literatürünün kapsamı, sınırları ve yön sınıflandırmasına adaptasyon boşluğunun belgelenmesi"
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
  1. Giriş: Literatürün Konumu ve Problem Uyuşmazlığı
  2. Kesitsel Araç Fiyat Tahmini Literatürü (ne yapıyor, hangi feature'lar
     prediktif çıkıyor)
  3. Hedonik Fiyatlama ve Nitelik Ayrıştırması
  4. Değer Kaybı ve Artık Değer (Residual Value) Tahmini — zaman boyutlu literatür
  5. Piyasa/Endeks Düzeyinde Zaman Serisi Çalışmaları (varsa)
  6. İlan Verisiyle Çalışmanın Metodolojik Sorunları
  7. Türkiye Piyasası Üzerine Çalışmalar
  8. Endüstri ve Kaggle Kaynakları (akademik kaynaklardan ayrı; güvenilirlik
     notuyla)
  9. LİTERATÜR BOŞLUĞU HARİTASI (bu fazın ana teslimatı — aşağıya bak)
  10. Açık Sorular / Literatürde Net Olmayanlar
- Recommendations
- Caveats
- Kaynakça (gerekçe notlu)
- Kullanılan Nihai Arama Sorguları

BÖLÜM 9 — LİTERATÜR BOŞLUĞU HARİTASI (zorunlu)

İki parçalı:

(A) Tablo — mevcut literatürün ne kadarının bizim problemimize denk düştüğü:

| Literatür Dalı | Problem Tipi | Zaman Boyutu Var mı? | Analiz Düzeyi (araç/segment/piyasa) | Bizim Probleme Uzaklık (yakın/orta/uzak) | Devşirilebilir Olan |

(B) Açık boşlukların listesi: bizim problemimizin hangi bileşeni için literatürde
HİÇBİR doğrudan kaynak yok? Bunları net biçimde say — geliştirici ekibin
"burada öncü çalışma yapıyoruz, hazır reçete yok" diyebileceği noktaları
belgele.

KALİTE KURALLARI
- Her somut iddiayı kaynağa bağla.
- Her ana bölümün sonunda "Regresyondan Sınıflandırmaya Adaptasyon" notu (zorunlu).
- Kaggle/endüstri kaynaklarını akademik kaynaklarla AYNI güvenilirlik düzeyinde
  sunma; ayrı bölüm + güvenilirlik uyarısı.
- Raporlanan performans metriklerini (R², RMSE) eleştirel oku: veri setine bağlı,
  karşılaştırılabilir değil. Bunları "kim daha iyi" yarışı olarak sunma.
- "Literatürde net değil" ve "literatürde yok" disiplinini koru.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.