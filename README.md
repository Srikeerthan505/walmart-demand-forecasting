# 🛒 Walmart Demand Forecasting & Inventory Optimization System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)
![Model](https://img.shields.io/badge/Model-ARIMA-orange)

## 📌 Overview
A machine learning web application that forecasts future product demand 
for Walmart stores using ARIMA time series modeling and recommends 
optimal inventory levels — helping businesses reduce overstock and stockouts.

## 🚀 Features
- 📈 Interactive weekly sales forecasting
- 📦 Automated inventory recommendations
- 🔍 Anomaly & trend detection
- 📊 Live Streamlit dashboard
- 🗂 Raw data explorer

## 🛠 Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data processing |
| Statsmodels | ARIMA model |
| Streamlit | Web dashboard |

## 📁 Project Structure
walmart-forecast/
├── data/          # Raw CSV datasets
├── src/           # Core logic modules
│   ├── data_loader.py
│   ├── preprocess.py
│   └── model.py
├── app.py         # Streamlit dashboard
├── requirements.txt
└── README.md

## ▶ Run Locally
```bash
git clone https://github.com/Srikeerthan505/walmart-forecast
cd walmart-forecast
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Dataset
[Walmart Store Sales Forecasting - Kaggle](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

