"""
AŞAMA 2 — TÜFE / enflasyon verisi (kaynak seviyesi A: TCMB EVDS3 API).

Kullanim:
    EVDS_API_KEY ortam degiskenini ayarlayip calistir (Asama 1 ile ayni anahtar):
        (PowerShell) $env:EVDS_API_KEY = "..."; python scripts/veri/asama2_tufe.py
        (bash)       EVDS_API_KEY=... python scripts/veri/asama2_tufe.py
    Repo kokunde .env dosyasi varsa (EVDS_API_KEY=...) otomatik okunur.

API anahtari KODA GOMULMEZ; yalnizca ortam degiskeninden / .env'den okunur.

Seri: TP.FG.J0 (TUFE Genel Endeks, TUIK -> TCMB EVDS uzerinden dagitilir).
TUFE dogasi geregi zaten AYLIK yayimlanir (TUIK gunluk endeks uretmez) - bu
yuzden Asama 1'deki "gunluk cek" ilkesi burada uygulanamaz; en ham/en dusuk
seviye zaten aylik endeks degeridir. Aylik degisim (%) EVDS'ten hazir
CEKILMEZ, ham endeksten yerel olarak (pandas pct_change ile) TURETILIR - ayni
"kendi hesapla, kaynagin agregasyonuna guvenme" ilkesi.

AS-OF DATE / yayim_tarihi: TUIK TUFE'yi referans ayini takip eden ayin
3. is gunu civarinda aciklar (Faz 2 tarama bulgusu: "TUFE ... Aylik (ayin 3'u)",
bkz. docs/02_arac_piyasasi_dinamikleri.md). EVDS API'si yayim tarihini ayri bir
alan olarak DONDURMEDIGI icin, yayim_tarihi burada bu kurala gore YAKLASIK
hesaplanir (takip eden ayin takvim-3'u; hafta sonuna denk gelirse gercek resmi
yayim 1-2 gun kayabilir - bu bir yaklasimdir, kesin vintage kaydi degildir).
"""
import os
import sys
import json
from datetime import date, timedelta
from pathlib import Path

import requests
import pandas as pd

# 2024-12 de cekilir: 2025-01'in aylik yuzde degisimini hesaplayabilmek icin
# bir onceki ayin endeksi taban olarak gerekir. Rapor edilen/islenen aralik
# yine de 2025-01 .. 2025-12'dir.
BASLANGIC_AY = "2024-12"
BITIS_AY = "2025-12"
HEDEF_BASLANGIC_AY = "2025-01"
HEDEF_BITIS_AY = "2025-12"

EVDS_BASE_URL = "https://evds3.tcmb.gov.tr/igmevdsms-dis/"
SERIES = ["TP.FG.J0"]  # TUFE Genel Endeks (2003=100)

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "tufe"
ENV_PATH = REPO_KOKU / ".env"


def _env_dosyasini_yukle():
    """Basit .env okuyucu (ek bagimlilik gerektirmez)."""
    if not ENV_PATH.exists():
        return
    for satir in ENV_PATH.read_text(encoding="utf-8").splitlines():
        satir = satir.strip()
        if not satir or satir.startswith("#") or "=" not in satir:
            continue
        anahtar, deger = satir.split("=", 1)
        os.environ.setdefault(anahtar.strip(), deger.strip())


def _ay_baslangic_bitis_tarihleri(baslangic_ay: str, bitis_ay: str) -> tuple[str, str]:
    b_yil, b_ay = (int(x) for x in baslangic_ay.split("-"))
    e_yil, e_ay = (int(x) for x in bitis_ay.split("-"))
    ay_sonu_gun = pd.Period(f"{e_yil:04d}-{e_ay:02d}", freq="M").days_in_month
    start_date = f"01-{b_ay:02d}-{b_yil:04d}"
    end_date = f"{ay_sonu_gun:02d}-{e_ay:02d}-{e_yil:04d}"
    return start_date, end_date


def _yaklasik_yayim_tarihi(referans_ayi: str) -> str:
    """Referans ayini takip eden ayin takvim-3'u (yaklasik, resmi vintage degil)."""
    donem = pd.Period(referans_ayi, freq="M") + 1
    return date(donem.year, donem.month, 3).isoformat()


def evds_aylik_seri_cek(api_key: str, seriler: list[str], baslangic_ay: str, bitis_ay: str):
    """Tek kaynak fonksiyonu: EVDS3'ten aylik frekansta TUFE endeks serisini ceker.

    Basarisiz olursa None doner (cagiran taraf raporlar, program durmaz).
    """
    start_date, end_date = _ay_baslangic_bitis_tarihleri(baslangic_ay, bitis_ay)
    params = {
        "series": "-".join(seriler),
        "startDate": start_date,
        "endDate": end_date,
        "type": "json",
    }
    # Not: "frequency"/"aggregationTypes" parametreleri bu seri icin HTTP 400
    # doner (seri zaten dogal olarak aylik yayimlanir, agregasyona gerek yok;
    # denendi ve kayit altina alindi - kaynak kesfi).
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = EVDS_BASE_URL + query

    try:
        resp = requests.get(url, headers={"key": api_key}, timeout=30)
    except requests.RequestException as exc:
        print(f"[HATA] EVDS istegi basarisiz: {exc}", file=sys.stderr)
        return None

    if resp.status_code != 200:
        print(f"[HATA] EVDS HTTP {resp.status_code}: {resp.text[:300]}", file=sys.stderr)
        return None

    try:
        payload = resp.json()
    except ValueError:
        print(f"[HATA] EVDS yaniti JSON degil: {resp.text[:300]}", file=sys.stderr)
        return None

    if "items" not in payload:
        print(f"[HATA] EVDS yanitinda 'items' yok: {payload}", file=sys.stderr)
        return None

    return payload


