# **Scripts Directory**  

This directory contains reusable Python scripts designed to modularize the codebase and improve maintainability. These scripts are meant to perform common tasks across the project, such as data visualization and utility functions.  

---



## **Scripts Overview**  

### **1. `plot.py`**  
This script provides reusable functions for generating data visualizations, including but not limited to:  
- Technical indicator plots (e.g., MACD, RSI).  
- Price trends for individual stocks.  
- Correlation heatmaps and histograms.  

#### **Functions**  
1. **`plot_macd(df, title="MACD Indicator")`**  
   Generates a MACD plot (lines and histogram) for a given DataFrame.  
   - **Parameters**:  
     - `df` (DataFrame): The data containing MACD columns (`MACD`, `MACD_Signal`, `MACD_Hist`).  
     - `title` (str): The title of the plot. Default is "MACD Indicator".  
   - **Returns**:  
     - A plot displayed using `matplotlib`.  
   - **Usage**:  
     ```python
     from scripts.plot import plot_macd
     plot_macd(stock_data, title="AAPL MACD Analysis")
     ```

2. **`plot_rsi(df, title="RSI Indicator", threshold=30)`**  
   Creates an RSI plot with optional overbought/oversold thresholds.  
   - **Parameters**:  
     - `df` (DataFrame): The data containing the `RSI` column.  
     - `title` (str): The title of the plot. Default is "RSI Indicator".  
     - `threshold` (int): RSI threshold (e.g., 30/70).  
   - **Usage**:  
     ```python
     from scripts.plot import plot_rsi
     plot_rsi(stock_data, title="AAPL RSI Indicator")
     ```

3. **`plot_price_trends(df, column="Close", title="Stock Price Trends")`**  
   Plots stock price trends over time.  
   - **Parameters**:  
     - `df` (DataFrame): The stock price data.  
     - `column` (str): The price column to plot (default is `"Close"`).  
     - `title` (str): The title of the plot.  
   - **Usage**:  
     ```python
     from scripts.plot import plot_price_trends
     plot_price_trends(stock_data, column="Close", title="AAPL Stock Prices")
     ```

---

## **How to Use the Scripts**  

1. **Import the Functions**  
   Include the `scripts` module in your project by importing the necessary functions:  
   ```python
   from scripts.plot import plot_macd, plot_rsi, plot_price_trends
   ```

2. **Call the Functions**  
   Pass the required data and parameters to generate the plots. Example:  
   ```python
   plot_macd(stock_data)
   plot_rsi(stock_data, threshold=70)
   plot_price_trends(stock_data, column="Open")
   ```

---

## **Future Enhancements**  
- Add more advanced visualization options.  
- Introduce interactive plots using **Plotly** or **Bokeh**.  
- Include scripts for other utility tasks (e.g., data cleaning, report generation).  

