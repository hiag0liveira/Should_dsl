from should_dsl import should, should_not
import pytest


def test_have_elements_passed():
    ['a', 'b', 'c'] | should | have(3).elements


def test_have_elements_passed2():
    "abcdef" | should | have(6).characters


def test_should_not_have_elements_failed():
    ['a', 'b', 'c'] | should_not | have(3).things
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have 3 'things', got 3


def test_have_elements_failed():
    "abcde" | should | have(6).alphabetical_characters
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected 6 'alphabetical characters', got 5


def test_should_not_have_elements_passed():
    (1, 2, 3) | should_not | have(2).numbers
