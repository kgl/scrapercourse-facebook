from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import credentials

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.submit()

time.sleep(60)
