import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Replace 'path_to_webdriver' with the actual path to your web driver executable (e.g., chromedriver.exe for Chrome)
driver_path = 'path_to_webdriver'
driver = webdriver.Chrome(executable_path="chromedriver")

driver.get("https://www.tendertiger.com/AdvanceTenderSearch.aspx?GemTenders=True")
time.sleep(3)

# Click the "Load More" button ten times
for _ in range(9):
    try:
        # Replace 'load_more_xpath' with the XPath of the "Load More" button on the webpage
        load_more_xpath = "/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[5]/center/input"

        # Wait for the "Load More" button to be clickable
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, load_more_xpath))
        )

        # Click the "Load More" button
        load_more_button.click()

    except Exception as e:
        print("Error: ", str(e))
        break

# Initialize Google Sheets credentials and open the sheet
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("auth.json")
file = gspread.authorize(credentials=credentials)

sheet = file.open("Data")
sheet = sheet.sheet1

api_requests_counter = 0
# Scraping and updating data to the Excel sheet
for i in range(1, 102):
    Department_name = driver.find_element(By.XPATH,
                                          f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[2]/td/b").text
    Services = driver.find_element(By.XPATH,
                                   f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[3]/td").text
    Location = driver.find_element(By.XPATH,
                                   f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[1]").text
    ApproxValue = driver.find_element(By.XPATH,
                                      f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[2]/i").text
    Deadline = driver.find_element(By.XPATH,
                                   f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[3]").text

    sheet.update_acell('A' + str(i + 1), Department_name)
    sheet.update_acell('B' + str(i + 1), Services)
    sheet.update_acell('C' + str(i + 1), Location)
    sheet.update_acell('D' + str(i + 1), ApproxValue[4:])
    sheet.update_acell('E' + str(i + 1), Deadline[12:])

    api_requests_counter += 1

    print(api_requests_counter)

    if api_requests_counter == 11:
        print("Pausing for 45 seconds to comply with API rate limits...")
        time.sleep(45)  # Pause for 30 seconds

        # Reset the API requests counter
        api_requests_counter = 0