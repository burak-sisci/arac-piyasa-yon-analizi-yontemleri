GÖREV: Bu repodaki tamamlanmış literatür tarama fazlarını tek bir sentez
dökümanına birleştir. Yeni araştırma yapma, web'e çıkma, yeni öneri/yol haritası
üretme — görev SENTEZ (mevcut bulguları birleştirme), keşif değil.

ÖNCE OKU (sırayla, tamamını):
1. CLAUDE.md ve docs/standards.md — proje bağlamı ve yazım/format kuralları.
2. docs/00_karar_kaydi.md — bu dökümanın omurgasıdır (8 kapsam kararı K1-K8 +
   13 bağlayıcı not N1-N13 + yapısal kararlar). Sentez bu kararları esas alır.
3. docs/01 … docs/08 (sekiz faz dökümanının tamamı) — her birinin TL;DR, Key
   Findings, ana teslimat tablosu/registri ve "Açık Sorular" bölümlerine özel
   dikkat et.

SONRA ÜRET: docs/09_sentez_ve_karar_dokumani.md

HEDEF KİTLE VE YAPI: İki katmanlı.
- ÜST KATMAN — Yönetici/Mentor Özeti (dökümanın başında, ~1.5-2 sayfa):
  Karar-odaklı, teknik jargonu minimumda tutan; projenin ne olduğu, hedefin ne
  (K8: ilan fiyatı yönü), literatürdeki konumu (N9: boşluk/novelty), önerilen
  baseline'ın özü (N11), en kritik risk (N13: K8 varsayımı) ve projenin başarı/
  terk kriterleri (N6, N13). Yönetici bu kısmı okuyup projeyi kavrayabilmeli.
- ALT KATMAN — Teknik Gövde: Sekiz fazı mantıksal bir anlatıya diz. Faz sırasını
  körü körüne takip etme; şu akışı kur: (a) Problem tanımı ve hedef [Faz 1, K8],
  (b) Veri gerçekliği ve sürücüler [Faz 2, N1/N2], (c) Metodolojik duruş —
  finansal literatürden ne alındı/alınmadı [Faz 3], (d) Literatürdeki boşluk ve
  devşirilen çekirdek [Faz 4, N9], (e) Feature/veri-hazırlık reçetesi [Faz 5,
  N10], (f) Model kararı [Faz 6, N11], (g) Güvenilirlik protokolü [Faz 7, N12],
  (h) Riskler ve terk kriterleri [Faz 8, N13].

ZORUNLU İÇERİK KURALLARI:
- Her ana bölüm, ilgili fazın ana teslimatına (sürücü haritası, aktarılabilirlik
  matrisi, boşluk haritası, feature tablosu, model karar ağacı, protokol kontrol
  listesi, başarısızlık registri) ATIFTA bulunmalı ama onu KOPYALAMAMALI —
  özetleyip "detay için Faz X" demeli. Sentez, fazların yerine geçmez; onları
  birbirine bağlar.
- Karar kaydındaki K ve N maddelerini anlatı içinde açıkça izlenebilir kıl
  (ör. "İlan fiyatı hedefi kararı [K8]..."). Böylece okuyucu sentezden karar
  kaydına gidebilir.
- FAZLAR ARASI BAĞLARI ÖNE ÇIKAR — sentezin asıl katma değeri budur:
  * N1 (kompozisyon sorunu, Faz 2) → N10 (çözümü, Faz 5) zinciri.
  * N9+K8 kritik varsayım (Faz 4) → N13 test tasarımı (Faz 8) zinciri.
  * N4 (SMOTE yasak, Faz 3) → N11 (model, Faz 6) → N12 (kalibrasyon protokolü,
    Faz 7) zinciri.
  * N2 (rejim çift-yönlülüğü, Faz 2) → N8 → N11 → N12 rejim-farkındalık zinciri.
- "Açık Sorular / Literatürde Net Değil" maddelerini fazlardan topla ve tek bir
  "Bilinen Belirsizlikler" bölümünde birleştir (özellikle N3: ilan-tabanlı yön
  etiketleme literatürü yok).
- Çelişki/gerilim işaretlerini koru (ör. Faz 7'deki blocked-CV gerilimi,
  Faz 3'teki SMOTE karşı-bulgusu) — sentez bunları düzleştirmemeli.

FORMAT (docs/standards.md'ye uy):
- YAML metadata bloğu ile başla: faz_no: 09, faz_adi, bagimli_oldugu_fazlar:
  [01,02,03,04,05,06,07,08], durum: taslak, kaynak_arac: "Claude Code (sentez)".
- Dil Türkçe; teknik terimler orijinal haliyle bırakılabilir.
- Yeni kaynak EKLEME; yalnızca fazlarda geçen kaynaklara atıf ver. Sentezin
  kendi "Kaynakça"sı, fazlardaki kilit kaynakların kısa bir konsolide listesi
  olabilir (tekrar üretme, faz numarasıyla işaret et).
- Uzunluk: yönetici özeti kısa ve öz; teknik gövde kapsamlı ama fazları
  tekrar etmeyen, bağlayan bir metin.

YAPMA:
- Web araması veya yeni literatür tarama.
- Yeni model/feature/metodoloji önerisi (bu fazların işiydi; sentez sadece
  birleştirir).
- Faz dökümanlarını değiştirme; yalnızca 09'u oluştur.
- Kararlarla çelişen bir "iyileştirme" önerme.

BİTİRİNCE: Kısa bir özet ver — hangi fazları/kararları nasıl bağladığını ve
varsa fark ettiğin tutarsızlıkları (düzeltme değil, RAPOR olarak) belirt.