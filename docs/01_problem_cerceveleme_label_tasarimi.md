---
faz_no: 01
faz_adi: "Problem Çerçeveleme ve Label Tasarımı"
tarih: 2026-07-13
kapsam_ozeti: "Yön sınıflandırması için label taksonomisi, threshold ve ufuk seçimi"
bagimli_oldugu_fazlar: []
durum: tamamlandi
hedef_kaynak_sayisi: 15
gerceklesen_kaynak_sayisi: 17
kaynak_arac: "claude.ai Research"
son_guncelleme: 2026-07-14
---

# Faz 01 — Problem Çerçeveleme ve Label Tasarımı: Yön Sınıflandırması için Literatür Taraması

## TL;DR
- Yön etiketlemesinde tek "doğru" yaklaşım yoktur; seçim üç bağlı parametre tarafından belirlenir: sınıf sayısı (2/3/N), threshold türü (sabit vs oynaklık-uyarlamalı vs istatistiksel test), ve tahmin ufku. Bu üçü class balance'ı ve sinyal-gürültü oranını **birlikte** belirler — literatür bunların ayrı ayrı optimize edilemeyeceğinde net biçimde hemfikirdir.
- Finansal ML literatürünün en olgun katkısı López de Prado'nun triple-barrier + meta-labeling metodolojisidir; ancak bu yöntemler yol-bağımlı (path-dependent) sürekli işlem verisi ve stop-loss/take-profit mantığı için tasarlanmıştır — ikinci el araç piyasasının düşük frekanslı, ilan-tabanlı, endeks-düzeyli yapısına doğrudan aktarılamaz, uyarlanması gerekir.
- Araç piyasası için en savunulabilir başlangıç: **aylık** (ve ikincil olarak haftalık) ufuk + **oynaklık-uyarlamalı 3-sınıf** (up/down/stable) etiketleme; stable bandını sabit yüzde yerine segment oynaklığına ölçekleyerek belirlemek, hem class balance'ı hem de heterojen segmentler arası tutarlılığı korur.

## Key Findings

1. **3-sınıf (up/down/stable) etiketleme, ham doğruluğu düşürür ama "actionable" sinyallerin güvenilirliğini artırır.** Chalkidis & Savani (2021, ICAIF), emtia vadeli işlem piyasalarında ("we perform backtests on commodity futures markets") binary vs ternary'yi doğrudan kıyaslar: ternary sınıflandırıcının toplam (non-selective) doğruluğu daha düşüktür, ancak *selective* doğruluğu daha yüksek, kapsama (coverage) ise daha düşüktür ("total non-selective accuracy is lower in the ternary case... the total selective accuracy is higher in the ternary case, and the coverage is less in the ternary case"). Ortadaki "flat/neutral" sınıf, veri kurgusuna göre etiketlerin %45–54'ünü oluşturarak ("between 45 and 54% of the labels are 0 (flat)") modelin yönsüz bir bahisten çekilmesine (abstention) izin veren bir gürültü/false-positive filtresi işlevi görür.

2. **Fixed-horizon labeling literatürün en yaygın ama en kusurlu yöntemidir.** López de Prado (2018) sabit threshold + sabit ufuk yaklaşımının iki temel kusurunu belirtir: (a) getiriler heteroskedastiktir, sabit threshold zamanla değişen oynaklığı yakalayamaz; (b) yol-bağımsızdır, yani aradaki fiyat hareketini (stop-loss/take-profit tetiklenmesini) yok sayar.

3. **Triple-barrier yöntemi bu iki kusuru giderir** — iki yatay bariyer (oynaklığa göre ölçeklenmiş kar-al/zarar-kes) + bir dikey bariyer (maksimum tutma süresi). Etiket ilk dokunulan bariyere göre atanır. Bariyerler tipik olarak günlük oynaklığa bir çarpanla ölçeklenir.

4. **Meta-labeling, yönü (side) ve büyüklüğü (size) ayırır.** Birincil model yönü tahmin eder; ikincil (meta) model, birincil sinyalin doğru olup olmadığını (act/pass) tahmin eden bir ikili sınıflandırıcıdır. Amacı false positive'leri filtreleyerek precision ve F1'i artırmaktır.

5. **Tahmin ufku, class balance'ı ve öğrenilebilirliği doğrudan belirler.** Ufuk uzadıkça sinyal daha çok gerçekleşir ama gürültü de birikir; "Label Horizon Paradox" (Song et al., 2026, ICML) optimal eğitim ufkunun çıkarım ufkuyla aynı olmayabileceğini gösterir.

