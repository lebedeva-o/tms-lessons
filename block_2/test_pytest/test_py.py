import pytest


@pytest.mark.wizard
class TestHomework:
    @pytest.mark.parametrize("first_name", ["John", "Harry", "Ron"])
    @pytest.mark.parametrize("last_name", [" Smith", " Potter", " Weasly"])
    def test_fail_if_john_smith(self, first_name, last_name, age):
        if first_name == "John" and last_name == "Smith":
            pytest.xfail("John Smith is fail")
        print(f'Hello, {first_name}{last_name}! your age is {age}')



