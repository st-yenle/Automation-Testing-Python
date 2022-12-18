# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22

from selenium.webdriver.common.by import By
import selenium


class BasePage:
    BASE_URL = "http://github.com"
    PAGE_URLS = {
        "home": BASE_URL + "/",
        "login": BASE_URL + "/login"
    }

