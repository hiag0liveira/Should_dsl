from should_dsl import *
import pytest


def test_include_any_of_passed():
    [1, 2, 3] | should | include_any_of([1, 2])


def test_include_any_of_falid():
    [1, 2, 3] | should | include_any_of([4, 5])
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2, 3] does not include any of[4, 5]
