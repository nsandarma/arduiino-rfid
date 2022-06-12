from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def open_portal(username,password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    global driver
    driver = webdriver.Chrome('/home/sandy/chromedriver')
    driver.maximize_window()
    driver.get('http://portal.unimal.ac.id/')

    username = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(username)
    password = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password)

    #enter username and password
    
    # username.clear()
    # username.send_keys(f'{u}')
    # password.clear()
    # password.send_keys(f'{p}')

    driver.find_element_by_class_name("button").click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "button"))).click()

#target the login button and click it
# button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!


