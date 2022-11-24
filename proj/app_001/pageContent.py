import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

url = "https://www.facebook.com"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
email = driver.find_element_by_name("email")
pswrd = driver.find_element_by_name("pass")
email.send_keys(username)
time.sleep(1)
pswrd.send_keys(password)
time.sleep(3)
email.submit()
time.sleep(10)
driver.get("https://mbasic.facebook.com/profile")

pageContent = driver.page_source

soup = BeautifulSoup(pageContent, "html.parser")
