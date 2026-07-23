"""
GENIŞLETME AŞAMA 1b — TÜFE verisi, 2024-01 -> bugün (kaynak seviyesi A).

MVP scriptinden (asama2_tufe.py) FARKLI ciktilara yazar; MVP ciktilarinin
uzerine YAZMAZ. 2023-12 taban ayi da cekilir (2024-01'in aylik degisimi icin).
"""
import os
import sys
import json
from datetime import date
from pathlib import Path

import requests
import pandas as pd

BASLANGIC_AY = "2023-12"  # taban ay (2024-01'in aylik degisimi icin)
BITIS_AY = date.today().strftime("%Y-%m")
HEDEF_BASLANGIC_AY = "2024-01"
HEDEF_BITIS_AY = BITIS_AY

EVDS_BASE_URL = "https://evds3.tcmb.gov.tr/igmevdsms-dis/"
SERIES = ["TP.FG.J0"]

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "tufe"
ENV_PATH = REPO_KOKU / ".env"


def _env_dosyasini_yukle():
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
    donem = pd.Period(referans_ayi, freq="M") + 1
    return date(donem.year, donem.month, 3).isoformat()


def evds_aylik_seri_cek(api_key: str, seriler: list[str], baslangic_ay: str, bitis_ay: str):
    start_date, end_date = _ay_baslangic_bitis_tarihleri(baslangic_ay, bitis_ay)
    params = {"series": "-".join(seriler), "startDate": start_date, "endDate": end_date, "type": "json"}
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = EVDS_BASE_URL + query
    try:
        resp = requests.get(url, headers={"key": api_key}, timeout=60)
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
        print("[HATA] EVDS_API_KEY bulunamadi.", file=sys.stderr)
        sys.exit(1)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    payload = evds_aylik_seri_cek(api_key, SERIES, BASLANGIC_AY, BITIS_AY)
    if payload is None:
        print("[UYARI] Veri cekilemedi.")
        sys.exit(1)

    ham_path = RAW_DIR / "tufe_2024_bugun_raw.json"
    with open(ham_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(payload["items"])
    df = df.rename(columns={"Tarih": "tarih", "TP_FG_J0": "tufe_endeks"})
    df = df.drop(columns=["UNIXTIME"], errors="ignore")
    df["tufe_endeks"] = pd.to_numeric(df["tufe_endeks"], errors="coerce")
    yil_ay = df["tarih"].str.split("-", n=1, expand=True)
    df["referans_ayi"] = yil_ay[0] + "-" + yil_ay[1].str.zfill(2)
    df = df.sort_values("referans_ayi").reset_index(drop=True)

    df["tufe_aylik_degisim"] = df["tufe_endeks"].pct_change() * 100
    df["tufe_yillik_degisim"] = df["tufe_endeks"].pct_change(12) * 100
    df["yayim_tarihi"] = df["referans_ayi"].map(_yaklasik_yayim_tarihi)

    tam_csv = RAW_DIR / "tufe_2024_bugun_tam_donem.csv"
    tam_xlsx = RAW_DIR / "tufe_2024_bugun_tam_donem.xlsx"
    df.to_csv(tam_csv, index=False, encoding="utf-8-sig")
    df.to_excel(tam_xlsx, index=False, sheet_name="tufe_tam_donem")

    hedef = df[(df["referans_ayi"] >= HEDEF_BASLANGIC_AY) & (df["referans_ayi"] <= HEDEF_BITIS_AY)].copy()
    hedef = hedef[["referans_ayi", "tufe_endeks", "tufe_aylik_degisim", "tufe_yillik_degisim", "yayim_tarihi"]].reset_index(drop=True)

    hedef_csv = RAW_DIR / "tufe_2024_bugun_aylik.csv"
    hedef_xlsx = RAW_DIR / "tufe_2024_bugun_aylik.xlsx"
    hedef.to_csv(hedef_csv, index=False, encoding="utf-8-sig")
    hedef.to_excel(hedef_xlsx, index=False, sheet_name="tufe_aylik")

    beklenen_aylar = pd.period_range(HEDEF_BASLANGIC_AY, HEDEF_BITIS_AY, freq="M").astype(str).tolist()
    gelen_aylar = hedef["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== GENISLETME 1b - TUFE OZET ===")
    print(f"Kapsam (hedef): {HEDEF_BASLANGIC_AY} .. {HEDEF_BITIS_AY}")
    print(f"Gelen ay: {len(gelen_aylar)}/{len(beklenen_aylar)}, eksik: {eksik_aylar if eksik_aylar else 'yok'}")
    print(hedef.to_string(index=False))


if __name__ == "__main__":
    main()
