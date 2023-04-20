# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

PHRASE = "SoftServe"
ROUTE = 'https://www.google.com'


def test_google_search():
    driver_chrome = webdriver.Chrome()
    driver = driver_chrome
    driver_chrome.maximize_window()
    driver_chrome.get(ROUTE)

    # Perform search operation
    elem = driver_chrome.find_element(By.NAME, "q")
    elem.send_keys(PHRASE)
    elem.submit()

    # Check if found
    link_divs = driver_chrome.find_elements(By.CSS_SELECTOR, ".MjjYud")
    assert len(link_divs) > 0

    # Check if phrase
    xpath = f"//*[@id='rso']//*[contains(text(),{PHRASE})]"
    phrase_results = driver_chrome.find_elements(By.XPATH, xpath)
    assert len(phrase_results) > 1

    # Close the browser.
    driver.close()
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pytest.test_google_search()

