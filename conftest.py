import pytest


@pytest.fixture(scope="session")
def browser():
    print("\nBrowser started")

    yield

    print("\nClosing browser")