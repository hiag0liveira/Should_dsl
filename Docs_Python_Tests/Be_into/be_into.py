from should_dsl import *
import pytest


def test_be_into():
    1 | should | be_into([1, 2, 3])


def test_should_not_be_into():
    1 | should_not | be_into([1, 2, 3])
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 1 is into[1, 2, 3]


def test_should_not_be_into_passed():
    5 | should_not | be_into([1, 2, 3])


def test_be_into_failed():
    'a' | should | be_into(['b', 'c'])
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'a' is not into['b', 'c']
