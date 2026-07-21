GÖREV: Araç piyasası fiyat yönü tahmini projesinin örnek (MVP) veri seti
aşaması için repo altyapısını kur, ilgili promptu arşivle ve değişiklikleri
commit'leyip push'la. Bu görevde VERİ ÇEKME veya kod ÇALIŞTIRMA yok — yalnızca
repo düzenini hazırlıyorsun. Veri çekme, ayrı bir oturumda (Sonnet 5) yapılacak.

BAĞLAM:
- Bu repo bir literatür tarama + baseline hazırlık projesidir. docs/ altında
  tamamlanmış faz dökümanları, prompts/ altında kullanılan promptların arşivi,
  docs/00_karar_kaydi.md içinde bağlayıcı kararlar var.
- Şimdi projenin veri mühendisliği aşamasına geçiliyor: kamuya açık kaynaklardan
  küçük bir örnek (MVP) veri seti kurulacak. Bu görev o aşamanın repo hazırlığı.

YAPILACAKLAR:

1) KLASÖR YAPISI KUR
   - prompts/veri/    → veri toplama promptlarının arşivi (MVP + sonraki genişleme)
   - data/            → çekilecek verinin konacağı klasör (henüz boş)
       data/raw/      → kaynaklardan gelen ham dosyalar
       data/processed/→ birleştirilmiş/temizlenmiş tablolar
   - Klasörler boşsa Git'te görünmesi için her birine .gitkeep koy.

2) MVP PROMPTUNU ARŞİVLE
   - Sana ayrıca verilecek "MVP Aşaması Promptu" içeriğini şu dosyaya kaydet:
       prompts/veri/01_mvp_cekirdek_veri_prompt.md
   - (İçeriği kullanıcı bu talimatla birlikte veya hemen ardından paylaşacak;
     paylaşılmadıysa iste. Kendin yeni prompt YAZMA — verilen içeriği aynen
     arşivle.)

3) .gitignore GÜNCELLE — VERİ VERSİYONLANMAYACAK
   - Bu projede ilke: "prompt/kod versiyonlanır, çekilen veri versiyonlanmaz."
     Sebep: (a) veri dosyaları repoyu şişirir, (b) bu prototip veri, ileride
     gerçek şirket içi veriyle KARIŞTIRILMAMALIDIR (karar K5: yalnızca kamuya
     açık kaynaklar, şirket içi veri repoya girmez).
   - .gitignore'a şunları ekle (zaten varsa tekrarlama):
       data/raw/*
       data/processed/*
       !data/raw/.gitkeep
       !data/processed/.gitkeep
   - Böylece klasör yapısı Git'te durur ama içindeki veri dosyaları izlenmez.
   - Not: exports/ için mevcut .gitignore kuralı korunur (docx/pptx/pdf çıktıları).

4) VERİ KLASÖRÜ İÇİN KISA README
   - data/README.md oluştur. İçeriği (Türkçe, kısa):
     * Bu klasörün amacı: kamuya açık kaynaklardan çekilen ÖRNEK/PROTOTİP veri.
     * UYARI: Buraya şirket içi, lisanslı veya özel veri KONULMAZ (karar K5).
     * Veri dosyaları .gitignore ile Git-dışıdır; yalnızca klasör yapısı versiyonlanır.
     * raw/ = ham kaynak çıktıları, processed/ = birleştirilmiş tablolar.
     * Bilinen sınır: kamuya açık fiyat serileri (BETAM sahibindex, arabam.com)
       mix/kompozisyon düzeltmesizdir (karar N1); MVP'de yer-tutucu hedef olarak
       kullanılır, nihai hedef değildir.

5) README GÜNCELLE (kök dizin)
   - Ana README.md'deki durum/aşama bölümüne kısa bir satır ekle: literatür
     tarama + sentez tamamlandı; proje artık MVP veri seti aşamasında.

6) COMMIT VE PUSH
   - Değişiklikleri anlamlı, Türkçe commit mesajlarıyla commit'le. Öneri:
       "veri: MVP veri seti klasör yapısı ve arşiv kuruldu"
   - Commit'lerde author olarak repo sahibinin git config'i kullanılsın
     (repodaki mevcut user.name/user.email — değiştirme).
   - GitHub'a push'la.

KISITLAR:
- Veri ÇEKME veya kod çalıştırma bu görevin parçası DEĞİL.
- docs/ ve prompts/ altındaki mevcut faz dökümanlarını DEĞİŞTİRME; yalnızca
  yeni klasör/dosya ekle ve README/.gitignore güncelle.
- data/ altına gerçek veri dosyası KOYMA (henüz veri yok; sadece iskelet + .gitkeep).
- Yeni içerik/prompt YAZMA; verilen MVP prompt içeriğini aynen arşivle.

BİTİRİNCE: Kısa rapor ver — hangi klasör/dosyalar oluşturuldu, .gitignore'a ne
eklendi, commit mesajı ne oldu, push başarılı mı. Bir sonraki adımın (Sonnet 5
ile veri çekme) hazır olduğunu belirt.