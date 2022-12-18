# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22

from .base import BasePage
from pytest_bdd import given, then, parsers, when


@given(parsers.parse('I have navigated to the "{page_name}" page'))
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@when(parsers.parse('I quit browser'))
def quit(browser):
    browser.quit()
