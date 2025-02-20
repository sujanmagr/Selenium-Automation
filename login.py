# script to login into a login page of saucedemo with certain users and password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://www.saucedemo.com/"
driver.get(url)

# Close the browser after a short delay
driver.maximize_window()
time.sleep(2)

#enter username and password
usernames=["standard_user","problem_user", "sujan", "performance_glitch_user"]
for users in usernames:
    #find the username and password field by id
    username=driver.find_element(By.ID, "user-name")
    password=driver.find_element(By.ID, "password")
    login=driver.find_element(By.ID, "login-button")
    username.clear()
    password.clear()
    username.send_keys(users)
    password.send_keys("secret_sauce")
    time.sleep(2)
    login.click()

    title=driver.current_url
    if (title=="https://www.saucedemo.com/inventory.html"):
        time.sleep(3)
        print("login successful")
        menu=driver.find_element(By.ID, "react-burger-menu-btn")
        menu.click()
        time.sleep(2)
        logout=driver.find_element(By.ID, "logout_sidebar_link")
        logout.click()
    else:
        print("login unsuccessful")

    
        



# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# time.sleep(2)
# login.click()

# title=driver.current_url
# if (title=="https://www.saucedemo.com/inventory.html"):
#     print("login successful")
# else:
#     print("login unsuccessful")


# title=driver.title
# print(title)
time.sleep(5)
driver.quit()