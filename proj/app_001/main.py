import selenium
from selenium import webdriver
# from selenium.webdriver import excepted_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
from time import sleep

from bs4 import BeautifulSoup

# import pandas as pd

chrome_options = Options()

chrome_options.add_argument('--disable-notifications')

content_list = []
time_list = []
name_list = []

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)

# cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _4jy3 _4jy2 selected"]')))

email = driver.find_element_by_id("email")
email.send_keys("plamkug@hotmail.com")
password = driver.find_element_by_id("pass")
password.send_keys("Plam0909634105")
sleep(1)
login = driver.find_element_by_name("login")
login.click()
sleep(2)
driver.get("https://www.facebook.com/groups/292346075507183")
sleep(4)

