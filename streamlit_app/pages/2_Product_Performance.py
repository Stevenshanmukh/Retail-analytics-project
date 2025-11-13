
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Product Performance", page_icon="📦", layout="wide")

st.title("Product Performance Analysis")

@st.cache_data
def load_product_data():
    try:
        top_products = pd.read_csv('../data/dashboard/top_products.csv')
        master_df = pd.read_csv('../data/processed/master_dataset.csv')
        return top_products, master_df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

top_products, master_df = load_product_data()

st.markdown("### Product Overview")

if top_products is not None:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_products = len(top_products)
        st.metric("Total Products", f"{total_products}")
    
    with col2:
        total_revenue = top_products['revenue'].sum()
        st.metric("Total Revenue", f"${total_revenue/1000000:.1f}M")
    
    with col3:
        avg_revenue = top_products['revenue'].mean()
        st.metric("Avg Product Revenue", f"${avg_revenue/1000:.1f}K")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Top 20 Products by Revenue")
    if top_products is not None:
        top_20 = top_products.head(20)
        
        fig = go.Figure(go.Bar(
            y=top_20['item_name'],
            x=top_20['revenue']/1000,
            orientation='h',
            marker=dict(
                color=top_20['revenue'],
                colorscale='Viridis',
                showscale=True
            )
        ))
        
        fig.update_layout(
            xaxis_title="Revenue (Thousands $)",
            yaxis_title="",
            height=600,
            margin=dict(l=0, r=0, t=20, b=0)
        )
        
        fig.update_yaxes(autorange="reversed")
        
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Top Products Data")
    if top_products is not None:
        display_df = top_products.head(20)[['item_name', 'revenue', 'transactions']].copy()
        display_df.columns = ['Product', 'Revenue ($)', 'Orders']
        display_df['Revenue ($)'] = display_df['Revenue ($)'].apply(lambda x: f"${x:,.0f}")
        
        st.dataframe(display_df, hide_index=True, use_container_width=True, height=600)

st.markdown("---")

if master_df is not None:
    st.markdown("### Category Performance")
    
    category_perf = master_df.groupby('desc').agg({
        'total_price': 'sum',
        'payment_key': 'count'
    }).reset_index()
    category_perf.columns = ['category', 'revenue', 'transactions']
    category_perf = category_perf.sort_values('revenue', ascending=False).head(10)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Top 10 Categories by Revenue")
        fig = px.bar(
            category_perf,
            x='category',
            y='revenue',
            color='revenue',
            color_continuous_scale='Blues'
        )
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Revenue ($)",
            showlegend=False,
            height=400
        )
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Category Revenue Share")
        fig = px.pie(
            category_perf,
            values='revenue',
            names='category',
            hole=0.4
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### Product Insights & Recommendations")

st.success("""
**Top Performers:**
- Red Bull 12oz: $1.3M revenue (energy drinks highly profitable)
- Coffee K-Cups: Multiple top sellers, high margin category

**Opportunities:**
- Expand Coffee K-Cups inventory (proven high performers)
- Promote Energy/Protein beverages (premium pricing)
- Focus on Healthy Food category (largest revenue generator)
""")

st.warning("""
**Monitor:**
- Chips category showing declining trend
- Consider price reduction to boost volume
""")
