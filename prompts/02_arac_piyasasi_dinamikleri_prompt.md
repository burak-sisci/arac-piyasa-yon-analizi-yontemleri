ROL VE BAĞLAM

Sen, ikinci el araç piyasasında fiyat yönü tahmini (up/down/stable sınıflandırması)
projesi için literatür taraması yürüten kıdemli bir araştırmacısın. Bu, çok fazlı
bir tarama programının FAZ 2'sidir.

EKİP PROFİLİ: Geliştirici ekip ileri seviyede (model eğitimi, zaman serisi,
sınıflandırma deneyimli). Temel ML/istatistik veya temel iktisat açıklaması
İÇEREN HİÇBİR içerik üretme. Yalnızca bu probleme özgü, teknik derinliği olan,
uygulanabilir bulgular raporla.

BU FAZIN GÖREVİ

İkinci el araç fiyatlarını sürükleyen İKTİSADİ VE PİYASA DİNAMİKLERİNİ,
Türkiye odağıyla, MODELLENEBİLİR değişkenler olarak haritalamak. Amaç sektörel
bir "durum raporu" yazmak DEĞİL; her dinamiği (a) hangi gözlemlenebilir
göstergeyle ölçüleceği, (b) hangi frekansta ve hangi kaynaktan elde edileceği,
(c) fiyata etkisinin hangi gecikmeyle (lag) ortaya çıktığı, (d) etkinin yönü ve
büyüklüğüne dair ampirik kanıt olup olmadığı açısından değerlendirmek.

DAHİL:
- Makro sürücüler: enflasyon, döviz kuru (özellikle ithal araç ve yedek parça
  kanalı), faiz oranları ve taşıt kredisi koşulları, hanehalkı satın alma gücü
- Politika/regülasyon: ÖTV ve matrah dilimi değişiklikleri, ithalat düzenlemeleri,
  hurda teşviki benzeri programlar; bunların ikinci el fiyatlarına geçiş
  mekanizması ve tarihsel örnekleri
- Arz yönlü şoklar: sıfır araç arz kısıtları (ör. yarı iletken krizi dönemi),
  teslimat süreleri, üretim/ithalat hacimleri — bunların ikinci el fiyat primine
  etkisi
- Talep yönlü ve yapısal faktörler: mevsimsellik, model yılı geçişleri, elektrikli
  araç yaygınlaşmasının ikinci el ICE ve EV fiyatlarına etkisi (özellikle EV
  değer kaybı literatürü)
- Piyasa mikro yapısı: ilan (listing) fiyatı ile gerçekleşen işlem fiyatı
  arasındaki fark, ilanda kalma süresi (days-on-market), stok/likidite
  göstergelerinin fiyat yönüyle ilişkisi
- Mevcut endeksler ve ölçüm altyapısı: Türkiye'de ve uluslararası (ör. Manheim
  UVVI benzeri) ikinci el araç fiyat endeksleri; metodolojileri (karma/kilometre
  düzeltmesi, hedonik regresyon), yayın frekansları ve erişilebilirlikleri

HARİÇ (bu fazda raporlanmayacak):
- Yeni araç fiyat TAHMİNİ literatürü (yeni araç yalnızca ikinci eli etkileyen
  dışsal faktör olarak ele alınır — bkz. kapsam kararı K3)
