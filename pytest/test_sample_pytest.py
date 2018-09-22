# simple program to test a method using pytest
# How to run: 'pytest <file_name>' or 'python -m pytest' to recursive look for files starting with test_
# Pre-requisite: pytest
# auto discovery rule: start with test_(file & function)


def add(val1, val2):
    return val1 + val2


def test_add_pass():
    assert add(1, 2) == 3


def test_add_fail():
    assert add(1, 2) == 2
