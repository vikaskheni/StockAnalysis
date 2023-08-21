from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def scrape_and_append_data(symbol, url):
    webdriver_path = 'C:/Users/Vikas/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

    # Initialize the Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(webdriver_path), options=chrome_options)

    # Open the desired URL
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
        for i in range(1, 25):  # Skip the header row
            cols = rows[i].find_elements(By.TAG_NAME, "td")
            date = cols[0].text
            traded = cols[1].text
            t_values[date] = traded

            nse_delivery = cols[2].text
            d_values[date] = nse_delivery

            percent_delivery = cols[3].text
            p_values[date] = percent_delivery
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

    csv_filename = f"{symbol}_stock_data.csv"
    existing_data = pd.read_csv(csv_filename)

    for key, value in p_values.items():
        day, month, year_value = key.split()
        month_number_value = month_number(month)
        year_number_value = year_number(year_value)
        for i, date_str in existing_data['Date'].items():
            yeare, monthe, daye = date_str.split('-')
            monthe = monthe.lstrip('0')
            if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(
                    month_number_value):
                existing_data.at[i, f"{name_percentage}"] = value

    print(f'{name_percentage} Data appended to columns in {csv_filename}')

    for key, value in d_values.items():
        day, month, year_value = key.split()
        month_number_value = month_number(month)
        year_number_value = year_number(year_value)
        for i, date_str in existing_data['Date'].items():
            yeare, monthe, daye = date_str.split('-')
            monthe = monthe.lstrip('0')
            if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(
                    month_number_value):
                existing_data.at[i, f"{name_delivery}"] = value

    print(f'{name_delivery} Data appended to columns in {csv_filename}')

    for key, value in t_values.items():
        day, month, year_value = key.split()
        month_number_value = month_number(month)
        year_number_value = year_number(year_value)
        for i, date_str in existing_data['Date'].items():
            yeare, monthe, daye = date_str.split('-')
            monthe = monthe.lstrip('0')
            if int(daye) == int(day) and int(yeare) == int(year_number_value) and int(monthe) == int(
                    month_number_value):
                #print(daye,day,monthe,month_number_value,yeare,year_number_value)
                existing_data.at[i, f"{name_trade}"] = value

    existing_data.to_csv(csv_filename, index=False)
    print(f'{name_trade} Data appended to columns in {csv_filename}')


# Usage
symbol = 'TCS'

url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/29-Apr-2021/"
url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/28-Feb-2022/"
url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/27-Jan-2022/"
url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/24-Dec-2022/"
#scrape_and_append_data(symbol, url)


def month_number(abbreviation):
    month_names = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    return month_names.get(abbreviation, None)


for i in range(2020, 2024):
    if i == 2020:
        for j in range(6, 13):
            month_value = month_number(j)
            day = "01"
            formatted_date = "{}-{}-{}".format(day, month_value, i)
            url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/{}".format(formatted_date)
            print(url)
            scrape_and_append_data(symbol, url)
    else:
        if i == 2021 or i == 2022:
            for j in range(1, 13):
                month_value = month_number(j)
                day = "01"
                formatted_date = "{}-{}-{}".format(day, month_value, i)
                url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/{}".format(formatted_date)
                print(url)
                scrape_and_append_data(symbol, url)
        elif i == 2023:
            for j in range(1, 8):
                month_value = month_number(j)
                day = "01"
                formatted_date = "{}-{}-{}".format(day, month_value, i)
                url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/{}".format(formatted_date)
                print(url)
                scrape_and_append_data(symbol, url)

            url = "https://trendlyne.com/equity/delivery-analysis/1372/TCS/tata-consultancy-services-ltd/NSE/14-Aug-2023/"
            print(url)
            scrape_and_append_data(symbol, url)


print("Data has Stored into CSV")





