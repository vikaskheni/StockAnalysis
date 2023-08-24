import yfinance as yf
import pandas as pd

symbol = 'TCS'
stock_data = yf.download(f"{symbol}.ns", start='2020-07-01', end='2023-08-15')  #yyyy-mm-dd

# Create a new DataFrame to store calculated 52-week high and low
yearly_high_low = pd.DataFrame()

# Calculate 52-week high and low for each specific year
for year in stock_data.index.year.unique():
    year_data = stock_data[stock_data.index.year == year]
    year_data['52_Week_High'] = year_data['High'].max()
    year_data['52_Week_Low'] = year_data['Low'].min()
    yearly_high_low = pd.concat([yearly_high_low, year_data])

# Calculate %delivery, Share Delivery, and select columns
yearly_high_low['%delivery'] = (yearly_high_low['Volume'] / yearly_high_low['Volume'].sum()) * 100
yearly_high_low['Share Delivery'] = yearly_high_low['Volume'] * yearly_high_low['%delivery'] / 100



selected_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', '%delivery', 'Share Delivery', '52_Week_High', '52_Week_Low']

# Create a new DataFrame with the selected columns
selected_data = yearly_high_low[selected_columns].reset_index()

csv_filename = f"{symbol}_stock_data.csv"
selected_data.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")
