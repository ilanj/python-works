import os
from selenium import webdriver

chromedriver = "C:\\Users\\auxouser\\PycharmProjects\\demo\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()
