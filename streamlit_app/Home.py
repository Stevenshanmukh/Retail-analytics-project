
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        master_df = pd.read_csv('../data/processed/master_dataset.csv')
        master_df['date_parsed'] = pd.to_datetime(master_df['date_parsed'])
        
        with open('../data/dashboard/kpis.json', 'r') as f:
            kpis = json.load(f)
        
        monthly_trends = pd.read_csv('../data/dashboard/monthly_trends.csv')
        segment_perf = pd.read_csv('../data/dashboard/segment_performance.csv')
        top_products = pd.read_csv('../data/dashboard/top_products.csv')
        
        return master_df, kpis, monthly_trends, segment_perf, top_products
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None, None, None

master_df, kpis, monthly_trends, segment_perf, top_products = load_data()

st.title("Retail Analytics Dashboard")
st.markdown("### Executive Overview")

if kpis:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = kpis['kpis']['revenue']['total_revenue']
        st.metric(
            label="Total Revenue",
            value=f"${total_revenue/1000000:.1f}M",
            delta=f"{kpis['kpis']['revenue']['yoy_growth']:.2f}% YoY"
        )
    
    with col2:
        total_customers = kpis['kpis']['customers']['total_customers']
        retention = kpis['kpis']['customers']['retention_rate']
        st.metric(
            label="Total Customers",
            value=f"{total_customers:,}",
            delta=f"{retention:.0f}% Retention"
        )
    
    with col3:
        aov = kpis['kpis']['transactions']['avg_order_value']
        st.metric(
            label="Avg Order Value",
            value=f"${aov:.2f}",
            delta=f"{kpis['kpis']['transactions']['aov_change']:.2f}%"
        )
    
    with col4:
        at_risk = kpis['kpis']['churn']['customers_at_risk']
        risk_pct = kpis['kpis']['churn']['churn_risk_percentage']
        st.metric(
            label="Customers at Risk",
            value=f"{at_risk:,}",
            delta=f"-{risk_pct:.1f}%",
            delta_color="inverse"
        )

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Monthly Revenue Trend")
    if monthly_trends is not None:
        monthly_trends['year_month'] = pd.to_datetime(monthly_trends['year_month'])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=monthly_trends['year_month'],
            y=monthly_trends['revenue_millions'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color='#2ecc71', width=3),
            marker=dict(size=6)
        ))
        
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Revenue (Millions $)",
            hovermode='x unified',
            height=300,
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Customer Segments")
    if segment_perf is not None:
        fig = px.pie(
            segment_perf,
            values='revenue_millions',
            names='customer_segment',
            hole=0.4
        )
        
        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=20, b=0),
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Top 10 Products")
    if top_products is not None:
        top_10 = top_products.head(10)
        
        fig = go.Figure(go.Bar(
            y=top_10['item_name'],
            x=top_10['revenue']/1000,
            orientation='h',
            marker=dict(color='#3498db')
        ))
        
        fig.update_layout(
            xaxis_title="Revenue (Thousands $)",
            yaxis_title="",
            height=400,
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        fig.update_yaxes(autorange="reversed")
        
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Segment Performance Metrics")
    if segment_perf is not None:
        display_df = segment_perf[['customer_segment', 'customer_key', 
                                    'revenue_millions', 'revenue_share']].copy()
        display_df.columns = ['Segment', 'Customers', 'Revenue ($M)', 'Share (%)']
        display_df['Revenue ($M)'] = display_df['Revenue ($M)'].round(2)
        display_df['Share (%)'] = display_df['Share (%)'].round(1)
        
        st.dataframe(
            display_df,
            hide_index=True,
            use_container_width=True,
            height=400
        )

st.markdown("---")
st.markdown("#### Business Health Score")

if kpis:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Revenue Growth", "85/100", "Good")
    with col2:
        st.metric("Customer Retention", "100/100", "Excellent")
    with col3:
        st.metric("Overall Health", "92/100", "Excellent")

st.sidebar.markdown("## Navigation")
st.sidebar.info("""
**Current Page:** Home Dashboard

**Other Pages:**
- Revenue Analytics
- Customer Insights  
- Product Performance
- Geographic Analysis
- Pricing Optimizer

Use the sidebar to navigate between pages.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### Data Summary")
if master_df is not None:
    st.sidebar.write(f"**Records:** {len(master_df):,}")
    st.sidebar.write(f"**Date Range:** {master_df['date_parsed'].min().strftime('%Y-%m-%d')} to {master_df['date_parsed'].max().strftime('%Y-%m-%d')}")
    st.sidebar.write(f"**Customers:** {master_df['customer_key'].nunique():,}")
    st.sidebar.write(f"**Products:** {master_df['item_key'].nunique()}")
