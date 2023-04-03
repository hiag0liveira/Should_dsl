from should_dsl import *
import pytest


def test_be_less_than_passed():
    0.9 | should | be_less_than(1)


def test_be_less_than_failed():
    2 | should | be_less_than(2)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not less than 2


def test_be_less_than_failed2():
    2 | should | be_less_than(1)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not less than 1


def test_should_not_be_less_than():
    2 | should_not | be_less_than(1)


def test_be_less_char():
    name = 'a'
    name | should | be_less_than('b')


def test_should_not_be_less_char():
    name = 'a'
    name | should_not | be_less_than('b')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'a' is less than 'b'
