import csv
import pandas as pd


symbol = 'TCS'  # Stock symbol for Tata Consultancy Services
csv_filename = f"{symbol}_stock_data.csv"

stock_data = pd.read_csv(csv_filename)
stock_data['P/E'] = (stock_data['Close'] / stock_data['Cash EPS (Rs.)'])
#stock_data['price to Book Ratio'] = (stock_data['Close'] / stock_data['Book Value [ExclRevalReserve]/Share (Rs.)'])
stock_data.to_csv(csv_filename, index=False)