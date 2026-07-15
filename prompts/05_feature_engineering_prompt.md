ROL VE BAĞLAM

Sen, ikinci el araç piyasasında İLAN FİYATININ yönünü (up/down/stable
sınıflandırması) tahmin etme projesi için literatür taraması yürüten kıdemli bir
araştırmacısın. Bu, çok fazlı programın FAZ 5'idir. Önceki dört faz tamamlandı.

EKİP PROFİLİ: İleri seviye (model eğitimi, zaman serisi, sınıflandırma
deneyimli). Temel açıklama İÇEREN HİÇBİR içerik üretme ("feature scaling nedir",
"one-hot encoding nasıl yapılır" gibi). Yalnızca bu probleme özgü, teknik
derinliği olan, uygulanabilir bulgular raporla.

ÖNCEKİ FAZLARDAN BAĞLAYICI GİRDİLER (bunları veri kabul et, yeniden tartışma):
- HEDEF: İlan (asking) fiyatının aylık yönü (up/down/stable). İşlem fiyatı değil.
- Faz 2 bir SÜRÜCÜ DEĞİŞKEN HARİTASI üretti: kur (USD/TRY, en baskın), TÜFE,
  taşıt kredisi faizi, tüketici güveni, ÖTV event'leri, ODMD sıfır araç satışı,
  TÜİK noter devri, BETAM days-on-market / satılan-satılık oranı / talep endeksi,
  arabam.com bireysel-kurumsal indirim farkı, yakıt türü payları, LPG payı.
  Bu harita bu fazın BAŞLANGIÇ NOKTASIDIR; feature'a çevrilecektir.
- N1: Kamuya açık Türk endeksleri kompozisyon (mix) düzeltmesizdir; model
  kompozisyon düzeltmesini KENDİ İÇİNDE yapmalı. Bu fazın merkezi görevlerinden.
- N9 devşirilebilir çekirdek: prediktif öznitelik seti (yaş, km, marka/model,
  motor, yakıt, şanzıman, donanım) ve Kaggle veri-temizlik pratikleri.
- N2: Arz değişkeni rejime bağlı çift yönlü — feature olarak da rejim etkileşimi
  düşünülmeli.

BU FAZIN GÖREVİ

Yön sınıflandırması için FEATURE ENGINEERING metodolojisini ve alternatif veri
kaynaklarını literatürden çıkarmak. Odak: hangi feature türleri düşük frekanslı,
segment-düzeyli, ilan-tabanlı bir yön tahmininde prediktif güç taşır ve nasıl
türetilir.

DAHİL:
- Zaman serisi feature'ları: lag'ler, hareketli ortalamalar, momentum, değişim
  oranları, oynaklık ölçütleri (finansal teknik göstergelerin araç piyasasına
  uyarlanması — RSI/MACD analojileri anlamlı mı, yoksa zorlama mı?)
- Makro feature'ların lag yapısı: Faz 2'deki her sürücünün optimal lag'inin
  nasıl belirleneceği (cross-correlation, Granger-tipi ön eleme); literatürde
  düşük frekanslı makro→fiyat lag seçimi nasıl yapılıyor
- KOMPOZİSYON DÜZELTMESİ (N1 gereği kritik): ham segment-ortalama ilan fiyatının
  mix kaymasından nasıl arındırılacağı. Hedonik reziduel, sabit-kompozisyon
  endeksi (Laspeyres/Paasche tarzı), matched-model yöntemleri; bunların
  feature/hedef üretiminde kullanımı
- Segment tasarımı: hangi granülerlik (marka / marka-model / segment-yaş hücresi)
  yön açısından en öngörülebilir ve istatistiksel güce sahip; hücre-seyrekliği
  (sparse cell) sorunu ve çözümleri
- Alternatif/dışsal veri: arama trendi (Google Trends), ilan hacmi/akısı,
  days-on-market, talep endeksi gibi öncü göstergelerin feature olarak değeri;
  literatürde bunların fiyat yönü tahminine katkısına dair kanıt
- Feature seçimi ve leakage riski: hangi feature'lar look-ahead içerir (ör.
  aynı-dönem gerçekleşen büyüklükler), zaman serisinde feature seçimi nasıl
  leakage'sız yapılır
