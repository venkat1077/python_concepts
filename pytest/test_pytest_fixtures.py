# program to test a method using pytest fixtures
# How to run: 'pytest -v <file_name>' or 'python -m pytest' to recursive look for files starting with test_
# Pre-requisite: pytest
# auto discovery rule: start with test_(file & function)


import pytest


# here scope is module level so it will run only once else it will run for before all test functions
@pytest.fixture(scope="module")
def my_setup_fixture():
    print "Setting up"
    # instead of return use yield when you want to perform something after this(like teardown)
    return 20


def add(val1, val2):
    return val1 + val2


# fixture defined earlier is passed as an argument here
# whatever is returned by fixture can be used directly here
def test_add_pass1(my_setup_fixture):
    assert add(1, 2) == 3 and my_setup_fixture == 20


def test_add_pass2(my_setup_fixture):
    assert add(1, 2) == 3 and my_setup_fixture+10 == 30


def test_add_fail(my_setup_fixture):
    assert add(1, 2) == 3 and my_setup_fixture == 10
