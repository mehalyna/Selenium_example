import json
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from src.pages.result import GoogleResultPage
from src.pages.search import GoogleSearchPage


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialize the TestProject WebDriver instance
    if config['browser'] == 'Firefox':
        browser = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        browser = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = ChromeOptions()
        opts.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    browser.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield browser

    # Quit the WebDriver instance for the cleanup
    browser.quit()


@pytest.fixture
def search_page(browser):
    return GoogleSearchPage(browser)


@pytest.fixture
def result_page(browser):
    return GoogleResultPage(browser)

