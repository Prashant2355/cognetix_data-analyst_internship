# Social Media Sentiment Analysis using VADER

This project performs **sentiment analysis on social media text data** using **Natural Language Processing (NLP)** techniques and the **VADER sentiment analyzer**.  
The goal is to extract meaningful insights from user-generated content by classifying posts into **Positive, Negative, and Neutral sentiments** and visualizing sentiment trends.

---

##  Objectives

- Clean and preprocess social media text data
- Apply sentiment analysis using the VADER model
- Classify sentiments into Positive, Negative, and Neutral
- Visualize sentiment distribution
- Extract key keywords driving sentiment
- Analyze sentiment trends over time
- Generate a final insight-driven report

---

##  Dataset Overview

- **File:** `sentimentdataset.csv`
- **Key Columns:**
  - `Text` – Social media post content
  - `Timestamp` – Date and time of post
  - `User` – User identifier
  - `Platform` – Social media platform (Twitter, Instagram, Facebook)
  - `Hashtags` – Hashtags used in posts
  - `Likes`, `Retweets` – Engagement metrics
  - `Country`, `Year`, `Month`, `Day`, `Hour`

---

##  Tools & Libraries Used

- **Python**
- **Jupyter Notebook**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **NLTK (VADER)** – sentiment analysis
- **Matplotlib & Seaborn** – visualizations
- **WordCloud** – keyword visualization
- **Regex & String** – text cleaning

---

##  Project Workflow

### ✅ Step 1: Load Dataset
- Imported dataset using Pandas
- Inspected structure and sample records

### ✅ Step 2: Text Cleaning & Preprocessing
Performed the following operations on the `Text` column:
- Converted text to lowercase
- Removed URLs
- Removed emojis
- Removed punctuation
- Removed stopwords

A new column `clean_text` was created for further analysis.

---

### ✅ Step 3: Apply Sentiment Model (VADER)
- Used **VADER SentimentIntensityAnalyzer**
- Generated sentiment scores:
  - `positive`
  - `neutral`
  - `negative`
  - `compound` (overall sentiment score)

---

### ✅ Step 4: Sentiment Classification
- Classified sentiment based on compound score:
  - Positive → score ≥ 0.05
  - Negative → score ≤ -0.05
  - Neutral → otherwise
- Created a new column `sentiment`

---

### ✅ Step 5: Sentiment Distribution Visualization
- Bar chart showing sentiment counts
- Pie chart showing sentiment proportions

---

### ✅ Step 6: WordCloud Generation
- Generated WordCloud using cleaned text
- Highlighted most frequent words across posts

---

### ✅ Step 7: Final Report & Insights
Extracted insights including:
- Percentage of Positive, Negative, and Neutral posts
- Common positive and negative keywords
- Sentiment trends over time using timestamps

---

##  Key Insights

- **~63% of posts are Positive**, indicating an overall favorable sentiment
- **~25.5% Negative sentiment**, highlighting specific pain points
- **~11.5% Neutral posts**, mostly informational
- Positive keywords reflect emotions, lifestyle, fitness, and leisure
- Negative keywords relate to traffic, stress, delays, and dissatisfaction
- Sentiment trends remain largely positive over time with occasional negative spikes
