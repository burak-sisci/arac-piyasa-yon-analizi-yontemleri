ROL VE BAĞLAM

Sen, araç piyasası fiyat yönü tahmini projesinin repo yöneticisi ve veri
mühendisisin. Görev: kamuya açık kaynaklardan, 2025 yılı için 12 aylık (Ocak–
Aralık 2025) örnek bir MVP veri seti çekmek, temizlemek, birleştirmek ve
commit'lemek. Bu, pipeline'ı ve as-of date mimarisini test etmek için bir
PROTOTİPTİR; model eğitmek için değil (12 gözlem eğitim için yetersizdir, bunu
kabul ediyoruz).

ÇALIŞMA İLKESİ — AŞAMALI VE EKSİKSİZ:
Tek seferde her şeyi çekmeye çalışma. Değişkenleri SIRAYLA, biri tamamen
bitip doğrulanmadan diğerine geçmeden çek. Her aşamadan sonra DUR, çektiğin
veriyi bana özetle ve devam onayı iste. Hız değil, eksiksizlik ve doğruluk esas.

PROJENİN BAĞLAYICI KISITLARI:
- HEDEF: İkinci el araç ilan (asking) fiyatının aylık yönü. İşlem fiyatı değil.
- YALNIZCA KAMUYA AÇIK KAYNAKLAR. Şirket içi/lisanslı/ödeme-duvarı veri yok.
- AS-OF DATE: Her makro değişkenin yayım gecikmesi vardır (ör. Aralık TÜFE'si
  Ocak başında açıklanır). Tabloya "referans_ayi" ve mümkünse "yayim_tarihi"
  sütunu ekle. Bu, ileride sızıntı önlemek için kritik.
- Veri dosyaları data/ altına yazılır ama .gitignore gereği Git-DIŞIDIR; yalnızca
  kod, veri sözlüğü ve raporlar versiyonlanır.
- Bu görev VERİ ÇEKME + TABLO KURMA ile sınırlı. Model eğitme, feature türetme,
  tahmin YOK (sonraki aşama).

ZAMAN KAPSAMI: 2025-01'den 2025-12'ye, aylık. Kod parametrik olsun (başlangıç/
bitiş ayı değişken) — ileride genişletmek kolay olsun.

KAYNAK ÖNCELİK KURALI (her değişken için SIRAYLA dene, ilk çalışanı kullan):
  (A) Resmi API → (B) Resmi açık indirme (CSV/Excel/JSON) → (C) Resmi sayfadan
  HTML/PDF tablo çıkarımı → (D) İkincil güvenilir kaynak → (E) Son çare: manuel
  giriş şablonu üret, benden iste. Hangi seviyeye inildiğini her değişken için
  raporla.

