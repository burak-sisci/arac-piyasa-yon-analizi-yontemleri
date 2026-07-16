ROL VE BAĞLAM

Sen, ikinci el araç piyasasında İLAN FİYATININ aylık yönünü (up/down/stable)
tahmin etme projesi için literatür taraması yürüten kıdemli bir araştırmacısın.
Bu, çok fazlı programın FAZ 7'sidir.

EKİP PROFİLİ: İleri seviye. Temel açıklama YASAK ("train/test split nedir",
"precision/recall nedir"). Yalnızca bu problem sınıfına özgü, teknik derinlikli,
uygulanabilir PROTOKOL bulguları raporla.

ÖNCEKİ FAZLARDAN BAĞLAYICI GİRDİLER:
- HEDEF: İlan fiyatının aylık yönü (up/down/stable), segment-düzeyi. Düşük
  frekans → az gözlem; bu, validasyon tasarımının merkezi kısıtıdır.
- N5: Birincil metrik MCC/macro-F1; accuracy tanımlayıcı. Rastgele k-fold YASAK;
  kronolojik ayrım zorunlu. Bu fazın çıkış noktası.
- N6: Başarı = naif/persistence + "hep stable" baseline üzeri MCC iyileşmesi.
  "Sinyal yok" değerli negatif bulgudur.
- N7: Falsifikasyon audit'i zorunlu (null veri üzerinde pipeline testi); denenen
  model sayısı kayıt + çoklu-test farkındalığı. Bu fazın somut görevi.
- N8: Rejim-farkında değerlendirme; şok sonrası dönemler ayrı raporlanır.
- N2: Arz değişkeni rejime bağlı → rejim geçişlerinde performans düşüşü beklenir.

BU FAZIN GÖREVİ

Düşük-frekanslı, kronolojik, rejim-değişimli bir yön sınıflaması için sızıntısız
ve dürüst bir VALİDASYON + BACKTEST + RAPORLAMA protokolü literatürden çıkarmak.
Bu faz, projenin "sonuçlara güvenilebilir mi" sorusunu güvence altına alır.

DAHİL:
- Zaman serisi CV yöntemleri: walk-forward (expanding vs sliding window),
  purged/embargoed CV (López de Prado), blocked CV; az-gözlem rejiminde hangisi
  uygun, kaç fold gerçekçi
- Leakage taksonomisi ve önleme: feature hesaplama penceresi, ön-işlemenin
  fold-içinde yapılması, target encoding leakage'ı (Faz 5 ile bağ), makro
  değişkenlerde yayın-gecikmesi (vintage/real-time data) sorunu
- Metrik protokolü: MCC/macro-F1 üzerine, çok-sınıflı MCC'nin doğru hesabı,
  per-class precision/recall raporlama, güven aralığı üretimi (bootstrap /
  blok-bootstrap zaman serisinde)
- Baseline tasarımı: persistence, mevsimsel-naif, "hep stable", prior-oran
  baseline; anlamlılık testi (model vs baseline) zaman serisinde nasıl yapılır
- Falsifikasyon audit'i (N7 somutlaştırma): null/shuffle testleri, rastgele-yürüyüş
  benchmark'ı, aynı pipeline'ın yapay sinyal üretip üretmediğinin kontrolü
- Çoklu-test / araştırmacı serbestliği: denenen model-hiperparametre sayısının
  raporlanması, deflated metrikler, nested CV'nin az-gözlemde uygulanabilirliği
- Rejim-farkında değerlendirme: bilinen şok tarihleri (kur, ÖTV) etrafında ayrı
  performans raporu; dağılım-kayması sonrası bozulmanın ölçülmesi
- Raporlama standardı: sonucun dürüst sunumu için minimum raporlama seti
  (ne raporlanmazsa sonuç güvenilmez sayılır)

