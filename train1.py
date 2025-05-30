from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def web_driver():
    options = webdriver.ChromeOptions()
    # Uncomment the next line to run headless (no browser window)
    options.add_argument('--headless')
    options.add_argument('--start-maximized')  # maximized window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Create driver and open the target URL
driver = web_driver()
driver.get('https://eticket.railway.gov.bd/booking/train/search?fromcity=Dhaka&tocity=Rajshahi&doj=08-Jun-2025&class=S_CHAIR')

# Wait for the page to load (optional sleep or use WebDriverWait)
time.sleep(5)

# Print entire page HTML
# print(driver.page_source)
with open("page_output.txt", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

while True:
    key = input("Type 'q' and press Enter to quit: ")
    if key.lower() == 'q':
        break

elements = driver.find_elements(By.CSS_SELECTOR, "div.available-text.open-for-all.ng-star-inserted")
# Extract text and write to a file
with open("div_texts.txt", "w", encoding="utf-8") as f:
    for el in elements:
        f.write(el.text + "\n")
        
# Optional: Close browser
driver.quit()