def main():
    _env_dosyasini_yukle()
    api_key = os.environ.get("EVDS_API_KEY")
    if not api_key:
        print("[HATA] EVDS_API_KEY bulunamadi (ortam degiskeni veya .env). Once ayarlayin.", file=sys.stderr)
        sys.exit(1)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    payload = evds_aylik_seri_cek(api_key, SERIES, BASLANGIC_AY, BITIS_AY)
    if payload is None:
        print("[UYARI] Veri cekilemedi.")
        sys.exit(1)

    # Ham API yanitini oldugu gibi kaydet (kaynak izlenebilirligi icin).
    ham_path = RAW_DIR / "tufe_2025_raw.json"
    with open(ham_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(payload["items"])
    df = df.rename(columns={"Tarih": "tarih", "TP_FG_J0": "tufe_endeks"})
    df = df.drop(columns=["UNIXTIME"], errors="ignore")
    df["tufe_endeks"] = pd.to_numeric(df["tufe_endeks"], errors="coerce")
    # Aylik EVDS tarihleri "YYYY-M" formatinda doner (ay sifir-doldurmasiz,
    # ör. "2025-1"); DD-MM-YYYY (gunluk seride oldugu gibi) DEGIL.
    yil_ay = df["tarih"].str.split("-", n=1, expand=True)
    df["referans_ayi"] = yil_ay[0] + "-" + yil_ay[1].str.zfill(2)
    df = df.sort_values("referans_ayi").reset_index(drop=True)

    # Aylik yuzde degisim yerel olarak turetilir (EVDS'in hazir degisim serisi KULLANILMAZ).
    df["tufe_aylik_degisim"] = df["tufe_endeks"].pct_change() * 100
    df["yayim_tarihi"] = df["referans_ayi"].map(_yaklasik_yayim_tarihi)

    # Ham cekilen tum donem (2024-12 dahil) ayri kaydedilir.
    tam_csv = RAW_DIR / "tufe_2025_tam_donem.csv"
    tam_xlsx = RAW_DIR / "tufe_2025_tam_donem.xlsx"
    df.to_csv(tam_csv, index=False, encoding="utf-8-sig")
    df.to_excel(tam_xlsx, index=False, sheet_name="tufe_tam_donem")

    # Hedef aralik (2025-01..2025-12) - pipeline'a girecek asil tablo.
    hedef = df[(df["referans_ayi"] >= HEDEF_BASLANGIC_AY) & (df["referans_ayi"] <= HEDEF_BITIS_AY)].copy()
    hedef = hedef[["referans_ayi", "tufe_endeks", "tufe_aylik_degisim", "yayim_tarihi"]].reset_index(drop=True)

    hedef_csv = RAW_DIR / "tufe_2025_aylik.csv"
    hedef_xlsx = RAW_DIR / "tufe_2025_aylik.xlsx"
    hedef.to_csv(hedef_csv, index=False, encoding="utf-8-sig")
    hedef.to_excel(hedef_xlsx, index=False, sheet_name="tufe_aylik")

    beklenen_aylar = pd.period_range(HEDEF_BASLANGIC_AY, HEDEF_BITIS_AY, freq="M").astype(str).tolist()
    gelen_aylar = hedef["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== ASAMA 2 - TUFE OZET ===")
    print("Kaynak seviyesi: A (TCMB EVDS3 API, seri TP.FG.J0 - TUIK TUFE Genel Endeks)")
    print(f"Kapsam (hedef): {HEDEF_BASLANGIC_AY} .. {HEDEF_BITIS_AY}")
    print(f"Cekilen tam donem (taban dahil): {BASLANGIC_AY} .. {BITIS_AY}")
    print(f"Hedef aralikta gelen ay sayisi: {len(gelen_aylar)} / {len(beklenen_aylar)}")
    print(f"Eksik aylar: {eksik_aylar if eksik_aylar else 'yok'}")
    print()
    print("NOT: yayim_tarihi YAKLASIK hesaplanmistir (takip eden ayin takvim-3'u);")
    print("EVDS gercek yayim/vintage tarihini ayri alan olarak dondurmuyor.")
    print()
    print(f"Ham (aylik, API yaniti - taban dahil): {ham_path}")
    print(f"Tam donem tablo (taban dahil): {tam_csv} , {tam_xlsx}")
    print(f"Hedef aylik tablo (2025): {hedef_csv} , {hedef_xlsx}")
    print()
    print("--- Hedef aylik tablo (tamamı) ---")
    print(hedef.to_string(index=False))


if __name__ == "__main__":
    main()
