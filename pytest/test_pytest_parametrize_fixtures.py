# program to test a method using pytest parametrized_fixtures
# How to run: 'pytest -v <file_name>' or 'python -m pytest' to recursive look for files starting with test_
# Pre-requisite: pytest
# auto discovery rule: start with test_(file & function)


import pytest


# this accepts two values:
# 1. string of all inputs of the test method
# 2. list of tuples of all inputs to be sent to test method
@pytest.mark.parametrize("input1, input2, expected", [
    (1, 2, 3),  # pass
    (3, 4, 7),  # pass
    (5, 6, 11),  # pass
    (7, 8, 14),  # fail
])
def test_add(input1, input2, expected):
    assert input1 + input2 == expected
