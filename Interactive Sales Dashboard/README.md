# Superstore Sales Dashboard (Plotly Dash)

This project is an **interactive sales analytics dashboard** built using **Python and Plotly Dash**.  
It analyzes the **US Superstore dataset** to provide actionable business insights through KPIs, interactive charts, and slicer-based filtering — similar to Power BI, but fully implemented in Python.

---

## Overview

The goal of this project is to:
- Analyze retail sales performance
- Build business KPIs
- Create interactive visualizations
- Develop a web-based dashboard using **Plotly Dash**

The dashboard allows users to dynamically explore sales data across **time, region, category, and customer segments**.

---


##  Tech Stack

- **Python**
- **Pandas** – data cleaning & aggregation
- **Plotly** – interactive charts
- **Dash** – web application framework
- **OpenPyXL** – Excel file handling
- **VS Code** – development environment

---

##  Key Features

### ✅ KPI Cards
- Total Sales
- Total Profit
- Total Orders
- Average Delivery Days

### ✅ Interactive Visuals
- Sales Over Time (Line Chart)
- Category-wise Sales (Bar Chart)
- Profit by Region (Bar Chart)
- Customer Segment Performance
- Top Products Analysis

### ✅ Filters & Slicers
- Region filter
- Category slicer
- Segment slicer
- Date range selector

All visuals and KPIs update dynamically based on selected filters.

---

##  Dashboard Layout

- **Top Section:** KPI summary cards  
- **Left Panel:** Filters (Region, Category, Segment, Date Range)  
- **Main Area:** Interactive charts arranged in a grid layout  

This layout closely resembles professional BI dashboards.

---

##  Data Preparation Steps

- Converted `Order Date` and `Ship Date` to datetime format
- Engineered a new feature: **Delivery Days**
- Aggregated data for monthly, category-wise, region-wise, and segment-wise analysis
- Handled empty filter selections gracefully to avoid blank dashboards

---