6. **Threshold + ufuk seçimi class balance'ı belirler; dengeli dağılım bir optimizasyon hedefi olarak kullanılır.** Kang (2025) Kore hisselerinde triple-barrier parametrelerini dengeli sınıf dağılımı için optimize eder: parametre taramasında zaman ufku 5–29 gün (1 gün adımla) ve yüzde eşiği %7–%15 (1 puan adımla) denenmiş, optimal konfigürasyon 29 günlük pencere ve %9 kar-al/zarar-kes olarak bulunmuştur ("The optimal configuration was found to be a prediction horizon of 29 days and take-profit/stop-loss percentage of 9%"), bu da stable %36.16 / up (take-profit) %34.89 / down (stop-loss) %28.95 dağılımını verir.

## Details

### 1. Giriş ve Problem Tanımı

Bu faz, ikinci el araç piyasasında fiyat yönü tahmini (up/down/stable) için problem çerçeveleme ve label tasarımının metodolojik temelini kurar. Nihai uygulama araç piyasası olsa da, yön etiketleme metodolojisinin en olgun olduğu alan finansal piyasalardır (hisse, kripto, emtia, limit order book). Bu nedenle tarama uluslararası finansal ML literatürüne odaklanır ve her bulgu araç piyasası bağlamına çevrilir.

Araç piyasasının üç yapısal özelliği tüm değerlendirmeyi biçimlendirir: (a) **düşük frekans** — günlük tick verisi değil, muhtemelen haftalık/aylık gözlem; (b) **endeks/segment düzeyi** — marka/model/yaş grubu bazında ortalama fiyat; (c) **ilan (listing) tabanlı** — sürekli işlem verisi değil, ilan fiyatları. Bu özellikler, HFT/LOB literatüründen gelen yöntemlerin (örn. tick-time bariyerler) doğrudan aktarılamayacağı anlamına gelir.

Karşılaştırma noktası olarak, Manheim Used Vehicle Value Index (Cox Automotive) aylık yayınlanan, karma/kilometre/mevsimsellik için düzeltilmiş bir toptan araç fiyat endeksidir ve yılda 5 milyondan fazla işlem ile 20 J.D. Power piyasa sınıfı üzerinden hesaplanır ("over 5 million transactions annually"). Aylık hareketler tipik olarak küçük ölçeklidir: Cox Automotive'in 8 Temmuz 2026 açıklamasına göre endeks Haziran 2026'da 212.9'a yükselmiş, bu yıllık %2.1 ama aya göre yalnızca %0.1 artışa karşılık gelmiştir; şirket ayrıca Haziran için uzun-dönem ortalama aylık hareketin +%0.5 olduğunu belirtir ("below the long-term average June increase of 0.5%"). Bu, araç fiyat serilerinin aylık ölçekte **düşük oynaklıklı** olduğunu ve threshold seçiminin bu düşük oynaklık düzeyine kalibre edilmesi gerektiğini gösterir.

### 2. Label Taksonomileri (2/3/N-sınıf karşılaştırması)

**2-sınıf (up/down).** En basit çerçeveleme; getirinin işaretine göre etiketleme. Avantajı: sınıf dengesi genelde makuldür (getiri dağılımı ~simetrik), öğrenilebilirlik yüksektir, backtest/trading mantığına doğrudan bağlanır. Dezavantajı: sıfıra yakın (gürültü) hareketleri zorla bir yöne atar, bu da etiket gürültüsü yaratır.

**3-sınıf (up/down/stable).** Ortaya bir "no-action/stable" bandı ekler. Chalkidis & Savani (2021, ICAIF, DOI: 10.1145/3490354.3494379, arXiv:2110.14914) bunu doğrudan kıyaslayan en iyi çalışmadır: ternary sınıflandırıcının toplam doğruluğu daha düşük ("the ternary classifier has to be strictly more discerning"), ancak selective doğruluğu daha yüksek, kapsaması daha düşüktür. Flat sınıfı etiketlerin %45–54'ünü oluşturur. Yani stable sınıfı bir abstention mekanizmasıdır. Aynı çalışma, class imbalance'ın özellikle threshold çarpanı uçlarda (0.3 veya 1.2) belirginleştiğini ve bunu class weighting ile ele aldıklarını belirtir.

**Continuous Trend Labeling (CTL).** Wu et al. (2020, Entropy 22(10):1162, DOI: 10.3390/e22101162) fixed-horizon'a alternatif olarak, ardışık tepe/dip noktaları arasındaki dalgalanma bir eşik ω'yı aştığında sürekli bir trend tanımlar. NOT: bu bir *binary* (up-trend/down-trend) yöntemdir, 2-vs-3 sınıf kıyaslaması değildir (yaygın bir yanlış atıf). Ortalama ML doğruluğu ~0.6–0.7; LSTM/GRU SSCI/SZCI'de ~0.72; net getiri (NYR) fixed-horizon varyantlarını aşar. Bu yöntem, "gerçek piyasa trendini" yakalamayı ve kısa vadeli rastgeleliği filtrelemeyi amaçlar.

