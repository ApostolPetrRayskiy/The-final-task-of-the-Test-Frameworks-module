import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket(browser):
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 200);")
    time.sleep(3)
    button = browser.find_element_by_css_selector('.btn.btn-lg')
    assert True, 'Button does not exist'
    