- Kategorik ve metin feature'ları: ilan metni/donanım alanlarından bilgi
  çıkarımı (Kaggle pratikleri), yüksek-kardinaliteli kategorikler (marka-model)
  için hedef-kaçırmayan kodlama (leakage-safe target encoding)

HARİÇ (ayrı fazların konusu):
- Model mimarileri ve algoritma seçimi (Faz 6)
- Validasyon protokolü, CV tasarımı, backtest detayı (Faz 7) — burada yalnızca
  "feature seçimi leakage üretmemeli" ilkesi düzeyinde değinilir
- Label/threshold tasarımı (Faz 1'de tamamlandı)
- Makro dinamiklerin İKTİSADİ açıklaması (Faz 2) — burada yalnızca bunların
  FEATURE'A ÇEVRİLMESİ ele alınır

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası metodoloji; Türkiye-özgü feature'lar Faz 2 haritasından.
- Yalnızca kamuya açık kaynaklar.
- Her feature ailesi için "leakage riski" ve "aylık ufka uygunluk" değerlendir.
- Faz 3'ün metrik/validasyon kararlarıyla (N5, N7) çelişme; feature seçimi
  bölümünde bunlara referans ver.

ARAMA STRATEJİSİ (başlangıç; genişletirsen raporla)
EN: feature engineering time series classification, technical indicators price
direction features, macroeconomic lag selection forecasting, mix adjustment
composition bias price index, hedonic residual index construction, target
encoding leakage time series, Google Trends nowcasting prices, leading indicators
price forecasting used goods, sparse category smoothing hierarchical, matched
model price index used cars
TR: zaman serisi öznitelik mühendisliği, öncü gösterge fiyat tahmini, kompozisyon
etkisi fiyat endeksi düzeltme

KAYNAK ÖNCELİĞİ: (1) hakemli feature engineering / nowcasting / endeks
metodolojisi makaleleri, (2) resmi istatistik kurumu endeks metodoloji
dökümanları (mix adjustment için — Eurostat, BLS, ONS), (3) nitelikli endüstri
pratikleri (leakage-safe encoding). Hedef: 15-20 kaynak.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 05
faz_adi: "Feature Engineering ve Alternatif Veri Kaynakları"
tarih: <bugünün tarihi>
kapsam_ozeti: "Yön sınıflandırması için feature türleri, kompozisyon düzeltmesi, segment tasarımı ve alternatif veri"
bagimli_oldugu_fazlar: [01, 02, 03, 04]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı: TL;DR → Key Findings → Details → Recommendations → Caveats → Kaynakça →
Arama Sorguları. Details iskeleti:
1. Giriş: Faz 2 Sürücü Haritasından Feature'a Geçiş Çerçevesi
2. Zaman Serisi Feature'ları (lag, momentum, oynaklık) ve Araç Piyasasına Uygunluk
3. Makro Feature Lag Seçimi Metodolojisi
4. Kompozisyon Düzeltmesi (N1 çözümü — kritik bölüm)
5. Segment Tasarımı ve Sparse Cell Yönetimi
6. Alternatif/Öncü Veri Kaynakları
7. Kategorik/Metin Feature ve Leakage-Safe Kodlama
8. FEATURE ÜRETİM TABLOSU (ana teslimat — aşağıya bak)
9. Açık Sorular / Literatürde Net Olmayanlar

BÖLÜM 8 — FEATURE ÜRETİM TABLOSU (zorunlu)

| Feature Ailesi | Kaynak Değişken (Faz 2/N9) | Türetim Yöntemi | Aylık Ufka Uygunluk | Leakage Riski | Beklenen Sinyal Türü | Öncelik |

En az 15 satır. "Leakage Riski" için düşük/orta/yüksek + kısa gerekçe.

KALİTE KURALLARI
- Her iddiayı kaynağa bağla.
- Her ana bölüm sonunda "Projeye Uygulanabilirlik" notu.
- Kompozisyon düzeltmesi (Bölüm 4) somut ve uygulanabilir olmalı — N1'in çözümü
  burada verilecek.
- Teknik gösterge analojilerinde "zorlama mı, anlamlı mı" ayrımını açıkça yap.
- "Literatürde net değil" disiplinini koru.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.