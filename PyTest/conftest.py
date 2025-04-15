import pytest


@pytest.fixture(autouse=True,scope="function")
def setup_and_tearDown():
    print("launch Browser")
    print("Opne Application URL in BRowser")
    yield
    print("Log out Application URL in BRowser")
    print("Close Browser")