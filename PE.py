import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from datetime import datetime


# URL of the webpage
url = "https://www.screener.in/company/TCS/consolidated/#profit-loss"
#https://www.screener.in/company/TCS/consolidated/#profit-loss

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

shareholding_section = soup.find(id='shareholding')

# Find the data-table within the shareholding section
eps_table = shareholding_section.find('table', class_='data-table')

my_fii ={}
my_dii = {}
name_fii = 'FII'
name_dii = 'DII'
if eps_table:
    rows = eps_table.find_all('tr')
    cols_date = rows[0].find_all('th')
    cols_fii = rows[2].find_all('td')
    cols_dii = rows[3].find_all('td')


    for i in range(1,13):
        my_fii[cols_date[i].get_text()]=cols_fii[i].get_text()
        my_dii[cols_date[i].get_text()]=cols_dii[i].get_text()





def month_number(abbreviation):
    month_names = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    return month_names.get(abbreviation, None)


# CSV file name and symbol
symbol = 'TCS'
csv_filename = f"{symbol}_stock_data.csv"
existing_data = pd.read_csv(csv_filename)
# Iterate over my_fii dictionary and update the existing_data DataFrame
for key, value in my_fii.items():
    month, year_value = key.split()
    month_number_value = month_number(month)
    for i, date_str in existing_data['Date'].items():
        yeare,monthe,daye = date_str.split('-')
        monthe = monthe.lstrip('0')  # Remove leading zero
        if int(yeare) == int(year_value) and (int(monthe) == int(month_number_value) - 1 or int(monthe) == int(month_number_value) - 2 or int(monthe) == int(month_number_value)):
            existing_data.at[i, f"{name_fii}"] = value

# Save the updated DataFrame back to the CSV fil
existing_data.to_csv(csv_filename, index=False)
print(f'{name_fii} Data appended to columns in {csv_filename}')

existing_data = pd.read_csv(csv_filename)
# Iterate over my_fii dictionary and update the existing_data DataFrame
for key, value in my_dii.items():
    month, year_value = key.split()
    month_number_value = month_number(month)
    for i, date_str in existing_data['Date'].items():
        yeare,monthe,daye = date_str.split('-')
        monthe = monthe.lstrip('0')  # Remove leading zero
        if int(yeare) == int(year_value) and (int(monthe) == int(month_number_value) - 1 or int(monthe) == int(month_number_value) - 2 or int(monthe) == int(month_number_value)):
            existing_data.at[i, f"{name_dii}"] = value

# Save the updated DataFrame back to the CSV fil
existing_data.to_csv(csv_filename, index=False)
print(f' {name_dii}Data appended  to columns in {csv_filename}')
