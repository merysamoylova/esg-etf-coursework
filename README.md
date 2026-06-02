# ESG ETF Dataset Collection

This repository contains the code and dataset for the data collection stage of the course paper:

**Analysis of Factors Influencing Financial Indicators**

The purpose of this repository is to show how the initial dataset was collected and merged.

## Dataset

The repository includes two dataset files:

1. `esg_dataset.csv` - the initial raw merged panel dataset created by merging ETF price data, VIX data, and macroeconomic variables. This dataset is used as the input file for the Colab notebook.

2. `esg_dataset_cleaned.csv` - the cleaned dataset produced in the Colab notebook after removing columns with excessive missing values and dropping observations with missing values in the main variables. This dataset is used for descriptive statistics, correlation analysis, regression analysis, hypothesis testing, figures, and machine learning models.

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

1. `esg_dataset.csv` - raw merged panel dataset before additional cleaning in the notebook.
2. `esg_dataset_cleaned.csv` - cleaned dataset used for the empirical analysis in the notebook.

Intermediate CSV files, such as ETF-only price data, macroeconomic data, and VIX data, are not included in the repository because they can be reproduced by running the data collection scripts.

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

The notebook `ESG_ETF_coursework.ipynb` uses `esg_dataset.csv` as the input file. It performs the cleaning procedure, saves the cleaned dataset as `esg_dataset_cleaned.csv`, and then uses the cleaned data for the empirical analysis.

To run the notebook, place `ESG_ETF_coursework.ipynb` and `esg_dataset.csv` in the same folder, install the required packages from `requirements.txt`, and run the notebook cells sequentially.

## Required packages

The required Python packages are listed in `requirements.txt`. They can be installed with:

```bash
pip install -r requirements.txt
```
