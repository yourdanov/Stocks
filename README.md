
# **Stocks Analysis and Forecasting Application**

---

## **Overview**
This application is a comprehensive stock analysis and forecasting tool. It allows users to visualize historical data, forecast future stock prices using multiple advanced models, and interact with data through a sleek graphical user interface (GUI). 

### **Features**
1. **Real-Time Stock Price Fetching**: Fetches the latest stock prices using Yahoo Finance.
2. **Historical Data Visualization**: Displays historical stock data for the last 10 years.
3. **Forecasting Models**:
   - ARIMA (Auto-Regressive Integrated Moving Average)
   - ETS (Exponential Smoothing)
   - Random Forest
   - LSTM (Long Short-Term Memory)
4. **Interactive Graphs**:
   - Displays model forecasts for the next 12 months.
   - Hover functionality to show predicted price and date.
5. **Modern GUI**:
   - User-friendly interface..
   - Interactive graphs with zoom and pan capabilities.
6. **Multi-Model Comparison**:
   - Compare forecasts from different models on the same graph.

---

## **Application Workflow**
1. **Data Fetching**:
   - Fetches historical stock data from Yahoo Finance for analysis.
   - Updates real-time prices using intraday data.
2. **Data Preprocessing**:
   - Cleans and prepares data for models.
   - Handles missing data, converts formats, and ensures compatibility.
3. **Forecast Generation**:
   - Each model generates predictions for the next 12 months.
   - Predictions start from the current date.
4. **Visualization**:
   - Forecasts are displayed on a graph.
   - Users can view specific predictions by hovering over points on the graph.

---

## **Modules and Functions**

### **1. Data Fetching**
**Function**: `fetch_stock_data(stock_symbol, start_date, end_date)`
- Fetches historical stock data from Yahoo Finance.
- Returns a time-series dataset for analysis.

**Function**: `fetch_intraday_price(stock_symbol)`
- Fetches the latest stock price using intraday data.

---

### **2. Forecasting Models**
- **ARIMA (AutoRegressive Integrated Moving Average)**:
  - Provides statistical-based predictions.
  - Suitable for time-series data with trends.
- **ETS (Exponential Smoothing)**:
  - Uses exponential smoothing for seasonal data.
- **Random Forest**:
  - A machine learning model that incorporates lag features and technical indicators.
- **LSTM (Long Short-Term Memory)**:
  - A neural network-based model for sequential data.

---

### **3. Graphical User Interface (GUI)**
**Function**:
- Launches the main GUI window.
- Displays historical data and model forecasts.
- Features:
  - Interactive graph with hover functionality.
  - Buttons to show historical data and exit.

**Function**:
- Opens a new window displaying historical data for the last 10 years.

---

## **Dependencies**
### **Python Libraries**
- `yfinance`: Fetches stock data.
- `pandas`: Data manipulation.
- `matplotlib`: Visualization.
- `tensorflow`: Neural network models (LSTM).
- `statsmodels`: ARIMA and ETS models.
- `sklearn`: Random Forest and preprocessing tools.
- `mplcursors`: Adds hover functionality.
- `tkinter`: GUI framework.

### **Installation**
```bash
pip install yfinance pandas matplotlib tensorflow statsmodels scikit-learn mplcursors tk
```

---

## **How to Use**
1. **Launch the Application**:
   - Run the script using `python stocks_forecast.py`.

2. **Select Stock**:
   - The application fetches data for IBM stocks by default.
   - Modify the `stock_symbol` variable to analyze other stocks.

3. **View Forecasts**:
   - Observe forecasts from ARIMA, ETS, Random Forest, and LSTM models.
   - Hover over points on the graph to view predictions.

4. **Exit**:
   - Click the "Exit" button to close the application.

---

## **Customization**
### **Modify Stock Symbol**
Change the `stock_symbol` variable in the `__main__` section:
```python
stock_symbol = "AAPL"  # For Apple stock
```

### **Adjust Forecast Horizon**
Modify the `steps` parameter in model functions to increase/decrease the forecast period.

### **Add More Models**
Additional models can be implemented e.g., XGBoost, Prophet.

---

## **Future Improvements**
1. **Additional Models**: Add models like Prophet, XGBoost, and SARIMA.
2. **User Preferences**: Allow users to select models and forecast durations dynamically.
3. **Data Export**: Functionality to save forecasts as CSV or Excel files.

---

## **Known Issues**
1. **LSTM Predictions**:
   - Requires sufficient data for accurate predictions.
   - Training may be slow for larger datasets.
2. **ARIMA Limitations**:
   - May not handle non-stationary data well without preprocessing.
3. **Real-Time Price Delay**:
   - Intraday data from Yahoo Finance may have a delay of up to 30 minutes.

---

## **Support**
For issues or suggestions, contact:
**Developer**: Atanas Youdanov  
**Email**: a.yourdanov@live.com 
**GitHub**: [GitHub Profile](https://github.com/yourdanov)

---
