# -*- coding: utf-8 -*-
# @Organization :  ST
# @Author       :  Yen Le T. N.
# @Time         :  11/20/22
import time

from _pytest.fixtures import SubRequest
import pytest
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

pwd = os.getcwd()
pwd = os.path.dirname(pwd)
pwd = os.path.dirname(pwd)


def config():
    browsers = ['Chrome', 'Firefox']
    # Read config file

    cfg = pwd + '/config.json'
    with open(cfg) as config_file:
        cfg = json.load(config_file)
    assert isinstance(cfg['headless'], bool)
    assert isinstance(cfg['implicit_wait'], int)
    assert cfg['implicit_wait'] > 0
    return cfg


# Create Selenium WebDriver with config to control my website
def browser_func(config):
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    b.implicitly_wait(config['implicit_wait'])
    return b


config = config()
browser_obj = browser_func(config)


@pytest.fixture
def browser(request: SubRequest):
    """
    Browser is a fixture, is called at top scenerio at top sceniro
    """
    # browser_obj = browser_func(config)
    yield browser_obj  # return value without change address memory of object


@pytest.fixture(scope='session', autouse=True)
def my_setup(request):
    # Setup before test: Begin code
    def fin():
        # Setup after all test
        time.sleep(2)
        browser_obj.quit()
    request.addfinalizer(fin)
