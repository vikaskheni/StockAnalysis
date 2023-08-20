from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
webdriver_path = 'C:/Users/Vikas/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Initialize the Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_path), options=chrome_options)

# Open the desired URL
url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/31-July-2020/"
driver.get(url)


table = driver.find_element(By.XPATH, "//table[@id='DataTables_Table_0']")

t_values = {}
d_values = {}
p_values = {}
name_trade = 'Traded_Volume'
name_delivery = 'Delivery_Volume'
name_percentage = '% Delivery'
if table:

    rows = table.find_elements(By.TAG_NAME, "tr")
    for i in range(1,25):  # Skip the header row
        cols = rows[i].find_elements(By.TAG_NAME, "td")
        date = cols[0].text
        traded = cols[1].text
        t_values[date] = traded

        nse_delivery = cols[2].text
        d_values[date] = nse_delivery

        percent_delivery = cols[3].text
        p_values[date] = percent_delivery

        #print(date, traded, nse_delivery, percent_delivery)

else:
    print("table is not getting ")

driver.quit()

def month_number(abbreviation):
    month_names = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    return month_names.get(abbreviation, None)

def year_number(abbreviation):
    year_names = {
        "'23": 2023, "'21": 2021, "'22": 2022, "'20": 2020
    }

    return year_names.get(abbreviation, None)


symbol = 'TCS'
csv_filename = f"{symbol}_stock_data.csv"
existing_data = pd.read_csv(csv_filename)

for key, value in p_values.items():
    day, month, year_value = key.split()
    month_number_value = month_number(month)
    year_number_value = year_number(year_value)
    #print(year_number_value,month_number_value)
    for i, date_str in existing_data['Date'].items():
        yeare, monthe, daye = date_str.split('-')#code not work then check the format of date split sometimes gives error
        monthe = monthe.lstrip('0')  # Remove leading zero
        #print(daye,monthe)
        if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(month_number_value):
            #print(day, daye, yeare, year_number_value, monthe, month_number_value, value)
            existing_data.at[i, f"{name_percentage}"] = value

print(f'{name_percentage} Data appended to columns in {csv_filename}')

for key, value in d_values.items():
    day, month, year_value = key.split()
    month_number_value = month_number(month)
    year_number_value = year_number(year_value)
    #print(year_number_value,month_number_value)
    for i, date_str in existing_data['Date'].items():
        yeare, monthe, daye = date_str.split('-')
        monthe = monthe.lstrip('0')  # Remove leading zero
        #print(daye,monthe)
        if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(month_number_value):
            #print(day, daye, yeare, year_number_value, monthe, month_number_value, value)
            existing_data.at[i, f"{name_delivery}"] = value

print(f'{name_delivery} Data appended to columns in {csv_filename}')

for key, value in t_values.items():
    day, month, year_value = key.split()
    month_number_value = month_number(month)
    year_number_value = year_number(year_value)
    #print(year_number_value,month_number_value)
    for i, date_str in existing_data['Date'].items():
        yeare, monthe, daye = date_str.split('-')
        monthe = monthe.lstrip('0')  # Remove leading zero
        #print(daye,monthe)
        if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(month_number_value):
            #print(day, daye, yeare, year_number_value, monthe, month_number_value, value)
            existing_data.at[i, f"{name_trade}"] = value

existing_data.to_csv(csv_filename, index=False)  # Save the updated DataFrame to the CSV file
print(f'{name_delivery} Data appended to columns in {csv_filename}')
