ROL VE BAĞLAM

Sen, bir araç piyasası fiyat yönü tahmin projesinin literatür tarama sürecini
planlayan kıdemli bir araştırma lideri olarak davranacaksın.

PROJE: İkinci el / yeni araç piyasasında fiyatların gelecekte yükselip
yükselmeyeceğini (yön sınıflandırması: up / down / stable) tahmin eden bir ML
sistemi geliştirilecek. Bizim işimiz sistemin kendisini kurmak değil; geliştirici
ekibin "gelmiş geçmiş en iyi baseline" ile işe başlamasını sağlayacak, literatüre
dayalı bir bilgi tabanı (dökümanlar + sunum) oluşturmak.

EKİP PROFİLİ: Geliştirici ekip ileri seviyede. Model eğitimi, zaman serisi,
sınıflandırma konularında deneyimliler. Temel ML bilgisi içeren hiçbir içerik
üretilmeyecek; yalnızca bu probleme özgü, teknik derinliği olan, uygulanabilir
bulgular hedeflenecek.

ÇALIŞMA ŞEKLİ: Bu iş tek seferde değil, zamana yayılmış birden fazla oturumda
yapılacak. Her oturum bir "faz" olacak ve her fazın çıktısı bağımsız bir Markdown
dökümanı olacak. Fazlar birbirinin üzerine inşa edilecek. En sonda tüm fazlar bir
sentez dökümanına ve bir karar-odaklı sunuma dönüştürülecek.

SENİN BU OTURUMDAKİ GÖREVİN: Literatür taraması YAPMA. Sadece aşağıdaki master
planı üret:

1. FAZ LİSTESİ
   - Taramayı mantıksal fazlara böl (tahminen 5-8 faz; sen gerekçelendirerek karar ver).
   - Aday faz konuları (bunları değerlendir, gerekirse değiştir/birleştir/ekle):
     a. Problem çerçeveleme ve label tasarımı literatürü (sınıf sayısı, tahmin ufku,
        threshold seçimi)
     b. Finansal piyasa yön tahmini literatürü (hisse/kripto/emtia — en olgun alan)
     c. Araç fiyat tahmini akademik literatürü
     d. Feature engineering ve alternatif veri kaynakları
     e. Model mimarileri ve ensemble stratejileri
     f. Validasyon, metrik seçimi, backtest metodolojisi
     g. Araç piyasasına özgü dinamikler (kur, vergi, arz şokları, EV geçişi,
        Türkiye'ye özgü faktörler)
     h. Başarısızlık modları, tuzaklar, data leakage riskleri

2. HER FAZ İÇİN
   - Fazın amacı ve kapsamı (ne dahil, ne HARİÇ)
   - Aranacak anahtar kelimeler / arama stratejisi (EN + TR)
   - Beklenen çıktı dökümanının başlık iskeleti (section outline)
   - Bu fazın hangi önceki fazlara bağımlı olduğu
   - Tahmini derinlik: kaç kaynak hedefleniyor, hangi kaynak türleri öncelikli

3. FAZ SIRALAMASI VE GEREKÇESİ
   - Fazların hangi sırayla yapılması gerektiğini ve nedenini açıkla.
   - Hangi fazlar paralel yapılabilir, hangileri sıralı olmalı?

4. DOSYA VE İSİMLENDİRME STANDARDI
   - Tüm faz çıktıları için tutarlı bir dosya isimlendirme şeması öner
     (ör. 01_problem_cerceveleme.md).
   - Her dökümanın başında yer alacak standart metadata bloğunu tanımla
     (faz no, tarih, kapsam, bağımlı olduğu fazlar, durum).

5. KALİTE KRİTERLERİ
   - Bir faz çıktısının "tamamlandı" sayılması için karşılaması gereken
     kontrol listesi (ör. her iddia kaynaklı mı, temel bilgi sızmış mı,
     projeye uygulanabilirlik notu var mı).

6. SENTEZ VE SUNUM PLANI
   - Tüm fazlar bittiğinde üretilecek sentez dökümanının ve sunumun iskeletini
     taslak olarak öner.

KISITLAR
- Bu oturumda kaynak arama/tarama YAPMA. Sadece plan üret.
- Plan Türkçe yazılsın.
- Her kararını kısaca gerekçelendir; gerekçesiz madde listesi verme.
- Emin olmadığın veya bana sorman gereken noktaları planın sonunda
  "Onaya/Karara Bağlı Noktalar" başlığı altında topla.