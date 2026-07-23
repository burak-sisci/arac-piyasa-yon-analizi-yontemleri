# PM Raporu — Genişletme: Hata Listesi Çözümleri (TÜFE, OSD, Tüketici Güveni)

**Tarih:** 2026-07-23

---

## 1. Ne Yapıldı

Önceki oturumda (`pm_rapor_genisletme_asama2_5.md`, Bölüm 7) bloklu bırakılan
kalemlerden **üçü**, bu oturumda yeni bir yöntemle çözüldü: **TCMB EVDS3'ün
kendi web arayüzü**, JavaScript render edebilen bir tarayıcı aracıyla (WebFetch
değil) gezilerek doğru seri kodları bulundu — önceki oturumlarda hep "EVDS
seri kataloğuna otomatik erişilemedi" diye not düşülen engel bu şekilde aşıldı.

1. **TÜFE 2026-02→06 boşluğu ÇÖZÜLDÜ.** Yeni EVDS kodu bulundu:
   `TP.TUKFIY2025.GENEL` (2025=100 baz). `scripts/veri/genisletme_1b_tufe.py`
   güncellendi: eski seri (`TP.FG.J0`, 2003=100) ile yeni seri arasında
   **zincirleme (chaining)** uygulanıyor — ortak ay olan 2026-01'de her iki
   serinin de değeri kullanılarak bir ölçek katsayısı hesaplanıyor
   (31,831245), yeni serinin tüm değerleri bu katsayıyla eski ölçeğe
   taşınıyor. Bu standart bir istatistiksel rebasing yöntemidir; yüzde
   değişimler matematiksel olarak etkilenmez.
2. **OSD üretim/ihracat (3b) ÇÖZÜLDÜ** — PDF taramaya hiç gerek kalmadan.
   TCMB EVDS3'te "Otomotiv Sanayii Üretimi (OSD)" adıyla doğrudan bir
   kategori bulundu: `TP.UR.S08` (Binek/otomobil), `TP.UR.S11` (Kamyonet).
   Yeni script: `scripts/veri/genisletme_3b_osd.py`.
3. **Tüketici güven endeksi (3d'nin ikinci yarısı) ÇÖZÜLDÜ.** Doğru kod:
   `TP.TG2.Y01`. **Ek bulgu:** aynı ankette doğrudan araca özgü bir soru daha
   var — **"Otomobil satın alma ihtimali (gelecek 12 aylık dönemde)"**
   (`TP.TG2.Y17`) — genel güven endeksinden daha doğrudan bir öncü gösterge
   olabileceği için o da çekildi. Yeni script:
   `scripts/veri/genisletme_3d_tuketici_guveni.py`.
4. `scripts/veri/genisletme_5_birlestir.py` güncellendi (OSD + tüketici
   güveni birleştirmeye eklendi) ve yeniden çalıştırıldı.

**Yöntem notu (önemli, tekrar kullanılabilir):** `evds3.tcmb.gov.tr`'nin
web arayüzü bir SPA'dır (WebFetch okuyamıyordu — önceki oturumlarda TÜİK veri
portalı için de aynı sorun yaşanmıştı). JS render eden bir tarayıcı aracıyla
siteye girilip üst kısımdaki arama kutusuna terim yazıldığında (ör. "TÜFE",
"Otomotiv Sanayii Üretimi", "Tüketici Güven Endeksi") ilgili kategori
bulunuyor, kategoriye tıklanınca sağ panelde seri listesi ve checkbox'ların
yanında **gerçek EVDS kodu** (ör. `TP.TUKFIY2025.GENEL`) görünüyor. Bu kod
API'ye aynı şekilde (`series=` parametresi, `key` header'ı) verilip
doğrulandı. **Bu yöntem henüz denenmemiş kalemler için de (2a, 2b) ilk
sırada denenmeli** — TÜİK veri portalı EVDS'inkinden farklı bir sistem olsa
da aynı teknik (tarayıcı + arama kutusu) işe yarayabilir.

---

## 2. Sayısal Özet

