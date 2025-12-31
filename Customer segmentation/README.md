#  Customer Segmentation using K-Means Clustering

This project focuses on **customer segmentation** using **unsupervised machine learning (K-Means clustering)**.  
The objective is to group customers based on their behavioral and demographic features to enable **data-driven marketing and business decisions**.

---

## Objectives

- Prepare and preprocess customer data for clustering
- Standardize numerical features
- Determine the optimal number of clusters
- Apply K-Means clustering
- Visualize and interpret customer segments
- Generate actionable business insights from clusters

---

##  Dataset Overview

The dataset contains customer-related attributes such as:

- Demographic features (e.g., age, income)
- Purchase behavior (e.g., spending patterns)
- Engagement and transaction-related metrics

> The dataset was cleaned and transformed before clustering to ensure reliable results.

---

##  Tools & Libraries Used

- **Python**
- **Jupyter Notebook**
- **Pandas** – data manipulation and preprocessing
- **NumPy** – numerical computations
- **Scikit-learn** – scaling and K-Means clustering
- **Matplotlib / Seaborn** – data visualization

---

##  Project Workflow

### ✅ Step 1: Data Loading & Exploration
- Loaded customer dataset using Pandas
- Reviewed data structure, column types, and summary statistics

### ✅ Step 2: Data Preprocessing
- Selected relevant numerical features for clustering
- Handled missing values (if any)
- Applied **StandardScaler** to normalize data and remove scale bias

### ✅ Step 3: Optimal Cluster Selection
- Used the **Elbow Method** to identify the optimal number of clusters (k)
- Analyzed Within-Cluster Sum of Squares (WCSS) to detect diminishing returns

### ✅ Step 4: K-Means Clustering
- Applied K-Means algorithm using the optimal k value
- Assigned cluster labels to each customer

### ✅ Step 5: Cluster Visualization
- Visualized clusters using scatter plots
- Compared customer behavior across different clusters

### ✅ Step 6: Cluster Interpretation
- Analyzed each cluster’s characteristics
- Identified high-value, medium-value, and low-engagement customer segments

---

##  Visualizations Included

- Elbow curve to determine optimal k
- Cluster distribution plots
- Feature-wise comparison across clusters

---

##  Key Insights

- Customers can be clearly grouped based on spending and engagement patterns
- High-value customers show distinct purchasing behavior
- Certain clusters represent low-engagement or price-sensitive customers
- Segmentation enables targeted marketing and personalized strategies

---
