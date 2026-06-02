import numpy as np
import pandas as pd

ETF_FILE = "etf_prices_returns_2021_2024.csv"
MACRO_FILE = "macro_daily_extended.csv"
VIX_FILE = "vix_daily.csv"
OUT_FILE = "esg_dataset.csv"

FINAL_COLUMNS = [
    "date",
    "ticker",
    "adj_close",
    "return",
    "excess_return",
    "volume",
    "log_volume",
    "t5yie",
    "sofr",
    "dgs10",
    "vix",
    "rf_daily",
    "high_inflation",
]


def main():
    etf = pd.read_csv(ETF_FILE)
    etf.columns = [column.strip() for column in etf.columns]

    if "date" not in etf.columns and "Date" in etf.columns:
        etf = etf.rename(columns={"Date": "date"})

    if "ticker" not in etf.columns and "Ticker" in etf.columns:
        etf = etf.rename(columns={"Ticker": "ticker"})

    volume_columns = [
        column for column in etf.columns
        if column.lower().startswith("volume")
    ]

    etf["volume"] = etf[volume_columns[0]] if volume_columns else np.nan

    required_columns = ["date", "ticker", "adj_close", "return", "volume"]
    missing_columns = [
        column for column in required_columns
        if column not in etf.columns
    ]

    if missing_columns:
        raise RuntimeError(
            f"Missing columns in ETF file: {missing_columns}. "
            f"Available columns: {etf.columns.tolist()}"
        )

    etf = etf[required_columns].copy()

    etf["date"] = pd.to_datetime(etf["date"], errors="coerce")
    etf["ticker"] = etf["ticker"].astype(str).str.upper().str.strip()
    etf["adj_close"] = pd.to_numeric(etf["adj_close"], errors="coerce")
    etf["return"] = pd.to_numeric(etf["return"], errors="coerce")
    etf["volume"] = pd.to_numeric(etf["volume"], errors="coerce")

    etf = etf.dropna(subset=["date", "ticker", "adj_close"])

    macro = pd.read_csv(MACRO_FILE, parse_dates=["date"])
    vix = pd.read_csv(VIX_FILE, parse_dates=["date"])

    macro = macro.merge(vix, on="date", how="left")
    dataset = etf.merge(macro, on="date", how="left")

    dataset["log_volume"] = np.log(dataset["volume"].where(dataset["volume"] > 0))
    dataset["rf_daily"] = (dataset["sofr"] / 100.0) / 252.0
    dataset["excess_return"] = dataset["return"] - dataset["rf_daily"]

    inflation_threshold = dataset["t5yie"].median(skipna=True)
    dataset["high_inflation"] = (
        dataset["t5yie"] > inflation_threshold
    ).astype(int)

    dataset = dataset[FINAL_COLUMNS].sort_values(["ticker", "date"])
    dataset.to_csv(OUT_FILE, index=False)

    print(f"File saved: {OUT_FILE}")
    print(f"Rows: {len(dataset)}")
    print(f"Columns: {len(dataset.columns)}")


if __name__ == "__main__":
    main()