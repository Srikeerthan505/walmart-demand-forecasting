import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train_model, forecast
from src.lstm_model import train_lstm, forecast_lstm
from src.metrics import calculate_metrics

st.set_page_config(page_title="Walmart Forecast", layout="wide")

st.title("🛒 Walmart Demand Forecasting System")

# Load
df = preprocess(load_data())

# Sidebar
store = st.sidebar.selectbox("Store", df['Store'].unique())
dept = st.sidebar.selectbox("Department", df['Dept'].unique())

filtered = df[(df['Store']==store)&(df['Dept']==dept)]
filtered = filtered[['Date','Weekly_Sales']].set_index('Date')

tab1, tab2 = st.tabs(["Forecast", "Comparison"])

# ---------- FORECAST TAB ----------
with tab1:
    st.line_chart(filtered)

    model_type = st.selectbox("Model", ["ARIMA","LSTM"])
    steps = st.slider("Forecast Weeks",1,12,8)

    if model_type=="ARIMA":
        model = train_model(filtered['Weekly_Sales'])
        future = forecast(model,steps)

    else:
        epochs = st.slider("Epochs",10,50,20)
        window = st.slider("Window Size",5,30,10)

        model, scaler, history = train_lstm(filtered['Weekly_Sales'],epochs,window)
        future = forecast_lstm(model,scaler,filtered['Weekly_Sales'],steps,window)

        # Loss graph
        st.subheader("Training Loss")
        st.line_chart(history.history['loss'])

    st.subheader("Forecast")
    st.line_chart(future)

    st.success(f"Recommended Stock: {int(future.mean()*1.1)} units")

# ---------- COMPARISON TAB ----------
with tab2:
    train = filtered[:-20]
    test = filtered[-20:]

    # ARIMA
    arima = train_model(train['Weekly_Sales'])
    arima_pred = arima.forecast(len(test))

    # LSTM
    model, scaler, _ = train_lstm(train['Weekly_Sales'],20,10)
    lstm_pred = forecast_lstm(model,scaler,train['Weekly_Sales'],len(test),10)

    mae_a, rmse_a = calculate_metrics(test['Weekly_Sales'], arima_pred)
    mae_l, rmse_l = calculate_metrics(test['Weekly_Sales'], lstm_pred)

    col1, col2 = st.columns(2)
    col1.metric("ARIMA RMSE", f"{rmse_a:.2f}")
    col1.metric("ARIMA MAE", f"{mae_a:.2f}")

    col2.metric("LSTM RMSE", f"{rmse_l:.2f}")
    col2.metric("LSTM MAE", f"{mae_l:.2f}")

    if rmse_l < rmse_a:
        st.success("LSTM performs better")
    else:
        st.info("ARIMA performs better")

    fig = go.Figure()
    fig.add_scatter(x=test.index,y=test['Weekly_Sales'],name="Actual")
    fig.add_scatter(x=test.index,y=arima_pred,name="ARIMA")
    fig.add_scatter(x=test.index,y=lstm_pred,name="LSTM")

    st.plotly_chart(fig, use_container_width=True)