"""
import yfinance as yf
import requests

import fmpy


symbol = 'TCS'
stock_data = yf.download(f"{symbol}.ns", start='2022-01-01', end='2023-08-01')

stock_data['%delivery'] = (stock_data['Volume'] / stock_data['Volume'].sum()) * 100
stock_data['Share Delivery'] = stock_data['Volume'] * stock_data['%delivery'] / 100

quarterly_stock_data = stock_data.resample('Q', convention='start').agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Adj Close': 'last',
    'Volume': 'sum',
    '%delivery': 'mean',
    'Share Delivery': 'sum',
})


quarterly_stock_data['52_Week_High'] = stock_data['High'].max()
quarterly_stock_data['52_Week_Low'] = stock_data['Low'].min()



csv_filename = f"{symbol}_quarterly_stock_data.csv"
quarterly_stock_data.to_csv(csv_filename)
print(f"Data saved to {csv_filename}")

"""
"""
import yfinance as yf
import pandas as pd
import requests


response = requests.get(alpha_vantage_base_url, params={
    "function": "EARNINGS",
    "symbol": symbol,
    "apikey": api_key
})
earnings_data = response.json()

# Extract the quarterly EPS data from the API response
quarterly_eps_data = earnings_data.get('annualEarnings', [])

# Create a DataFrame from the quarterly EPS data
eps_df = pd.DataFrame(quarterly_eps_data)
eps_df['fiscalDateEnding'] = pd.to_datetime(eps_df['fiscalDateEnding'])
eps_df.set_index('fiscalDateEnding', inplace=True)

# Resample the EPS data to daily frequency and forward-fill
eps_df_resampled = eps_df.resample('D').ffill()

# Merge the EPS data with stock_data on matching index dates
merged_data = pd.merge(stock_data, eps_df_resampled, left_index=True, right_index=True, how='left')

# Copy the reportedEPS values to the 'EPS(TTM)' column
merged_data['EPS(TTM)'] = merged_data['reportedEPS']

# Drop the 'reportedEPS' column
merged_data.drop('reportedEPS', axis=1, inplace=True)




"""
import yfinance as yf


symbol = 'TCS'
stock_data = yf.download(f"{symbol}.ns", start='2020-01-01', end='2023-08-10') #yyyy-mm-dd


stock_data['%delivery'] = (stock_data['Volume'] / stock_data['Volume'].sum()) * 100
stock_data['Share Delivery'] = stock_data['Volume'] * stock_data['%delivery'] / 100
stock_data['52_Week_High'] = stock_data['High'].max()
stock_data['52_Week_Low'] = stock_data['Low'].min()
selected_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', '%delivery', 'Share Delivery','52_Week_High','52_Week_Low']
selected_data = stock_data[selected_columns]


csv_filename = f"{symbol}_stock_data.csv"
selected_data.to_csv(csv_filename)

print(f"Data saved to {csv_filename}")