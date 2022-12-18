# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22

from selenium import webdriver
from .base import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        self.browser: webdriver.Chrome = browser

    def get_page_title(self):
        return self.browser.title
