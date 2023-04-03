from should_dsl import *
import pytest


class Foo(object):
    pass


class Bar(object):
    pass


foo = Foo()


def test_be_kind_of_passed():
    foo | should | be_kind_of(Foo)


def test_be_kind_of_failed():
    foo | should | be_kind_of(Bar)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: < Foo object at ... > is not a kind of < class 'Bar' >
