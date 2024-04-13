import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import allure

from base.BaseClass import Base
from utilites.Logger import Logger

class Login_page(Base):

    url = 'https://dodopizza.ru/tver/'

    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser



    #locators
    select_product = "//div[@class='grid']//li[@class='sc-1uavg9b-4 eIDeiS']"
    select_pizza = "//main[@class='sc-1tpn8pe-0 dszYBt']//img[@src='https://dodopizza-a.akamaihd.net/static/Img/Products/d7bbbc4c74af442e8b9b3ea2faf3c941_138x138.jpeg']"
    peperoni = "//button[@class='sc-x3sf4h-1 dLPczQ']//img[@src='https://dodopizza-a.akamaihd.net/static/Img/Ingredients/bd896a42a5b44169ae9dfdc2573c34f2.png']"
    chicken = "//button[@class='sc-x3sf4h-1 dLPczQ']//img[@src='https://dodopizza-a.akamaihd.net/static/Img/Ingredients/000D3A39D824A82E11E9AFA5B328D35A']"
    click_to_cart = "//div[@class='sc-8hteo7-17 hUiIRM']//button[@data-testid='button_add_to_cart']"
    button_address = "//div[@class='sc-1putgs4-0 izKysX']//button[@type='button']"
    enter_add = "//div[@class='sc-1qbfx43-0 dDnYuS']//input[@id='animated-input-1']"
    location_button = "//button[@class='item__action item__action_button']"
    add_p = "//div[@class='sc-1qbfx43-0 dDnYuS control-medium']//input[@id='animated-input-2']"
    add_kd = "//div[@class='sc-1qbfx43-0 dDnYuS control-medium']//input[@id='animated-input-3']"
    add_floor = "//div[@class='sc-1qbfx43-0 dDnYuS control-medium']//input[@id='animated-input-4']"
    add_kv = "//div[@class='sc-1qbfx43-0 dDnYuS control-medium']//input[@id='animated-input-5']"
    button_click = "//button[@type='submit']"


    #Getters

    def get_select_product(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product))))

    def get_select_pizza(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pizza))))

    def get_peperoni(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.peperoni))))

    def get_chicken(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.chicken))))

    def get_click_to_cart(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_to_cart))))

    def get_button_address(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_address))))

    def get_enter_add(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_add))))

    def get_click_location(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.location_button)))) #находим кнопку, т.е. то что у тебя подсказка вылезла

    def get_add_p(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_p))))

    def get_add_kd(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_kd))))

    def get_add_floor(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_floor))))

    def get_add_kv(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_kv))))

    def get_button_click(self):
        return (WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_click))))

    #Actions

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    def click_select_pizza(self):
        self.get_select_pizza().click()
        print("Click select pizza")

    def click_peperoni(self):
        self.get_peperoni().click()
        print("Click peperoni")

    def click_chicken(self):
        self.get_chicken().click()
        print("Click chicken ")

    def click_click_to_cart(self):
        self.get_click_to_cart().click()
        print("Click to cart ")

    def click_button_address(self):
        self.get_button_address().click()
        print("Click to address ")

    def input_enter_add(self, enter_add):
        self.get_enter_add().send_keys(enter_add)
        print("Input address")


    def click_location_button(self):
        self.get_click_location().click() #кликаем

    def input_add_p(self, add_p):
        self.get_add_p().send_keys(add_p)
        print("Input entrance")

    def input_add_kd(self, add_kd):
        self.get_add_kd().send_keys(add_kd)
        print("Input code home")

    def input_add_floor(self,add_floor):
        self.get_add_floor().send_keys(add_floor)
        print("Input floor")

    def input_add_kv(self, add_kv):
        self.get_add_kv().send_keys(add_kv)
        print("Input flat")

    def click_button_click(self):
        self.get_button_click().click()
        print("Click button")


    #Metods
    def autorization(self):
        #with allure.step("add_to_cart"):
            #Logger.add_start_step(method="autorization")
            self.browser.get(self.url)
            self.browser.maximize_window()
            self.click_select_product()
            time.sleep(2)
            self.click_select_pizza()
            time.sleep(2)
            self.click_peperoni()
            time.sleep(2)
            self.click_chicken()
            time.sleep(2)
            self.click_click_to_cart()
            time.sleep(2)
            self.click_button_address()
            time.sleep(2)
            self.input_enter_add("Тверь, Оборонная улица,10 ")
            time.sleep(5)
            self.click_location_button()
            time.sleep(10)
            self.input_add_p("4")
            time.sleep(2)
            self.input_add_kd("134")
            time.sleep(2)
            self.input_add_floor("4")
            time.sleep(2)
            self.input_add_kv("134")
            time.sleep(2)
            self.click_button_click()
            time.sleep(5)
            #Logger.add_end_step(url=self.browser.current_url, method="autorization")



