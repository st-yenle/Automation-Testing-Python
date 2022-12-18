# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22

from pytest_bdd import scenarios, given, parsers
from src.pages.home import HomePage
from src.pages.common import *
import time

scenarios('../features/home_page.feature')


@then(parsers.parse('The page title is "{page_title}"'))
def check_page_title(browser, page_title):
    time.sleep(1)
    assert page_title == HomePage(browser).get_page_title()



