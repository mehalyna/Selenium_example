import pytest


@pytest.mark.parametrize('phrase', ['Warsaw', 'Gliwice', 'Krakow'])
def test_basic_google_search(search_page, result_page, phrase):
    # Given the Google home page is displayed
    search_page.load()

    # When the user searches for the phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    assert phrase in result_page.title()

