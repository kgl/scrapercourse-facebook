from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import credentials
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)

driver.get("https://www.facebook.com/")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.submit()

time.sleep(60)
