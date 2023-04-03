from should_dsl import *
import re
import pytest


def test_be_like_passed():
    'Hello World' | should | be_like(r'Hello W.+')


def test_be_like_failed():
    '123 is a number' | should | be_like(r'^[12]+ is a number')
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: '123 is a number' is not like '^[12]+ is a number'


def test_be_like_passed2():
    'Hello\nWorld' | should | be_like(r'Hello.+', re.DOTALL)


def test_be_like_failed2():
    'Hello\nWorld' | should | be_like(r'hello.+', re.DOTALL)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'Hello\nWorld' is not like 'hello.+' with given flags


def test_should_not_be_like():
    'Hello\nWorld' | should_not | be_like(r'hello.+', re.DOTALL + re.IGNORECASE)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: 'Hello\nWorld' is like 'hello.+' with given flags
