from selenium.webdriver.common.by import By


class GoogleResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, ".MjjYud")
    SEARCH_INPUT_RESULT = (By.CSS_SELECTOR, "#APjFqb")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_RESULT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

