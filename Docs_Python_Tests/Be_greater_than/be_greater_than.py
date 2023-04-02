from should_dsl import *
import pytest


def test_be_greater_than_passed():
    1 | should | be_greater_than(0.9)


def test_be_greater_than_failed():
    1 | should | be_greater_than(1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 1 is not greater than 1


def test_be_greater_than_failed2():
    1 | should | be_greater_than(2)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 1 is not greater than 2


def test_should_not_be_greater_than():
    1 | should_not | be_greater_than(2)


def test_be_greater_than_char():
    name = 'b'
    name | should | be_greater_than('a')


def test_be_should_not_greater_than_char():
    name = 'b'
    name | should_not | be_greater_than('a')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'b' is greater than 'a'
