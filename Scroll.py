from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage to test
url="https://merolagani.com/CompanyDetail.aspx?symbol=ADBL"
driver.get(url)

# Close the browser after a short delay
driver.maximize_window()
# Calculate Height
page_height=driver.execute_script("return document.body.scrollHeight")
scroll_speed=500
scroll_iteration=int(page_height/scroll_speed)
#loop to perform scroll
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});") 
    time.sleep(4)

title=driver.title
print(title)
time.sleep(5)
driver.quit()