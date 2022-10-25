from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# browser = webdriver.Chrome()
# browser = webdriver.Chrome('C:/DRIVERS/chromedriver.exe')
browser = webdriver.Chrome()


# browser.get('http://www.yahoo.com')
browser.get("http://www.google.com")
time.sleep(2)

# assert 'Yahoo' in browser.title
assert 'Google' in browser.title


time.sleep(5)

my_element = browser.find_element(By.CLASS_NAME, "QS5gu")

# elem = browser.find_element_by_name('p')
# elem.send_keys('seleniumhq' + Keys.RETURN)


