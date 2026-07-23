"""
AŞAMA 1 — USD/TRY kur verisi (kaynak seviyesi A: TCMB EVDS3 API).

Kullanim:
    EVDS_API_KEY ortam degiskenini ayarlayip calistir:
        (PowerShell) $env:EVDS_API_KEY = "..."; python scripts/veri/asama1_usdtry.py
        (bash)       EVDS_API_KEY=... python scripts/veri/asama1_usdtry.py
    Repo kokunde .env dosyasi varsa (EVDS_API_KEY=...) otomatik okunur.

API anahtari KODA GOMULMEZ; yalnizca ortam degiskeninden / .env'den okunur.

Not (kaynak kesfi): Eski "evds2.tcmb.gov.tr/service/evds" REST yolu artik
calismiyor (SPA fallback donuyor) - TCMB, EVDS3'e gectiginde API'yi
"https://evds3.tcmb.gov.tr/igmevdsms-dis/" tabanina tasidi ve anahtar artik
"key" HTTP header'i ile gonderiliyor (URL parametresi degil).

Veri GUNLUK cekilir (EVDS'in kendi aylik agregasyonu KULLANILMAZ) - boylece
ham veri butun gozlemleriyle saklanir ve gorsel/elle kontrol edilebilir.
Aylik ara tablo (ay sonu + ay ortalamasi) bu gunluk veriden yerel olarak
(pandas ile) turetilir.
"""
import os
import sys
import json
from pathlib import Path

import requests
import pandas as pd

BASLANGIC_AY = "2025-01"
BITIS_AY = "2025-12"

EVDS_BASE_URL = "https://evds3.tcmb.gov.tr/igmevdsms-dis/"
SERIES = ["TP.DK.USD.A", "TP.DK.USD.S"]  # ABD Dolari alis / satis (TCMB)

REPO_KOKU = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_KOKU / "data" / "raw" / "usdtry"
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


def evds_gunluk_seri_cek(api_key: str, seriler: list[str], baslangic_ay: str, bitis_ay: str):
    """Tek kaynak fonksiyonu: EVDS3'ten GUNLUK frekansta ham seri ceker.

    Basarisiz olursa None doner (cagiran taraf raporlar, program durmaz).
    """
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

    payload = evds_gunluk_seri_cek(api_key, SERIES, BASLANGIC_AY, BITIS_AY)
    if payload is None:
        print("[UYARI] Veri cekilemedi.")
        sys.exit(1)

    # Ham API yanitini oldugu gibi kaydet (kaynak izlenebilirligi icin).
    ham_path = RAW_DIR / "usdtry_2025_raw.json"
    with open(ham_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(payload["items"])
    df = df.rename(columns={
        "Tarih": "tarih",
        "TP_DK_USD_A": "usdtry_alis",
        "TP_DK_USD_S": "usdtry_satis",
    })
    df = df.drop(columns=["UNIXTIME"], errors="ignore")
    df["tarih"] = pd.to_datetime(df["tarih"], format="%d-%m-%Y")
    df["usdtry_alis"] = pd.to_numeric(df["usdtry_alis"], errors="coerce")
    df["usdtry_satis"] = pd.to_numeric(df["usdtry_satis"], errors="coerce")
    df["usdtry_orta"] = (df["usdtry_alis"] + df["usdtry_satis"]) / 2
    df = df.sort_values("tarih").reset_index(drop=True)

    gunluk_dolu = df.dropna(subset=["usdtry_alis", "usdtry_satis"])
    tatil_gun_sayisi = len(df) - len(gunluk_dolu)

    # Gunluk (ham) tabloyu CSV + Excel olarak kaydet.
    gunluk_csv = RAW_DIR / "usdtry_2025_gunluk.csv"
    gunluk_xlsx = RAW_DIR / "usdtry_2025_gunluk.xlsx"
    df.to_csv(gunluk_csv, index=False, encoding="utf-8-sig")
    df.to_excel(gunluk_xlsx, index=False, sheet_name="usdtry_gunluk")

    # Aylik ara tablo: gunluk veriden yerelde turetilir (EVDS agregasyonu KULLANILMADI).
    df["referans_ayi"] = df["tarih"].dt.to_period("M").astype(str)
    aylik_ortalama = gunluk_dolu.copy()
    aylik_ortalama["referans_ayi"] = aylik_ortalama["tarih"].dt.to_period("M").astype(str)
    aylik_ortalama = aylik_ortalama.groupby("referans_ayi")[["usdtry_alis", "usdtry_satis", "usdtry_orta"]].mean()
    aylik_ortalama = aylik_ortalama.rename(columns={
        "usdtry_alis": "usdtry_ortalama_alis",
        "usdtry_satis": "usdtry_ortalama_satis",
        "usdtry_orta": "usdtry_ortalama",
    })

    aylik_sonu = gunluk_dolu.copy()
    aylik_sonu["referans_ayi"] = aylik_sonu["tarih"].dt.to_period("M").astype(str)
    aylik_sonu = aylik_sonu.sort_values("tarih").groupby("referans_ayi").last()[["usdtry_alis", "usdtry_satis", "usdtry_orta"]]
    aylik_sonu = aylik_sonu.rename(columns={
        "usdtry_alis": "usdtry_aysonu_alis",
        "usdtry_satis": "usdtry_aysonu_satis",
        "usdtry_orta": "usdtry_aysonu",
    })

    aylik_birlesik = aylik_sonu.join(aylik_ortalama, how="outer").reset_index()
    aylik_birlesik = aylik_birlesik.sort_values("referans_ayi").reset_index(drop=True)

    aylik_csv = RAW_DIR / "usdtry_2025_aylik.csv"
    aylik_xlsx = RAW_DIR / "usdtry_2025_aylik.xlsx"
    aylik_birlesik.to_csv(aylik_csv, index=False, encoding="utf-8-sig")
    aylik_birlesik.to_excel(aylik_xlsx, index=False, sheet_name="usdtry_aylik")

    beklenen_aylar = pd.period_range(BASLANGIC_AY, BITIS_AY, freq="M").astype(str).tolist()
    gelen_aylar = aylik_birlesik["referans_ayi"].tolist()
    eksik_aylar = [ay for ay in beklenen_aylar if ay not in gelen_aylar]

    print("=== ASAMA 1 - USD/TRY OZET ===")
    print("Kaynak seviyesi: A (TCMB EVDS3 API, https://evds3.tcmb.gov.tr/igmevdsms-dis/)")
    print(f"Kapsam: {BASLANGIC_AY} .. {BITIS_AY}")
    print(f"Gunluk gozlem sayisi: {len(df)} (bunlardan {tatil_gun_sayisi} tanesi hafta sonu/resmi tatil - deger yok)")
    print(f"Aylik ara tabloda gelen ay sayisi: {len(gelen_aylar)} / {len(beklenen_aylar)}")
    print(f"Eksik aylar: {eksik_aylar if eksik_aylar else 'yok'}")
    print()
    print(f"Ham (gunluk, API yaniti): {ham_path}")
    print(f"Gunluk tablo: {gunluk_csv} , {gunluk_xlsx}")
    print(f"Aylik ara tablo: {aylik_csv} , {aylik_xlsx}")
    print()
    print("--- Gunluk veri (ilk 5 ve son 5 satir) ---")
    print(pd.concat([df.head(5), df.tail(5)]).to_string(index=False))
    print()
    print("--- Aylik ara tablo (tamamı) ---")
    print(aylik_birlesik.to_string(index=False))


if __name__ == "__main__":
    main()