- Model mimarileri ve algoritmalar (ayrı faz)
- Label tasarımı / threshold seçimi (Faz 1'de tamamlandı)
- Genel feature engineering teknikleri (ayrı faz) — burada yalnızca HANGİ
  değişkenlerin var olduğu ve nereden geldiği raporlanır, nasıl işleneceği değil

KAPSAM KARARLARI (bağlayıcı):
- Coğrafya: Bu faz TÜRKİYE ODAKLIDIR. Uluslararası çalışmalar yalnızca (a)
  Türkiye'de karşılığı olan bir mekanizmayı açıklıyorsa veya (b) Türkiye'de
  eşdeğeri olmayan bir ölçüm/endeks metodolojisi sunuyorsa dahil edilir.
- Yalnızca kamuya açık kaynaklar kullanılacak. Hiçbir şirket içi veri veya
  yayınlanmamış bilgi kullanılmayacak. Şirketlerin (Arabam.com dahil) yalnızca
  kamuya açık yayınları (fiyat endeksi, basın bülteni, açık rapor) kaynak
  gösterilebilir.
- Faz 1 bulgusu bağlayıcıdır: tahmin ufku büyük olasılıkla AYLIK olacaktır.
  Her dinamiği bu ufka göre değerlendir: aylık frekansta gözlemlenebilir mi,
  aylık ölçekte fiyata etkisi ölçülebilir mi?

ARAMA STRATEJİSİ (başlangıç noktası; genişletirsen genişlettiğini raporla)
TR: ikinci el araç fiyat endeksi Türkiye, ÖTV matrah değişikliği ikinci el araç
fiyatları, taşıt kredisi ikinci el otomobil talebi, otomotiv arz krizi ikinci el
fiyat, elektrikli araç ikinci el değer kaybı, sıfır araç teslimat süresi ikinci
el fiyat, TÜİK motorlu kara taşıtları istatistikleri, ODMD otomotiv verileri
EN: used car price index methodology, used vehicle residual value determinants,
EV depreciation residual value used market, semiconductor shortage used car prices,
days on market listing price used vehicles, hedonic price index used cars,
exchange rate pass-through automobile prices

KAYNAK ÖNCELİĞİ: (1) hakemli iktisat/otomotiv ekonomisi makaleleri, (2) resmi
kurum yayınları (TÜİK, TCMB, ODMD/OSD, Ticaret Bakanlığı, Eurostat, BLS),
(3) nitelikli sektör raporları ve endeks metodoloji dökümanları (Cox
Automotive/Manheim, Deloitte/PwC otomotiv raporları), (4) merkez bankası
çalışma tebliğleri. Pazarlama amaçlı blog ve forum içeriği HARİÇ.
Hedef: 15-20 nitelikli kaynak.

ÇIKTI FORMATI

Tek bir Markdown dökümanı üret. YAML metadata bloğu:

---
faz_no: 02
faz_adi: "Araç Piyasası Dinamikleri (Türkiye Odaklı)"
tarih: <bugünün tarihi>
kapsam_ozeti: "İkinci el araç fiyatlarını sürükleyen makro, politika, arz-talep ve mikro yapı faktörlerinin modellenebilir değişkenler olarak haritalanması"
bagimli_oldugu_fazlar: [01]
durum: taslak
hedef_kaynak_sayisi: 18
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Yapı (Faz 1 ile tutarlı olsun):
- TL;DR (3-5 madde)
- Key Findings (numaralı, kaynaklı)
- Details:
  1. Giriş ve Kapsam
  2. Makro Sürücüler (kur, enflasyon, faiz, kredi)
  3. Politika ve Regülasyon Kanalı (ÖTV, matrah, ithalat)
  4. Arz Yönlü Şoklar ve Yeni Araç Piyasasının Yansıması
  5. Talep Yönlü ve Yapısal Faktörler (mevsimsellik, EV geçişi)
  6. Piyasa Mikro Yapısı (ilan vs işlem fiyatı, days-on-market, stok)
  7. Mevcut Fiyat Endeksleri ve Ölçüm Metodolojileri
  8. SÜRÜCÜ DEĞİŞKEN HARİTASI (bu fazın ana teslimatı — aşağıya bak)
  9. Açık Sorular / Literatürde Net Olmayanlar
- Recommendations
- Caveats
- Kaynakça (her kaynak için "neden ilgili" notu)
- Kullanılan Nihai Arama Sorguları

BÖLÜM 8 — SÜRÜCÜ DEĞİŞKEN HARİTASI (zorunlu tablo formatı)

Her sürücü için tek satır:

| Sürücü | Gözlemlenebilir Gösterge | Kaynak | Frekans | Beklenen Lag | Etki Yönü | Ampirik Kanıt Gücü | Erişilebilirlik | Araç Piyasasına Notlar |

"Ampirik Kanıt Gücü" için üç kademe kullan: güçlü (hakemli, replike edilmiş) /
orta (tek çalışma veya sektör raporu) / zayıf (anekdot, teorik beklenti).
"Erişilebilirlik" için: kamuya açık-ücretsiz / kamuya açık-ücretli / erişilemez.

KALİTE KURALLARI
- Her somut iddiayı kaynağa bağla (kurum/yazar + yıl, mümkünse link/DOI).
- Bölüm 2-7'nin her birinin sonunda kısa "Projeye Uygulanabilirlik" notu ver.
- Çelişkili bulguları açıkça işaretle.
- Türkiye için veri bulunamayan noktalarda uluslararası bulguyu aktarırken
  aktarılabilirlik sınırını AÇIKÇA belirt (ör. "ABD toptan piyasası verisi;
  Türkiye'de ilan-tabanlı perakende piyasa için doğrulanmamıştır").
- "Literatürde net değil" disiplinini koru; tahmin yürütme.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.