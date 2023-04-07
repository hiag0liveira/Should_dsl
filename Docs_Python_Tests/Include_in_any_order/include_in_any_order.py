from should_dsl import *
import pytest


def test_include_in_any_order_passed():
    [1, 2, 3] | should | include_in_any_order([3, 1])


def test_include_in_any_order_falid():
    [1, 2, 3] | should | include_in_any_order([3, 4])
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2, 3] does not include in any order[3, 4]


def test_include_in_any_order_passed2():
    [1, 2, 3] | should | include_in_any_order((3, 1))


def test_include_in_any_order_falid2():
    [1, 2, 3] | should | include_in_any_order((3, 4))
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2, 3] does not include in any order (3, 4)


def test_include_in_any_order_caracter():
    'should' | should | include_in_any_order(('s', 'd', 'l'))


def test_include_in_any_order_caracter_falid():
    'should' | should | include_in_any_order(('h', 'a'))
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'should' does not include in any order ('h', 'a')
