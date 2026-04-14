# 🛒 Walmart Demand Forecasting & Inventory Optimization System

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Streamlit Deployed](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B.svg)](https://walmart-demand-forecasting-srikeerthan.streamlit.app/)
[![Model ARIMA](https://img.shields.io/badge/Model-ARIMA-orange.svg)]()

> **Live Application:** [View the Interactive Streamlit Dashboard Here](https://walmart-demand-forecasting-srikeerthan.streamlit.app/)

## 📌 Overview

An end-to-end data science and analytics web application that forecasts future product demand for Walmart stores using ARIMA time series modeling. By translating predictive data into actionable business intelligence, this system recommends optimal inventory levels to help businesses reduce overstock, minimize holding costs, and prevent stockouts.

## 🚀 Features

* 📈 **Interactive Weekly Sales Forecasting:** Generates reliable future demand predictions across different store branches.
* 📦 **Automated Inventory Recommendations:** Calculates optimal weekly stock levels based on forecasted demand.
* 🔍 **Anomaly & Trend Detection:** Automatically identifies historical sales spikes and seasonal trends for better context.
* 📊 **Live Streamlit Dashboard:** A user-friendly, real-time interface for stakeholders to interact with the data.
* 🗄️ **Raw Data Explorer:** Allows users to drill down into the underlying historical data (400K+ records).

## 🛠️ Tech Stack

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Pandas** | Data processing, cleaning, and feature extraction |
| **Statsmodels** | Time series modeling (ARIMA) |
| **Streamlit** | Web application and interactive dashboard framework |

## 📁 Project Structure

```text
walmart-forecast/
├── data/                  # Raw CSV datasets
├── src/                   # Core logic modules
│   ├── data_loader.py
│   ├── preprocess.py
│   └── model.py
├── app.py                 # Main Streamlit dashboard script
├── requirements.txt       # Python dependencies
└── README.md
```

## ▶️ Run Locally

To run this project on your local machine, follow these steps:
# Clone the repository
git clone [https://github.com/Srikeerthan505/walmart-forecast](https://github.com/Srikeerthan505/walmart-forecast)

# Navigate to the project directory
cd walmart-forecast

# Install the required dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py

## 📊 Dataset

The project utilizes the Walmart Store Sales Forecasting dataset from Kaggle, containing comprehensive historical sales data across multiple Walmart stores and departments.