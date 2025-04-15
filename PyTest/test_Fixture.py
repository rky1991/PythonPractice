import pytest


@pytest.fixture()
def setup_and_tearDown():
    print("launch Browser")
    print("Opne Application URL in BRowser")
    yield
    print("Log out Application URL in BRowser")
    print("Close Browser")



def test_login_with_valid_cred(setup_and_tearDown):
    print("Test login with valid credentials")


def test_login_with_valid_email_and_invalid_password(setup_and_tearDown):
    print("Testing with valid email and invalid password")