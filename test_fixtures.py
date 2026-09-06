import pytest


@pytest.fixture
def login_page(setup_browser):
    print("\nLogin page opened")


@pytest.fixture
def user_creds():
    print("\nUser achieved")
    return "username", "password"


def test_login(login_page, user_creds):
    username, password = user_creds
    assert username == "username"
    assert password == "password"
    print("\nUser logged in")


def test_logout(login_page, user_creds):
    username, password = user_creds
    assert username == "username"
    assert password == "password"
    print("\nUser logged out")