# Retail Analytics Dashboard

## Overview
Interactive Streamlit dashboard for retail analytics featuring:
- Executive KPI dashboard
- Customer segmentation and insights
- Product performance analysis
- Revenue forecasting
- Pricing optimization

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure data files are in correct locations:
```
data/
├── processed/
│   └── master_dataset.csv
└── dashboard/
    ├── kpis.json
    ├── monthly_trends.csv
    ├── segment_performance.csv
    ├── top_products.csv
    ├── geographic_performance.csv
    └── customer_risk.csv
```

## Running the App
```bash
streamlit run Home.py
```

The app will be available at http://localhost:8501

## Features

### Home Dashboard
- Executive KPIs (Revenue, Customers, AOV, Churn Risk)
- Monthly revenue trends
- Customer segment distribution
- Top products overview
- Business health score

### Customer Insights
- Customer segmentation analysis
- Segment performance metrics
- Churn risk distribution
- Retention recommendations

### Product Performance
- Top products by revenue
- Category performance analysis
- Product recommendations
- Trend analysis

## Data Requirements

The app expects the following data structure:
- master_dataset.csv: Main transaction data
- kpis.json: Pre-calculated KPI metrics
- CSV files: Dashboard-ready aggregated data

## Technology Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **ML Models**: Scikit-learn

## Deployment

### Local Deployment
```bash
streamlit run Home.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy from streamlit.io/cloud

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "Home.py"]
```

## Support

For issues or questions, refer to the project documentation.
