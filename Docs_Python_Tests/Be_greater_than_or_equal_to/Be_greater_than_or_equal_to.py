from should_dsl import *
import pytest


def test_be_greater_than_or_equal_to_passed():
    1 | should | be_greater_than_or_equal_to(0.9)


def test_be_greater_than_or_equal_to_passed2():
    1 | should | be_greater_than_or_equal_to(1)


def test_be_greater_than_or_equal_to_failed():
    1 | should | be_greater_than_or_equal_to(2)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 1 is not greater than or equal to 2


def test_should_not_be_greater_than_or_equal_to_passed():
    1 | should_not | be_greater_than_or_equal_to(2)


def test_be_greater_than_or_equal_to_char_passed1():
    name = 'b'
    name | should | be_greater_than_or_equal_to('a')


def test_be_greater_than_or_equal_to_char_passed2():
    name = 'b'
    name | should | be_greater_than_or_equal_to('b')


def test_should_not_be_greater_than_or_equal_to_char():
    name = 'b'
    name | should_not | be_greater_than_or_equal_to('a')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'b' is greater than or equal to 'a'
