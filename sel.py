# import necessary module for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#for microsoft edge
# import time
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


# Open a webpage to test
url="https://merolagani.com/"
driver.get(url)
time.sleep(3)
#maximize the window as selenium always open the browser in a half window
driver.maximize_window()
title=driver.title #just to print the title of the webpage
print(title)
# Close the browser after a short delay
time.sleep(5)
driver.quit()
