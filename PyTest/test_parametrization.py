import pytest


@pytest.mark.parametrize("userName,password", [("rahul", "1234"), ("neha", "1234"), ("mukku", "4321")])
def test_case_one(userName, password):
    print(userName + "-" + password)
