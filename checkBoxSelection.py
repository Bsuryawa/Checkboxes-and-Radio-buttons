import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window
#Checkbox handling
checkboxes = driver.find_elements(By.XPATH, "//input[@type ='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        checkbox.is_selected()
        break
time.sleep(2)
#radio button handling
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobuttons))
radiobuttons[2].click()
radiobuttons[2].is_selected()

driver.close()


