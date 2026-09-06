import pytest
from selene import browser, be,have

@pytest.fixture
def search_page(setup_browser):
    browser.open("https://google.com")


def test_search_positive(search_page):
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('QA.GURU: Курсы тестировщиков'))


def test_search_negative(search_page):
    browser.element('[name="q"]').should(be.blank).type("'tal'kfnsdodvcnzc;zsmvfcoisefhnasfd;ma;fdma;lfdm").press_enter()
    browser.element('html').should(have.text('не найдено'))