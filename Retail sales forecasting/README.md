# Retail Sales Time Series Analysis & Forecasting

This project focuses on **time series analysis and forecasting of retail sales data** using Python. The objective is to analyze **trend, seasonality, and patterns** in historical sales data and build a forecasting model to predict future sales.

---

##  Project Objectives :-

- Convert raw sales data into a **time series format**
- Perform **monthly resampling** of weekly sales
- Analyze **trend and seasonality**
- Apply **rolling statistics** for smoothing
- Decompose the time series into trend, seasonality, and residuals
- Build an **ARIMA model** for sales forecasting

---

##  Dataset Overview

The dataset contains retail sales data with the following key fields:

- `Date`
- `Weekly_Sales`
- `Store`
- `Department`

To support time series analysis:
- The `Date` column was converted to datetime
- Weekly sales were aggregated to **monthly sales**

---

##  Tools & Libraries Used

- **Python**
- **Jupyter Notebook**
- **Pandas** – data preprocessing and resampling
- **Matplotlib** – time series visualization
- **Statsmodels** – decomposition, stationarity testing, ARIMA modeling
- **NumPy** – numerical operations
- **Git & GitHub** – version control

---

##  Analysis Performed

### 🔹 Data Preparation
- Converted date column to datetime format
- Set date as index
- Resampled weekly sales data to monthly frequency

### 🔹 Trend & Seasonality Analysis
- Line plot of monthly sales
- Rolling mean to smooth short-term fluctuations
- Time series decomposition to separate:
  - Trend
  - Seasonality
  - Residuals

### 🔹 Stationarity Check
- Performed **ADF (Augmented Dickey-Fuller) test**
- Applied differencing to make the series stationary

### 🔹 Forecasting Model
- Built an **ARIMA model**
- Forecasted future monthly sales
- Visualized actual vs forecasted values

---

##  Visualizations Included

- Monthly sales line plot
- Rolling mean trend plot
- Decomposed time series components
- Forecast vs actual sales plot

---

##  Key Insights

- Retail sales show a **clear long-term trend**, indicating business growth or decline over time.
- Strong **seasonality patterns** are present, common in retail datasets.
- Rolling mean helps highlight the underlying trend by reducing noise.
- ARIMA effectively captures short-term dependencies in sales data.
- The forecast provides a reasonable estimate for **future demand planning**.

---
