
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Customer Insights", page_icon="👥", layout="wide")

st.title("Customer Insights & Segmentation")

@st.cache_data
def load_customer_data():
    try:
        segment_perf = pd.read_csv('../data/dashboard/segment_performance.csv')
        customer_risk = pd.read_csv('../data/dashboard/customer_risk.csv')
        return segment_perf, customer_risk
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

segment_perf, customer_risk = load_customer_data()

st.markdown("### Customer Segmentation Analysis")

if segment_perf is not None:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_customers = segment_perf['customer_key'].sum()
        st.metric("Total Customers", f"{int(total_customers):,}")
    
    with col2:
        total_revenue = segment_perf['revenue_millions'].sum()
        st.metric("Total Revenue", f"${total_revenue:.1f}M")
    
    with col3:
        avg_aov = segment_perf['avg_order_value'].mean()
        st.metric("Avg Order Value", f"${avg_aov:.2f}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Segment Revenue Distribution")
    if segment_perf is not None:
        fig = px.bar(
            segment_perf,
            x='customer_segment',
            y='revenue_millions',
            color='customer_segment',
            title=""
        )
        fig.update_layout(
            xaxis_title="Segment",
            yaxis_title="Revenue (Millions $)",
            showlegend=False,
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Customer Distribution")
    if segment_perf is not None:
        fig = px.pie(
            segment_perf,
            values='customer_key',
            names='customer_segment',
            hole=0.4
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### Churn Risk Analysis")

if customer_risk is not None:
    risk_summary = customer_risk.groupby('risk_level').agg({
        'customer_key': 'count',
        'total_spent': 'sum'
    }).reset_index()
    
    col1, col2, col3, col4 = st.columns(4)
    
    risk_levels = ['Low', 'Medium', 'High', 'Critical']
    for idx, level in enumerate(risk_levels):
        level_data = risk_summary[risk_summary['risk_level'] == level]
        if not level_data.empty:
            count = int(level_data['customer_key'].values[0])
            with [col1, col2, col3, col4][idx]:
                st.metric(f"{level} Risk", f"{count:,}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Risk Distribution")
    if customer_risk is not None:
        risk_summary = customer_risk.groupby('risk_level')['customer_key'].count().reset_index()
        risk_summary.columns = ['Risk Level', 'Customer Count']
        
        fig = go.Figure(data=[go.Bar(
            x=risk_summary['Risk Level'],
            y=risk_summary['Customer Count'],
            marker_color=['green', 'orange', 'red', 'darkred']
        )])
        
        fig.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Number of Customers",
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Segment Performance Table")
    if segment_perf is not None:
        display_df = segment_perf[['customer_segment', 'customer_key', 
                                    'revenue_millions', 'revenue_share']].copy()
        display_df.columns = ['Segment', 'Customers', 'Revenue ($M)', 'Share (%)']
        display_df['Revenue ($M)'] = display_df['Revenue ($M)'].round(2)
        display_df['Share (%)'] = display_df['Share (%)'].round(1)
        
        st.dataframe(display_df, hide_index=True, use_container_width=True, height=350)

st.markdown("---")
st.markdown("### Recommendations")

st.info("""
**Priority Actions:**
- **Champions**: Implement VIP loyalty program
- **Loyal Customers**: Launch upsell campaigns  
- **At Risk**: Immediate retention outreach
- **Low Engagement**: Targeted win-back offers with 10-15% discount
""")
