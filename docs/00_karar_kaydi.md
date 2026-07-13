---
dokuman_tipi: karar_kaydi
proje: "Araç Piyasası Fiyat Yönü Tahmini — Literatür Taraması"
tarih: 2026-07-13
iliskili_dokuman: 00_master_plan_literatur_taramasi.md
durum: onaylandi
---

# Karar Kaydı — Master Plan Açık Noktaları

Master planın "Onaya/Karara Bağlı Noktalar" bölümündeki 7 madde, proje sahibi ve
proje yöneticisi (PM agent) tarafından aşağıdaki gibi karara bağlanmıştır. Bu
kararlar tüm faz promptlarına ve dökümanlarına bağlayıcıdır. Master plan bu karar
kaydı ile birlikte ONAYLANMIŞ sayılır.

## Kararlar

**K1 — Tahmin ufku:** Ön tercih dayatılmayacak. Faz 1, literatürdeki ufuk
seçeneklerini trade-off'larıyla sunacak; nihai karar Faz 1 çıktısı gözden
geçirilerek verilecek. (Stajdaki ekipten iş tarafı beklentisi öğrenilirse bu
kayda eklenecek.)

**K2 — "Stable" bandı:** İş kısıtı tanımlanmadı; tamamen literatür bulgusuna
bırakıldı. Faz 1'de sabit threshold'a ek olarak oynaklığa-göre-uyarlanmış
threshold yaklaşımları zorunlu kapsamdadır.

**K3 — İkinci el / yeni araç kapsamı:** Tarama İKİNCİ EL piyasası odaklıdır.
Yeni araç fiyatları yalnızca Faz 2'de, ikinci el fiyatlarını etkileyen dışsal
faktör (ör. sıfır araç zamları, stok durumu) olarak ele alınır. Faz 4'te yeni
araç fiyat tahmini literatürü kapsam dışıdır.

**K4 — Coğrafi kapsam (hibrit):** Metodoloji fazları (1, 3, 5, 6, 7, 8)
uluslararası literatürü tarar. Faz 2 Türkiye odaklıdır. Faz 4 uluslararasıdır
ancak Türkiye piyasası üzerine çalışma bulunursa öncelikli raporlanır.

**K5 — Şirket bilgisi sınırı:** Bu çalışma Arabam.com'dan bağımsız, tamamen
kamuya açık kaynaklarla yürütülür; çıktılar daha sonra şirketteki geliştirici
ekibe sunulacaktır. Repo public'tir. KURAL: Hiçbir faz dökümanına şirket içi
veri, rapor, metrik veya yayınlanmamış bilgi giremez. Şirketlerin (Arabam.com
dahil) yalnızca kamuya açık yayınları kaynak olarak kullanılabilir.

**K6 — Kaynak türü kapsamı:** Geniş kapsam esas alınır: peer-reviewed akademik
literatür + gri literatür (arXiv/SSRN working paper, tez) + sektör raporları
(ODMD, OSD, TÜİK, TCMB vb.) + nitelikli endüstri kaynakları (Kaggle üst sıra
çözümleri, şirket mühendislik blogları). Faz 2 ve 4'te sektör raporları "resmi
kaynak" statüsündedir. Her fazın kendi prompt'unda belirtilen kaynak öncelik
sıralaması geçerlidir; düşük kaliteli içerik (forum, pazarlama amaçlı blog)
hariçtir.

**K7 — Faz çıktı uzunluğu:** Üst sınır yoktur. Derinlik, fazın hedef kaynak
sayısı ile; disiplin, kalite kontrol listesindeki scope creep maddesi ile
sağlanır. Şişirme değil yoğunluk esastır.

## Yapısal Kararlar (dosya düzeni)

**Y1:** Sentez dökümanı, master planın önerdiği gibi `docs/09_sentez_ve_karar_dokumani.md`
olarak numaralı seride tutulur (okuma sırası korunur). Sunum kaynak dosyaları
`docs/sentez/` altında kalır.

**Y2:** Faz dökümanlarının metadata bloğu olarak master plandaki genişletilmiş
YAML şeması esas alınır (bkz. güncellenmiş `docs/standards.md`).