======================================================================
AŞAMA 1 — USD/TRY (en temiz kaynak, önce bununla pipeline'ı kur)
======================================================================
- Kaynak önceliği A: TCMB EVDS API. API anahtarı gerekir — anahtarı KODA GÖMME;
  ortam değişkeni (ör. EVDS_API_KEY) veya benden iste. Anahtarı nereden alacağımı
  bilmiyorsam söyle (TCMB EVDS sitesinden ücretsiz hesap).
- Seri: USD/TRY. Aylık düzeye indirirken HEM ay sonu değeri HEM ay ortalamasını
  ayrı sütun olarak tut.
- Çıktı: data/raw/usdtry_2025_raw.* (ham) + pipeline için ara tablo.
- Aşama sonunda: 12 ayın tamamı geldi mi, eksik ay var mı, hangi kaynak
  seviyesi kullanıldı — özetle ve DUR, onay iste.

======================================================================
AŞAMA 2 — TÜFE / Enflasyon (aynı sistemden, kolay)
======================================================================
- Kaynak önceliği A: TÜİK API veya TCMB EVDS üzerinden TÜFE serisi.
- Sütunlar: tufe_endeks (baz), tufe_aylik_degisim (%). yayim_tarihi ekle
  (TÜFE ilgili ayı takip eden ayın başında açıklanır — as-of date için önemli).
- Çıktı: data/raw/tufe_2025_raw.*
- Aşama sonunda özetle ve DUR, onay iste.

======================================================================
AŞAMA 3 — PROXY FİYAT SERİSİ (en zor; hedefin yer-tutucusu)
======================================================================
- Kaynak: BETAM "sahibindex Otomobil Piyasası Görünümü" 2025 aylık raporları
  (kamuya açık, aylık, ilan-tabanlı). Alternatif: arabam.com kamuya açık aylık
  fiyat endeksi bültenleri.
- Bu kaynaklar makine-okunur API sunmaz; PDF/HTML'den yapılandırılmış çıkarım
  gerekir. Her aydan çıkarabildiğin serileri al: talep endeksi, ortalama/medyan
  ilan fiyatı (cari ve varsa reel), ilan sayısı, satılan/satılık oranı, ilanda
  kalma süresi (days-on-market).
- Çıkardığın HER sayının kaynağını kaydet (rapor tarihi + hangi rapor/sayfa).
- KRİTİK UYARI (veri sözlüğüne yaz): Bu seriler mix/kompozisyon düzeltmesizdir;
  ham ortalama ilan fiyatıdır (karar N1). MVP'de yer-tutucu hedef olarak
  kullanılır, NİHAİ HEDEF DEĞİLDİR. Nihai hedef ileride hedonik düzeltmeyle
  (N10) üretilecek.
- Bu aşamada eksik ay olması muhtemel (rapor yayımlanmamış olabilir). Eksikse
  UYDURMA; "eksik" olarak işaretle ve raporla.
- Aşama sonunda özetle ve DUR, onay iste.

======================================================================
AŞAMA 4 — BİRLEŞTİRME VE BELGELEME
======================================================================
- Üç kaynağı "referans_ayi" (YYYY-MM) anahtarıyla birleştir. Tek satır = tek ay.
  Sütunlar: referans_ayi, usdtry_aysonu, usdtry_ortalama, tufe_endeks,
  tufe_aylik_degisim, proxy_fiyat, proxy_ilan_sayisi, proxy_dom (varsa),
  ve ilgili yayim_tarihi sütunları.
- Çıktı: data/processed/mvp_2025_birlesik.csv (ve tercihen .xlsx).
- VERİ SÖZLÜĞÜ üret: data/processed/veri_sozlugu.md — her sütun için ad, birim,
  kaynak, kaynak seviyesi (A–E), frekans, yayım gecikmesi, bilinen sınırlar
  (özellikle proxy fiyatın mix-düzeltmesiz olduğu).
- ÇEKME RAPORU üret: data/processed/cekme_raporu.md — her değişken hangi
  seviyeden geldi, ne çalıştı/çalışmadı, eksik aylar, kalite uyarıları.

KOD KALİTESİ:
- Her kaynak için ayrı, yorumlu fonksiyon; biri patlarsa diğerini bloklamasın.
- Ağ hatası/boş yanıt/format değişikliğini yakala ve raporla.
- API anahtarı/kimlik ASLA koda gömülmez.
- Tarihler ISO (YYYY-MM); birleştirme ay anahtarıyla.
- Scraping'de nazik ol: robots.txt'ye uy, istekler arası gecikme koy, ödeme/
  login duvarı aşma.

REPO YÖNETİMİ:
- Kod dosyalarını mantıklı bir yere koy (ör. scripts/veri/ altında aşama başına
  bir dosya veya tek modül). Kodları, veri sözlüğünü ve raporları commit'le.
- data/raw ve data/processed içindeki VERİ dosyaları .gitignore gereği
  commit'lenmez — yalnızca .gitkeep'ler durur. Kod + belgeler versiyonlanır.
- Anlamlı Türkçe commit mesajları kullan (ör. "veri: aşama-1 USD/TRY çekimi").
- Her aşama onaylandıktan sonra o aşamayı commit'le ve push'la (push'u kendin yap).

YAPMA:
- Tek seferde tüm aşamaları koşturma; aşama aformı bittikçe DUR ve onay iste.
- Eksik veriyi uydurma; işaretle.
- Model eğitme/feature türetme/tahmin.
- Şirket içi veya lisanslı veri kullanma.
- Veri dosyalarını Git'e ekleme (ilke: veri versiyonlanmaz).

BAŞLANGIÇ: Önce kısa bir çalışma planı sun (hangi aşamada hangi kaynağı hangi
sırayla deneyeceğini), sonra benim onayımla AŞAMA 1'den başla.