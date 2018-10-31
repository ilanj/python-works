from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox("C:\\Users\\auxouser\\PycharmProjects\\demo\\driver\\geckodriver.exe")
driver.get("http://www.python.org")