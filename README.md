# Araç Piyasası Fiyat Yönü Tahmini — Literatür Tarama Bilgi Tabanı

Bu repo, araç piyasasında fiyat yönünü (up / down / stable) tahmin edecek ML
sisteminin geliştirici ekibine temel oluşturacak literatür taramasının bilgi
tabanıdır. Çıktılar Markdown dökümanlarıdır; nihai teslimatlar bir sentez raporu
ve karar-odaklı bir sunumdur.

## Nasıl Çalışır

1. Master plan `docs/00_master_plan.md` içindedir; tarama fazlara bölünmüştür.
2. Her fazın taraması claude.ai Deep Research ile yapılır; kullanılan prompt
   `prompts/` altına, çıktı `docs/` altına eklenir.
3. Organizasyon, tutarlılık kontrolü, sentez ve format dönüşümleri Claude Code
   ile bu repo içinde yürütülür. Oturum bağlamı `CLAUDE.md` dosyasındadır.
4. Döküman standartları ve kalite kontrol listesi: `docs/standards.md`

## Klasörler

| Yol | İçerik |
|---|---|
| `docs/` | Master plan ve numaralı faz çıktıları |
| `docs/sentez/` | Sentez raporu ve sunum taslağı |
| `prompts/` | Fazlarda kullanılan promptların arşivi |
| `exports/` | docx/pptx/pdf dönüşümleri (Git'e girmez) |

## Durum

- [x] Faz 0 — Planlama promptu hazırlandı
- [x] Faz 0 — Master plan üretildi ve onaylandı
- [x] Faz 1 — Problem Çerçeveleme ve Label Tasarımı
- [ ] Faz 2 — Araç Piyasasına Özgü Dinamikler
- [ ] Faz 3 — Finansal Piyasa Yön Tahmini Literatürü
- [ ] Faz 4 — Araç Fiyat Tahmini Akademik Literatürü
- [ ] Faz 5 — Feature Engineering ve Alternatif Veri Kaynakları
- [ ] Faz 6 — Model Mimarileri ve Ensemble Stratejileri
- [ ] Faz 7 — Validasyon, Metrik Seçimi, Backtest Metodolojisi
- [ ] Faz 8 — Başarısızlık Modları, Tuzaklar, Data Leakage Riskleri
- [ ] Sentez raporu (`09_sentez_ve_karar_dokumani.md`)
- [ ] Sunum
