import pytest
from should_dsl import should, should_not, matcher


def test_have_at_most_passed():
    ['a', 'b', 'c'] | should | have_at_most(3).elements


def test_have_at_most_passed2():
    "abcdef" | should | have_at_most(7).characters


def test_should_not_have_at_most_failed():
    ['a', 'b', 'c'] | should_not | have_at_most(3).things
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have at most 3 'things', got 3


def test_have_at_most_failed():
    "abcde" | should | have_at_most(4).alphabetical_characters
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected at most 4 'alphabetical characters', got 5


def test_should_not_have_at_most_passed():
    (1, 2, 3) | should_not | have_at_most(2).numbers


class Car(object):
    def __init__(self, *wheels):
        self.wheels = wheels

    def wild_wheels(self):
        return self.wheels


def test_have_at_most_class_passed():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_most(5).wheels


def test_have_at_most_class_passed2():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_most(4).wheels


def test_have_at_most_class_failed():
    my_car = Car(1, 2, 3, 4)
    my_car | should | have_at_most(3).wheels
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected at most 3 'wheels', got 4


def test_should_not_have_at_most_class_passed():
    my_car = Car(1, 2, 3, 4)
    my_car | should_not | have_at_most(3).wheels


def test_should_not_have_at_most_class_failed():
    my_car = Car(1, 2, 3, 4)
    my_car | should_not | have_at_most(4).wheels
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have at most 4 'wheels', got 4
