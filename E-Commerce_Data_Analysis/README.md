# E-Commerce Data Analysis

This project focuses on analyzing an **Online Retail dataset** to understand sales performance, customer demand, geographic revenue distribution, and time-based trends. The analysis aims to generate **actionable business insights** using Python and data visualization techniques.

---

##  Objective :-

The primary goals of this project are to:
- Analyze **revenue performance** across products, countries, and time
- Identify **top-selling products and key markets**
- Study **monthly revenue trends and growth**
- Build a **KPI summary** for executive-level insights

---

## 📂 Dataset Note

The dataset used in this project (`OnlineRetail.csv`) exceeds GitHub’s file size limit (25 MB), so it is not included in the repository.

You can download the dataset from the official source:
- https://www.kaggle.com/datasets/vijayuv/onlineretail

After downloading, place the file in the project directory and run the notebook.

##  Dataset Overview :-

- **Dataset:** Online Retail Dataset
- **Data Type:** Transaction-level sales data
- **Key Columns:**
  - InvoiceNo
  - InvoiceDate
  - Country
  - StockCode
  - Description (Product)
  - Quantity
  - UnitPrice

A new column **Revenue** is derived as:
- Revenue = Quantity × UnitPrice

Invalid and cancelled transactions were removed for accurate analysis.

---

## Tools & Technologies Used  :-

- **Python**
- **Jupyter Notebook**
- **Pandas** – data cleaning and aggregation
- **Matplotlib** – data visualization
- **Git & GitHub** – version control and project sharing

---

##  Key Analyses & Visualizations

### 🔹 Product Analysis
- Top 10 best-selling products by revenue
- Identification of revenue concentration (Pareto effect)

### 🔹 Time-Based Analysis
- Monthly revenue trend
- Month-over-month revenue growth analysis
- Seasonality detection

### 🔹 Geographic Analysis
- Country-wise revenue comparison
- Identification of top revenue-contributing countries

### 🔹 KPI Summary
The following KPIs were calculated:
- **Total Revenue**
- **Total Orders**
- **Top Product by Revenue**
- **Top Country by Revenue**
- **Monthly Revenue Growth Trend**

---

##  Visualizations Included

- Bar charts (Top products, category/country revenue)
- Line charts (Monthly revenue & growth trend)

All visualizations are designed to clearly communicate insights to both technical and non-technical stakeholders.

---

##  Key Insights

- Revenue is **highly concentrated among a small number of products**, indicating a strong Pareto effect.
- The **UK is the primary revenue driver**, contributing the majority of total sales.
- Monthly revenue shows **clear seasonality**, with peaks during year-end months.
- Business performance is strongly influenced by **product availability during peak periods**.
- Geographic diversification can help reduce dependency on a single market.

---


