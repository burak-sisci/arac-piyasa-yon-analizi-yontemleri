ROL VE BAĞLAM

Sen, araç piyasası fiyat yönü tahmini projesinin repo yöneticisi ve veri
mühendisisin. MVP veri çekme (2025, 12 ay) tamamlandı: USD/TRY, TÜFE ve proxy
fiyat serisi çekildi. Şimdi görev: çekilen veriyi TEMİZLEMEK, tutarsızlıkları
GİDERMEK ve modelin HEDEF DEĞİŞKENİNİ (aylık yön etiketi) üretmek.

Bu görevde YENİ KAYNAK ÇEKME yok (yalnızca mevcut boşlukları BETAM raporlarından
teyit hariç). Model EĞİTME yok. Yalnızca temizleme + etiket üretimi.

BAĞLAM — PROJENİN BAĞLAYICI KISITLARI:
- HEDEF: İkinci el araç ilan fiyatının aylık YÖNÜ (up/down/stable).
- Bu proxy fiyat serisi mix/kompozisyon düzeltmesizdir (karar N1). MVP'de
  yer-tutucu hedef olarak kullanılır. Bu aşamada tam hedonik düzeltme YAPILMAZ
  (o sonraki aşama); ancak sınırın veri sözlüğünde belirtilmesi ZORUNLUDUR.
- AS-OF DATE korunur: yayım tarihi sütunları bozulmaz.
- Veri dosyaları Git-dışıdır; kod + veri sözlüğü + rapor commit'lenir.

======================================================================
GÖREV 1 — PROXY FİYAT SERİSİNİ TEK KAYNAĞA SABİTLE
======================================================================
Sorun: proxy_fiyat_2025_raw.csv'de Şubat 2025 satırı BETAM değil arabam.com
kaynağından geliyor (BETAM o ay rapor yayımlamamış). İki farklı kaynağın fiyat
düzeyi birbirine karışmış; bu, aylık değişim hesabını bozar.

Yapılacak:
- Fiyat serisinin OMURGASI olarak BETAM sahibindex "cari fiyat"ı (proxy_fiyat_
  cari_tl) kullan — çünkü 11 ayın tamamı bu kaynaktan, tutarlı.
- Şubat 2025 (BETAM eksik) için: BETAM'ın Mart 2025 raporunu KONTROL ET —
  genelde bu raporlar bir önceki 1-2 ayın revize serisini de içerir; Şubat'ın
  BETAM cari fiyatı orada olabilir. Varsa onu kullan.
- BETAM'da Şubat cari fiyatı gerçekten yoksa: satırı SİLME, ama fiyatı "eksik"
  (NaN) olarak işaretle ve kaynağı ayrı bir sütunda "arabam.com (BETAM eksik)"
  diye tut. Aylık değişim hesabında bu eksikliği doğru ele al (aşağıya bak).
- arabam.com değerini BETAM serisiyle AYNI sütunda karıştırma; ayrı bir
  referans/karşılaştırma sütununda tutulabilir ama omurga tek kaynak olmalı.

======================================================================
GÖREV 2 — YILLIK / AYLIK YÜZDE KARIŞMASINI GİDER
======================================================================
Sorun: CSV'de proxy_fiyat_nominal_yillik_pct gibi sütunlar YILLIK değişimi
tutuyor. Modelin hedefi AYLIK yön. BETAM raporları hem yıllık hem aylık değişim
verir; bunlar karışmamalı.

Yapılacak:
- Her ay için BETAM raporundaki AYLIK değişimi (bir önceki aya kıyasla, hem cari
  hem reel) ayrı ve net sütunlara al: proxy_nominal_aylik_pct, proxy_reel_aylik_pct.
  (Örn. Aralık 2025 raporu: yıllık +%22, AYLIK +%0,6 — bunlar ayrı sütun.)
- Rapordan doğrudan aylık değişim vermiyorsa, cari fiyat serisinden KENDİN
  hesapla: aylik_degisim_t = ln(fiyat_t / fiyat_{t-1}). Log-değişim kullan
  (bileşiklenme ve simetri için).
- Yıllık sütunları silme; ayrı ve etiketli tut. Karışıklığı gider, veriyi atma.

======================================================================
GÖREV 3 — HEDEF DEĞİŞKENİ (AYLIK YÖN ETİKETİ) ÜRET
======================================================================
Bu MVP'nin asıl çıktısı. Karar kaydındaki K1/K2'ye göre:

- Temel büyüklük: mix-düzeltmesiz cari fiyattan aylık log-değişim (Görev 2).
  UYARI olarak veri sözlüğüne yaz: MVP'de mix düzeltmesi yapılmadığından bu
  etiket geçicidir; hedonik düzeltme sonrası (N10) yeniden üretilecektir.
