import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace with the actual URL
url = 'https://indiancompanies.in/listed-companies-in-nse-with-symbol/'

#https://indiancompanies.in/listed-companies-in-nse-with-symbol/

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

stock_data = []

# Find the table containing stock data
table = soup.find('table')

# Extract data from the table rows
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    if len(columns) >= 3:
        symbol = columns[2].text.strip()
        full_name = columns[1].text.strip()
        stock_data.append({'SYMBOL': symbol, 'FULL NAME OF COMPANY': full_name})


df = pd.DataFrame(stock_data)
print(df)

df.to_csv('Nse_Stocks.csv', index=False)

print('Data saved to nse_stocks.csv')
