import os
from selenium import webdriver

geckodriver = "C:\\Users\\auxouser\\PycharmProjects\\demo\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver
driver = webdriver.Firefox(executable_path=r'C:\\Users\\auxouser\\PycharmProjects\\demo\\geckodriver.exe')
driver.get("http://toolsqa.com/automation-practice-form/")
driver.get("http://toolsqa.com/automation-practice-form/");
driver.find_element_by_name("firstname").send_keys("ila")
driver.find_element_by_name("lastname").send_keys("j")
driver.find_element_by_id("sex-0").click()
driver.find_element_by_id("exp-3").click()
driver.find_element_by_xpath("//*[@id='datepicker']").send_keys("2018-05-05")
#driver.quit()