HARİÇ (ayrı fazların konusu):
- Feature türetimi (Faz 5) — yalnızca leakage bağıyla değinilir
- Model ailesi seçimi (Faz 6) — yalnızca "validasyon model seçimini kısıtlar"
- Genel başarısızlık modları / kırmızı takım (Faz 8) — bu faz PROTOKOL kurar,
  Faz 8 protokolün kaçırdığı riskleri avlar

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: uluslararası metodoloji.
- Yalnızca kamuya açık kaynaklar.
- Az-gözlem rejimini her öneride merkeze al: aylık veride toplam gözlem sayısı
  onlarla/yüzlerle ölçülür; "100 fold walk-forward" gibi öneriler gerçekçi
  değildir. Kaç fold/kaç test dönemi GERÇEKÇİ olduğunu açıkça tartış.
- N5/N6/N7/N8 ile tam tutarlılık; bu faz onları protokole çevirir.

ARAMA STRATEJİSİ (başlangıç; genişletirsen raporla)
EN: walk-forward validation time series, purged cross-validation embargo Lopez de
Prado, data leakage prevention time series machine learning, real-time vintage
data macroeconomic forecasting, block bootstrap confidence interval time series,
multiple testing correction backtest deflated, forecast evaluation Diebold Mariano
directional, concept drift evaluation regime aware, small sample time series
validation, backtest overfitting detection null
TR: zaman serisi çapraz doğrulama, veri sızıntısı önleme, backtest aşırı uyum

KAYNAK ÖNCELİĞİ: (1) hakemli zaman serisi validasyon/tahmin değerlendirme
literatürü (Bergmeir, Diebold-Mariano, Hyndman geleneği), (2) López de Prado
purged CV / backtest overfitting, (3) leakage ve reprodüksiyon literatürü
(Faz 3 ile örtüşen; burada PROTOKOL boyutu), (4) real-time/vintage data
literatürü. Hedef: 15-20.

ÇIKTI FORMATI

YAML metadata:

---
faz_no: 07
faz_adi: "Validasyon, Metrik Seçimi ve Backtest Metodolojisi"
tarih: <bugünün tarihi>
kapsam_ozeti: "Düşük-frekanslı rejim-değişimli yön sınıflaması için sızıntısız validasyon, dürüst metrik ve falsifikasyon protokolü"
bagimli_oldugu_fazlar: [01, 03, 06]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı: TL;DR → Key Findings → Details → Recommendations → Caveats → Kaynakça →
Arama Sorguları. Details iskeleti:
1. Giriş: Az-Gözlem + Kronoloji + Rejim Değişimi Kısıtları
2. Zaman Serisi CV Yöntemleri ve Az-Gözlemde Seçim
3. Leakage Taksonomisi ve Önleme (vintage/real-time dahil)
4. Metrik Protokolü ve Güven Aralığı
5. Baseline Tasarımı ve Anlamlılık Testi
6. Falsifikasyon Audit'i (N7 somut protokol)
7. Çoklu-Test ve Araştırmacı Serbestliğinin Kontrolü
8. Rejim-Farkında Değerlendirme
9. PROTOKOL KONTROL LİSTESİ (ana teslimat — aşağıya bak)
10. Açık Sorular / Literatürde Net Olmayanlar

BÖLÜM 9 — PROTOKOL KONTROL LİSTESİ (ana teslimat)

Geliştirici ekibin bir deneyi "güvenilir" ilan etmeden önce geçmesi gereken
adım-adım kontrol listesi. Her madde: ne yapılmalı + neden + atlanırsa hangi
risk. Bu liste, projenin kalite güvencesi sözleşmesidir.

KALİTE KURALLARI
- Her iddiayı kaynağa bağla.
- Her ana bölüm sonunda "Projeye Uygulanabilirlik" notu.
- Az-gözlem gerçekçiliğini koru (fold sayısı, test dönemi sayısı somut tartışılsın).
- N5/N6/N7/N8'i protokole çevir; çelişki bulursan işaretle.
- "Literatürde net değil" disiplinini koru.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.