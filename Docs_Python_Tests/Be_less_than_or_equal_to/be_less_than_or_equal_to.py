from should_dsl import *
import pytest


def test_be_less_than_or_equal_to_passed():
    0.9 | should | be_less_than_or_equal_to(1)


def test_be_less_than_or_equal_to_passed2():
    1 | should | be_less_than_or_equal_to(1)


def test_be_less_than_or_equal_to_failed():
    2 | should | be_less_than_or_equal_to(1)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not less than or equal to 1


def test_should_not_be_less_than_or_equal_to():
    2 | should_not | be_less_than_or_equal_to(1)


def test_be_less_than_or_equal_to_char_passed():
    name = 'a'
    name | should | be_less_than_or_equal_to('b')


def test_be_less_than_or_equal_to_char_passed2():
    name = 'a'
    name | should | be_less_than_or_equal_to('a')


def test_should_not_be_less_than_or_equal_to_char():
    name = 'a'
    name | should_not | be_less_than_or_equal_to('b')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'a' is less than or equal to 'b'