- Eşikleme (K2): Sabit yüzde yerine OYNAKLIK-UYARLI bant kullan. 12 aylık seri
  çok kısa olduğundan (tek segment, ~11 değişim gözlemi), şunu uygula:
    * Serinin aylık log-değişimlerinin standart sapmasını (σ) hesapla.
    * Bant: |değişim| < k·σ ise "stable"; değişim ≥ k·σ ise "up";
      değişim ≤ -k·σ ise "down". Başlangıç k = 0.5 (parametrik yaz, kolay
      değiştirilsin).
  NOT: 12 gözlemle σ tahmini gürültülüdür; bunu veri sözlüğünde açıkça belirt.
  Bu eşik bir PROTOTİP; gerçek seride segment-bazlı ve daha uzun pencereyle
  yeniden kalibre edilecek.
- Alternatif/karşılaştırma etiketi olarak tercile (3 eşit parça) tabanlı bir
  etiket de üret (proxy_yon_tercile) — hangi yöntemin daha dengeli sınıf
  dağılımı verdiğini görmek için. İkisini de sakla.
- Çıktı sütunları: proxy_aylik_log_degisim, proxy_yon_etiketi (up/stable/down),
  proxy_yon_tercile, kullanilan_esik_k, kullanilan_sigma.

REEL Mİ NOMİNAL Mİ:
- Hem nominal hem TÜFE-deflate edilmiş (reel) aylık değişimden ayrı etiket üret
  (proxy_yon_nominal, proxy_yon_reel). Reel için: nominal fiyatı TÜFE endeksiyle
  deflate et, sonra log-değişim. Hangisinin hedef olacağı sonra kararlaştırılır;
  şimdilik ikisini de üret.

======================================================================
GÖREV 4 — BİRLEŞİK TABLO VE BELGELEME
======================================================================
- Üç kaynağı referans_ayi (YYYY-MM) ile birleştir. Tek satır = tek ay.
  Sütunlar: referans_ayi, usdtry_aysonu, usdtry_ortalama, tufe_endeks,
  tufe_aylik_degisim, proxy_fiyat_cari_tl, proxy_nominal_aylik_pct,
  proxy_reel_aylik_pct, proxy_aylik_log_degisim, proxy_yon_nominal,
  proxy_yon_reel, proxy_yon_tercile, proxy_dom_gun, proxy_satis_orani_pct,
  proxy_ilan_sayisi (varsa), + yayım tarihi sütunları.
- Çıktı: data/processed/mvp_2025_etiketli.csv (+ .xlsx).
- VERİ SÖZLÜĞÜNÜ güncelle (data/processed/veri_sozlugu.md): yeni sütunlar +
  şu uyarılar AÇIKÇA yer alsın:
    (a) proxy fiyat mix-düzeltmesiz (N1) — etiket geçici;
    (b) 12 gözlemle σ/eşik gürültülü — prototip;
    (c) Şubat kaynak farkı nasıl ele alındı;
    (d) hedef henüz "ilan fiyatı yönü" (K8) — işlem fiyatı değil.
- TEMİZLEME RAPORU üret (data/processed/temizleme_raporu.md): hangi
  tutarsızlık nasıl giderildi, Şubat nasıl çözüldü, etiket dağılımı
  (kaç up/stable/down çıktı), sınıf dengesi nasıl.

KOD KALİTESİ:
- Parametrik (eşik k, reel/nominal seçimi değişken), yorumlu, tekrar çalıştırılabilir.
- Eksik veriyi (Şubat) doğru ele al; NaN'ı 0 sanma. Log-değişimde eksik ay
  varsa o geçiş için etiket üretme, "eksik" işaretle.
- Kod dosyalarını scripts/veri/ altına koy; commit'le.

REPO YÖNETİMİ:
- Kod + veri sözlüğü + temizleme raporunu commit'le (veri dosyaları .gitignore
  gereği girmez). Türkçe commit mesajı: "veri: temizleme ve aylık yön etiketi üretimi".
- Push'u kendin yap.

YAPMA:
- Yeni dışsal kaynak çekme (ODMD, ÖTV, faiz — sonraki aşama).
- Tam hedonik/mix düzeltmesi (sonraki aşama; şimdi yalnızca uyarı notu).
- Model eğitme, tahmin.
- Eksik veriyi uydurma.

BİTİRİNCE: Kısa rapor — Şubat nasıl çözüldü, yıllık/aylık karışması giderildi mi,
etiket sınıf dağılımı ne (up/stable/down sayıları), hangi eşik kullanıldı, ve
bir sonraki adım (seriyi 2021-2024'e genişletme veya ilk dışsal faktörü ekleme)
için öneri.