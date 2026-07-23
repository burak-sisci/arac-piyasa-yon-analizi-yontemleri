"""
GENIŞLETME AŞAMA 3c/3d — Taşıt kredisi faizi + politika faizi, 2024-01 -> bugün
(kaynak seviyesi A, TCMB EVDS3).

Seriler:
- TP.KTF12: Taşıt kredisi ağırlıklı ortalama faiz oranı (HAFTALIK yayımlanır).
- TP.APIFON4: TCMB politika faizi / fonlama faizi (GÜNLÜK yayımlanır).
Ikisi de yerelde aylik ortalamaya indirgenir (kaynagin kendi agregasyonu
KULLANILMAZ, Asama 1 ilkesiyle tutarli).

NOT (denendi, basarisiz - PM'e birakildi): Tuketici guven endeksi (TP.TUKGUVEN
ve 6 farkli alternatif kod) EVDS'te bulunamadi (hepsi HTTP 400). Bu script
onu icermez; 3d'nin yalnizca "politika faizi" yarisini kapsar.
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
SERIES = {
    "tasit_kredisi_faiz": "TP.KTF12",
    "politika_faizi": "TP.APIFON4",
}

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "faiz"
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


def evds_seri_cek(api_key: str, seri: str, baslangic_ay: str, bitis_ay: str):
    start_date, end_date = _ay_baslangic_bitis_tarihleri(baslangic_ay, bitis_ay)
    params = {"series": seri, "startDate": start_date, "endDate": end_date, "type": "json"}
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = EVDS_BASE_URL + query
    try:
        resp = requests.get(url, headers={"key": api_key}, timeout=60)
    except requests.RequestException as exc:
        print(f"[HATA] {seri}: {exc}", file=sys.stderr)
        return None
    if resp.status_code != 200:
        print(f"[HATA] {seri} HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        return None
    try:
        payload = resp.json()
    except ValueError:
        print(f"[HATA] {seri} JSON degil: {resp.text[:200]}", file=sys.stderr)
        return None
    if "items" not in payload:
        print(f"[HATA] {seri} 'items' yok: {payload}", file=sys.stderr)
        return None
    return payload


def main():
    _env_dosyasini_yukle()
    api_key = os.environ.get("EVDS_API_KEY")
    if not api_key:
        print("[HATA] EVDS_API_KEY bulunamadi.", file=sys.stderr)
        sys.exit(1)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    aylik_seriler = {}

    for ad, kod in SERIES.items():
        payload = evds_seri_cek(api_key, kod, BASLANGIC_AY, BITIS_AY)
        if payload is None:
            print(f"[UYARI] {ad} ({kod}) cekilemedi, atlaniyor.")
            continue

        ham_path = RAW_DIR / f"{ad}_2024_bugun_raw.json"
        with open(ham_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        df = pd.DataFrame(payload["items"])
        deger_kolon = kod.replace(".", "_")
        df = df.rename(columns={deger_kolon: "deger"})
        df["deger"] = pd.to_numeric(df["deger"], errors="coerce")
        df["tarih_parsed"] = pd.to_datetime(df["Tarih"], format="%d-%m-%Y", errors="coerce")
        df = df.dropna(subset=["tarih_parsed"])
        df["referans_ayi"] = df["tarih_parsed"].dt.to_period("M").astype(str)
        aylik = df.dropna(subset=["deger"]).groupby("referans_ayi")["deger"].mean().reset_index()
        aylik = aylik.rename(columns={"deger": ad})
        aylik_seriler[ad] = aylik

        gunluk_csv = RAW_DIR / f"{ad}_2024_bugun_ham.csv"
        df.to_csv(gunluk_csv, index=False, encoding="utf-8-sig")
        print(f"[OK] {ad} ({kod}): {len(df)} gozlem, {len(aylik)} aylik satir")

    if not aylik_seriler:
        print("[HATA] Hicbir seri cekilemedi.")
        sys.exit(1)

    birlesik = None
    for ad, aylik in aylik_seriler.items():
        birlesik = aylik if birlesik is None else birlesik.merge(aylik, on="referans_ayi", how="outer")
    birlesik = birlesik.sort_values("referans_ayi").reset_index(drop=True)

    hedef_csv = RAW_DIR / "faizler_2024_bugun_aylik.csv"
    hedef_xlsx = RAW_DIR / "faizler_2024_bugun_aylik.xlsx"
    birlesik.to_csv(hedef_csv, index=False, encoding="utf-8-sig")
    birlesik.to_excel(hedef_xlsx, index=False, sheet_name="faizler_aylik")

    print()
    print("=== GENISLETME 3c/3d - FAIZ SERILERI OZET ===")
    print(f"Kapsam: {BASLANGIC_AY} .. {BITIS_AY}")
    print("NOT: Tuketici guven endeksi (3d'nin ikinci yarisi) EVDS'te bulunamadi - HATA, PM'e birakildi.")
    print(birlesik.to_string(index=False))
    print(f"\nCikti: {hedef_csv} , {hedef_xlsx}")


if __name__ == "__main__":
    main()
