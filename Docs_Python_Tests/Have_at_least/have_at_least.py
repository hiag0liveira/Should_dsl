from should_dsl import should, should_not, matcher
import pytest


def test_have_at_least_passed():
    ['a', 'b', 'c'] | should | have_at_least(3).elements


def test_have_at_least_passed2():
    "abcdef" | should | have_at_least(5).characters


def test_should_not_have_at_least_failed():
    ['a', 'b', 'c'] | should_not | have_at_least(3).things
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have at least 3 'things', got 3


def test_have_at_least_failed():
    "abcde" | should | have_at_least(6).alphabetical_characters
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected at least 6 'alphabetical characters', got 5


def test_should_not_have_at_least_passed():
    (1, 2, 3) | should_not | have_at_least(4).numbers


class Car(object):
    def __init__(self, *wheels):
        self.wheels = wheels

    def wild_wheels(self):
        return self.wheels


def test_have_at_least_class_passed():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_least(3).wheels


def test_have_at_least_class_passed2():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_least(4).wheels


def test_have_at_least_class_failed():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_least(5).wheels
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected at least 5 'wheels', got 4


def test_should_not_have_at_least_class_passed():
    my_car = Car(1, 2, 3, 4)
    my_car | should_not | have_at_least(5).wheels


def test_should_not_have_at_least_class_failed():
    my_car | should_not | have_at_least(4).wheels
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have at least 4 'wheels', got 4
