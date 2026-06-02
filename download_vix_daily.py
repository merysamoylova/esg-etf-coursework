import pandas as pd
import yfinance as yf

START = "2021-01-01"
END = "2024-12-31"
OUT_FILE = "vix_daily.csv"


def main():
    data = yf.download(
        "^VIX",
        start=START,
        end=END,
        progress=False,
    )

    if data.empty:
        raise RuntimeError("No VIX data were downloaded")

    data = data.reset_index()
    data = data[["Date", "Close"]].rename(
        columns={
            "Date": "date",
            "Close": "vix",
        }
    )

    data["date"] = pd.to_datetime(data["date"])
    data.to_csv(OUT_FILE, index=False)

    print(f"File saved: {OUT_FILE}")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")


if __name__ == "__main__":
    main()