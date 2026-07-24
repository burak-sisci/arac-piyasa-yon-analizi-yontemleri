# PM Raporu — Koşullu Geriye Genişletme (2021-2023) Fizibilite Sonucu

**Tarih:** 2026-07-24

---

## 1. Ne Yapıldı

1. **Kırmızı bayrak taraması** (`data/processed/genisletme/veri_2024_bugun_etiketli.csv`
   üzerinde): tarih sürekliliği, imkânsız değerler, hedef zinciri elle
   doğrulama (3 ay), reel hesap spot kontrolü (3 ay).
2. **CLAUDE.md güncellemesi**: "Otonomi Sınırı — Kullanıcı Gerekli / Gerekli
   Değil" bölümü eklendi (proje sahibinin verdiği metinle, birebir).
   Commit: `67f6005`.
3. **Fizibilite doğrulama**: proje sahibinden gelen "2021-2023 aylık ikinci
   el fiyat verisi kaynak araştırması" çıktısındaki 3 aday kaynak (Eurostat
   HICP CP0711, BETAM Aralık 2023 PDF'i, ODMD/Indicata raporları)
   **bağımsız olarak** test edildi — hiçbiri araştırma çıktısına güvenilerek
   kabul edilmedi; her biri gerçekten fetch/indirilip/okundu.
4. **Karar: genişletme yapılmadı** (Görev 3'ün olumsuz dalı uygulandı — bkz.
   Bölüm 3). Hedef tanımı, kapsam veya k/σ parametreleri değiştirilmedi.

