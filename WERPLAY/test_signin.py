import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_names=[]
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_css_selector(".login").click()
driver.find_element_by_css_selector("#email").send_keys("abcefghi111@gmail.com")
driver.find_element_by_css_selector("#passwd").send_keys("abc123")
driver.find_element_by_css_selector("#SubmitLogin > span:nth-child(1)").click()
driver.find_element_by_css_selector(".sf-menu > li:nth-child(2) > a:nth-child(1)").click()
driver.find_element_by_css_selector("#subcategories > ul:nth-child(2) > li:nth-child(3) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click()
products = driver.find_elements_by_css_selector("ul[class='product_list grid row'] > li")
driver.execute_script("window.scrollTo(0,500);")
for product in products:

    expected_names.append(product.find_element_by_class_name("product-name").text)
    hover = WebDriverWait(product,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='right-block']")))
    ActionChains(driver).move_to_element(hover).perform()
    time.sleep(1)
    product.find_element_by_css_selector("div[class='right-block'] > div[class='button-container'] > a[title='Add to cart'] > span").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".continue > span:nth-child(1)").click()


driver.execute_script("window.scrollTo(500,0);")
driver.find_element_by_css_selector("a[title='View my shopping cart']").click()
name_in_cart = driver.find_elements_by_css_selector("div[id='center_column'] > div[id='order-detail-content'] > table[id='cart_summary'] > tbody > tr > td[class='cart_description'] > p > a")
actual_names = []
for name in name_in_cart:
    actual_names.append(name.text)

assert len(actual_names) == len(expected_names)
assert all([a == b for a, b in zip(actual_names, expected_names)])