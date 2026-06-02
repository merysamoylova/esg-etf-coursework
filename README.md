# ESG ETF Dataset Collection

This repository contains the code and dataset for the data collection stage of the course paper:

**Analysis of Factors Influencing Financial Indicators**

The purpose of this repository is to show how the initial dataset was collected and merged.

## Dataset

The main dataset is:

`esg_dataset.csv`

It contains the initial merged panel dataset before additional cleaning in Google Colab.

The dataset has:

- 26,104 observations
- 13 variables
- 26 ESG-related ETF tickers
- daily data for 2021-2024

Each row represents one ETF on one trading day together with macroeconomic indicators observed on the same date.

## Data sources

The dataset was constructed from three main sources:

1. ETF price data were collected from Yahoo Finance using `yfinance`.
2. VIX data were collected from Yahoo Finance using `yfinance`.
3. Macroeconomic variables were collected from FRED using the FRED API.

The FRED variables used in the dataset are:

1. `T5YIE` - 5-Year Breakeven Inflation Rate
2. `SOFR` - Secured Overnight Financing Rate
3. `DGS10` - 10-Year Treasury Constant Maturity Rate

## Files in this repository

### Data files

1. `etf_prices_returns_2021_2024.csv` - ETF prices, daily returns, and volume data.
2. `macro_daily_extended.csv` - macroeconomic variables from FRED.
3. `vix_daily.csv` - daily VIX data.
4. `esg_dataset.csv` - final raw merged dataset used as the input for further cleaning and analysis.

### Python scripts

1. `download_etf_prices.py` downloads ETF price data and calculates daily returns.
2. `download_macro_extended.py` downloads macroeconomic variables from FRED.
3. `download_vix_daily.py` downloads daily VIX data.
4. `merge_final_dataset.py` merges all data sources into the final raw dataset.

## How the dataset is created

The dataset is created in four steps:

1. Download ETF prices and calculate daily returns.
2. Download macroeconomic variables from FRED.
3. Download daily VIX data.
4. Merge all datasets by date and create additional variables such as excess return and the high-inflation dummy.

To reproduce the dataset, run in Terminal:

```bash
python3 download_etf_prices.py
python3 download_macro_extended.py
python3 download_vix_daily.py
python3 merge_final_dataset.py
```

The final output file is: `esg_dataset.csv`

A FRED API key is required only if the user wants to re-download the macroeconomic variables using `download_macro_extended.py`. The API key is not included in this repository for security reasons.

Before running the FRED download script, set the key locally:

```bash
export FRED_API_KEY="your_api_key_here"
```

However, the final dataset `esg_dataset.csv` is already included in the repository, so the API key is not needed just to view or use the dataset.

## Colab notebook

To run the notebook, place ESG_ETF_coursework.ipynb and esg_dataset.csv in the same folder, install the required packages from requirements.txt, and run the notebook cells sequentially.

## Required packages

The required Python packages are listed in `requirements.txt`. They can be installed with:

```bash
pip install -r requirements.txt
```
