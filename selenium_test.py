from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('http://www.google.com')

q = driver.find_element(By.NAME, 'q')
q.send_keys('Black Hat Data Wrangling')
q.submit()

