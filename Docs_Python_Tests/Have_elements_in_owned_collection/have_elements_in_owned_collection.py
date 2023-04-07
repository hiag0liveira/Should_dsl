from should_dsl import should, should_not, matcher


class Car(object):
    def __init__(self, wheels):
        self.wheels = wheels

    def wild_wheels(self):
        return self.wheels

    def broken_wheels(self):
        return len(self.wheels)


def test_have_elements_in_owned_collection_passed():
    Car([1, 2, 3, 4]) | should | have(4).wheels


def test_have_elements_in_owned_collection_failed():
    Car([1, 2, 3]) | should | have(4).wheels
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected 4 'wheels', got 3


def test_have_should_not_elements_in_owned_collection_passed():
    Car([1, 2, 3, 4]) | should_not | have(5).wheels


def test_have_should_not_elements_in_owned_collection_failed():
    Car([1, 2]) | should_not | have(2).wheels
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target not to have 2 'wheels', got 2


def test_have_elements_in_owned_collection_falha():
    Car([1, 2, 3, 4]) | should | have(4).legs
    # Traceback (most recent call last):
    #     ...
    # TypeError: target does not have a 'legs' collection, nor it is an iterable


def test_have_elements_in_owned_collection_falha2():
    2 | should | have(1).things
    # Traceback (most recent call last):
    #     ...
    # TypeError: target does not have a 'things' collection, nor it is an iterable


def test_have_elements_in_owned_collection_falha3():
    Car(42) | should | have(42).wheels
    # Traceback (most recent call last):
    #     ...
    # TypeError: target's 'wheels' is not an iterable


def test_have_elements_in_owned_collection_passed2():
    Car([1, 2, 3, 4]) | should | have(4).wild_wheels


def test_have_elements_in_owned_collection_falha4():
    Car([1, 2, 3, 4]) | should | have(4).broken_wheels
    # Traceback (most recent call last):
    #     ...
    # TypeError: target's 'broken_wheels()' does not return an iterable


def test_have_elements_in_owned_collection_passed3():
    {'a': 1, 'b': 2, 'c': 3} | should | have(3).keys


def test_have_elements_in_owned_collection_passed4():
    {'a': 1, 'b': 2, 'c': 3} | should | have(3).values
