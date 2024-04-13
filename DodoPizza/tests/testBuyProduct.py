import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import allure

from pages.LoginPage import Login_page



class TestBuyProduct():
    @allure.description("Test select product")
    def test_select_product(self):
        browser = webdriver.Firefox()

        print("Start test")

        login = Login_page(browser)
        login.autorization()

        print("GOOD")

