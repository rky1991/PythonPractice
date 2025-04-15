import pytest

class TestExample:

    def test_case_one(self):
        assert 1 + 1 == 2

    def test_case_two(self):
        assert "hello".upper() == "HELLO"

    def test_case_three(self):
        assert isinstance(123, int)