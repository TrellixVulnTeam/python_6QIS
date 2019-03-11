from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw1").clear
    driver.find_element_by_css_selector("#kw").send_keys("selenium")
    driver.find_element_by_css_selector("#su").submit()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(3)
driver.quit()