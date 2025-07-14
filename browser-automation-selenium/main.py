from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service('edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://demoqa.com/login')
driver.quit()