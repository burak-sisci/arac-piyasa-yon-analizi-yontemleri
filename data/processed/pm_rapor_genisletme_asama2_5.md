# PM Raporu — Genişletme Aşama 2-5: Talep/Likidite, Dışsal Sürücüler, ÖTV Olayları, Birleştirme

**Tarih:** 2026-07-22
**Yöntem notu:** Talimat "tüm aşamaları 2 kez yapmayı dene, hata aldıklarını
sona bırak, birlikte yaparız" idi — bu yüzden Aşama 2→5 arasında DURMADAN,
her kalemi (başarısız olanlarda 2 deneme sonrası) sırayla işledim. Aşağıda
hem başarılanlar hem BLOKLANANLAR (hep birlikte çözülecek) eksiksiz listeli.

---

## 1. Ne Yapıldı

**Başarılı (script + veri üretildi):**
1. `scripts/veri/genisletme_3a_odmd.py` — ODMD sıfır araç satışı (toplam +
   otomobil-yalnız), 2024-01→2026-06. **Verimlilik notu:** WebFetch PDF
   metnini okuyamadı (ham stream); Claude'un kendi PDF-görüntü okuyucusuyla
   (Read aracı) okundu. Her ODMD bülteni ekinde ("Ek 1/2/3") 2010'dan beri
   TÜM ayların tablosunu yayımladığı keşfedildi — bu sayede **30 ay için 30
   ayrı PDF yerine yalnızca 2 güncel bülten** (3 Aralık 2024 + 2 Haziran 2026)
   yeterli oldu.
2. `scripts/veri/genisletme_3c_faiz.py` — Taşıt kredisi faizi (`TP.KTF12`,
   haftalık→aylık) + politika faizi (`TP.APIFON4`, günlük→aylık), TCMB EVDS3,
   2024-01→2026-07, **31/31 ay, ilk denemede tam başarı**.
3. `scripts/veri/genisletme_4_otv_olaylari.py` — ÖTV event-dummy. Araştırma:
   pencerede tek büyük, iyi-belgelenmiş olay bulundu (24 Temmuz 2025, 7555
   sayılı Kanun + 10115 sayılı CB Kararı).
4. `scripts/veri/genisletme_5_birlestir.py` — Tüm genişletilmiş serilerin
   birleştirilmesi. Çıktı: `data/processed/veri_2024_bugun_birlesik.csv/.xlsx`
   (30 satır × 21 sütun, 2024-01→2026-06).

**BLOKLANDI (2 deneme sonrası bırakıldı — birlikte çözülecek):**
- 2a: Noter devir adedi (TÜİK veri portalı)
- 2b: Alım gücü proxy'si (TÜİK reel kazanç/asgari ücret)
- 2c: Erişilebilirlik endeksi (2a/2b'ye bağımlı, otomatik bloklandı)
- 3b: OSD üretim/ihracat
- 3d (yarısı): Tüketici güven endeksi (politika faizi kısmı BAŞARILI oldu)
- TÜFE: 2026-02'den itibaren 6 ay (Aşama 1'de raporlanmıştı, burada da
  birleştirilmiş tabloyu etkiliyor — bkz. Bölüm 3)

**Henüz yapılmadı (bilinçli olarak — talimat gereği):** Hedef etiket üretimi
(k·sigma bandı, nominal/reel/tercile). Bu, TÜFE boşluğu çözülmeden REEL
etiket için 2026-02-06'yı sağlıklı üretemez; bu yüzden Aşama 5'i yalnızca
"birleştirme" ile sınırlı tuttum, etiketlemeyi PM onayına bıraktım.

---

## 2. Sayısal Özet

**`veri_2024_bugun_birlesik.csv`:** 30 satır × 21 sütun, 2024-01→2026-06.
Toplam eksik hücre: 96/630 (%15,2).

| Sütun grubu | Kapsam | Eksik | Kaynak seviyesi |
|---|---|---|---|
| USD/TRY | 2024-01→2026-06 (tam) | 0 | A |
| TÜFE | 2024-01→2026-01 | **5 ay eksik (2026-02→06)** | A |
| Proxy fiyat (BETAM-only omurga) | 2024-01→2026-06 | 2 ay eksik (2024-05, 2025-02 — arabam.com referansla dolduruldu) | C(28)/D(2) |
| Taşıt kredisi faizi, politika faizi | 2024-01→2026-06 | 0 | A |
| ODMD toplam | 2024-01→2026-06 | 0 | C |
| ODMD otomobil-yalnız | 2024-01→2026-06 | 1 ay (2026-06, kaynak yalnız toplam verdi) | C |
| ÖTV event-dummy | 2024-01→2026-06 | 0 (yapı gereği) | C |

