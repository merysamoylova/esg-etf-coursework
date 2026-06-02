import os

import pandas as pd
import requests

FRED_API_KEY = os.getenv("FRED_API_KEY")

if not FRED_API_KEY:
    raise RuntimeError(
        "FRED_API_KEY is not set. Please set it locally before running this script."
    )

START = "2021-01-01"
END = "2024-12-31"

SERIES = {
    "T5YIE": "t5yie",
    "SOFR": "sofr",
    "DGS10": "dgs10",
}

OUT_FILE = "macro_daily_extended.csv"


def fetch_series(series_id: str, column_name: str) -> pd.DataFrame:
    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": START,
        "observation_end": END,
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()

    observations = response.json()["observations"]

    data = pd.DataFrame(observations)[["date", "value"]]
    data["date"] = pd.to_datetime(data["date"])
    data["value"] = pd.to_numeric(
        data["value"].replace(".", pd.NA),
        errors="coerce",
    )

    return data.rename(columns={"value": column_name})


def main():
    dataframes = []

    for series_id, column_name in SERIES.items():
        print(f"Downloading {series_id}...")
        dataframes.append(fetch_series(series_id, column_name))

    macro = dataframes[0]

    for data in dataframes[1:]:
        macro = macro.merge(data, on="date", how="outer")

    macro = macro.sort_values("date")
    macro.to_csv(OUT_FILE, index=False)

    print(f"File saved: {OUT_FILE}")
    print(f"Rows: {len(macro)}")
    print(f"Columns: {len(macro.columns)}")


if __name__ == "__main__":
    main()