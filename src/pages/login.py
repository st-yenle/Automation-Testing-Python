# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22

from selenium import webdriver
from selenium.webdriver.common.by import By
from .base import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        self.browser: webdriver.Chrome = browser

    def get_page_title(self):
        return self.browser.title

    def find_contain_text(self, text):
        self.browser.find_element(by=By.XPATH, value=f"//*[contains(text(), '{text}')]")
        return True

    def is_displayed(self, text):
        self.browser.find_element(By.ID, text).is_displayed()
        return True

    def enter_username(self, username):
        box_text = self.browser.find_element(by=By.ID, value='login_field')
        box_text.send_keys(username)
        self.browser.implicitly_wait(10)

    def enter_password(self, password):
        box_text = self.browser.find_element(by=By.ID, value='password')
        box_text.send_keys(password)
        self.browser.implicitly_wait(10)

    def click_login_button(self):
        self.browser.find_element(by=By.NAME, value='commit').click()
        self.browser.implicitly_wait(10)


