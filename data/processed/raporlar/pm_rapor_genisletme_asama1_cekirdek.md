# PM Raporu — Genişletme Aşama 1: Çekirdek Serilerin Genişletilmesi (2024-01 → bugün)

**Tarih:** 2026-07-22
**Kapsam:** USD/TRY (1a), TÜFE (1b), Proxy fiyat/BETAM (1c) — 2024-01'den
içinde bulunulan aya kadar genişletme. MVP (yalnızca 2025) çıktılarının
ÜZERİNE YAZILMADI; ayrı dosyalara yazıldı.

---

## 1. Ne Yapıldı

1. `scripts/veri/genisletme_1a_usdtry.py` — TCMB EVDS3 API, `TP.DK.USD.A/S`,
   2024-01→2026-07 (günlük). Çıktı: `data/raw/usdtry_2024_bugun_gunluk.csv/.xlsx`,
   `usdtry_2024_bugun_aylik.csv/.xlsx`, `usdtry_2024_bugun_raw.json`.
2. `scripts/veri/genisletme_1b_tufe.py` — TCMB EVDS3 API, `TP.FG.J0`,
   2023-12(taban)→2026-07(hedef). Çıktı: `data/raw/tufe_2024_bugun_aylik.csv/.xlsx`,
   `tufe_2024_bugun_tam_donem.csv/.xlsx`, `tufe_2024_bugun_raw.json`.
3. `scripts/veri/genisletme_1c_proxy_fiyat.py` — BETAM sahibindex (28 ay) +
   arabam.com (2 ay, alternatif), 2024-01→2026-06 (WebFetch ile manuel
   doğrulanmış, kaynak alıntılı). Çıktı: `data/raw/proxy_fiyat_2024_bugun_raw.csv/.xlsx`.
4. `prompts/veri/02_temizleme_ve_etiket_prompt.md`, `03_genis_veri_cekme_prompt.md`
   arşivlendi (önceki görev talimatları).