**Quantile/tercile-tabanlı N-sınıf.** Getirileri kendi ampirik dağılımının terciline/kuantillerine göre bölme (örn. alt/orta/üst üçte bir). Avantajı: **tanım gereği dengeli sınıflar** üretir (her sınıf eşit sayıda gözlem). Dezavantajı: sınıf sınırları veri-bağımlıdır ve zamanla kayar; eşik ekonomik olarak yorumlanabilir bir "stable" tanımına karşılık gelmeyebilir. Kuantil-tabanlı sınıflandırıcılar özellikle çarpık/kalın kuyruklu dağılımlarda iyi çalışır (Hennig & Viroli, 2016 geleneği).

**Projeye Uygulanabilirlik (Bölüm 2).** Araç piyasası aylık ölçekte düşük oynaklıklı olduğundan, 2-sınıf etiketleme çok sayıda gürültü hareketini zorla yönlendirir; 3-sınıf, "stable" segmentlerini (fiyatın yatay seyrettiği model/yaş grupları) doğal olarak yakalar ve iş açısından da anlamlıdır (bir bayi için "hareketsiz" bir segment gerçek bir karardır). Quantile-tabanlı yaklaşım, segmentler arası heterojen oynaklığı otomatik dengelediği için çok-segmentli bir kurgu (marka/model/yaş) için cazip bir yedek seçenektir.

### 3. Threshold/Bant Belirleme Yöntemleri

**Sabit (fixed) threshold.** Getiri τ'yı aşarsa up, -τ altındaysa down, arada ise stable. Basit ve yorumlanabilir; ancak heteroskedastisiteyi yok sayar. López de Prado (2018) ve DeepLOB literatürü bunun temel zayıflığını vurgular: yüksek oynaklıkta bir eşiği aşmak kolay, düşük oynaklıkta zordur — "one size does not fit all".

**Oynaklık-uyarlamalı (volatility-adjusted) threshold.** Eşik, geçmiş n-periyot oynaklığının (std sapma, EWMA veya ATR) bir çarpanı olarak dinamik belirlenir. Triple-barrier bariyerleri de tipik olarak böyle ölçeklenir. Bu, heteroskedastik serilerde sınıf tanımını istikrarlı tutar.

**İstatistiksel test tabanlı yaklaşımlar.**
- *Trend-scanning* (López de Prado, 2020, *Machine Learning for Asset Managers*, §5.4–5.5): t ile t+L arası çoklu OLS regresyonu, eğim katsayısının |t-değeri|'ni maksimize eden L seçilir; t-değerinin işareti etiketi (+1/0/-1), büyüklüğü ise sample weight'i verir. Eşik önceden sabitlenmez; istatistiksel anlamlılıktan türetilir. Doğal olarak üçlü (up/no-trend/down) çıktı verir ve minimum t-değeri eşiği ile "no-trend" sınıfı tanımlanır.
- *CUSUM filtresi* (López de Prado, 2018, Ch. 2, §2.5.2.1): pozitif/negatif kümülatif toplamlar (S⁺/S⁻) bir eşiği aştığında olay örneklenir ve toplam sıfırlanır. Amaç, sabit zaman ızgarası yerine "anlamlı" hareketlerde örnekleme yapmaktır; eşik sıklıkla sabit yerine anlık (EWMA) oynaklığa bağlanır.

Kovačević et al. (2023, IEEE Access 11:83822–83832, DOI: 10.1109/ACCESS.2023.3303283) etiketleme algoritmalarının "robustness"ını (sınıflandırıcının genelleme hatası karşısında etiketlerin dayanıklılığı) ölçen formal bir metrik ve bir gürültü modeli önerir; sınıflandırıcı eğitmeden robustness değerlendirmeye izin verir ve Oracle > Continuous Trend > Fixed Horizon sıralamasını bulur.

**Projeye Uygulanabilirlik (Bölüm 3).** Aylık araç serilerinde sabit %1/%3/%5 threshold'lar cazip görünse de, segmentler arası oynaklık farkı (lüks vs kompakt, EV vs non-EV) tek bir sabit eşiği sorunlu kılar. Oynaklık-uyarlamalı eşik (her segmentin kendi aylık getiri std sapmasının katı) burada en savunulabilir yöntemdir. Trend-scanning düşük frekanslı seride kısa L pencereleriyle (örn. 3–12 ay) uygulanabilir ve "no-trend" segmentlerini istatistiksel anlamlılıkla tanımlar — bu, ilan-tabanlı gürültüye karşı doğal bir savunmadır.

