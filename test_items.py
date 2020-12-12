import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_buttonAdd(browser): #принимаем экземпляр браузера
    browser.get(link)
    browser.implicitly_wait(5) #button.btn.btn-lg.btn-primary
    time.sleep(30)
    add_btn = browser.find_element_by_class_name('btn-primary')
    assert  add_btn, 'кнопка существует'




