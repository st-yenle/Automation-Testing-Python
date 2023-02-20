# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22
import time

from pytest_bdd import scenarios, given, parsers
from src.pages.login import LoginPage
from src.pages.common import *

scenarios('../features/login.feature')


@then(parsers.parse('The page contain "{text}"'))
def check_page_contain_text(browser, text):
    assert LoginPage(browser).find_contain_text(text)


@then(parsers.parse('The page displays "{text}"'))
def check_page_display(browser, text):
    assert LoginPage(browser).is_displayed(text)


@when(parsers.parse('I enter a username of "{username}"'))
def enter_username(browser, username):
    LoginPage(browser).enter_username(username)
    # time.sleep(1)


@when(parsers.parse('I enter a password of "{password}"'))
def enter_password(browser, password):
    LoginPage(browser).enter_password(password)
    # time.sleep(1)


@when(parsers.parse('I click on login button'))
def click_login(browser):
    LoginPage(browser).click_login_button()


@then(parsers.parse('The page title is "{title}"'))
def check_page_title(browser, title):
    assert LoginPage(browser).get_page_title() == title



