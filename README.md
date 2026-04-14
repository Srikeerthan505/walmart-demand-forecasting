# 🛒 Walmart Demand Forecasting & Inventory Optimization System

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Streamlit Deployed](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B.svg)](https://walmart-demand-forecasting-keerthan.streamlit.app/)
[![Model ARIMA & LSTM](https://img.shields.io/badge/Models-ARIMA%20%7C%20LSTM-orange.svg)]()

> **Live Application:** [View the Interactive Streamlit Dashboard Here](https://walmart-demand-forecasting-keerthan.streamlit.app/)

## 📌 Overview

An end-to-end data science and analytics web application that forecasts future product demand for Walmart stores using time series modeling (ARIMA and LSTM). By translating predictive data into actionable business intelligence, this system recommends optimal inventory levels to help businesses reduce overstock, minimize holding costs, and prevent stockouts.

## 🪼 Features

* 📈 **Interactive Weekly Sales Forecasting:** Generates reliable future demand predictions across different store branches.
* 📦 **Automated Inventory Recommendations:** Calculates optimal weekly stock levels based on forecasted demand.
* 🧠 **Deep Learning Integration:** Includes an experimental LSTM neural network architecture for complex sequence prediction.
* 📊 **Live Streamlit Dashboard:** A user-friendly, real-time interface for stakeholders to interact with the data.
* 🗄️ **Raw Data Explorer:** Allows users to drill down into the underlying historical data (400K+ records).

## 🛠️ Tech Stack

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Pandas** | Data processing, cleaning, and feature extraction |
| **Statsmodels** | Statistical time series modeling (ARIMA) |
| **TensorFlow / Keras** | Deep learning time series modeling (LSTM) |
| **Streamlit** | Web application and interactive dashboard framework |

## 📁 Project Structure

```text
WALMART-DEMAND-FORECASTING/
├── data/                  
├── src/                   
│   ├── data_loader.py     
│   ├── preprocess.py     
│   ├── model.py           
│   ├── lstm_model.py      
│   └── metrics.py       
├── venv/                  
├── app.py                
├── requirements.txt      
├── runtime.txt           
├── .gitignore             
└── README.md             
```

## ▶️ Run Locally

# Clone the repository
git clone [https://github.com/Srikeerthan505/walmart-forecast](https://github.com/Srikeerthan505/walmart-forecast)

# Navigate to the project directory
cd WALMART-DEMAND-FORECASTING

# Install the required dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py

## 📊 Dataset

The project utilizes the Walmart Store Sales Forecasting dataset from Kaggle, containing comprehensive historical sales data across multiple Walmart stores and departments.
