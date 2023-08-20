from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time



# Set the path to your Chrome WebDriver executable
webdriver_path = 'C:/Users/Vikas/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Initialize the Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_path), options=chrome_options)

# Open the desired URL
url = "https://www.nseindia.com/report-detail/eq_security"
driver.get(url)


symbol_input = driver.find_element(By.ID, "hsa-symbol").send_keys("TCS")
time.sleep(2)
symbol_input2 = driver.find_element(By.ID, "hsa-symbol_listbox").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
symbol_input2.send_keys(Keys.ENTER)
time.sleep(2)



custom_button = driver.find_element(By.XPATH, "//span[@id='custom']")
custom_button.click()

wait = WebDriverWait(driver, 10)

# Wait for the date picker element to be clickable
wait = WebDriverWait(driver, 10)
date_picker = wait.until(EC.element_to_be_clickable((By.ID, "pbc-startDate")))

# Remove the readonly attribute using JavaScript
driver.execute_script("arguments[0].removeAttribute('readonly');", date_picker)

# Set the value of the date picker using JavaScript
js_code = "arguments[0].value = '19-06-2023';"
driver.execute_script(js_code, date_picker)

wait = WebDriverWait(driver, 10)

# Wait for the date picker element to be clickable
wait = WebDriverWait(driver, 10)
date_picker = wait.until(EC.element_to_be_clickable((By.ID, "pbc-endDate")))

# Remove the readonly attribute using JavaScript
driver.execute_script("arguments[0].removeAttribute('readonly');", date_picker)

# Set the value of the date picker using JavaScript
js_code = "arguments[0].value = '19-08-2023';"
driver.execute_script(js_code, date_picker)

wait = WebDriverWait(driver, 10)
custom_button_go = driver.find_element(By.XPATH, "//button[contains(text(),'GO')]")

custom_button_go.click()



# Wait for the table to load
table_wait = WebDriverWait(driver, 50)
table = table_wait.until(EC.presence_of_element_located((By.ID, "hsaTable")))

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")
if(rows):
    print("rows done")
# Initialize a list to store the DATE column data
date_column_data = []
"""
# Loop through the rows (start from index 1 to skip the header row)
for row in rows[1:]:
    # Find the DATE cell in each row
    date_cell = row.find_element(By.XPATH, "//th[@id='Date']")  # Adjust the column index if needed

    # Get the text from the DATE cell and append it to the list
    date_column_data.append(date_cell.text)

# Print the data from the DATE column
for date in date_column_data:
    print(date)
"""
# Close the browser
driver.quit()


