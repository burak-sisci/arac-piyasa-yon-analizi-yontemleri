# PM Raporu — Genişletme: Noter Devir ve Alım Gücü Çözümleri

**Tarih:** 2026-07-23

---

## 1. Ne Yapıldı

Aynı oturumda, TÜFE/OSD/tüketici güveni çözüldükten sonra kalan iki kalem
de aynı "tarayıcı ile SPA'yı gez" yöntemiyle çözüldü — bu kez EVDS değil,
**TÜİK'in kendi veri portalı** (veriportali.tuik.gov.tr) üzerinde.

1. **Noter devir adedi (2a) ÇÖZÜLDÜ.** TÜİK'in "Motorlu Kara Taşıtları"
   aylık bültenlerinde, "Tablolar" bölümünde doğrudan indirilebilir bir
   `.xls` dosyası bulundu: "Aylara göre devri yapılan motorlu kara
   taşıtları sayısı". Bu tablo yalnızca **cari yıl + bir önceki yılı**
   içeriyor (ODMD'nin aksine tam tarihçe değil), bu yüzden **2 bülten**
   kullanıldı: "Aralık 2025" bülteni (2024 tam yıl + 2025 tam yıl) ve
   "Haziran 2026" bülteni (2025 çapraz-doğrulama + 2026 Ocak-Haziran).
   Yeni script: `scripts/veri/genisletme_2a_noter_devir.py`. **30/30 ay,
   sıfır eksik.**
2. **Alım gücü proxy'si (2b) ÇÖZÜLDÜ.** TÜİK'in "İşgücü Girdi Endeksleri"
   bülteninde (en güncel: I. Çeyrek 2026) bulunan "İşgücü Girdi Endeksleri
   (2021=100).xls" tablosu **tek başına 2009-2026 arası tam çeyreklik
   tarihçeyi** içeriyordu (ODMD tarzı, tek belge yeterli oldu). "Brüt
   ücret-maaş endeksi" (toplam ekonomi, arındırılmamış) sütunu çekildi.
   **Bu veri ÇEYREKLİK** olduğu için her çeyreğin değeri o çeyreğin 3 ayına
   aynen kopyalanarak aylık tabloya genişletildi (`alim_gucu_ceyrek` sütunu
   hangi çeyreğin değeri olduğunu açıkça işaretliyor — gerçek ay-ay
   varyasyon UYDURULMADI). Yeni script:
   `scripts/veri/genisletme_2b_alim_gucu.py`. **27/30 ay** (yalnızca
   2026-Q2/Nisan-Haziran eksik — henüz yayımlanmadı, bir sonraki bülten
   21 Ağustos 2026).
3. **Kritik doğrulama:** Noter devir tablosundaki Haziran 2026 rakamları
   (941.964 adet toplam, %64,6 otomobil) önceki oturumda WebSearch'ten
   toplanan ve "2024" diye etiketlenmiş rakamlarla **birebir aynı** çıktı
   — bu, önceden şüphelenilen **yıl-karışması hatasının kesin kanıtı**
   oldu. Ayrıca resmi tabloyla karşılaştırınca, önceki WebSearch
   bulgularından "Şubat 2024" ve "Mayıs 2024" değerlerinin de YANLIŞ
   (sırasıyla 2025 ve 2026'ya ait) olduğu doğrulandı; "Ocak 2024" ve
   "Mart 2024" ise doğru çıkmıştı. Bu eski değerlerin HİÇBİRİ bu script'te
   kullanılmadı — hepsi resmi tablodan sıfırdan yeniden alındı.
4. `scripts/veri/genisletme_5_birlestir.py` güncellendi (her iki kalem de
   birleştirmeye eklendi) ve yeniden çalıştırıldı.

---

## 2. Sayısal Özet

**`veri_2024_bugun_birlesik.csv` — oturum başı/sonu karşılaştırması:**

| | Oturum başı | Oturum sonu |
|---|---|---|
| Sütun sayısı | 21 | **30** |
| Eksik hücre oranı | %15,2 (96/630) | **%9,1 (82/900)** |
| Bloklu/eksik ana değişken | TÜFE (6 ay), OSD (tamamı), tüketici güveni (tamamı), noter devir (tamamı), alım gücü (tamamı) | Yalnızca 2c (erişilebilirlik endeksi — tanım bekliyor) |

| Kalem | Kapsam | Eksik |
|---|---|---|
| Noter devir (toplam + otomobil) | 2024-01→2026-06 | **0/30** |
| Alım gücü (brüt ücret-maaş endeksi) | 2024-01→2026-06 | 3/30 (2026-Q2, henüz yayımlanmadı) |

---

## 3. Karşılaşılan Sorunlar

### 3.1 TÜİK'in noter devir tablosu ODMD gibi değil (yalnızca 2 yıl)
ODMD'nin bültenleri her seferinde 2010'dan bugüne TÜM tarihçeyi
yayımlıyordu; TÜİK'in "Aylara göre devri..." tablosu yalnızca **cari yıl +
bir önceki yılı** gösteriyor. Çözüm: 2 farklı tarihli bülten kullanıldı
(Aralık 2025 + Haziran 2026), ODMD'dekiyle aynı verimlilikte (2 belge)
sonuca ulaşıldı.

### 3.2 Alım gücü verisi çeyreklik, aylık değil
TÜİK bu anketi (İşgücü Girdi Endeksleri) aylık değil çeyreklik yayımlıyor.
Aylık veri setine eklemek için çeyrek değeri 3 aya aynen kopyalandı — bu,
**gerçek ay-ay değişimi YANSITMAZ**, yalnızca çeyrek-çeyrek değişimi
yansıtır. `alim_gucu_ceyrek` sütunuyla açıkça işaretlendi. Model eğitiminde
bu sütun kullanılacaksa bu sınırlama dikkate alınmalı.

### 3.3 Yıl-karışması hatası kesin olarak doğrulandı (Bölüm 1.3'e bkz.)
Önceki oturumda "hata" olarak işaretlenen WebSearch güvenilirlik sorunu,
bu turda resmi veriyle karşılaştırılarak **kanıtlandı**. Proje için genel
ders: TÜİK/EVDS gibi kaynaklardan WebSearch ile toplanan sayısal veri,
resmi kaynakla (tercihen indirilebilir tablo/API) çapraz doğrulanmadan
kullanılmamalı.

---

## 4. Veri Örneği

**Noter devir (`noter_devir_2024_bugun_aylik.csv`), ilk/son satır:**
```
referans_ayi  noter_devir_toplam_adet  noter_devir_otomobil_adet
     2024-01                   782589                     530744
     2026-06                   941964                     608484
```

**Alım gücü (`alim_gucu_2024_bugun_aylik.csv`), ilk/son satır:**
```
referans_ayi  brut_ucret_maas_endeksi_2021_100  alim_gucu_ceyrek
     2024-01                        693.111053           2024-Q1
     2026-03                       1374.314470           2026-Q1
```

**Kaynak doğruluğu:**
| Sayı | Kaynak | Doğrulama |
|---|---|---|
| Haziran 2026 noter devir toplam: 941.964 | [Motorlu Kara Taşıtları - Haziran 2026](https://veriportali.tuik.gov.tr/tr/press/58043) | Bülten metninde birebir: "Haziran ayında 941 bin 964 adet taşıtın devri yapıldı" |
| 2026-Q1 brüt ücret-maaş endeksi yıllık değişim: %37,0 | [İşgücü Girdi Endeksleri - I. Çeyrek 2026](https://veriportali.tuik.gov.tr/tr/press/57966) | Ham tablo hesap kontrolü: 1374,31/1002,94 = 1,3703 → %37,03 ≈ bülten metnindeki "%37,0" |

---

## 5. Varsayımlar / Kararlar

| Karar | K/N uyumu | Not |
|---|---|---|
| Noter devir için 2 bülten (Aralık 2025 + Haziran 2026) kullanıldı, 2025 değerleri çapraz-doğrulandı | Doğrulanabilirlik ilkesi | Kendi kararım — iki bültendeki 2025 rakamları birebir eşleşti, tutarlılık teyit edildi. |
| Alım gücü çeyreklik veri, aya "aynen kopyalanarak" (gerçek aylık varyasyon uydurulmadan) genişletildi | "Eksik/bilinmeyen veriyi uydurma" ilkesi | Kendi kararım — alternatif (enterpolasyon) daha "pürüzsüz" görünür ama var olmayan bilgi uydurmuş olurdu; ham çeyreklik tekrar daha dürüst. |
| Erişilebilirlik endeksi (2c) BU TURDA HESAPLANMADI | "Kaynaksız iddia yazılmaz" + PM onayı gereken bir tanım sorunu | Kendi kararım — "erişilebilirlik" için kesin formül (ör. kaç aylık maaşa bir araç) proje talimatında net değildi, PM'siz varsayım yapmak istemedim. |

---

## 6. Açık Sorular / PM Onayı Gerekenler

1. **Erişilebilirlik endeksi (2c) nasıl tanımlanmalı?** Örnek aday formül:
   `proxy_fiyat_cari_tl / brut_ucret_maas_endeksi_2021_100` (kaç "ücret
   birimi" bir araca eşdeğer) — ama bu benim tahminim, PM onayı gerekir.
2. **Hedef etiket üretimine şimdi geçilsin mi?** Artık TÜFE, OSD, tüketici
   güveni, noter devir, alım gücü hepsi mevcut — kapsam dışı kalan tek
   şey 2c (tanımı belirsiz, ayrı bir karar).

---

## 7. Önerilen Sonraki Adım (başlatılmadı — PM onayı bekliyor)

1. Hedef etiket üretimi (nominal + reel + tercile) — artık tüm ana
   dışsal sürücüler mevcut, bekleyen tek şey PM onayı.
2. Erişilebilirlik endeksi (2c) — formül PM ile netleşince eklenebilir.