**Kapsam dışı bırakılan (bloklu) değişkenler:** noter devir adedi, alım gücü
proxy'si, erişilebilirlik endeksi, OSD üretim/ihracat, tüketici güveni —
bunlar tabloda YOK (sütun olarak bile eklenmedi, çünkü veri hiç çekilemedi).

---

## 3. Karşılaşılan Sorunlar (saklanmadı, gruplu)

### 3.1 TÜİK web portalı (veriportali.tuik.gov.tr) — WebFetch ile erişilemiyor
2 kez denedim (ana sayfa + belirli bir bülten sayfası): ikisi de **boş içerik**
döndürdü. Kök neden muhtemelen JS-render edilen SPA (EVDS2'nin bilinen
sorunuyla aynı kategori). Bu, **2a (noter devir) ve 2b (alım gücü)'nün ikisini
de bloke etti**; 2c bunlara bağımlı olduğundan o da bloklandı.
**Denenmemiş alternatif:** TÜİK bültenlerinin PDF versiyonları (ODMD'de işe
yarayan "PDF indir + Claude'un kendi PDF okuyucusuyla oku" yöntemi) burada
denenmedi — zaman/öncelik nedeniyle. **Bu, ilk denenecek çözüm önerisi.**

### 3.2 EVDS: bazı seri kodları tahminle bulunamadı
- Tüketici güven endeksi: 7 farklı kod denendi (`TP.TUKGUVEN`, `TP.TGE01`,
  `TP.TUKETICIGUVEN`, `TP.GUVENTUK`, `TP.TG01`, `TP.TUK.GUVEN`, `TP.TGUVENE`)
  — hepsi HTTP 400. **Taşıt kredisi faizi ve politika faizi kodları (`TP.KTF12`,
  `TP.APIFON4`) İLK denemede bulundu** — yani yöntem/erişim sorunu değil,
  yalnızca doğru kod tahmin edilemedi.

