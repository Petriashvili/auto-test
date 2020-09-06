from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    result = int(x) + int(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    button = browser.find_element_by_css_selector("button[type = 'submit']").click()

finally:
    time.sleep(30)
    browser.quit()