### 4. Tahmin Ufku Seçimi ve Trade-off'lar

Song et al. (2026, ICML/PMLR 306, arXiv:2602.03395) "Label Horizon Paradox"ı ortaya koyar: eğitim etiketinin optimal ufku, çıkarım hedefinin ufkuyla aynı olmak zorunda değildir. Neden: ufuk uzadıkça (1) marjinal sinyal gerçekleşmesi artar (bilgi fiyata yansır), ama (2) marjinal gürültü birikimi de artar; optimal ufuk bu ikisinin eşitlendiği noktadır. Yazarlar bunu bir bi-level optimizasyon çerçevesiyle tek bir eğitim koşusunda öğrenilebilir kılar. Günlük hisse getirilerinin düşük sinyal-gürültü oranı iyi bilinir ve kısa ufuklu nokta tahminini zorlaştırır.

LOB literatüründe ufuk "tick" cinsindendir (FI-2010: k=10,20,30,50,100 tick; Ntakaris et al., 2018); kısa k daha çok gürültü, uzun k daha çok yumuşatma getirir. Kripto çalışmaları günlük/haftalık/aylık ufukları kıyaslar (örn. 2 gün, 2 hafta, 2 ay).

**Projeye Uygulanabilirlik (Bölüm 4).** Araç piyasasında günlük ufuk anlamsızdır (ilan verisi günlük anlamlı sinyal taşımaz). Haftalık ufuk, ilan yenilenme döngüsü ve mevsimsellik gürültüsü nedeniyle sınırda; aylık ufuk, Manheim gibi endekslerin de yayın frekansıdır ve sinyal-gürültü açısından daha savunulabilir. Label Horizon Paradox'un pratik çıkarımı: nihai hedef aylık yön olsa bile, eğitim etiketi için 1-aydan farklı bir proxy ufuk (örn. 2–3 aylık kümülatif hareket) denenmeli.

### 5. Class Imbalance – Label Tasarımı Etkileşimi

Threshold ve ufuk, sınıf dağılımını doğrudan belirler: geniş stable bandı → baskın neutral sınıf; dar bant → baskın yön sınıfları. Kang (2025, arXiv:2504.02249) triple-barrier parametrelerini *dengeli dağılım için* optimize eder (29 gün, %9): time-limit (stable) %36.16, take-profit (up) %34.89, stop-loss (down) %28.95 — nispeten dengeli bir bölünme. Değerlendirmede macro-F1 kullanır çünkü accuracy dengesiz sınıflarda yanıltıcıdır.

