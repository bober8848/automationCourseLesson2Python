import pytest

@pytest.fixture
def browser():
    print("\nBrowser started")

    yield

    print("\nClosing browser")


@pytest.fixture
def login_page(browser):
    print("\nLogin page opened")


@pytest.fixture
def user_creds():
    print("\nUser achieved")
    return "username", "password"



def test_login(login_page, user_creds):
    username, password = user_creds
    assert username == "username"
    assert password == "password"

