from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import credentials
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


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

time.sleep(5)

driver.get("https://www.facebook.com/groups/235385084142732")

for i in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")

posts = soup.find_all("div", {
    "class": "du4w35lb l9j0dhe7"})

result = []
for post in posts:
    content = post.find("span", {
                        "class": "d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d9wwppkn iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"})
    description = content.getText() if content else "no content"
    result.append(description)

print(result)
