# Döküman ve Kalite Standartları

Bu dosya, repodaki tüm faz dökümanlarının uyması gereken standartları tanımlar.
Konumu: `docs/standards.md`

## 1. Dosya İsimlendirme

- Faz çıktıları: `NN_kisa_baslik.md` — iki haneli sıra numarası + snake_case Türkçe
  kısa başlık. Örnek: `01_problem_cerceveleme.md`, `04_model_mimarileri.md`
- Master plan: `00_master_plan.md`
- Sentez dosyaları `docs/sentez/` altında: `sentez_raporu.md`, `sunum_taslagi.md`
- Prompt arşivi: `prompts/NN_faz_adi_prompt.md` — hangi fazda hangi prompt
  kullanıldıysa aynen saklanır (tekrarlanabilirlik için).

## 2. Zorunlu Metadata Bloğu

Her faz dökümanı şu blokla başlar:

```markdown
---
faz: 03
baslik: Feature Engineering ve Alternatif Veri Kaynakları
tarih: 2026-07-20
durum: taslak | incelemede | tamamlandi
bagimli_fazlar: [01, 02]
kaynak_arac: claude.ai Deep Research | Claude Code
kapsam_ozeti: <1-2 cümle>
---
```

## 3. Faz Dökümanı İskeleti

1. **Kapsam ve Hariç Tutulanlar** — bu fazda neye bakıldı, neye bilinçli bakılmadı
2. **Ana Bulgular** — numaralı, her bulgu kaynaklı
3. **Projeye Uygulanabilirlik** — her ana bulgunun bizim probleme çevirisi
4. **Açık Sorular / Literatürde Net Olmayanlar**
5. **Kaynakça** — her kaynak için 1-2 cümlelik "neden ilgili" notu

## 4. Kalite Kontrol Listesi (bir faz "tamamlandı" sayılmadan önce)

- [ ] Metadata bloğu eksiksiz ve güncel
- [ ] Temel/giriş seviyesi ML açıklaması İÇERMİYOR
- [ ] Her iddia en az bir kaynağa bağlı
- [ ] Her ana bulgunun "projeye uygulanabilirlik" karşılığı var
- [ ] Belirsiz noktalar "literatürde net değil" olarak işaretlenmiş, tahmin yok
- [ ] Kaynakçadaki her girişte gerekçe notu var
- [ ] Kullanılan prompt `prompts/` klasörüne arşivlenmiş
- [ ] Proje sahibi gözden geçirip onayladı (durum: tamamlandi ancak bundan sonra)

## 5. Yazım Kuralları

- Dil: Türkçe. Teknik terimler yaygın İngilizce haliyle bırakılabilir
  (ör. data leakage, walk-forward validation) — zorlama çeviri yapılmaz.
- İddialar ölçülü yazılır: literatür ne diyorsa o; abartı ve pazarlama dili yok.
- Uzun paragraflar yerine kısa, taranabilir bölümler; ancak madde işaretleri
  tek kelimelik değil, açıklayıcı cümleler halinde olur.

## 6. Format Dönüşümleri

- Kaynak format her zaman Markdown'dır; docx/pptx yalnızca `exports/` altına,
  pandoc / python-docx / python-pptx ile üretilir ve Git'e commit edilmez
  (`.gitignore` içinde `exports/`).
- Kurumsal şablon gerektiğinde şablon dosyası repoya eklenir ve dönüşümlerde
  referans alınır.
