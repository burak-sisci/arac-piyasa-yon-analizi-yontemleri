# Araç Piyasası Fiyat Yönü Tahmini — Literatür Tarama Bilgi Tabanı

Bu repo, araç piyasasında fiyat yönünü (up / down / stable) tahmin edecek ML
sisteminin geliştirici ekibine temel oluşturacak literatür taramasının bilgi
tabanıdır. Çıktılar Markdown dökümanlarıdır; nihai teslimatlar bir sentez raporu
ve karar-odaklı bir sunumdur.

## Nasıl Çalışır

1. Master plan `docs/00_master_plan_literatur_taramasi.md` içindedir; tarama fazlara bölünmüştür.
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
| `prompts/veri/` | MVP veri seti toplama promptlarının arşivi |
| `data/` | MVP örnek veri seti (raw/processed); veri dosyaları Git'e girmez — bkz. `data/README.md` |
| `exports/` | docx/pptx/pdf dönüşümleri (Git'e girmez) |

## Durum

**Not:** Faz 1–7 tamamlandı; Faz 8 (başarısızlık modları) ve sentez raporu
taslak aşamasında, proje sahibi onayı bekliyor. Bununla paralel olarak proje
artık MVP (örnek) veri seti aşamasına geçti — bkz. `data/` ve `prompts/veri/`.

- [x] Faz 0 — Planlama promptu hazırlandı
- [x] Faz 0 — Master plan üretildi ve onaylandı
- [x] Faz 1 — Problem Çerçeveleme ve Label Tasarımı
- [x] Faz 2 — Araç Piyasasına Özgü Dinamikler
- [x] Faz 3 — Finansal Piyasa Yön Tahmini Literatürü
- [x] Faz 4 — Araç Fiyat Tahmini Akademik Literatürü
- [x] Faz 5 — Feature Engineering ve Alternatif Veri Kaynakları
- [x] Faz 6 — Model Mimarileri ve Ensemble Stratejileri
- [x] Faz 7 — Validasyon, Metrik Seçimi, Backtest Metodolojisi
- [x] Faz 8 — Başarısızlık Modları, Tuzaklar, Data Leakage Riskleri
- [x] Sentez raporu (`09_sentez_ve_karar_dokumani.md`)
- [x] Sunum
