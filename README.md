# 🛍️ Retail Analytics & Machine Learning Project

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Analysis](https://img.shields.io/badge/Analysis-Jupyter-orange.svg)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Unlocking $10.9M in Revenue Opportunities through Advanced Analytics & Machine Learning**

---

## 📊 Executive Summary

This project demonstrates an end-to-end data solution analyzing **1M+ transactions** to solve critical retail challenges: churn, pricing inefficiency, and revenue forecasting. By combining robust ETL pipelines with machine learning models, we identified actionable strategies to drive a **10.3% projected revenue increase**.

### 🎯 Key Outcomes
| Metric | Impact |
|--------|--------|
| **Revenue Opportunity** | **$10.9M** identified via pricing & retention strategies |
| **Forecast Accuracy** | **98.03%** (MAPE 1.97%) for reliable planning |
| **Operational Insight** | **$6M** unlocked through optimized pricing elasticity |
| **Customer Retention** | **$7.8M** saved by proactively targeting at-risk segments |

---

## 🚀 The Solution: Interactive Intelligence

This project culminates in a comprehensive analysis dashboard. Below are effective views from our analysis showing the power of data-driven decision making.

### 1. Executive Control Tower
*Real-time visibility into business health, providing a consolidated view of KPIs, revenue trends, and churn risk.*

![Executive Dashboard](reports/dashboard_home.png)

### 2. Customer Segmentation & Churn Prediction
*We moved beyond simple demographics to behavioral segmentation. Using K-Means clustering, we identified 3 distinct personas.*

![Customer Insights](reports/customer_insights.png)

> **Insight:** The "At Risk" segment constitutes only 9% of customers but represents a disproportionate **$7.8M** in potential revenue loss. Targeted retention campaigns for this specific group yield the highest ROI.

### 3. Pricing Strategy Optimization
*Using Price Elasticity of Demand (PED) analysis, we determined optimal price points for each product category.*

![Product Performance](reports/product_performance.png)

> **Insight:** High-volume items like "Coffee K-Cups" showed inelastic demand (-0.8), suggesting a price increase would drive pure margin growth without sacrificing volume.

---

## 🛠️ Technical Architecture

The system is built on a modular "Lakehouse" architecture, validating data integrity at every stage from raw CSVs to the final serving layer.

```mermaid
graph LR
    subgraph Data Pipeline
        Raw[Raw Data (CSV)] --> |Pandas/NumPy| Clean[Processed Data]
        Clean --> |Feature Engineering| Features[ML Features]
    end
    
    subgraph Machine Learning
        Features --> |RF/XGBoost| Forecast[Revenue Forecast Model]
        Features --> |K-Means| Segments[Customer Clusters]
        Features --> |Elasticity Algo| Pricing[Pricing Model]
    end
    
    subgraph Insights
        Forecast --> |KPIs| Report
        Segments --> |Cohorts| Report
        Pricing --> |Strategy| Report
    end
```

### Tech Stack
-   **Data Processing:** Python, Pandas, NumPy
-   **Machine Learning:** Scikit-learn, Statsmodels (ARIMA/SARIMA)
-   **Visualization:** Plotly Interactive Charts, Matplotlib
-   **Environment:** Jupyter Notebooks

---

## 📂 Project Structure

```
├── notebooks/          # 8-step analysis pipeline
│   ├── 00_Setup_Data_Overview.ipynb
│   ├── 01_EDA.ipynb
│   ├── 03_Forecasting.ipynb   # Revenue prediction models
│   ├── 04_Pricing.ipynb       # Elasticity analysis
│   └── 05_Segmentation.ipynb  # Clustering & CLV
├── reports/            # Generated assets & visualizations
├── data/               # Data storage (Raw & Processed)
└── models/             # Serialized ML models
```

---

## 💻 Explore the Code

To replicate the analysis or explore the notebooks:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/stevenlagadapati/retail-analytics-project.git
    cd retail-analytics-project
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Jupyter Notebooks**
    ```bash
    jupyter notebook notebooks/
    ```

---

## 📧 Contact

**Steven Lagadapati**  
*Data Scientist & Analytics Engineer*  
[Email](mailto:stevenlagadapati1012@gmail.com) | [GitHub](https://github.com/stevenlagadapati)

---
*Made with ❤️ and Python*