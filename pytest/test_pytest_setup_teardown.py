# program to test a method using setup & teardown modules
# How to run: 'pytest -v <file_name>' or 'python -m pytest' to recursive look for files starting with test_
# Pre-requisite: pytest
# auto discovery rule: start with test_(file & function)

glob_val = 10


# to setup the execution environment
# this will get executed before the starting the tests
def setup_module(module):
    global glob_val
    glob_val += 1


# to cleanup the execution environment
# this will get executed after the end of all tests
def teardown_module(module):
    global glob_val
    glob_val = 10


def add(val1, val2):
    return val1 + val2 + glob_val


def test_add_pass():
    assert add(1, 2) == 14


def test_add_fail():
    assert add(1, 2) == 15