### 3.3 OSD (Otomotiv Sanayii Derneği) — temiz aylık tablo bulunamadı
2 deneme (site navigasyonu + istatistikler sayfası): yalnızca **yıllık
kataloglar** (PDF) bulundu, ODMD'deki gibi "Ek 1/2/3 tam aylık tarihçe"
formatında bir tablo görülmedi. Üçüncü bir deneme (OSD'nin kendi "aylık basın
bülteni" kategorisini, ODMD yöntemiyle PDF-oku yaklaşarak) denenmedi.

### 3.4 TÜFE 2026-02+ (Aşama 1'den devam eden, hâlâ çözülmedi)
Detay Aşama 1 raporunda (`pm_rapor_genisletme_asama1_cekirdek.md`). Özet:
TÜİK Ocak 2026'da CPI'yi 2025=100 bazına geçirdi; eski `TP.FG.J0` kodu
Ocak 2026'dan sonra güncellenmiyor; yeni kodu bulamadım (6 deneme).

### 3.5 ODMD — BAŞARI hikayesi (karşı-örnek olarak not edilmeli)
Bu, "PDF'i WebFetch okuyamıyor" sorununun HER ZAMAN blokleyici olmadığının
kanıtı: Claude'un kendi PDF-görüntü okuyucusu (Read aracı) devreye
sokulduğunda ve kaynağın kendi "çok-yıllık özet tablosu" formatı
keşfedildiğinde, 30 aylık bir seri yalnızca 2 belge ile tamamlanabildi. **Bu
yöntem 2a/2b (TÜİK) ve 3b (OSD) için de denenmelidir** — henüz denenmedi.

---

## 4. Veri Örneği (ham, `veri_2024_bugun_birlesik.csv`)

**İlk 3 satır (seçili sütunlar):**
```
referans_ayi  usdtry_aysonu  tufe_endeks  proxy_fiyat_cari_tl  tasit_kredisi_faiz  politika_faizi  odmd_toplam_adet  otv_event_ay_mi
     2024-01       30.3326      1984.02             860443.0             41.5775       42.703182             79701                0
     2024-02       31.1481      2073.88             855781.0             40.9650       45.239524            105990                0
     2024-03       32.2887      2139.47             859035.0             42.3020       47.287619            109828                0
```

**Son 3 satır:**
```
referans_ayi  usdtry_aysonu  tufe_endeks  proxy_fiyat_cari_tl  tasit_kredisi_faiz  politika_faizi  odmd_toplam_adet  otv_event_ay_mi
     2026-04      45.02555          NaN            1168000.0              36.615            40.0            104298                0
     2026-05      45.67230          NaN            1175000.0              38.426            40.0             83442                0
     2026-06      46.59705          NaN            1169000.0              40.335            40.0            105041                0
```
(NaN'lar: TÜFE 2026-02'den itibaren eksik — bkz. Bölüm 3.4.)

---

## 5. Kaynak Doğruluğu (bağımsız teyit için, örnek)

| Sayı | Kaynak | Orijinal ifade |
|---|---|---|
| Taşıt kredisi faizi (2024-01, haftalık ilk gözlem): %42,10 | TCMB EVDS3 `TP.KTF12` | API JSON: `{"Tarih":"05-01-2024","TP_KTF12":"42.10000000"}` |
| ODMD toplam 2024-Kasım: 121.094 adet | [ODMD Basın Bülteni 3 Aralık 2024](https://www.odmd.org.tr/folders/2837/categorial1docs/4791/ODMD%20Bas%C4%B1n%20Bulteni%203%20Aral%C4%B1k%202024.pdf), s.2 | "2024 Kasım ayında otomobil ve hafif ticari araç pazarı 2023 yılı Kasım ayına göre %5,3 artarak 121.094 adet oldu." |
| ODMD 2025 tam yıl toplam: 191.620 (Aralık) | [ODMD Basın Bülteni 2 Haziran 2026](https://www.odmd.org.tr/folders/2837/categorial1docs/6111/ODMD%20Bas%C4%B1n%20Bulteni%202%20Haziran%202026.docx.pdf), s.8 (Ek 1 tablosu) | Tablo satırı: "2025 ... Aralık: 191.620" |
| ÖTV düzenlemesi 24 Temmuz 2025 | [verginet.net Vergi Sirküleri 2025-74](https://www.verginet.net/dtt/11/Vergi-Sirkuleri-2025-74.aspx) | "23 Temmuz 2025 tarihli ve 7555 sayılı Kanun'un 13. maddesi... 10115 sayılı Cumhurbaşkanı Kararı ile 24 Temmuz 2025 tarihinden itibaren geçerli..." |

---

## 6. Varsayımlar / Kararlar

| Karar | K/N uyumu | Not |
|---|---|---|
| Hedef aralığı 2026-06'da kesme (2026-07 değil) | Veri gerçekliği (proxy+ODMD'nin yapısal gecikmesi) | Kendi kararım, gerekçeli. |
| Hedef etiket üretimini bu turda YAPMAMA | Talimatla uyumlu (TÜFE eksikken reel etiket sağlıksız olurdu) | Kendi kararım — "eksik veriyi uydurma" ilkesini etiket seviyesinde de uyguladım. |
| ODMD için PDF-görüntü okuma yöntemi | Kaynak seviyesi C'ye uygun (resmi sayfa/PDF çıkarımı) | Yöntemsel keşif — dokümante edildi, tekrar kullanılabilir. |
| Bloklanan kalemlerin sütun olarak bile eklenmemesi (kısmi/tahmini doldurmama) | "Eksik veriyi uydurma" ilkesi | — |

---

## 7. Açık Sorular / PM Onayı Gerekenler

1. **TÜİK verilerine (2a, 2b) ODMD'de işe yarayan "PDF-görüntü okuma" yöntemi
   denensin mi?** Muhtemelen çözer, ama zaman/token maliyeti var (Kural 9).
2. **OSD (3b) için aynı yöntem denensin mi?**
3. **TÜFE yeni seri kodu — EVDS arayüzünden (evds3.tcmb.gov.tr, manuel giriş
   gerektirebilir) birlikte mi bakalım?**
4. **Hedef etiket üretimine ne zaman geçilsin?** TÜFE boşluğu kapanmadan mı
   (yalnızca nominal etiket, 2026-02-06 için reel olmadan), yoksa boşluk
   kapanana kadar mı beklensin?
5. Tüketici güveni (3d'nin ikinci yarısı) ve OSD, görev talimatında sırasıyla
   "opsiyonel" ve zorunlu olarak geçiyordu — tüketici güveni düşük öncelikli
   sayılabilir, OSD daha kritik olabilir.

---

## 8. Önerilen Sonraki Adım (başlatılmadı — PM onayı bekliyor)

Öncelik sırası önerim:
1. **TÜFE yeni seri kodu** — bunsuz reel etiket 2026-02'den sonra hep eksik
   kalır, bu en çok "downstream" işi bloke eden kalem.
2. **TÜİK noter devir (2a) — ODMD yöntemiyle (PDF-görüntü okuma) tekrar
   dene** — kanıtlanmış bir yöntem var, uygulanmadı.
3. Hedef etiket üretimi (yalnızca nominal, TÜFE beklenirken paralel
   yapılabilir).
4. OSD, alım gücü proxy'si, tüketici güveni — daha düşük öncelik.

**Bu adımları BEN BAŞLATMIYORUM — PM ile birlikte karar verilecek.**