Bir başka çalışma (arXiv:2605.25894, kazanç açıklama günleri) τ=%3 ile 3-sınıf hedef üretir ve NEUTRAL sınıfının ~%67'ye ulaştığını, bunu weighted cross-entropy ile hafiflettiğini raporlar. Bu, dar/geniş bant kararının imbalance'ı nasıl belirlediğinin somut ve karşıt bir örneğidir (Kang'da dengeli, burada aşırı dengesiz).

Literatürdeki imbalance yönetimi araçları: (a) threshold/ufuğu dengeli dağılım için optimize etmek (label tasarımı düzeyinde çözüm), (b) class weighting / weighted loss, (c) oversampling/undersampling (SMOTE ve türevleri), (d) macro-F1 gibi dengeli metrikler. Kredi/finansal distress literatürü (örn. resampling çalışmaları) hiçbir tekniğin evrensel üstün olmadığını, seçimin maliyet yapısına bağlı olduğunu vurgular.

**Projeye Uygulanabilirlik (Bölüm 5).** Araç piyasasında düşük aylık oynaklık, sabit bir stable bandının (örn. ±%3) neutral sınıfını aşırı şişireceği anlamına gelir (arXiv:2605.25894'teki ~%67 durumuna benzer risk). Bunu önlemenin en temiz yolu label tasarımı düzeyinde çözmektir: ya oynaklık-uyarlamalı bant, ya da doğrudan quantile-tabanlı bölme (her sınıf ~1/3). Resampling'i son çare olarak bırakmak, label tasarımıyla dengeyi kurmak tercih edilmelidir çünkü sentetik örnekleme düşük frekanslı seride veri yapısını bozabilir.

### 6. Meta-Labeling ve Alternatif Yaklaşımlar

Meta-labeling (López de Prado, 2018; Joubert, 2022, SSRN 4032018 & JFDS DOI: 10.3905/jfds.2022.1.098) yönü (side) ve büyüklüğü (size) ayırır: birincil model yönü verir (-1/0/1), ikincil ikili model her sinyal için "act/pass" kararı verir. Amaç: false positive'leri filtreleyerek precision ve F1 artırmak. Meyer, Joubert & Alfeus (2022, JFDS DOI: 10.3905/jfds.2022.1.108) çeşitli meta-labeling mimarilerini (feature-driven, strategy-driven, inverse meta-labeling) sistematize eder.

Ampirik durum karışıktır: Singh & Joubert (Hudson & Thames working paper) meta-labeling + triple-barrier + event-based sampling'in strateji performansını (Sharpe, drawdown) iyileştirdiğini bulur; ancak bu genelde sentetik/simüle veri ve trading-metrik odaklıdır, saf yön-sınıflandırma doğruluğu değil.

Alternatif/genişletme yaklaşımları:
- *Trend-scanning* (yukarıda) — bariyer yerine istatistiksel trend.
- *Adaptive Event-Driven Labeling / AEDL* (Bellafkih et al., 2025, Applied Sciences 15(24):13204, DOI: 10.3390/app152413204): fixed/triple-barrier/trend-scanning'i doğrudan kıyaslar; 16 varlık, 2000–2025. Ortalama Sharpe: Fixed Horizon −0.29, Triple Barrier −0.03, Trend Scanning 0.00, AEDL 0.48 (yazar-raporlu, orta-kademe dergi, dikkatle yorumlanmalı). Wilcoxon testleriyle Fixed Horizon'a göre iyileşme p=0.0024. Önemli karşı-bulgu: trend-scanning bu çalışmada risk-ayarlı metrikte üstün çıkmamıştır.

**Projeye Uygulanabilirlik (Bölüm 6).** Meta-labeling'in tam hali (side/size ayrımı, bet sizing) bir *trading* stratejisi için tasarlanmıştır; araç piyasası bir işlem/portföy problemi değil, bir tahmin/istihbarat problemi ise, meta-labeling'in katma değeri sınırlıdır. Ancak "corrective" mantığı (bir birincil yön tahmininin güvenilirliğini ikincil bir modelle skorlamak) araç segment tahmininde bir güven/abstention katmanı olarak uyarlanabilir — özellikle bazı segmentlerde (yüksek belirsizlik) tahminden çekilmek istendiğinde.

### 7. Projeye Uygulanabilirlik Notları — Karar Matrisi ve Öneri Sıralaması

**Karar Matrisi: Etiketleme Seçenekleri × Trade-off'lar (araç piyasası bağlamı)**

| Seçenek | Class Balance | Öğrenilebilirlik / Sinyal-Gürültü | İş Yorumlanabilirliği | Araç Piyasasına Uygunluk | Ana Risk |
|---|---|---|---|---|---|
| 2-sınıf (up/down), sabit τ | İyi (simetrik getiri) | Gürültü hareketleri zorla yönlenir → etiket gürültüsü | Yüksek | Orta | Düşük oynaklıkta anlamsız yön ataması |
| 3-sınıf, sabit τ (%1/%3/%5) | Kötü (düşük oynaklıkta neutral şişer) | Orta | Yüksek | Düşük–Orta | Sabit eşik segment heterojenliğini yok sayar |
| 3-sınıf, oynaklık-uyarlamalı bant | İyi (dinamik) | İyi (heteroskedastisiteye dayanıklı) | Orta–Yüksek | **Yüksek** | Oynaklık tahmini penceresi seçimi |
| Quantile/tercile (3-sınıf) | Mükemmel (tanım gereği ~1/3) | İyi | Orta (sınırlar veri-bağımlı) | **Yüksek** | Sınıf sınırları zamanla kayar; ekonomik anlam zayıf |
| Triple-barrier | Optimize edilebilir | İyi (yol-bağımlı) | Orta (trading odaklı) | Düşük–Orta | İlan verisinde "yol" ve stop-loss mantığı yok |
| Trend-scanning (t-value) | Orta (no-trend oranı L'ye bağlı) | İyi (istatistiksel anlamlılık filtresi) | Orta | Orta–Yüksek | Düşük frekansta kısa L ile örneklem yetersizliği |
| Meta-labeling (katman) | — (ikincil) | Precision/F1 artırır | Düşük (black-box üstü) | Düşük (trading için) | Tahmin problemi için aşırı mühendislik |

**Ufuk × Threshold alt-matrisi:**

| Ufuk | Sinyal-Gürültü | Class Balance eğilimi | Araç piyasası uygunluğu |
|---|---|---|---|
| Günlük | Çok düşük | Aşırı neutral | Uygun değil (ilan verisi) |
| Haftalık | Düşük–Orta | Neutral ağırlıklı | Sınırda; ilan döngüsü gürültüsü |
| Aylık | Orta | Dengeye yakın | **Tercih edilen** |
| 2–3 aylık (proxy) | Orta–Yüksek | Yön sınıfları güçlenir | Eğitim proxy'si olarak denenmeli |

**Gerekçeli Öneri Sıralaması (karar matrisinden türetilmiş):**

1. **Birincil öneri: Aylık ufuk + oynaklık-uyarlamalı 3-sınıf (up/down/stable).** Stable bandını her segmentin kendi aylık getiri oynaklığının bir katı (örn. ±0.5σ–1σ) olarak tanımla. Gerekçe: heteroskedastisiteye dayanıklı, class balance'ı segmentler arası korur, iş açısından yorumlanabilir. Manheim benzeri endekslerin aylık düşük oynaklığı (aya göre ~%0.1, uzun-dönem ~%0.5) bu yaklaşımı destekler — sabit yüzde eşikleri bu düzeyde ya çok geniş ya çok dar olur.
2. **İkincil/yedek: Quantile-tabanlı 3-sınıf (tercile).** Class balance garanti; çok-segmentli kurguda heterojen oynaklığı otomatik dengeler. Ekonomik "stable" tanımı zayıfladığı için birincil değil yedek.
3. **Değerlendirme aracı olarak: Trend-scanning etiketleri (kısa L, 3–12 ay).** Birincil etiketlemenin "no-trend" segmentlerini istatistiksel anlamlılıkla doğrulamak için ikinci bir görüş; sample weight olarak t-value kullanımı.
4. **Erken evrede kullanma: Triple-barrier ve tam meta-labeling.** İlan-tabanlı, yol-bilgisi olmayan veride triple-barrier'ın yatay bariyer mantığı zayıflar; meta-labeling bir trading katmanıdır. Ancak ileri fazda bir "güven/abstention" katmanı olarak yeniden değerlendirilebilir.

**Öneriyi değiştirecek eşikler/benchmarklar:** (a) Eğer aylık veri az ise (ör. <100 gözlem/segment), 3-sınıf yerine 2-sınıfa düşülmeli. (b) Eğer oynaklık-uyarlamalı bant hâlâ %60+ neutral üretiyorsa, quantile-tabanlıya geçilmeli. (c) Eğer 2–3 aylık proxy ufuk cross-validation'da aylık hedefte macro-F1'i anlamlı artırıyorsa (Label Horizon Paradox), proxy ufuk benimsenmeli.

### 8. Açık Sorular / Literatürde Net Olmayanlar

- **2-vs-3 sınıf temiz F1 kıyası yok.** Aynı veri/model üzerinde "binary F1 = X, ternary F1 = Y" veren tek bir hakemli çalışma bulunamadı; Chalkidis & Savani (2021) en yakını ama tek bir F1 çifti yerine etkinin yönünü ve coverage aralıklarını raporlar. **Bu nokta literatürde net değildir.**
- **Düşük frekanslı, ilan-tabanlı piyasalar için etiketleme literatürü yoktur.** Tüm olgun metodoloji sürekli işlem verisi (hisse/kripto/LOB) içindir. Araç piyasasına aktarımın ampirik doğrulaması literatürde yoktur — bu, projeye özgü deney gerektirir.
- **Optimal stable bandı genişliği için önceden belirlenmiş bir değer yoktur.** %1/%3/%5 gibi değerler tamamen veri/oynaklık bağımlıdır; literatür sabit bir tavsiye vermez.
- **Trend-scanning'in üstünlüğü tartışmalı.** mlfinlab/López de Prado geleneği güçlü sunar, ancak AEDL (2025) çalışmasında risk-ayarlı metrikte üstün çıkmamıştır (Sharpe 0.00). Çelişkili bulgu olarak işaretlenmiştir.
- **Meta-labeling ampirik kanıtı çoğunlukla trading-metrik ve sentetik veri temelli**; saf yön-sınıflandırma doğruluğu üzerindeki etkisi bağımsız olarak daha az doğrulanmıştır.

## Recommendations

**Aşama 1 (hemen):** Aylık ufukta, segment-bazlı oynaklık-uyarlamalı 3-sınıf etiketleme prototipi kur. Stable bandını ±0.5σ ile ±1σ arasında tara ve her bant için sınıf dağılımını raporla. Benchmark: hiçbir sınıf %60'ı aşmamalı.

**Aşama 2 (kalibrasyon):** Paralelde quantile-tabanlı (tercile) etiketlemeyi yedek olarak üret ve iki yaklaşımın sınıf dağılımını + (ileri fazda) öğrenilebilirliğini kıyasla. Eğer oynaklık-uyarlamalı bant %60+ neutral üretiyorsa quantile'a geç.

**Aşama 3 (ufuk deneyi):** Label Horizon Paradox'u test et — nihai hedef aylık yön kalırken, eğitim etiketi için 2 ve 3 aylık proxy ufukları dene. macro-F1'de anlamlı iyileşme varsa proxy ufuğu benimse.

**Aşama 4 (opsiyonel derinleştirme):** Trend-scanning etiketlerini kısa L pencereleriyle (3–12 ay) ikinci bir görüş/sample-weight kaynağı olarak ekle. Meta-labeling'i yalnızca bir abstention/güven katmanı gerekirse değerlendir.

**Değiştirici benchmarklar:** Segment başına gözlem <100 → 2-sınıfa düş. Neutral oranı sürekli %60+ → quantile. Proxy ufuk macro-F1'i artırmıyor → aylık hedef ufukta kal.

## Caveats

- Bu faz yalnızca label tasarımını kapsar; sınıflandırma algoritmaları, model mimarileri, genel feature engineering ve araç piyasasına özgü iktisadi dinamikler (kur, vergi, arz şokları) kapsam dışıdır ve yalnızca bağlam için değinilmiştir.
- Finansal ML bulguları araç piyasasına *analojik* olarak aktarılmıştır; doğrudan ampirik doğrulama literatürde yoktur (bkz. Bölüm 8).
- Bazı kaynaklar (AEDL 2025, MDPI Applied Sciences) orta-kademe dergilerdir ve sayısal sonuçlar yazar-raporludur; dikkatle yorumlanmalıdır.
- López de Prado kitaplarının kesin sayfa numaraları bağımsız açık kaynaktan doğrulanamadı; bölüm referansları (AFML Ch.2-3; MLAM §5.4-5.5) güvenilirdir.
- Manheim/MUVVI verileri ABD toptan araç piyasasına aittir; Türkiye ikinci el araç piyasasının oynaklık düzeyi farklı olabilir ve projeye özgü olarak ayrıca ölçülmelidir.
- Hedef kitle ileri seviye olduğundan temel ML/istatistik açıklamaları kasıtlı olarak dahil edilmemiştir.

## Kaynakça

1. **Marcos López de Prado (2018), *Advances in Financial Machine Learning*, Wiley.** — Triple-barrier ve meta-labeling metodolojisinin, CUSUM filtresinin (Ch.2, §2.5.2.1) ve triple-barrier'ın (Ch.3) birincil kaynağı; fixed-horizon labeling'in kusurlarını tanımlar.
2. **Marcos López de Prado (2020), *Machine Learning for Asset Managers*, Cambridge University Press.** — Trend-scanning etiketleme yönteminin (§5.4-5.5) birincil kaynağı.
3. **Chalkidis & Savani (2021), "Trading via Selective Classification", ICAIF '21, DOI: 10.1145/3490354.3494379 (arXiv:2110.14914).** — Binary vs ternary yön etiketlemesinin en iyi doğrudan ampirik kıyaslaması; selective accuracy/coverage trade-off'u; flat sınıfı %45–54.
4. **Wu, Wang, Su, Tang & Wu (2020), "A Labeling Method for Financial Time Series Prediction Based on Trends", Entropy 22(10):1162, DOI: 10.3390/e22101162.** — Continuous Trend Labeling; fixed-horizon'a alternatif binary trend yöntemi.
5. **Kovačević, Merćep, Begušić & Kostanjčar (2023), "Optimal Trend Labeling in Financial Time Series", IEEE Access 11:83822-83832, DOI: 10.1109/ACCESS.2023.3303283.** — Etiketleme algoritmalarının robustness'ını ölçen formal metrik ve gürültü modeli.
6. **Song, Liu & Chen (2026), "The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting", ICML/PMLR 306, arXiv:2602.03395.** — Optimal eğitim ufkunun çıkarım ufkuyla aynı olmayabileceğine dair teori + bi-level optimizasyon.
7. **Kang (2025), "Stock Price Prediction Using Triple Barrier Labeling and Raw OHLCV Data: Evidence from Korean Markets", arXiv:2504.02249.** — Triple-barrier parametrelerini dengeli sınıf dağılımı için optimize eder (29 gün, %9; %36.16/%34.89/%28.95).
8. **Zhang, Zohren & Roberts (2019), "DeepLOB: Deep Convolutional Neural Networks for Limit Order Books", IEEE TSP (arXiv:1808.03668).** — 3-sınıf mid-price hareket etiketlemesi; ufuk k ve threshold α tanımı; neutral sınıfın false-positive azaltma gerekçesi.
9. **Ntakaris et al. (2018), FI-2010 benchmark dataset.** — 5 ufuk (k=10,20,30,50,100 tick) için 3-sınıf etiketli LOB benchmark'ı; ufuk-gürültü ilişkisi.
10. **Joubert (2022), "Meta-Labeling: Theory and Framework", JFDS, DOI: 10.3905/jfds.2022.1.098 (SSRN 4032018).** — Meta-labeling'in üç bileşene ayrıştırılması ve strateji-metriği ilişkisi.
11. **Meyer, Joubert & Alfeus (2022), "Meta-Labeling Architecture", JFDS, DOI: 10.3905/jfds.2022.1.108.** — Feature/strategy-driven ve inverse meta-labeling mimarileri.
12. **Singh & Joubert (2022), "Does Meta-Labeling Add to Signal Efficacy?", Hudson & Thames working paper.** — Meta-labeling + triple-barrier + event-based sampling'in strateji metriklerini iyileştirdiğine dair ampirik kanıt (dikkat: trading-metrik odaklı, working paper).
13. **Bellafkih et al. (2025), "Adaptive Event-Driven Labeling (AEDL): Multi-Scale Causal Framework with Meta-Learning for Financial Time Series", Applied Sciences 15(24):13204, DOI: 10.3390/app152413204.** — Fixed/triple-barrier/trend-scanning doğrudan Sharpe kıyası (orta-kademe dergi, yazar-raporlu); Wilcoxon p=0.0024.
14. **Grądzki et al. (2025), "Algorithmic crypto trading using information-driven bars, triple barrier labeling and deep learning", Financial Innovation 11:136, DOI: 10.1186/s40854-025-00866-w.** — Kriptoda triple-barrier + bilgi-tabanlı bar örneklemesi; farklı tahmin ufukları (2 gün/2 hafta/2 ay).
15. **"Predicting Stock Price Direction on Earnings Announcement Days using Multi-modal Deep Learning" (arXiv:2605.25894).** — τ=%3 ile 3-sınıf; NEUTRAL ~%67 imbalance ve weighted cross-entropy ile yönetimi; macro-F1 ve maliyet-duyarlı metrikler.
16. **Cox Automotive / Manheim Used Vehicle Value Index (2025-2026), coxautoinc.com & Moody's Analytics.** — Aylık toptan araç fiyat endeksi (>5M işlem/yıl, 20 sınıf); araç serilerinin aylık ölçekte düşük oynaklığına (aya göre ~%0.1, uzun-dönem ~%0.5) dair bağlam.
17. **Namlı & Ünlü, "Fiyat Tahminlemesinde Makine Öğrenmesi Teknikleri ve Doğrusal Regresyon Yöntemlerinin Kıyaslanması: Türkiye'de Satılan İkinci El Araç Fiyatlarının Tahminlenmesine Yönelik Bir Vaka Çalışması", Konya Journal of Engineering Sciences.** — Türkiye ikinci el araç fiyat tahmini bağlamı (regresyon odaklı; yön etiketleme değil — kapsam farkının altını çizmek için).

### Kullanılan Nihai Arama Sorguları (şeffaflık)
İngilizce: "triple barrier labeling meta-labeling Lopez de Prado"; "price direction classification up down stable three-class"; "threshold selection financial time series direction labeling"; "prediction horizon selection signal to noise financial forecasting"; "meta-labeling critique extension empirical study F1"; "quantile based labeling returns classification tercile"; "triple barrier labeling class imbalance stock prediction arXiv"; "volatility adjusted dynamic threshold labeling returns heteroskedastic"; "trend scanning labeling Lopez de Prado t-value regression"; "class imbalance financial direction prediction resampling cost sensitive"; "DeepLOB limit order book mid-price movement three class labeling horizon k"; "cryptocurrency price direction prediction triple barrier three class study"; "fixed horizon labeling problems noise Dixon deep learning financial"; "meta-labeling architecture Joubert 2022 primary secondary model position sizing"; "used car price index forecasting Manheim wholesale monthly".
Türkçe: "fiyat yönü sınıflandırma zaman serisi etiketleme"; "ikinci el araç fiyat tahmini makine öğrenmesi Türkiye".

*İlk verilen sorgu listesinden genişletilen sorgular (şeffaflık gereği):* trend-scanning t-value; class imbalance resampling/cost-sensitive; DeepLOB/LOB horizon-k; meta-labeling architecture (Joubert/Meyer); Manheim/MUVVI araç fiyat endeksi; Türkçe ikinci el araç fiyat tahmini. Bu genişletmeler, (a) istatistiksel-test-tabanlı threshold yöntemlerini derinleştirmek, (b) araç piyasası bağlamı için düşük-frekanslı bir referans endeks bulmak ve (c) 2-vs-3 sınıf ile trend-scanning'in ampirik kıyaslarını (subagent aracılığıyla) sağlamlaştırmak için yapılmıştır.