import pytest

@pytest.fixture
def browser():
    print("Browser started")


@pytest.fixture
def login_page(browser):
    print("Login page opened")


@pytest.fixture
def user_creds():
    print("User achieved")
    return "username", "password"



def test_login(login_page, user_creds):
    username, password = user_creds
    assert username == "username"
    assert password == "password"
