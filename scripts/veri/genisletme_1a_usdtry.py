"""
GENIŞLETME AŞAMA 1a — USD/TRY kur verisi, 2024-01 -> bugün (kaynak seviyesi A).

MVP (yalnızca 2025) scriptinden (scripts/veri/asama1_usdtry.py) FARKLI ÇIKTI
DOSYALARINA yazar - MVP ciktilarinin uzerine YAZMAZ, o prototip asamasi ayri
kaydedilmis olarak kalir.

Kullanim: EVDS_API_KEY ortam degiskeni / .env (Asama 1 ile ayni).
"""
import os
import sys
import json
from datetime import date
from pathlib import Path

import requests
import pandas as pd

BASLANGIC_AY = "2024-01"
BITIS_AY = date.today().strftime("%Y-%m")

EVDS_BASE_URL = "https://evds3.tcmb.gov.tr/igmevdsms-dis/"
SERIES = ["TP.DK.USD.A", "TP.DK.USD.S"]

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "usdtry"
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
    bugun = date.today()
    if e_yil == bugun.year and e_ay == bugun.month:
        end_date = bugun.strftime("%d-%m-%Y")
    else:
        ay_sonu_gun = pd.Period(f"{e_yil:04d}-{e_ay:02d}", freq="M").days_in_month
        end_date = f"{ay_sonu_gun:02d}-{e_ay:02d}-{e_yil:04d}"
    start_date = f"01-{b_ay:02d}-{b_yil:04d}"
    return start_date, end_date


def evds_gunluk_seri_cek(api_key: str, seriler: list[str], baslangic_ay: str, bitis_ay: str):
    start_date, end_date = _ay_baslangic_bitis_tarihleri(baslangic_ay, bitis_ay)
    params = {
        "series": "-".join(seriler),
        "startDate": start_date,
        "endDate": end_date,
        "type": "json",
    }
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

    payload = evds_gunluk_seri_cek(api_key, SERIES, BASLANGIC_AY, BITIS_AY)
    if payload is None:
        print("[UYARI] Veri cekilemedi.")
        sys.exit(1)

    ham_path = RAW_DIR / "usdtry_2024_bugun_raw.json"
    with open(ham_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(payload["items"])
    df = df.rename(columns={"Tarih": "tarih", "TP_DK_USD_A": "usdtry_alis", "TP_DK_USD_S": "usdtry_satis"})
    df = df.drop(columns=["UNIXTIME"], errors="ignore")
    df["tarih"] = pd.to_datetime(df["tarih"], format="%d-%m-%Y")
    df["usdtry_alis"] = pd.to_numeric(df["usdtry_alis"], errors="coerce")
    df["usdtry_satis"] = pd.to_numeric(df["usdtry_satis"], errors="coerce")
    df["usdtry_orta"] = (df["usdtry_alis"] + df["usdtry_satis"]) / 2
    df = df.sort_values("tarih").reset_index(drop=True)
    df["referans_ayi"] = df["tarih"].dt.to_period("M").astype(str)

    gunluk_dolu = df.dropna(subset=["usdtry_alis", "usdtry_satis"])

    gunluk_csv = RAW_DIR / "usdtry_2024_bugun_gunluk.csv"
    gunluk_xlsx = RAW_DIR / "usdtry_2024_bugun_gunluk.xlsx"
    df.to_csv(gunluk_csv, index=False, encoding="utf-8-sig")
    df.to_excel(gunluk_xlsx, index=False, sheet_name="usdtry_gunluk")

    aylik_ortalama = gunluk_dolu.groupby("referans_ayi")[["usdtry_alis", "usdtry_satis", "usdtry_orta"]].mean()
    aylik_ortalama = aylik_ortalama.rename(columns={
        "usdtry_alis": "usdtry_ortalama_alis", "usdtry_satis": "usdtry_ortalama_satis", "usdtry_orta": "usdtry_ortalama",
    })
    aylik_sonu = gunluk_dolu.sort_values("tarih").groupby("referans_ayi").last()[["usdtry_alis", "usdtry_satis", "usdtry_orta"]]
    aylik_sonu = aylik_sonu.rename(columns={
        "usdtry_alis": "usdtry_aysonu_alis", "usdtry_satis": "usdtry_aysonu_satis", "usdtry_orta": "usdtry_aysonu",
    })
    aylik_birlesik = aylik_sonu.join(aylik_ortalama, how="outer").reset_index().sort_values("referans_ayi").reset_index(drop=True)

    aylik_csv = RAW_DIR / "usdtry_2024_bugun_aylik.csv"
    aylik_xlsx = RAW_DIR / "usdtry_2024_bugun_aylik.xlsx"
    aylik_birlesik.to_csv(aylik_csv, index=False, encoding="utf-8-sig")
    aylik_birlesik.to_excel(aylik_xlsx, index=False, sheet_name="usdtry_aylik")

    beklenen_aylar = pd.period_range(BASLANGIC_AY, BITIS_AY, freq="M").astype(str).tolist()
    gelen_aylar = aylik_birlesik["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== GENISLETME 1a - USD/TRY OZET ===")
    print(f"Kapsam: {BASLANGIC_AY} .. {BITIS_AY}")
    print(f"Gunluk gozlem: {len(df)}, aylik satir: {len(gelen_aylar)}/{len(beklenen_aylar)}")
    print(f"Eksik aylar: {eksik_aylar if eksik_aylar else 'yok'}")
    print(aylik_birlesik.to_string(index=False))


if __name__ == "__main__":
    main()
