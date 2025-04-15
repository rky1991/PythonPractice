import pytest


@pytest.mark.sample
class TestMarker:

    @pytest.mark.skip
    def test_case_one(self):
        print("Marker Test Case 1-->>>Skiped")
        assert 1 + 1 == 2

    def test_case_two(self):
        print("Marker Test Case 2")
        assert "hello".upper() == "HELLO"

    def test_case_three(self):
        print("Marker Test Case 3")
        assert isinstance(123, int)