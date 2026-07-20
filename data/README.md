# data/ — MVP Örnek Veri Seti

Bu klasör, araç piyasası fiyat yönü tahmini projesinin MVP (örnek/prototip)
veri setini barındırır. Kamuya açık kaynaklardan çekilecek küçük, uçtan uca
çalışan bir aylık zaman serisi veri setidir (bkz. `prompts/veri/01_mvp_cekirdek_veri_prompt.md`).

**UYARI:** Bu klasöre şirket içi, lisanslı veya özel veri **konulmaz** (karar
K5 — `docs/00_karar_kaydi.md`). Yalnızca kamuya açık kaynaklardan (TCMB EVDS,
TÜİK, BETAM sahibindex, arabam.com vb.) çekilen veri kullanılır.

Veri dosyaları `.gitignore` ile Git dışıdır; yalnızca klasör yapısı (`raw/`,
`processed/` ve bu README) versiyonlanır. Prompt/kod versiyonlanır, çekilen
veri versiyonlanmaz.

## Klasörler

- `raw/` — her kaynaktan çekilen ham dosyalar (değiştirilmemiş).
- `processed/` — birleştirilmiş, temizlenmiş, aylık tek tablo haline getirilmiş veri.

## Bilinen sınır

Kamuya açık ikinci el araç fiyat serileri (BETAM sahibindex, arabam.com aylık
fiyat endeksi) mix/kompozisyon düzeltmesizdir (karar N1). MVP aşamasında bu
seriler **yer tutucu (proxy) hedef** olarak kullanılır; nihai hedef değildir.
