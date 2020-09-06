from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//img[@id = 'treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_xpath("//input[@id = 'answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_xpath("//input[@id = 'robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_xpath("//input[@id = 'robotsRule']")
    radio.click()
    button = browser.find_element_by_xpath("//button[@type = 'submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
