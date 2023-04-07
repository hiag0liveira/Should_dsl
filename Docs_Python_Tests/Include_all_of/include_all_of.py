from should_dsl import *
import pytest


def test_include_all_of_passed():
    [1, 2, 3] | should | include_all_of([2, 3])


def test_include_all_of_falid():
    [1, 2, 3] | should | include_all_of([3, 4])
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: [1, 2, 3] does not include all of [3, 4]
