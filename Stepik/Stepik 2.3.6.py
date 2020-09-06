# Узнаем имя новой страницы по индексу массива
# new_window = browser.window_handles[1]
# Переход на другую страницу по имени
# browser.switch_to.window(new_window)
# Сохранение первой страницы в переменную с помощью индекса массива для возврата
# first_window = browser.window_handles[0]


from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type = 'submit']").click()
    new_window = browser.window_handles[1]
    window = browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    button_click = browser.find_element_by_css_selector("button[type = 'submit']").click()

finally:
    time.sleep(30)
    browser.quit()

