import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="session")
def setup():
    browser.config.browser_name = "chrome"
    browser.config.base_url = "https://www.google.com/ncr "
    browser.config.window_height = '768'
    browser.config.window_width = '1366'
    browser.open('https://www.google.com')


@pytest.fixture(scope="function")
def clear_search_field():
    browser.element('[name="q"]').clear()


def test_search_results_successful(setup, clear_search_field):
    browser.element('button+button').click()  # эта строка закрывает GDPR поп-ап(нажимает Accept all)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_results_unsuccessful(setup, clear_search_field):
    browser.element('[name="q"]').should(be.blank).type('j//nbn1231m==nm!!--a343n-').press_enter()
    browser.element('.card-section').should(
        have.text('Na váš předmět vyhledávání - j//nbn1231m==nm!!--a343n- - nebyl nalezen žádný odkaz.'))
