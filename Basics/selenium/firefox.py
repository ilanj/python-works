import os
from selenium import webdriver

geckodriver = ("C:\\Users\\auxouser\\PycharmProjects\\demo\\driver\\geckodriver.exe")
os.environ["webdriver.gecko.driver"] = geckodriver
driver = webdriver.Firefox(geckodriver)
driver.get("http://stackoverflow.com")
driver.quit()