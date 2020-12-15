import pytest
from urllib.request import urlopen
from selenium import webdriver
from PIL import Image

expected_logo = Image.open("logo.jpg")
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("http://automationpractice.com/index.php")
logo = driver.find_element_by_css_selector(".logo")
src = logo.get_attribute('src')
actual_logo = Image.open(urlopen(src))

assert actual_logo == expected_logo
