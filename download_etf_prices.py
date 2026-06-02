import pandas as pd
import yfinance as yf

TICKERS = [
    "ESGU", "ESGV", "SUSA", "EFIV", "USSG", "SUSL",
    "ESGD", "ESGE", "VSGX", "EFAX",
    "ICLN", "QCLN", "PBW", "TAN", "ACES", "PZD",
    "KRMA", "CNRG", "GRID", "SMOG", "LIT", "DRIV",
    "SHE", "DSI", "NULG", "NULV",
]

START = "2021-01-01"
END = "2024-12-31"
OUT_FILE = "etf_prices_returns_2021_2024.csv"


def main():
    all_data = []

    for ticker in TICKERS:
        print(f"Downloading {ticker}...")

        data = yf.download(
            ticker,
            start=START,
            end=END,
            auto_adjust=True,
            progress=False,
        )

        if data.empty:
            print(f"No data for {ticker}")
            continue

        data = data.reset_index()
        data["adj_close"] = data["Close"]
        data["ticker"] = ticker
        data["return"] = data["adj_close"].pct_change()

        data = data[["Date", "ticker", "adj_close", "return", "Volume"]]
        data = data.rename(
            columns={
                "Date": "date",
                "Volume": "volume",
            }
        )

        all_data.append(data)

    if not all_data:
        raise RuntimeError("No ETF data were downloaded.")

    panel = pd.concat(all_data, ignore_index=True)
    panel.to_csv(OUT_FILE, index=False)

    print(f"File saved: {OUT_FILE}")
    print(f"Rows: {len(panel)}")
    print(f"Columns: {len(panel.columns)}")


if __name__ == "__main__":
    main()