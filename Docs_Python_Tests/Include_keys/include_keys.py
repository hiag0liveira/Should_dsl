from should_dsl import should, should_not
import pytest


def test_include_keys_passed():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('a')


def test_include_keys_passed2():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('a', 'c')


def test_include_keys_passed3():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('a', 'c', 'b')


def test_include_keys_falid():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('a', 'd')
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include key 'd'


def test_include_keys_falid2():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('a', 'd', 'e')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include keys 'd' and 'e'


def test_include_keys_falid3():
    {'a': 1, 'b': 2, 'c': 3} | should | include_keys('f', 'a', 'd', 'e')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include keys 'f', 'd' and 'e'


def test_should_not_include_keys_passed():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_keys('d', 'e')


def test_should_not_include_keys_falid():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_keys('a', 'b', 'd')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to not include keys 'a' and 'b'


def test_should_not_include_keys_falid2():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_keys('c', 'd')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to not include key 'c'


def test_include_keys_no_keys_falid():
    ['a', 'b', 'c'] | should | include_keys('a', 'b', 'c')
    # Traceback(most recent call last):
    #     ...
    # TypeError: target must be a dictionary