| Kalem | Önce | Sonra |
|---|---|---|
| TÜFE (`tufe_endeks`) | 25/31 ay (2026-02→06 eksik) | **30/31 ay** (yalnızca 2026-07 eksik — henüz yayımlanmadı, TÜİK genelde ayın 3'ünde açıklıyor) |
| OSD (binek+kamyonet) | 0/31 (hiç yoktu) | **30/31 ay**, 0 eksik hücre |
| Tüketici güven endeksi | 0/31 (hiç yoktu) | **31/31 ay, 0 eksik hücre** |
| Otomobil satın alma ihtimali endeksi | yoktu (yeni sütun) | **31/31 ay, 0 eksik hücre** |

**`veri_2024_bugun_birlesik.csv` güncel durumu:** 30 satır × **26 sütun**
(önceki 21 sütundan), 2024-01→2026-06. Toplam eksik hücre: 76/780 (%9,7 —
önceki turdaki %15,2'den düştü).

---

## 3. Karşılaşılan Sorunlar

Bu turda **yeni bir sorun çıkmadı** — sadece önceki turun bloklarını çözdük.
Tek küçük not: `genisletme_1b_tufe.py`'de zincirleme katsayısı hesaplanırken
ortak ayın (2026-01) her iki seride de bulunması gerekiyor; bu kontrol
script'e eklendi (`if eski_ortak.empty or yeni_ortak.empty: sys.exit(1)`),
gelecekte ortak ay kayması durumunda script sessizce yanlış veri üretmek
yerine açıkça hata verecek.

---

## 4. Veri Örneği

**TÜFE zincirleme geçişi (2025-12 → 2026-02, `tufe_2024_bugun_aylik.csv`):**
```
referans_ayi  tufe_endeks  tufe_aylik_degisim  tufe_baz_kaynagi
     2025-12  3513.870000            0.887464  TP.FG.J0 (2003=100), ham
     2026-01  3683.830000            4.836832  TP.FG.J0 (2003=100), ham
     2026-02  3793.011171            2.963795  TP.TUKFIY2025.GENEL (2025=100) x 31.831245 zincirleme katsayisi
```

**OSD (`osd_2024_bugun_aylik.csv`), ilk/son satır:**
```
referans_ayi  osd_binek_adet  osd_kamyonet_adet  osd_binek_kamyonet_toplam_adet
     2024-01         67059.0            33507.0                        100566.0
     2026-06         67113.0            41354.0                        108467.0
```

**Tüketici güveni (`tuketici_guveni_2024_bugun_aylik.csv`), ilk/son satır:**
```
referans_ayi  tuketici_guven_endeksi  otomobil_satinalma_ihtimali_endeksi
     2024-01               80.423109                            15.982470
     2026-07               89.829717                            26.693396
```

**Kaynak doğruluğu (ham API yanıtları, doğrudan alıntı):**
| Sayı | Kaynak | Ham API yanıtı |
|---|---|---|
| TÜFE 2026-02 (yeni baz): 119,16 | `TP.TUKFIY2025.GENEL` | `{"Tarih":"2026-2","TP_TUKFIY2025_GENEL":"119.16000000"}` |
| OSD 2024-01 Binek: 67.059 adet | `TP.UR.S08` | `{"Tarih":"2024-1","TP_UR_S08":"67059.00000000"}` |
| Tüketici güven endeksi 2024-01: 80,42 | `TP.TG2.Y01` | `{"Tarih":"2024-1","TP_TG2_Y01":"80.42310949"}` |

---

## 5. Varsayımlar / Kararlar

| Karar | K/N uyumu | Not |
|---|---|---|
| TÜFE zincirleme (rebasing) katsayısı 2026-01 ortak ayından hesaplandı | Standart istatistik pratiği (TÜİK/TCMB'nin kendisi de baz değiştirirken bu yöntemi kullanır) | Kendi kararım — dokümante edildi, `tufe_baz_kaynagi` sütunuyla izlenebilir kılındı. **Sonuç ölçek olarak ne resmi 2003=100'e ne 2025=100'e birebir eşittir** — türetilmiş/zincirlenmiş bir ölçektir, bu açıkça işaretlendi. |
| OSD'de yalnızca Binek + Kamyonet çekildi (Çekici/Kamyon/Midibüs/Minibüs/Otobüs/Traktör hariç) | K1 (yolcu taşıtları piyasası kapsamı) | Kendi kararım — projenin kapsamı dışı kalan ağır ticari araç kategorileri çekilmedi. |
| Tüketici güveninde ek olarak "Otomobil satın alma ihtimali" sorusu da eklendi | Görev talimatına ek bir bulgu, zarar vermiyor | Kendi kararım — proje için genel endeksten daha doğrudan bir sinyal olabilir düşüncesiyle. |

---

## 6. Açık Sorular / PM Onayı Gerekenler

1. **Kalan 3 bloklu kalem (2a noter devir, 2b alım gücü, 2c erişilebilirlik)
   için aynı "tarayıcı + EVDS arama kutusu" yöntemi TÜİK veri portalında
   denensin mi?** TÜİK'in portalı EVDS'ten farklı bir sistem, bu yüzden
   başarı garantisi yok, ama en azından denenmemiş bir yol.
2. **Hedef etiket üretimine şimdi geçilsin mi?** TÜFE artık 2026-06'ya kadar
   tam (yalnızca 2026-07 eksik, yapısal/normal bir gecikme) — reel etiket
   için artık bir engel yok.

---

## 7. Önerilen Sonraki Adım (başlatılmadı — PM onayı bekliyor)

1. Hedef etiket üretimi (nominal + reel + tercile, MVP'deki `asama5`
   yöntemiyle) — artık TÜFE engeli olmadığı için tam 2024-01→2026-06 aralığı
   için üretilebilir.
2. Kalan 3 kalem (2a/2b/2c) için TÜİK veri portalını tarayıcı aracıyla
   tekrar dene.
