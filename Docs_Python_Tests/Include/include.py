from should_dsl import *
import pytest


def test_include_passed():
    [1, 2, 3] | should | include(1)


def test_include_falid():
    [1, 2] | should | include(3)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2] does not include 3


def test_should_not_include_passed():
    [1, 2] | should_not | include(3)


def test_should_not_include_falid():
    'should' | should_not | include('oul')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'should' does include 'oul'


def test_contain_passed():
    [1, 2, 3] | should | contain(1)


def test_contain_falid():
    [1, 2] | should | contain(3)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2] does not contain 3


def test_should_not_contain_passed():
    [1, 2] | should_not | contain(3)


def test_should_not_contain_falid():
    'should' | should_not | contain('oul')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'should' does contain 'oul'
