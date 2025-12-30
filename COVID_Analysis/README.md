#  COVID-19 Data Analysis & Country Comparison

This project focuses on **exploratory data analysis (EDA)** and **time-series analysis** of COVID-19 data using Python.  
The goal is to understand the **spread of COVID-19 over time**, analyze **country-wise trends**, apply **rolling averages**, and compare the progression across major countries.


---

##  Objectives

- Clean and standardize country names
- Perform country-level filtering
- Analyze daily COVID-19 case trends
- Apply rolling averages to smooth time-series data
- Compare COVID-19 trends across countries (India, USA, China)
- Visualize insights using Matplotlib and Seaborn

---

## Tools & Libraries Used

- **Python**
- **Jupyter Notebook**
- **Pandas** – data cleaning & manipulation
- **Matplotlib** – line charts & trend visualization
- **Seaborn** – enhanced statistical visualizations

---

##  Project Workflow

### ✅ Step 1: Data Loading
- Loaded COVID-19 dataset using Pandas
- Inspected data structure, columns, and basic statistics
- 
### ✅ Step 2: Data Cleaning
- Converted the `Date` column to **datetime format** for time-series analysis
- Checked and **handled missing values** to ensure data consistency
- **Standardized country names** to resolve inconsistencies (e.g., US → United States, Mainland China → China, Korea, South → South Korea)

### ✅ Step 3: Country-wise Filtering
- Filtered data specifically for **India**
- Sorted records by date for time-series accuracy

### ✅ Step 4: Daily Trend Visualization
- Plotted daily:
  - Confirmed cases
  - Deaths
  - Recovered cases
- Used line charts to analyze COVID-19 progression over time

### ✅ Step 5: Rolling Average
- Applied **7-day rolling average** on confirmed cases
- Smoothed daily fluctuations to highlight underlying trends

### ✅ Step 6: Country Comparison
- Compared COVID-19 confirmed cases across:
  - India
  - United States
  - China
- Visualized differences in outbreak patterns and growth trends

---

## Visualizations Included

- Daily confirmed cases trend
- Death and recovery trends
- 7-day rolling average plot
- Multi-country comparison line charts

---

## Key Insights

- Daily COVID-19 data is highly volatile; rolling averages provide clearer trends
- India shows a steady long-term rise in confirmed cases
- The USA records the highest overall confirmed cases
- China’s case curve stabilizes early, indicating early containment
- Comparative analysis highlights different outbreak patterns across countries

---
