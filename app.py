import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

# PAGE CONFIG
st.set_page_config(
    page_title='Sales Forecasting Dashboard',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# CUSTOM CSS
st.markdown("""
    <style>
    .main { padding-top: 2rem; }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('# 📊 AI-Powered Sales Forecasting Dashboard')
st.markdown('*Predict future sales with Prophet ML & interactive visualizations*')
st.divider()

# SIDEBAR
with st.sidebar:
    st.header('⚙️ Configuration')
    uploaded_file = st.file_uploader('📁 Upload CSV (date, sales columns)', type=['csv'])
    forecast_periods = st.slider('🔮 Forecast Period (days)', 7, 365, 30, 7)
    confidence_interval = st.slider('📊 Confidence Interval', 0.5, 0.99, 0.95, 0.05)
    
    st.divider()
    st.info('1. Upload CSV\n2. Adjust parameters\n3. View predictions')

# MAIN LOGIC
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if 'date' not in df.columns or 'sales' not in df.columns:
            st.error('❌ CSV must contain date and sales columns!')
            st.stop()
        
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date').drop_duplicates(subset=['date'], keep='first')
        
        df_prophet = df[['date', 'sales']].copy()
        df_prophet.columns = ['ds', 'y']
        
        # METRICS
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric('📅 Date Range', f'{df["date"].min().date()} to {df["date"].max().date()}')
        with col2:
            st.metric('📊 Data Points', len(df))
        with col3:
            st.metric('💰 Total Sales', f'${df["sales"].sum():,.0f}')
        with col4:
            st.metric('📈 Avg Daily Sales', f'${df["sales"].mean():,.0f}')
        
        st.divider()
        
        # TRAIN MODEL
        with st.spinner('🤖 Training Prophet model...'):
            model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=True,
                daily_seasonality=False,
                interval_width=confidence_interval
            )
            model.fit(df_prophet)
        
        future = model.make_future_dataframe(periods=forecast_periods)
        forecast = model.predict(future)
        
        # TABS
        tab1, tab2, tab3 = st.tabs(['📈 Forecast', '📊 Trends', '📉 Metrics'])
        
        with tab1:
            st.subheader('Sales Forecast Chart')
            fig_forecast = go.Figure()
            
            fig_forecast.add_trace(go.Scatter(
                x=df['date'], y=df['sales'],
                name='Historical', mode='lines',
                line=dict(color='#1f77b4', width=2)
            ))
            
            fig_forecast.add_trace(go.Scatter(
                x=forecast['ds'], y=forecast['yhat'],
                name='Forecast', mode='lines',
                line=dict(color='#ff7f0e', width=2)
            ))
            
            fig_forecast.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat_upper'],
                fill=None, mode='lines',
                line_color='rgba(0,0,0,0)',
                showlegend=False
            ))
            
            fig_forecast.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat_lower'],
                fill='tonexty', mode='lines',
                line_color='rgba(0,0,0,0)',
                name='95% CI'
            ))
            
            fig_forecast.update_layout(
                title='Historical vs Predicted Sales',
                xaxis_title='Date',
                yaxis_title='Sales ($)',
                hovermode='x unified',
                height=500
            )
            st.plotly_chart(fig_forecast, use_container_width=True)
        
        with tab2:
            st.subheader('Trend Decomposition')
            fig_components = model.plot_components(forecast)
            st.pyplot(fig_components)
        
        with tab3:
            st.subheader('Forecast Metrics')
            st.write(f'**Total Forecasted Sales (30 days):** ${forecast.tail(30)["yhat"].sum():,.0f}')
            st.write(f'**Average Forecasted Daily Sales:** ${forecast.tail(30)["yhat"].mean():,.0f}')
            
            metrics_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10)
            metrics_df.columns = ['Date', 'Forecast', 'Lower CI', 'Upper CI']
            st.dataframe(metrics_df, use_container_width=True)
    
    except Exception as e:
        st.error(f'❌ Error: {str(e)}')
else:
    st.info('👈 Please upload a CSV file to get started')
    st.markdown('### Sample CSV Format:')
    st.code('date,sales\n2023-01-01,2500\n2023-01-02,2700', language='csv')
