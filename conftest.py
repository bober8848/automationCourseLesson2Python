import pytest
from selene import browser, be, have
import time


@pytest.fixture(scope="session")
def fake_browser():
    print("\nBrowser started")

    yield

    print("\nClosing browser")


@pytest.fixture(scope="session")
def setup_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 900

    _ = browser.driver
    time.sleep(2)

    yield

    browser.quit()