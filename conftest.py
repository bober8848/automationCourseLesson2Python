import pytest
import undetected_chromedriver as uc
from selene import browser, be, have
import time


browser.config.driver_manager_enabled = False


@pytest.fixture(scope="session")
def fake_browser():
    print("\nBrowser started")

    yield

    print("\nClosing browser")


@pytest.fixture(scope="session")
def setup_browser():
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1200,800")

    driver = uc.Chrome(options=options)

    browser.config.driver = driver

    yield

    driver.quit()