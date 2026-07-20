# CLAUDE.md — Proje Bağlamı

## Proje Kimliği

**Proje:** Araç Piyasası Fiyat Yönü Tahmini — Literatür Tarama ve Bilgi Tabanı
**Sahip:** Arabam.com Data Science Intern (proje yürütücüsü)
**Nihai amaç:** Geliştirici ekibin, araç piyasasında fiyat yönünü (up / down / stable)
tahmin eden bir ML sistemine "gelmiş geçmiş en iyi baseline" ile başlamasını sağlayacak,
literatüre dayalı bir bilgi tabanı üretmek.

Bu repo bir yazılım projesi DEĞİLDİR. Çıktılar: Markdown dökümanları, sentez raporu
ve karar-odaklı sunum. Kod yalnızca döküman dönüşümü (pandoc, python-docx, python-pptx)
gibi yardımcı işler için yazılır.

## Hedef Kitle: Geliştirici Ekip Profili

- İleri seviye. Model eğitimi, zaman serisi analizi ve sınıflandırma deneyimliler.
- KURAL: Temel/giriş seviyesi ML açıklaması İÇEREN HİÇBİR içerik üretme.
  ("Random Forest nedir", "cross-validation nedir" gibi içerik yasak.)
- Her bulgu şu soruya bağlanmalı: "Bu, bizim fiyat yönü tahmin problemimize
  nasıl uygulanır?"

## Problem Çerçevesi (mevcut karar durumu)

- Görev tipi: Yön sınıflandırması (up / down / stable). Sınıf sayısı, tahmin ufku
  ve threshold kararları Faz 0 planı ve ilgili faz taramaları sonrası netleşecek.
- Kapsam: Akademik (peer-reviewed) + finansal piyasa yön tahmini literatürü
  (hisse/kripto/emtia) + endüstri/Kaggle/blog kaynakları + araç piyasasına özgü
  dinamikler (kur, ÖTV/vergi, arz şokları, EV geçişi, Türkiye'ye özgü faktörler).

## Çalışma Modeli

- İş zamana yayılmış, çok fazlı yürütülür. Her faz ayrı oturum, her fazın çıktısı
  ayrı bir Markdown dosyasıdır.
- Ağır literatür taramaları claude.ai Deep Research'te yapılır; çıktılar bu repoya
  taşınır. Claude Code'un görevi: organizasyon, tutarlılık kontrolü, sentez,
  format dönüşümleri ve sunum üretimi.
- Master plan: `docs/00_master_plan.md` (Faz 0 çıktısı geldiğinde buraya konur).
  Her oturumda önce master planı ve ilgili önceki faz dosyalarını OKU, sonra çalış.

## Depo Yapısı

```
.
├── CLAUDE.md                  # bu dosya — her oturumda bağlam
├── README.md                  # repo tanıtımı
├── docs/
│   ├── standards.md           # döküman ve kalite standartları
│   ├── 00_master_plan.md      # Faz 0 çıktısı (master plan)
│   ├── 01_*.md ... NN_*.md    # faz çıktıları (numaralı)
│   └── sentez/                # sentez raporu ve sunum kaynak dosyaları
├── prompts/                   # her faz için kullanılan promptların arşivi
└── exports/                   # docx/pptx/pdf dönüşüm çıktıları (git'e girmez)
```

## Zorunlu Kurallar

1. Tüm içerik Türkçe yazılır; kaynak başlıkları orijinal dilinde bırakılır.
2. Her faz dökümanı `docs/standards.md` içindeki metadata bloğu ile başlar ve
   kalite kontrol listesinden geçmeden "tamamlandı" işaretlenmez.
3. Kaynaksız iddia yazılmaz. Emin olunmayan nokta "literatürde net değil" diye
   açıkça işaretlenir; tahmin yürütülmez.
4. Var olan faz dosyaları sahibinin onayı olmadan yeniden yazılmaz; düzeltmeler
   küçük ve gerekçeli commit'lerle yapılır.
5. Git commit'leri: author olarak proje sahibinin adı/e-postası kullanılır
   (repo `git config user.name` / `user.email` ayarı ile). Commit mesajları
   Türkçe ve açıklayıcı olur: `faz-03: feature engineering taraması eklendi` gibi.
6. Belirsizlik varsa varsayım yapıp ilerleme; proje sahibine soru sor.
7. `README.md` içindeki "Durum" listesi (8 faz + sentez + sunum,
   `docs/00_master_plan_literatur_taramasi.md` Bölüm 1'deki faz adlarıyla birebir)
   her commit'te son duruma göre güncellenir: tamamlanan/eklenen faz `[x]`
   işaretlenir; bir dökümanın `durum` alanı `taslak`'a dönerse (ör. revizyon)
   README'deki işaret de geri alınır. Bu, her faz commit'inin bir parçasıdır,
   ayrı bir görev değildir.
8. Proje sahibi commit + push işlemini önceden onaylamıştır: değişiklikler
   tamamlandıkça (ayrı bir onay beklemeden) mantıksal commit'lere bölünüp
   `origin/main`'e push edilir. Bu onay geri alınana kadar geçerlidir.
