from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

edge_options = Options()
edge_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {"download.default_directory": download_path}
edge_options.add_experimental_option("prefs", prefs)

service = Service('edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(options=edge_options, service=service)
driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

username_field.send_keys('test54321')
password_field.send_keys('Password@123')
driver.execute_script("arguments[0].click();", login_button)

elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

fullname_field.send_keys('John Smith')
email_field.send_keys('John5431@gmail.com')
current_address_field.send_keys('John Smith 100, NY, USA')
permanent_address_field.send_keys('John Smith 100, NY, USA')
driver.execute_script("arguments[0].click();", submit_button)


upload_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_button.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

driver.quit()