# Döküman ve Kalite Standartları (v2)

Bu dosya, repodaki tüm faz dökümanlarının uyması gereken standartları tanımlar.
Konumu: `docs/standards.md`
Revizyon notu: v2 — master plan (00) ve karar kaydı (00_karar_kaydi.md) ile
uyumlu hale getirildi. Metadata şeması genişletildi, sentez dosya düzeni
netleştirildi (karar Y1, Y2).

## 1. Dosya İsimlendirme

- Faz çıktıları master plandaki şemayı izler (yürütme sırasına göre numaralı):

```
docs/00_master_plan_literatur_taramasi.md
docs/00_karar_kaydi.md
docs/01_problem_cerceveleme_label_tasarimi.md
docs/02_arac_piyasasi_dinamikleri.md
docs/03_finansal_piyasa_yon_tahmini.md
docs/04_arac_fiyat_akademik_literatur.md
docs/05_feature_engineering_alternatif_veri.md
docs/06_model_mimarileri_ensemble.md
docs/07_validasyon_metrik_backtest.md
docs/08_basarisizlik_modlari_tuzaklar.md
docs/09_sentez_ve_karar_dokumani.md
docs/sentez/                       (sunum kaynak dosyaları)
```

- Prompt arşivi: `prompts/NN_faz_adi_prompt.md` — her fazda kullanılan prompt,
  çalıştırılmadan önce aynen arşivlenir (tekrarlanabilirlik kuralı).

## 2. Zorunlu Metadata Bloğu (master plan şeması)

Her faz dökümanı şu YAML front-matter ile başlar:

```yaml
---
faz_no: 01
faz_adi: "Problem Çerçeveleme ve Label Tasarımı"
tarih: 2026-07-13
kapsam_ozeti: "Yön sınıflandırması için label taksonomisi, threshold ve ufuk seçimi"
bagimli_oldugu_fazlar: []
durum: taslak            # taslak | inceleniyor | tamamlandi
hedef_kaynak_sayisi: 15
gerceklesen_kaynak_sayisi: 0
kaynak_arac: "claude.ai Research"   # claude.ai Research | Claude Code
son_guncelleme: 2026-07-13
---
```

`bagimli_oldugu_fazlar` alanı revizyon takibi içindir: bir faz güncellendiğinde,
o fazı bağımlılık listesinde taşıyan tüm dökümanlar gözden geçirme kuyruğuna girer.

## 3. Faz Dökümanı İskeleti

Her fazın kendi başlık iskeleti master planda tanımlıdır ve o iskelet esastır.
Ortak zorunlu bölümler: her ana bulgu bölümünün altında "Projeye Uygulanabilirlik"
notu, ayrıca dökümanın sonunda "Açık Sorular / Literatürde Net Olmayanlar" ve
gerekçe notlu "Kaynakça".

## 4. Kalite Kontrol Listesi (master plan Bölüm 5 esas alınır)

Bir faz, aşağıdakilerin HEPSİ sağlanmadan `tamamlandi` olamaz:

- [ ] Her somut iddia en az bir kaynağa atıfla destekleniyor (yazar/kurum + yıl, mümkünse DOI/link)
- [ ] Temel ML/istatistik bilgisi tekrarı yok
- [ ] Her ana bulgu bölümünde somut, aksiyon alınabilir "Projeye Uygulanabilirlik" notu var
- [ ] Kaynak çeşitliliği yeterli (tek tip kaynağa dayanmıyor)
- [ ] Çelişkili bulgular açıkça işaretlenmiş
- [ ] Kapsam dışına taşma yok (scope creep kontrolü)
- [ ] Arama stratejisi (anahtar kelimeler) dökümanda şeffaf belirtilmiş
- [ ] Önceki fazlarla çelişen bulgular çapraz-referanslanmış
- [ ] Metadata bloğu eksiksiz, `durum` güncel
- [ ] Kullanılan prompt `prompts/` klasörüne arşivlenmiş
- [ ] Şirket içi hiçbir bilgi içermiyor (karar K5) — yalnızca kamuya açık kaynak
- [ ] Proje sahibi gözden geçirip onayladı

## 5. Yazım Kuralları

- Dil: Türkçe. Teknik terimler yaygın İngilizce haliyle bırakılabilir
  (data leakage, walk-forward validation vb.); zorlama çeviri yapılmaz.
- Kaynak başlıkları orijinal dilinde bırakılır.
- İddialar ölçülü yazılır; abartı ve pazarlama dili yok. Literatürde net
  olmayan noktalar tahminle doldurulmaz, açıkça işaretlenir.
- Uzunluk üst sınırı yok (karar K7); yoğunluk esas, şişirme yasak.

## 6. Bağlayıcı Kapsam Kararları (özet — detay: 00_karar_kaydi.md)

- İkinci el piyasası odağı; yeni araç yalnızca Faz 2'de dışsal faktör (K3)
- Coğrafya: metodoloji fazları uluslararası, Faz 2 Türkiye, Faz 4 hibrit (K4)
- Yalnızca kamuya açık kaynaklar; şirket içi bilgi yasak (K5)
- Geniş kaynak kapsamı; faz bazlı öncelik sıralaması geçerli (K6)

## 7. Format Dönüşümleri

- Kaynak format her zaman Markdown; docx/pptx yalnızca `exports/` altına
  pandoc / python-docx / python-pptx ile üretilir, Git'e commit edilmez
  (`.gitignore`: `exports/`).
