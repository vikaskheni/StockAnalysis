import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


def update_eps_data(csv_filename, row_number):
    url = f'https://www.moneycontrol.com/financials/{symbol}/ratiosVI/{symbol}#VI{symbol}'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the EPS data table based on its class or other attributes
    eps_table = soup.find('table', {'class': 'mctable1'})

    # Specify the CSV filename

    existing_data = pd.read_csv(csv_filename)
    years = pd.to_datetime(existing_data['Date']).dt.year

    if eps_table:
        rows = eps_table.find_all('tr')
        cols = rows[row_number].find_all('td')
        EPS = cols[0].get_text()

        # Assign eps values
        eps_2023 = cols[1].get_text()
        eps_2022 = cols[2].get_text()
        eps_2021 = cols[3].get_text()
        eps_2020 = cols[4].get_text()


        # Use loop to assign values based on years
        for i, year in enumerate(years):
            if year == 2023:
                existing_data.at[i, f"{EPS}"] = eps_2023
            elif year == 2022:
                existing_data.at[i, f"{EPS}"] = eps_2022
            elif year == 2021:
                existing_data.at[i, f"{EPS}"] = eps_2021
            elif year == 2020:
                existing_data.at[i, f"{EPS}"] = eps_2020

        # Write the updated data to the CSV file
        existing_data.to_csv(csv_filename, index=False)

        print(f'Data {EPS} appended to columns in {csv_filename}')
    else:
        print('EPS data table not found')


symbol = 'TCS'  # Stock symbol for Tata Consultancy Services
csv_filename = f"{symbol}_stock_data.csv"
update_eps_data(csv_filename,2) #Basic EPS
update_eps_data(csv_filename,4) #Cash EPS
update_eps_data(csv_filename,5) #Book Value
update_eps_data(csv_filename,7) #Dividend Value

