"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


symbol = 'TCS'  # Stock symbol for Tata Consultancy Services
csv_filename = f"{symbol}_stock_data.csv"
existing_data = pd.read_csv(csv_filename)
years = pd.to_datetime(existing_data['Date']).dt.year


# URL of the page to scrape
url = "https://companiesmarketcap.com/tata-consultancy-services/pb-ratio/"

# Send a GET request to the URL
response = requests.get(url)


# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the P/B ratio data
pb_ratio_table = soup.find("table", {"class": "table"})

pb_ratios = []
if pb_ratio_table:
    # Find all rows in the table
    rows = pb_ratio_table.find_all("tr")

    # Extract data for the years 2020 to 2022
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            part = cells[0].text.strip().split("-")
            year2 = part[0]
            pb_ratio_data = cells[1].text.strip()
            pb_ratios.append(pb_ratio_data)
            print(f"Year: {year2}, P/B Ratio: {pb_ratio_data}")


else:
    print("P/B Ratio table not found.")
for i, year in enumerate(years):
    if year == 2023:
        existing_data.at[i, "p"] = 0
    elif year == 2022:
        existing_data.at[i, "p"] = pb_ratios[0]
    elif year == 2021:
        existing_data.at[i, "p"] = pb_ratios[1]
    elif year == 2020:
        existing_data.at[i, "p"] = pb_ratios[2]

# Write the updated data to the CSV file
existing_data.to_csv(csv_filename, index=False)
"""