Bu rapor dışında yeni script/veri dosyası üretilmedi (genişletme başlatılmadığı
için Aşama 1-5'in geriye-uzatılmış versiyonları yazılmadı).

---

## 2. Kırmızı Bayrak Sonucu

**TEMİZ — hiçbir hata bulunmadı.**

| Kontrol | Sonuç |
|---|---|
| Tarih sürekliliği (2024-01→2026-06) | 30/30 ay, eksik yok, çift yok |
| İmkânsız değerler (11 sütun, negatif/sıfır) | Yok |
| Aşırı aylık değişim (proxy fiyat >±%50, USD/TRY >±%25) | Yok |
| Hedef zinciri elle doğrulama (2024-03, 2025-04, 2026-06) | `ln(fiyat_t/fiyat_t-1)` elle hesaplanan değer tablodakiyle makine hassasiyetinde eşleşti (fark ~1e-17); üretilen etiketler tabloyla birebir tutarlı |
| Reel hesap spot kontrolü (aynı 3 ay) | `proxy_fiyat/tufe_endeks` üzerinden elle türetilen log-değişim tablodakiyle tam eşleşti |

Genişletmeye (ya da başka bir işleme) engel bir veri kalitesi sorunu yok.

---

## 3. Fizibilite Doğrulama

### Aday 1 — Eurostat HICP CP0711 "Motor cars" (TR, 2015=100)

- **İddia:** Aylık, 1996-2025, TR için erişilebilir; örnek değerler verilmiş.
- **Doğrulama:** Ham JSON gerçekten fetch edildi (WebFetch'in AI-özetlemesi
  ilk denemede YANLIŞ rakamlar üretti — zaman-indeks pozisyonlarıyla karışan
  halüsinasyon; ham veri Python ile ayrıştırılarak doğru okundu). 6 örnek
  ay (2021-01, 2021-12, 2022-06, 2022-12, 2023-06, 2023-12) **birebir
  eşleşti** (283.88 / 444.98 / 533.52 / 583.68 / 782.21 / 1005.30).
  CP07112 (ikinci-el-özel) ve CP07111 (yeni-özel) kırılımlarının TR için
  tamamen boş olduğu da doğrulandı (360/360 pozisyon "no-data").
- **KARAR: KULLANILAMAZ (hedef için).** Erişilebilir ve sayısal olarak
  doğru olmasına rağmen **yanlış büyüklüğü ölçüyor** — CP0711 yeni+ikinci
  el araçları ayrıştırmadan birleştiren bir TÜFE kalemi; salt ikinci el
  fiyat seviyesi bu kaynaktan çıkarılamıyor. Ayrıca TR verisi Eurostat'ın
  kendi "definition differs" bayrağını taşıyor (metodolojik sapma).

### Aday 2 — BETAM Aralık 2023 raporu (tarihsel grafik)

- **İddia:** Ocak 2020'den itibaren aylık tarihsel grafik + birkaç metin
  rakamı içeriyor.
- **Doğrulama:** PDF gerçekten indirilip sayfa-sayfa görüntü olarak açıldı.
  Metindeki iki rakam (Kasım 2023 ortalama fiyat = 879.146 TL; reel endeks
  Haziran 2023=293, Kasım 2023=223) **birebir doğrulandı**. Grafikler
  (Ocak 2020 - Kasım 2023 aralığını kapsayan) gerçekten var ve görüldü.
- **KARAR: KULLANILAMAZ (2021-2023 boşluğu için).** Doğru büyüklüğü
  ölçüyor (aynı BETAM metodolojisi, salt ikinci el) ama grafik çözünürlüğü
  ay-ay kesin değer okumaya yetmiyor — yalnızca kaba, geniş bantlı görsel
  tahminler mümkün (ör. "2022 sonu ~650-750 bin TL" gibi). Asıl 2021-2022
  boşluğu için kesin sayı yok; metinde kesin geçen tek noktalar (Haziran/
  Kasım 2023) zaten hedef boşluğun (2021-2023) en ucunda, çip krizi
  dönemini (2021-2022) hiç kapsamıyor.

### Aday 3 — ODMD / Indicata "İkinci El Online Sektör Raporu"

- **İddia:** Aylık raporlar, 2021-2023'ü kapsıyor, % değişim veriyor.
- **Doğrulama:** AA haberindeki rakam (Aralık 2022, +%4,21) ODMD'de barınan
  PDF'in 7. sayfasında birebir doğrulandı. ANCAK ODMD arşivinde **2021-2023
  için yalnızca YILDA BİR (Aralık) rapor var — toplam 3 PDF**, aylık değil.
  PDF linkleri href değil JS onclick içinde, tahmin edilemez rastgele
  hash'li URL'lerde (görevde verilen URL kalıbı yalnızca en güncel yıla
  özgü, geriye genellenmiyor).
- **KARAR: KULLANILAMAZ (36 aylık seri için).** Doğru yöndeki bir ölçü
  (fiyat değişimi) ama kapsam iddia edilenin çok altında — 3 yıl için 3
  veri noktası (+segment bazlı, agrege olmayan, düşük-güvenilirlik grafik
  etiketleri) sağlıyor, 36 aylık temiz bir seri değil.

### NET KARAR

**Genişletme yapılmadı.** Üç adayın hiçbiri "doğrulanmış + kapsam doğru +
doğru büyüklüğü ölçen + aylık + makine-okunur/güvenilir-çıkarılabilir"
gereksinimlerinin tamamını karşılamıyor. Görev 3'ün olumsuz dalı uygulandı:
hedef tanımı, kapsam veya k/σ parametreleri değiştirilmedi.

---

## 4. Sayısal Özet

Uygulanamadı (genişletme yapılmadığı için yeni bir tablo/sınıf dağılımı yok).
Mevcut veri seti değişmeden kalıyor: `veri_2024_bugun_etiketli.csv`, 30 satır
× 41 sütun, 2024-01→2026-06. Reel etiket dağılımı hâlâ 1 up / 8 stable /
16 down (25 geçerli gözlem) — bu oturumda değişmedi.

---

## 5. Seri Birleştirme Notu

Uygulanamadı — hiçbir kaynak birleştirmeye uygun bulunmadığı için birleştirme
denemesi yapılmadı. (Eğer ileride bir kaynak bulunursa: aynı büyüklüğü ölçen
kaynaklar için zincirleme, farklı büyüklük ölçen kaynaklar için ayrı sütun
ilkesi geçerli olmaya devam ediyor — bu oturumda test edilmedi.)

---

## 6. Veri Örneği

Uygulanamadı — yeni veri üretilmedi. Doğrulama sırasında elde edilen ham
örnekler Bölüm 3'te (her adayın altında) verilmiştir.

---

## 7. Karşılaşılan Sorunlar (saklanmadı)

- Eurostat API'nin WebFetch ile ilk okunmasında **AI-özetleme halüsinasyonu**
  oluştu (zaman-indeks pozisyon numaraları gerçek değer sanıldı) — ham JSON
  Python ile ayrıştırılarak düzeltildi. Bu, projenin genel "dış araç
  çıktısını doğrulamadan kullanma" ilkesinin kendi içinde bir örneği:
  WebFetch'in kendi özetlemesi bile bazen hatalı olabiliyor, ham veriye
  inmek gerekiyor.
- BETAM PDF'indeki grafiklerin çözünürlüğü, otomatik/güvenilir sayısal
  çıkarım için yetersiz — yalnızca insan gözüyle kaba bant tahmini mümkün.
- ODMD'nin PDF bağlantıları JS `onclick` içinde, statik HTML kazımayla
  bulunamıyor; tarayıcı gerekiyor.
- Araştırma çıktısındaki URL kalıbı varsayımı ("AralikYYYY_..._Raporu.pdf")
  yanlış çıktı — gerçek URL'ler yıldan yıla rastgele hash'li, tahmin
  edilemiyor.

---

## 8. Açık Sorular / PM Onayı Gerekenler

1. Reel etiketin şiddetli sınıf dengesizliği (1 up/25) 2021-2023 genişletmesiyle
   çözülemeyeceğine göre, bu sorun nasıl ele alınsın? (Bkz. Bölüm 9 öneriler.)
2. BETAM'a doğrudan ham veri talebi (e-posta ile) gönderilsin mi? Bu, dış
   bir kuruma resmi başvuru anlamına geldiği için "kullanıcı gerekli"
   kategorisine giriyor — CLAUDE.md'deki yeni otonomi sınırı bölümüne göre
   ben başlatmıyorum.
3. Hedef tanımını (3-sınıf → regresyon veya 2-sınıf gibi) değiştirmek proje
   sahibi/PM kararı — ben öneri sunuyorum, değiştirmiyorum (Bölüm 9).

---

## 9. Önerilen Sonraki Adım (başlatılmadı — yalnızca öneri)

Hipotez ("çip krizi = reel yükseliş, eksik up sınıfını kazandırır") veriyle
test EDİLEMEDİ — bu, hipotezin yanlış olduğu anlamına gelmez, yalnızca bu
turda kamuya açık/kolay erişilebilir bir kaynakla doğrulanamadığı anlamına
gelir. Olası yollar (öncelik sırasıyla, hiçbiri başlatılmadı):

1. **BETAM'a doğrudan ham veri talebi** — araştırma çıktısının da işaret
   ettiği gibi, bu tek "temiz" çözüm olurdu (aynı metodoloji, sürekli seri).
   Dış kuruma resmi başvuru gerektirdiği için PM/proje sahibi kararı.
2. **Reel etiket sorununu genişletme dışı çözmek**: sınıf ağırlıklandırma
   (class-weighting) veya threshold-moving (N4'te zaten zorunlu kılınmış
   sıralama) ile mevcut dengesizliği modelleme aşamasında ele almak —
   veri genişletmeye gerek kalmadan.
3. **Hedef tanımını yeniden çerçevelemek** (regresyon: sürekli log-değişimi
   tahmin et, sınıflandırma yerine) — sınıf dengesizliği sorununu kökten
   ortadan kaldırır ama bu K1/K2 düzeyinde bağlayıcı bir karardır, PM
   onayı gerektirir.
4. **Zamanla beklemek**: veri seti her ay büyüyor; farklı bir rejime
   (örn. gelecekte olası bir reel yükseliş dönemi) doğal olarak
   ulaşılabilir — pasif ama sıfır ek risk.
5. Eurostat CP0711, hedef için değil ama **ek bir makro kontrol
   değişkeni** (genel motorlu taşıt TÜFE enflasyonu) olarak mevcut
   2024-2026 penceresinde kullanılabilir — bu ayrı, daha küçük bir öneri,
   bu oturumda başlatılmadı.
