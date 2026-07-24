# PM Raporu — Genişletme Aşama 6: Hedef Etiket Üretimi

**Tarih:** 2026-07-23

---

## 1. Ne Yapıldı

Bu oturumun başında, paralel bir başka oturumun (kullanıcı onaylı) TÜFE baz
geçişi, OSD, tüketici güveni, noter devir ve alım gücünü zaten çözüp
`veri_2024_bugun_birlesik.csv`'yi 21 sütundan 30 sütuna çıkardığı tespit
edildi (bkz. `pm_rapor_genisletme_hata_listesi_cozumleri.md` ve
`pm_rapor_genisletme_noter_devir_alim_gucu.md`). Bu rapor yalnızca bu
oturumda net-yeni üretilen kısmı — **hedef etiket** — kapsar.

1. `scripts/veri/genisletme_6_hedef_etiket.py` yazıldı: MVP'nin
   `asama5_temizle_etiketle.py`'daki oynaklık-uyarlamalı (k·σ bandı) +
   tercile etiketleme mantığı, artık tam olan `veri_2024_bugun_birlesik.csv`
   girdisine uygulandı.
2. **Metodolojik karar (PM ile birlikte netleştirildi):** k çarpanı MVP ile
   aynı (0,5) bırakıldı; σ ise MVP'nin güvenilmez 9-gözlemlik tahmini yerine
   bu turda **25 geçerli geçişten** hesaplandı — "30 aylık veriyle
   kalibrasyon" isteği, k'yi değiştirmeden σ'nın güvenilirliğini artırarak
   karşılandı.
3. Çıktı: `data/processed/genisletme/veri_2024_bugun_etiketli.csv/.xlsx`
   (30 satır × 38 sütun — birleşik tablonun 30 sütunu + 8 yeni etiket/yardımcı
   sütun).

---

## 2. Sayısal Özet

**Kullanılan parametreler:** k=0,5; σ_nominal=0,01261; σ_reel=0,01521;
geçerli geçiş sayısı: 25/29 olası (2024-05 ve 2025-02'deki BETAM boşlukları
her biri 2 geçişi NaN bırakıyor).

| Etiket | up | stable | down | eksik |
|---|---|---|---|---|
| `proxy_yon_nominal` | 17 | 7 | **1** | 5 |
| `proxy_yon_reel` | **1** | 8 | 16 | 5 |
| `proxy_yon_tercile` | 8 | 8 | 9 | 5 |

**Kritik bulgu:** Nominal ve reel etiketler neredeyse tam ters yönde skewed.
Nominal seri neredeyse hep "up" (TL değer kaybı/enflasyon nedeniyle ham
fiyat sürekli artıyor); reel seri (TÜFE'ye bölünmüş) neredeyse hep "down"
(enflasyondan arındırılınca piyasa aslında geriliyor). Tercile etiketi,
yapısı gereği dengeli (yaklaşık 1/3'er).

---

## 3. Karşılaşılan Sorunlar (saklanmadı)

### 3.1 Nominal/reel etiketlerde ciddi sınıf dengesizliği
`proxy_yon_nominal`'de yalnızca **1 "down"** ay var (25 geçerli gözlemin
%4'ü); `proxy_yon_reel`'de yalnızca **1 "up"** ay var. Karar kaydı K2'nin
belirttiği "%60 neutral eşiği" burada aşılmıyor (stable oranı ikisinde de
%23-27 arası) — o yüzden metodoloji değişikliği (quantile'a geçiş) K2
kriterine göre TETİKLENMEDİ. Ancak bu, "up/down/stable" sınıflandırmasının
pratikte iki uç sınıftan birinde neredeyse hiç örnek bulunmaması riski
taşıdığını gösteriyor — model eğitiminde (ileride) class-weighting/threshold-
moving (N4) bu yüzden özellikle önemli olacak.

### 3.2 σ hâlâ göreli küçük bir örneklemden (25 gözlem)
MVP'nin 9 gözlemine göre çok daha güvenilir, ama yine de büyük bir örneklem
değil — tek bir aşırı ay σ'yı halen belirgin ölçüde değiştirebilir. Segment-
bazlı/daha uzun pencereli yeniden kalibrasyon ileride (Faz 7 protokolüne
göre N≥80 eşiği) gerekecek.

---

## 4. Veri Örneği (ilk/son 3 satır, kilit sütunlar)

```
referans_ayi  proxy_fiyat_cari_tl  proxy_aylik_log_degisim  proxy_yon_nominal  proxy_yon_reel  proxy_yon_tercile
     2024-01             860443.0                      NaN              eksik           eksik              eksik
     2024-02             855781.0                -0.005433             stable            down               down
     2024-03             859035.0                 0.003795             stable            down               down
     2026-04            1168000.0                 0.006873                 up            down             stable
     2026-05            1175000.0                 0.005975             stable            down               down
     2026-06            1169000.0                -0.005119             stable            down               down
```

---

## 5. Varsayımlar / Kararlar

| Karar | K/N uyumu | Not |
|---|---|---|
| k=0,5 sabit tutuldu, σ 25 gözlemden yeniden hesaplandı | K2 uyumlu (oynaklık-uyarlamalı bant) | PM ile birlikte alınan karar — MVP ile metodolojik tutarlılık + istatistiksel güç dengesi. |
| Hem nominal hem reel hem tercile üretildi | K8/N1 uyumlu (ilan fiyatı ham gösterge, düzeltme modelin işi) | PM'in açık talebi — nominal/reel arasındaki zıt skew, projenin en önemli erken bulgularından biri olarak kaydedildi. |
| Tercile yalnızca nominal log-değişimden üretildi (MVP ile aynı) | — | Reel tercile ayrıca üretilmedi; talep gelirse eklenir. |
| Erişilebilirlik endeksi (2c) bu etikete dahil edilmedi | Bilinçli — 2c hâlâ tanım/formül bekliyor | Ayrı, bloklu kalmaya devam ediyor. |

---

## 6. Açık Sorular / PM Onayı Gerekenler

1. Nominal/reel etiketlerdeki uç-sınıf kıtlığı (1 "down", 1 "up") — model
   eğitim aşamasına geçilince class-weighting stratejisiyle mi ele
   alınacak, yoksa etiketleme yöntemi (örn. quantile'a geçiş) şimdiden mi
   gözden geçirilsin?
2. Erişilebilirlik endeksi (2c) formülü hâlâ netleşmedi — PM ile birlikte
   tanımlanması gerekiyor (örn. "ortalama araç fiyatı / brüt ücret-maaş
   endeksi" gibi bir oran mı olacak?).

---

## 7. Önerilen Sonraki Adım (başlatılmadı — PM onayı bekliyor)

1. Bu raporu ve script'i commit+push et (rule 8 gereği önceden onaylı).
2. Erişilebilirlik endeksi (2c) formülünü PM ile netleştir.
3. MVP (2025) ve genişletme (2024-2026) etiketli tablolarını karşılaştırmalı
   bir şekilde gözden geçir — iki dönem arasında sınıf dağılımı nasıl
   değişmiş, tutarlı mı diye bakılabilir.
