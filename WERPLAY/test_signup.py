import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_css_selector(".login").click()
driver.find_element_by_css_selector("#email_create").send_keys("abcefghi111@gmail.com")
driver.find_element_by_css_selector("#SubmitCreate > span:nth-child(1)").click()
driver.find_element_by_css_selector("#id_gender1").click()
driver.find_element_by_css_selector("#customer_firstname").send_keys("a")
driver.find_element_by_css_selector("#customer_lastname").send_keys("b")
driver.find_element_by_css_selector("#passwd").send_keys("abc123")
Select(driver.find_element_by_css_selector("#days")).select_by_value("14")
Select(driver.find_element_by_css_selector("#months")).select_by_value("8")
Select(driver.find_element_by_css_selector("#years")).select_by_value("1994")
driver.find_element_by_css_selector("#newsletter").click()
driver.find_element_by_css_selector("#optin").click()
driver.find_element_by_css_selector("#company").send_keys("weRplay")
driver.find_element_by_css_selector("#address1").send_keys("Islamabad")
driver.find_element_by_css_selector("#address2").send_keys("Islamabad")
driver.find_element_by_css_selector("#city").send_keys("Islamabad")
Select(driver.find_element_by_css_selector("#id_state")).select_by_value("1")
driver.find_element_by_css_selector("#postcode").send_keys("44000")
driver.find_element_by_css_selector("#other").send_keys("N/A")
driver.find_element_by_css_selector("#phone").send_keys("+92-311-1234567")
driver.find_element_by_css_selector("#phone_mobile").send_keys("12233")
driver.find_element_by_css_selector("#alias").clear()
driver.find_element_by_css_selector("#alias").send_keys("abc")
driver.find_element_by_css_selector("#submitAccount > span:nth-child(1)").click()

greet_mesg = driver.find_element_by_css_selector(".info-account").text

assert "Welcome" in greet_mesg
