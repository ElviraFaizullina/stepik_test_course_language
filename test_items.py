from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest


class TestRegistration:
    def test_registration1(self, browser):
        # open browser
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)

        # find basket button
        button_basket = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        time.sleep(30)
        assert button_basket, "The button was not found"
