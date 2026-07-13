# Faz 1 Promptu — Problem Çerçeveleme ve Label Tasarımı

Kullanım: claude.ai'de yeni sohbet, **Research (Deep Research) AÇIK**.
Arşiv konumu: `prompts/01_problem_cerceveleme_prompt.md`

---

## KULLANILACAK PROMPT (kopyala-yapıştır)

```
ROL VE BAĞLAM

Sen, bir araç piyasası fiyat yönü tahmin projesi için literatür taraması yürüten
kıdemli bir araştırmacısın. Bu, çok fazlı bir tarama programının FAZ 1'idir.

PROJE: İkinci el araç piyasasında fiyatların gelecekte yükselip yükselmeyeceğini
(yön sınıflandırması: up / down / stable) tahmin eden bir ML sistemi için,
geliştirici ekibe temel oluşturacak bilgi tabanı hazırlanıyor.

EKİP PROFİLİ: Geliştirici ekip ileri seviyede; model eğitimi, zaman serisi ve
sınıflandırma deneyimliler. Temel ML/istatistik açıklaması İÇEREN HİÇBİR içerik
üretme ("sınıflandırma nedir", "cross-validation nedir" gibi). Yalnızca bu
probleme özgü, teknik derinliği olan, uygulanabilir bulgular raporla.

BU FAZIN GÖREVİ

Yön sınıflandırması probleminin tanımını literatüre dayandırmak: kaç sınıf
kullanılmalı, tahmin ufku nasıl seçilmeli, "stable" bandı / threshold nasıl
belirlenmeli.

DAHİL:
- Label taksonomileri: 2-sınıf (up/down), 3-sınıf (up/down/stable),
  quantile-tabanlı ve N-sınıf yaklaşımların karşılaştırması; hangi koşulda
  hangisi tercih edilmiş, hangi gerekçelerle
- Threshold/bant belirleme yöntemleri: sabit threshold, oynaklığa-göre-uyarlanmış
  (volatility-adjusted) threshold, istatistiksel test tabanlı yaklaşımlar
- Triple-barrier labeling ve türevleri; meta-labeling yaklaşımları
- Tahmin ufku seçimi: farklı ufuklarda (günlük/haftalık/aylık) etiketlemenin
  sinyal-gürültü oranına, class dengesine ve öğrenilebilirliğe etkisi
- Label tasarımı ile class imbalance etkileşimi: threshold ve ufuk seçiminin
  sınıf dağılımını nasıl belirlediği, literatürde bunun nasıl yönetildiği

HARİÇ (bu fazda raporlanmayacak):
- Sınıflandırma algoritmaları ve model mimarileri (ayrı fazda)
- Genel feature engineering (ayrı fazda)
- Araç piyasasına özgü iktisadi dinamikler (ayrı fazda)

KAPSAM KARARLARI (bağlayıcı):
- Uygulama hedefi ikinci el araç piyasasıdır; ancak bu faz METODOLOJİ fazıdır,
  uluslararası literatürü tara (finansal piyasalar dahil — yön etiketleme
  literatürünün en olgun olduğu alan orasıdır). Bulguları araç piyasası
  bağlamına çevirerek raporla: araç piyasası düşük frekanslı, endeks/segment
  düzeyinde, işlem verisinden çok ilan verisine dayalı bir piyasadır; hangi
  etiketleme yaklaşımının bu yapıya uyup uymadığını her bölümde değerlendir.
- Tahmin ufku ve stable bandı için ÖN KARAR YOK: seçenekleri trade-off'larıyla
  sun, tek bir öneriye indirgemek yerine karar matrisi çıkar; en sonda
  gerekçeli bir öneri sıralaması ver.

ARAMA STRATEJİSİ (başlangıç noktası; gerektiğinde genişlet ve genişlettiğini raporla)
EN: price direction classification, triple barrier labeling, threshold selection
financial time series classification, multi-class stable up down labeling,
meta-labeling, volatility adjusted labeling, prediction horizon selection
classification
TR: fiyat yönü sınıflandırma, zaman serisi etiketleme yöntemi, eşik değeri
seçimi fiyat tahmini, üç sınıflı fiyat tahmini

KAYNAK ÖNCELİĞİ: (1) peer-reviewed finansal ML makaleleri, (2) yüksek atıflı
working paper'lar (arXiv q-fin, SSRN), (3) ileri düzey kitap bölümleri.
Blog/tutorial içerik bu fazda HARİÇ. Hedef: 12-18 nitelikli kaynak.
Yalnızca kamuya açık kaynaklar kullanılacak.

ÇIKTI FORMATI

Tek bir Markdown dökümanı üret. Başında şu YAML metadata bloğu olsun:

---
faz_no: 01
faz_adi: "Problem Çerçeveleme ve Label Tasarımı"
tarih: <bugünün tarihi>
kapsam_ozeti: "Yön sınıflandırması için label taksonomisi, threshold ve ufuk seçimi"
bagimli_oldugu_fazlar: []
durum: taslak
hedef_kaynak_sayisi: 15
gerceklesen_kaynak_sayisi: <gerçekleşen>
kaynak_arac: "claude.ai Research"
son_guncelleme: <bugünün tarihi>
---

Başlık iskeleti (bu yapıya uy):
1. Giriş ve Problem Tanımı
2. Label Taksonomileri (2/3/N-sınıf karşılaştırması)
3. Threshold/Bant Belirleme Yöntemleri
4. Tahmin Ufku Seçimi ve Trade-off'lar
5. Class Imbalance – Label Tasarımı Etkileşimi
6. Meta-Labeling ve Alternatif Yaklaşımlar
7. Projeye Uygulanabilirlik Notları (karar matrisi + gerekçeli öneri sıralaması)
8. Açık Sorular / Literatürde Net Olmayanlar
9. Kaynakça (her kaynak için 1-2 cümlelik "neden ilgili" notu)

KALİTE KURALLARI
- Her somut iddiayı kaynağa bağla (yazar/kurum + yıl, mümkünse DOI/link).
- Her ana bölümün (2-6) sonunda kısa bir "Projeye Uygulanabilirlik" notu ver;
  bölüm 7'de bunları birleştir.
- Çelişkili bulguları açıkça işaretle, tek taraflı sunma.
- Emin olmadığın veya literatürün net olmadığı noktaları "literatürde net değil"
  diye açıkça yaz; tahmin yürütme.
- Kullandığın nihai arama sorgularını dökümanın sonunda şeffaf şekilde listele.
- Dil: Türkçe; kaynak başlıkları orijinal dilinde.
```

---

## Kullanım Notları (prompta dahil değil)

1. Çalıştırmadan önce bu dosyayı `prompts/01_problem_cerceveleme_prompt.md`
   olarak commit'le.
2. Research çıktısını `docs/01_problem_cerceveleme_label_tasarimi.md` olarak
   kaydet, `durum: taslak` bırak.
3. Çıktıyı bana getir — kalite kontrol listesinden geçirip revizyon önerilerimi
   vereceğim; onaydan sonra `tamamlandi` işaretleyip Faz 2/3/4 promptlarına
   geçeceğiz (bu üçü paralel çalıştırılabilir).
