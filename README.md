# 🏪 E-Commerce Revenue Drivers: Exploratory Analysis 

## 🎯 Objective
To explore what drives revenue success in an e-commerce business using synthetic transactional data. An analysis was focused on the following criteria: **pricing structure, discount strategies, comparing category performance, diving into the highest performers**, and **monthly sales trends**. The goal was to simulate how a business analyst would identify patterns and make forward-looking predictions.

---

## 📦 Dataset Overview
- **Source**: Synthetic dataset of **3,660 transactions**
- **Contains**: Transaction dates, product categories, prices, discounts, revenue per order
- **Tools Used**:
  - **Excel** – for data cleaning, pivot-based analysis, and charting
  - **Tableau** – to recreate visuals and experiment with dashboards
  - **Python** – for loading data into SQLite and preparing for scalable querying
  - **Markdown** – to reflect on findings and document insights

---

## 🔍 Key Analyses & Insights

### 🧼 Data Preparation
- Converted .csv to an .xlsx for file type and format compatibility with Excel.
- Cleaned inconsistent date formatting and structured key columns
- Created helper columns for **price tiers** and **discount ranges** to enable grouped analysis

---

### 📊 Revenue by Product Category
- **Clothing** was the highest revenue-generating category
- Slightly higher sales volume and average price, and similar average discount than the lowest performer in Electronics
- No single product dominated sales - all 531 items sold were unique
- ✅ *Insight*: High-performance is due to the high volume and mid-tier prices, not extreme discounts

---

### 📆 Monthly Revenue Trends
- **April** was the highest revenue month for clothing: ₹15,877
- Average month: ₹10,665 → April was ~49% higher
- April had more transactions and higher-than-average price points
- ✅ *Insight*: Quantity sold × price per item drives revenue. This further supports the claim that discounts ≠ guaranteed results

---

### 💸 Discount Impact Analysis
- Grouped transactions by discount brackets (e.g., 0–10%, 11–20%)
- Lower discounts (especially 0–10%) yielded the highest **transaction count** and **revenue**
- High discounts (30%+) brought more units per sale but lower overall revenue
- ✅ *Insight*: Discounts need strategic targeting - not all discounts help revenue

---

### 🪙 Price Tier Performance
- Grouped prices into ₹100 brackets
- Most purchases were in the ₹100–₹200 range, followed by ₹200–₹300
- Sales dropped rapidly above ₹400
- ✅ *Insight*: Mid-tier pricing (₹100–₹300) appeals most to buyers. Very high prices deter volume

---

### 📈 Forecasting Revenue (Excel)
- Time series forecast built using Jan–Oct 2024 monthly revenue
- November excluded due to partial data
- Model predicts revenue to **stabilize around ₹72,000/month**
- ✅ *Insight*: Revenue follows a stable trend with occasional dips and recoveries

---

## 📘 What I Learned
- The importance of pairing **volume and price** for revenue growth
- How to use **helper columns** (price tiers, discount buckets) for concentrated analysis
- When to use **Excel vs Tableau vs Python**
- That forecasting requires **consistent time intervals**
- How to present insights with **clear visual storytelling**
- The process of clean and organized **documentation**

---

## 📌 Next Steps
- Add Python-based forecasting using `statsmodels` for statistical analysis
- Further explore the impact of areas affecting revenue (i.e. pricing tiers VS revenue correlation)
- Deploy this into an SQL-connected dashboard
- Improve on Data-storytelling by expanding on Tableau charting/visuals
- Publicize this on a Python notebook for ease of demonstration
- Research the instances in which scaling with SQL and Python would be applicable

---

## 🧠 Reflection
This project was built entirely self-guided - from selecting the dataset to analyzing trends and communicating insights. It demonstrates curiosity, structured thinking, and a business-first mindset in how I approach problems as an analyst.

---

## 🔗 Project Assets & References

- 📁 **Excel Dataset**: [Link to file on Github](https://github.com/WellsonLau/Exploration-of-E-Commerce-Transactions/blob/main/ecommerce_dataset.xlsx)
- 🧾 **Full Project Notes**: [View Notes on Github](https://github.com/WellsonLau/Exploration-of-E-Commerce-Transactions/blob/main/Notes_Analysis.md)
- 🐍 **Loading & Querying Sql into Python**: [View code on GitHub](https://github.com/WellsonLau/Exploration-of-E-Commerce-Transactions/blob/main/load_and_query.py)
- 📊 **Tableau Dashboard**: [View on Tableau Public](https://public.tableau.com/app/profile/wellson.lau/viz/ExplorationofE-CommerceTransactions/Dashboard1)

