import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train_model, forecast

st.set_page_config(page_title="Walmart Forecast", layout="wide")

st.title("🛒 Walmart Demand Forecasting & Inventory System")

# Load data
df = load_data()
df = preprocess(df)

# Sidebar filters
st.sidebar.header("Filters")
store = st.sidebar.selectbox("Select Store", df['Store'].unique())
dept = st.sidebar.selectbox("Select Department", df['Dept'].unique())

filtered = df[(df['Store'] == store) & (df['Dept'] == dept)]

filtered = filtered[['Date', 'Weekly_Sales']]
filtered = filtered.set_index('Date')

st.subheader("📊 Historical Sales")
st.line_chart(filtered)

# Train model
model = train_model(filtered['Weekly_Sales'])

# Forecast slider
weeks = st.slider("Forecast Weeks", 1, 12, 8)

future = forecast(model, weeks)

st.subheader("🔮 Forecast")
st.line_chart(future)

# Inventory recommendation
avg = future.mean()
recommended = int(avg * 1.1)

st.subheader("📦 Inventory Recommendation")
st.success(f"Recommended weekly stock: {recommended} units")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(filtered.tail())