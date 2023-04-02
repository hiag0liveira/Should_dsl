from should_dsl import should, should_not
import pytest


def test_be_empty_list_nil():
    [] | should | be_empty


def test_be_empty():
    [1] | should | be_empty
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected[1] to be empty


def test_should_not_be_empty_list_nil():
    [] | should_not | be_empty
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected[] not to be empty


def test_should_not_be_empty():
    [1] | should_not | be_empty


def test_be_empty_tuple_nil():
    () | should | be_empty


def test_be_empty_tuple():
    (1,) | should | be_empty
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected(1,) to be empty


def test_should_not_be_empty_tuple():
    (1,) | should_not | be_empty


def test_should_not_be_empty_tuple_nil():
    () | should_not | be_empty
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected() not to be empty


def test_be_empty_var_nil():
    '' | should | be_empty


def test_should_not_be_empty_var():
    'a' | should_not | be_empty


def test_be_empty_dict_nil():
    {} | should | be_empty


def test_should_not_be_empty_dict():
    {'a': 1} | should_not | be_empty


class MyCollection:

    def __init__(self, count):
        self.count = count

    def __len__(self):
        return self.count


def test_be_empty_class_nil():
    MyCollection(0) | should | be_empty


def test_should_not_be_empty_class():
    MyCollection(1) | should_not | be_empty
