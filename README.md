# 🧠 AI-Enhanced Financial Fraud Detection Dashboard

An end-to-end data analytics project that combines Machine Learning (Isolation Forest) and AI (OpenAI GPT-style logic) with Power BI to detect and explain suspicious financial transactions.

---

## 🚀 Project Overview

**Goal**: Detect potential fraudulent transactions and explain their risk factors using simulated AI analysis.

**Tools Used**:
- Python (Pandas, scikit-learn, Matplotlib)
- Power BI (for dashboarding)
- GPT-style logic (via OpenAI or simulated GPT responses)
- Isolation Forest (unsupervised anomaly detection)
- Excel (initial formatting)

---

## 🧾 Dataset Description

| Column Name          | Description                                     |
|----------------------|-------------------------------------------------|
| `transaction_id`     | Unique ID for the transaction                   |
| `amount`             | Transaction amount in local currency            |
| `location`           | Location where the transaction occurred         |
| `device_type`        | Device used (Mobile, Desktop, Tablet)           |
| `time`               | Timestamp of the transaction                    |
| `merchant_category`  | Type of merchant (Retail, Travel, Grocery, etc) |
| `fraud_flag`         | Flagged by ML model: `-1` for suspicious        |
| `ai_reason`          | Explanation for suspicious activity (AI-based)  |

---

## 📌 Key Components

### 🔹 1. Python (fraud_detection_model.py)
- Loads `large_financial_transactions.csv`
- Applies Isolation Forest model to detect anomalies
- Flags suspicious transactions (saved in `flagged_frauds.csv`)
- Trained model saved as `isolation_forest_model.pkl`

### 🔹 2. GPT-Style AI Reasoning (generate_ai_fraud_reasons.py)
- Adds contextual explanations for each suspicious transaction
- Outputs final dataset: `ai_flagged_frauds.csv`

### 🔹 3. Power BI Dashboard
Interactive visual dashboard built using `ai_flagged_frauds.csv`, includes:
- Fraud count by location, category, device type
- Transaction value analysis by risk level
- Dynamic filters and slicers
- Drill-down charts and card KPIs

---

## 📊 Key Metrics

- **Total Transactions Analyzed**: 1000+
- **Suspicious Transactions**: ~10% (based on contamination rate)
- **AI-Enriched Explanations**: Yes (generated for each flagged fraud)

---

---

## 🤖 AI Reasoning Logic

Each suspicious transaction is explained using contextual AI logic based on:
- 📍 High-risk location (e.g. unfamiliar cities)
- 💰 Large transaction amount
- ⌚ Odd hours or weekend timeframes
- 📱 Less secure devices
- 🛒 Risky merchant categories

> Sample Explanation:
> “Transaction flagged due to high amount via mobile device in Mumbai under ‘Retail’ category.”

---

## 🎯 Objective

To help analysts and stakeholders:
- Detect early signs of financial fraud
- Understand *why* a transaction might be suspicious
- Take proactive fraud prevention action

---

## 👨‍💻 Author

**Akarsh Saroj**  
_Data Analyst | Python | Power BI | SQL | Excel | GPT APIs_  
🔗 [LinkedIn](https://www.linkedin.com/in/akarshsaroj)

---

## ✅ Outcome

- ✅ End-to-end fraud detection pipeline
- ✅ AI-enriched explanations for interpretability
- ✅ Dashboard-ready insights
- ✅ Ready for resume, interview, and GitHub



