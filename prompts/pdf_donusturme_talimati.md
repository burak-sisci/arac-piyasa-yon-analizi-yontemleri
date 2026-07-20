GÖREV: docs/ klasöründeki sekiz faz dökümanını (01–08) tek tek, ayrı ayrı PDF
dosyalarına çevir. Çıktılar exports/ klasörüne yazılsın.

HANGİ DOSYALAR:
docs/01_problem_cerceveleme_label_tasarimi.md
docs/02_arac_piyasasi_dinamikleri.md
docs/03_finansal_piyasa_yon_tahmini.md
docs/04_arac_fiyat_akademik_literatur.md
docs/05_feature_engineering_alternatif_veri.md
docs/06_model_mimarileri_ensemble.md
docs/07_validasyon_metrik_backtest.md
docs/08_basarisizlik_modlari_tuzaklar.md
(Dosya adları farklıysa docs/ içindeki 0*.md kalıbıyla eşleşen tümünü al;
09_sentez ve 00_karar_kaydi bu görevin DIŞINDADIR — yalnızca 01–08.)

ÇIKTI: Her .md için aynı adı taşıyan bir .pdf, exports/ altına.
Örn: docs/01_problem_cerceveleme_label_tasarimi.md
  →  exports/01_problem_cerceveleme_label_tasarimi.pdf

ARAÇ VE YÖNTEM:
- pandoc kuruluysa onu kullan; PDF motoru olarak xelatex tercih et (Türkçe
  karakterler ç/ş/ğ/ı/ö/ü ve Unicode için en güvenilir motor budur).
  Örnek komut kalıbı:
    pandoc "docs/DOSYA.md" -o "exports/DOSYA.pdf" \
      --pdf-engine=xelatex \
      -V mainfont="DejaVu Sans" \
      -V geometry:margin=2cm \
      -V colorlinks=true
- pandoc veya xelatex yoksa: önce kurmayı dene (ör. Debian/Ubuntu'da
  `sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended`).
  Kurulum mümkün değilse, yedek olarak markdown→HTML→PDF yolunu kullan
  (Python `markdown` + `wkhtmltopdf`), yeter ki Türkçe karakterler ve tablolar
  düzgün render edilsin.

ZORUNLU KALİTE KURALLARI:
1. Her dosyanın başındaki YAML front-matter bloğu (--- ... --- arası:
   faz_no, faz_adi, durum, kapsam_ozeti vb.) çıktıda ham kod olarak GÖRÜNMESİN.
   pandoc bunu varsayılan olarak başlık metaverisi gibi işler; sorun çıkarsa
   front-matter'ı dökümanın başına düzgün bir "başlık + künye" bloğu olarak
   render et. Bilgi kaybolmasın ama "---" çizgileri ve ham "anahtar: değer"
   satırları çıktıda görünmesin.
2. TABLOLAR eksiksiz ve okunur olmalı. Bu dökümanların en değerli kısmı geniş
   tablolardır (sürücü haritası, aktarılabilirlik matrisi, feature üretim
   tablosu, model karar ağacı, başarısızlık registri). Sayfaya sığması için
   gerekiyorsa tablo font boyutunu küçült veya sayfayı yatay (landscape) yap —
   ama HİÇBİR SÜTUN veya SATIR kırpılmasın. Çevirdikten sonra her PDF'in tablo
   sayısını ve satır sayısını kaynak .md ile karşılaştırıp doğrula.
3. Türkçe karakterler doğru render edilmeli (kutu/soru işareti olarak değil).
4. Kod blokları (```...```) ve satır içi kod düzgün monospace görünmeli.
5. Sayfa numarası altbilgide olsun.

YAPMA:
- .md dosyalarını değiştirme; yalnızca exports/ altında PDF üret.
- 00_karar_kaydi ve 09_sentez'i çevirme (bu görev yalnızca 01–08).
- exports/ klasörünü .gitignore'dan çıkarma; PDF'ler zaten Git-dışı kalmalı
  (türetilmiş çıktı ilkesi). Sadece dosyaları üret, commit etme.

BİTİRİNCE: Kısa bir rapor ver — kaç PDF üretildi, hangi araç/motor kullanıldı,
her dosyada kaç tablo olduğunu ve tabloların kaynakla eşleşip eşleşmediğini
(satır sayısı kontrolü) belirt. Türkçe karakter veya tablo taşması gibi bir
sorun fark ettiysen açıkça raporla.