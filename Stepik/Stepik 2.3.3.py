# Подтверждение Alert
# alert = browser.switch_to.alert
# alert.accept()
# Получение текста
# alert = browser.switch_to.alert
# alert_text = alert.text
# Подтверждение Confirm
# confirm = browser.switch_to.alert
# confirm.accept()
# Отмена Confirm
# confirm.dismiss()
# Запись в Prompt и подтверждение
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type = 'submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button[type = 'submit']").click()

finally:
    time.sleep(30)
    browser.quit()