5. Commit + push: aşağıda (bu raporla birlikte tek commit'te).

---

## 2. Sayısal Özet

| Değişken | Kapsam | Satır | Eksik | Kaynak seviyesi |
|---|---|---|---|---|
| USD/TRY (aylık) | 2024-01 → 2026-07 | 31/31 | 0 | A |
| TÜFE (aylık) | 2024-01 → 2026-01 | **25/31** | **6 (2026-02 → 2026-07)** | A |
| Proxy fiyat (BETAM+referans) | 2024-01 → 2026-06 | 30/30 | 2 BETAM-cari (2024-05, 2025-02; arabam.com ile referans dolduruldu) | C (28 ay) / D (2 ay) |

USD/TRY ve proxy fiyat "içinde bulunulan aya kadar" istenen kapsamı
karşılıyor (proxy'nin kendi yapısal 1-aylık yayım gecikmesiyle sınırlı olarak
— bkz. Bölüm 3). **TÜFE 2026-01'den sonra durdu — bu bir kod hatası değil,
kaynağın kendisinde bir değişiklik** (bkz. Bölüm 3).

---

## 3. Karşılaşılan Sorunlar (saklanmadı)

### 3.1 TÜFE: 2026-02'den itibaren EVDS'ten veri gelmiyor (ÇÖZÜLEMEDİ — PM'e bırakıldı)

`TP.FG.J0` serisi doğrudan sorgulandığında (2026-01→2026-07 aralığı) yalnızca
**1 gözlem** (2026-01) döndü — kod hatası değil, EVDS'in kendisinde veri yok.
Araştırdım: TÜİK, **Ocak 2026'dan itibaren TÜFE'yi 2003=100 bazından
2025=100 bazına geçirdi** (AB uyum süreci, ECOICOP v2 sınıflandırması —
kaynak: tcmbblog.org, "2026 Yılı Tüketici Fiyat Endeksindeki Güncellemeler
ve Etkileri"). Bağımsız haber taramasıyla TÜİK'in **Haziran 2026 enflasyonunu
gerçekten açıkladığını doğruladım** (haber3.com, Capital.com.tr, 3 Temmuz
2026 tarihli) — yani veri TÜİK'te VAR, ama muhtemelen `TP.FG.J0` eski-baz
kodu yeni veriyle güncellenmiyor; yeni bazın EVDS kodu farklı olmalı.

**Denediğim ve başarısız olan:** 6 farklı olası seri kodu (`TP.FG.J1`,
`TP.FG2.J0`, `TP.FG25.J0`, `TP.FG.J025`, `TP.TUFE25.J0`, `TP.FE.OKTG01`) —
hepsi HTTP 400 veya boş sonuç verdi. EVDS'in resmi seri kataloğuna (SPA,
sunucu-taraflı render edilmiyor) otomatik erişemedim.

**Bunu "hata" kategorisine bırakıyorum — birlikte çözelim:** Doğru EVDS seri
kodu ya TCMB EVDS arayüzünden (evds3.tcmb.gov.tr, "Tüm Seriler" ekranı,
manuel arama) ya da TÜİK'in kendi veri portalından bulunmalı. Alternatif:
TÜİK'in web bültenlerinden (B seviyesi) doğrudan endeks değerini çekmek.

### 3.2 Proxy fiyat: BİRİNCİ boşluk teyit edildi, İKİNCİ boşluk yeni bulundu

- **2025-02 (Şubat):** Önceki (MVP) aşamada zaten biliniyordu — BETAM "Mart 2025"
  raporu hiç yayımlanmamış.
- **2024-05 (Mayıs) — YENİ TESPİT:** Aynı desen tekrarladı — BETAM "Haziran 2024"
  raporu da hiç yayımlanmamış (doğrudan URL denemesi 404 verdi; web araması
  "Temmuz 2024" raporunun doğrudan Haziran verisine atladığını, Mayıs'ın hiç
  ayrı bir rapor konusu olmadığını doğruladı). İki durumda da arabam.com'dan
  yalnızca FİYAT (referans sütununda) dolduruldu, diğer alanlar (DOM, satış
  oranı, talep endeksi) uydurulmadı.
- **Desen artık 2 kez doğrulandı:** BETAM zaman zaman bir ayı tamamen atlıyor
  (rapor yayımlamıyor), sonraki rapor da o ayı geriye dönük telafi etmiyor.
  Bu, projenin genel bir varsayımı olarak not edilmeli: **proxy fiyat
  serisinde BETAM kaynaklı, öngörülemeyen aylık boşluklar olağan kabul
  edilmelidir.**

### 3.3 Kapsam sınırı: proxy fiyat 2026-06'da bitiyor, USD/TRY 2026-07'ye kadar gidiyor

Bu bir hata değil, BETAM'ın kendi 1-aylık yayım gecikmesinin yapısal sonucu
(Temmuz 2026 raporu Haziran 2026 verisini verir; Ağustos 2026 raporu
yayımlanmadan Temmuz 2026 verisi elde edilemez). Aşama 5'te (birleştirme)
tabloyu 2026-06'da kesmeyi öneriyorum — aksi halde son satır proxy_fiyat'ta
NaN olur.

---

## 4. Veri Örneği (ham)

**USD/TRY aylık — ilk 3 / son 3 satır:**
```
referans_ayi  usdtry_aysonu  usdtry_ortalama
     2024-01       30.33260        30.026725
     2024-02       31.14810        30.731800
     2024-03       32.28865        31.957981
     2026-05       45.67230        45.355869
     2026-06       46.59705        46.176875
     2026-07       47.15585        46.859003
```

**TÜFE aylık — son 3 gelen satır (2026-01'de kesiliyor):**
```
referans_ayi  tufe_endeks  tufe_aylik_degisim  tufe_yillik_degisim
     2025-11      3482.96            0.865022           31.074841
     2025-12      3513.87            0.887464           30.892328
     2026-01      3683.83            4.836832           30.648485
```

**Proxy fiyat — ilk 3 / son 3 satır:**
```
referans_ayi  proxy_fiyat_cari_tl  kaynak_rapor_basligi
     2024-01             860443.0                Şubat 2024
     2024-02             855781.0                 Mart 2024
     2024-03             859035.0                Nisan 2024
     2026-04            1168000.0                Mayıs 2026
     2026-05            1175000.0               Haziran 2026
     2026-06            1169000.0                Temmuz 2026
```

---

## 5. Kaynak Doğruluğu (bağımsız teyit için)

| Sayı | Kaynak URL | Orijinal ifade |
|---|---|---|
| USD/TRY 2024-01 ay-sonu: 30,3326 | TCMB EVDS3 API (`TP.DK.USD.A/S`) | API JSON yanıtı, doğrudan sayısal |
| TÜFE 2026-01: 3683,83 | TCMB EVDS3 API (`TP.FG.J0`) | API JSON yanıtı: `{"Tarih":"2026-1","TP_FG_J0":"3683.83000000"}` |
| Proxy 2024-01: 860.443 TL | [BETAM Şubat 2024](https://betam.bahcesehir.edu.tr/2024/03/sahibindex-otomobil-piyasasi-gorunumu-subat-2024/) | "Ortalama satılık otomobil cari fiyatı geçen yılın ocak ayına göre yüzde 50,9 artmış, aralığa kıyasla ise değişmemiştir." (860.480'e çok yakın Aralık 2023 değeriyle çapraz-tutarlı) |
| Proxy 2024-05 (referans): 913.190 TL | [AA — arabam.com Mayıs](https://www.aa.com.tr/tr/isdunyasi/otomotiv/arabamcom-mayis-ayi-ikinci-el-ilan-verilerini-paylasti/702807) | "nisan ayında 912 bin 45 lira olan ilan fiyatları mayıs ayında ortalama 913 bin 190 lira oldu." |
| TÜFE rebase gerekçesi | [TCMB Blog](https://tcmbblog.org/wps/wcm/connect/blog/tr/main+menu/analizler/2026+yili+tuketici+fiyat+endeksindeki+guncellemeler+ve+etkileri) | "TÜFE'de temel yıl 2003=100'den 2025=100'e güncellendi... Ocak 2026'dan itibaren." |

---

## 6. Varsayımlar / Kararlar

| Karar | K/N uyumu | Not |
|---|---|---|
| MVP çıktılarının üzerine yazılmaması, ayrı dosya isimleri (`*_2024_bugun_*`) | Rule 4 ruhuyla uyumlu (var olan çıktıları bozma) | Kendi kararım — talimat açıkça belirtmemişti ama "MVP prototip" ile "genişletilmiş" veriyi karıştırmamak mantıklı göründü. |
| TÜFE'de yeni seri kodu bulunamayınca ısrar etmeyip PM'e bırakma | Görev talimatına uygun ("hata aldıklarını sona bırak") | — |
| Proxy 2024-05 için de arabam.com fallback (Şubat 2025 ile aynı yöntem) | K5 (yalnızca kamuya açık) ile uyumlu | Tutarlılık için aynı yöntem tekrarlandı. |
| Proxy serisini 2026-06'da kesme önerisi (2026-07 değil) | K-N'ye aykırı değil, veri gerçekliği | Aşama 5'te uygulanacak, henüz uygulanmadı. |

---

## 7. Açık Sorular / PM Onayı Gerekenler

1. **TÜFE'nin doğru 2025=100 seri kodu nedir?** Ben bulamadım (6 deneme
   başarısız); EVDS arayüzünden manuel bakılması gerekebilir, ya da TÜİK
   portalına (B seviyesi) geçilmesi gerekebilir.
2. **TÜFE 2026-02→07 boşluğu doldurulana kadar Aşama 5 (birleştirme) nasıl
   ilerlesin?** NaN bırakılıp devam mı edilsin, yoksa TÜFE tamamlanana kadar
   mı beklensin?
3. Aşama 2'ye (noter + alım gücü) devam ediyorum — onayınla, yoksa burada
   duracağım.

---

## 8. Önerilen Sonraki Adım

TÜFE seri kodu sorunu **Aşama 5'i (birleştirme) bloklayabilir** (reel
etiketler için TÜFE şart) — bu yüzden bu sorunun mümkün olan en kısa sürede
(PM ile birlikte) çözülmesini öneriyorum. Bu arada Aşama 2-4'e devam
ediyorum (görev talimatın gereği "tüm aşamaları dene").
