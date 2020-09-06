from selenium import webdriver
import time
import os

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input[name = 'firstname']")
    first_name.send_keys("Kirill")
    last_name = browser.find_element_by_css_selector("input[name = 'lastname']")
    last_name.send_keys("Petriashvili")
    email = browser.find_element_by_css_selector("input[name = 'email']")
    email.send_keys("kirillpetriashvili@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'yes.txt')
    attach = browser.find_element_by_css_selector("#file")
    attach.send_keys(file_path)
    button = browser.find_element_by_css_selector("button[type = 'submit']").click()

finally:
    time.sleep(30)
    browser.quit()

