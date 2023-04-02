from should_dsl import *
import pytest


def test_be_passed():
    1 | should | be(1)


def test_be_failed():
    1 | should | be(2)


def test_be_should_not_passed():
    1 | should_not | be(1.1)


def test_be_forced_failure_failed():
    'a' | should | be('b')

    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'a' was expected to be 'b'


def test_be_should_not_failed():
    1 | should_not | be(1)

    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 1 was not expected to be 1
