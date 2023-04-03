from should_dsl import *
import pytest


def divide_one_by_zero():
    return 1 / 0


def divide_x_by_y(x, y):
    return x / y


def test_be_thrown_by_passed():
    ZeroDivisionError | should | be_thrown_by(divide_one_by_zero)


def test_should_not_be_thrown_by_failed():
    ZeroDivisionError | should_not | be_thrown_by(divide_one_by_zero)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: ...ZeroDivisionError... is thrown by < function divide_one_by_zero at ... >


def test_be_thrown_by_passed2():
    ZeroDivisionError | should | be_thrown_by((divide_x_by_y, 5, 0))


def test_be_thrown_by_failed():
    ZeroDivisionError | should | be_thrown_by([divide_x_by_y, 2, 1])
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: ...ZeroDivisionError... is not thrown by [< function divide_x_by_y at ... > , 2, 1]


def test_should_not_be_thrown_by_passed():
    AttributeError | should_not | be_thrown_by((divide_x_by_y, 1, 0))
