# 📈 AI-Powered Sales Forecasting Dashboard

> A modern, interactive Streamlit dashboard that predicts future sales using Prophet time-series forecasting and provides actionable business insights.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Prophet](https://img.shields.io/badge/Prophet-Forecasting-blue.svg)](https://facebook.github.io/prophet/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 **Project Overview**

This project demonstrates a **Time-Series Forecasting** application built with cutting-edge ML/AI technologies. The dashboard enables users to:

- 📈 Visualize **historical vs. forecasted sales data**
- 📊 Analyze **trend patterns and seasonal variations**
- 🔮 Get **data-driven predictions** for business planning
- 💡 Extract **actionable insights** with interactive metrics

**Task Name:** AI‑Powered Sales Forecasting Dashboard  
**Tech Stack:** Python, Streamlit, Prophet, Pandas, Plotly

---

## 🚀 **Key Features**

| Feature | Description |
|---------|-------------|
| 📈 **Dual-Chart View** | Historical data + forecast comparison with confidence intervals |
| 📊 **Trend Analysis** | Decomposition showing trend, seasonality, and residuals |
| 📝 **Key Metrics** | Total sales, average daily sales, growth rate, and forecast accuracy |
| 🖋️ **Interactive UI** | Real-time updates, metric cards, and responsive design |
| 📄 **Data Flexibility** | Works with any time-series CSV data |

---

## 📦 **Installation & Setup**

### **Prerequisites**
- Python 3.8 or higher
- Git (for version control)
- pip (Python package manager)

### **Step-by-Step Installation**

#### **1. Clone the Repository**
```bash
git clone https://github.com/Itsimaady/FUTURE_ML_01.git
cd FUTURE_ML_01
```

#### **2. Create Virtual Environment (Recommended)**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Run the Dashboard**
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📁 **Project Structure**

```
FUTURE_ML_01/
├── app.py                 # Main Streamlit application
├── sales.csv              # Sample time-series sales data
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore configuration
```

---

## 📈 **Sample Data Format**

The `sales.csv` should contain two columns:

```csv
date,sales
2023-01-01,2500
2023-01-02,2700
2023-01-03,2300
...add more data...
```

**Data Requirements:**
- **date**: YYYY-MM-DD format
- **sales**: Numeric sales values
- **Minimum 365 days** of historical data recommended

---

## 💡 **How It Works**

### **Workflow**

```
📅 Load CSV Data
    ↓
🔍 Data Preprocessing & Validation
    ↓
🤖 Train Prophet Model
    ↓
🔮 Generate Forecasts
    ↓
📊 Visualize Results & Insights
    ↓
💾 Display Metrics & Trends
```

### **Key Algorithms**

1. **Prophet (Time-Series Forecasting)**
   - Handles trend, seasonality, and holidays
   - Robust to missing data points
   - Generates confidence intervals

2. **Decomposition Analysis**
   - Separates trend from seasonal patterns
   - Identifies underlying data patterns
   - Enables better business decisions

---

## 🌨️ **Dashboard Features Explained**

### **1. Sales Forecast Chart**
- Blue line: Historical sales data
- Red line: Predicted future sales
- Shaded area: Confidence interval (95%)

### **2. Key Metrics**
- **Total Sales**: Sum of all historical sales
- **Average Daily Sales**: Mean daily revenue
- **Growth Rate**: Percentage change over period
- **Forecast Trend**: Predicted direction of sales

### **3. Trend Decomposition**
- **Trend Component**: Long-term sales direction
- **Seasonal Component**: Recurring patterns
- **Residuals**: Unexplained variations

---

## 💶 **Skills Demonstrated**

✅ Time-Series Analysis & Forecasting  
✅ Data Preprocessing & Validation  
✅ Machine Learning Model Training  
✅ Data Visualization & UI Design  
✅ Python Programming  
✅ Streamlit Web Development  
✅ Git Version Control

---

## 🛧️ **Troubleshooting**

| Issue | Solution |
|-------|----------|
| **ModuleNotFoundError** | Run `pip install -r requirements.txt` |
| **Port 8501 already in use** | `streamlit run app.py --server.port 8502` |
| **CSV not loading** | Ensure file is in same directory, format is correct |
| **Forecast looks off** | Ensure ≥65 days of historical data |

---

## 📋 **Usage Example**

```python
# Basic usage in Python
from prophet import Prophet
import pandas as pd

# Load data
df = pd.read_csv('sales.csv')
df['date'] = pd.to_datetime(df['date'])

# Prepare for Prophet
df_prophet = df[['date', 'sales']].copy()
df_prophet.columns = ['ds', 'y']

# Create and train model
model = Prophet()
model.fit(df_prophet)

# Generate forecast for next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# View predictions
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```

---

## 💫 **About the Developer**

**Name:** Aditya M  
**Location:** Hyderabad, India  
**Institution:** Chaitanya Bharathi Institute of Technology (CBIT)  
**Focus Areas:** Machine Learning, Data Science, Web Development  
**GitHub:** [@Itsimaady](https://github.com/Itsimaady)

---

## 🙋 **Acknowledgments**

- **Facebook Research** - Prophet library
- **Streamlit** - Amazing web framework
- **CBIT** - Academic support
- **FUTURE Program** - Task inspiration

---

## ⭐ **Show Your Support**

If you found this project helpful:
- ⭐ Star this repository
- 🔗 Share with fellow developers
- 🗣️ Provide feedback or suggestions

---

**Made with ❤️ by Aditya M**  
*Last Updated: December 2024*
