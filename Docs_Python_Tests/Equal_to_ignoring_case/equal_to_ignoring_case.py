#coding: utf-8

from should_dsl import *

def test_equal_to_ignoring_case_passed():
    "I'm specifying it" |should| equal_to_ignoring_case("I'M SPECIFYING it")


def test_equal_to_ignoring_case_passed2():
    "I" |should| equal_to_ignoring_case("i")


def test_equal_to_ignoring_case_passed3(): 
    "i" |should| equal_to_ignoring_case("I")


def test_equal_to_ignoring_case_passed4():
    "I" |should| equal_to_ignoring_case("I")


def test_equal_to_ignoring_case_failed():    
    "I" |should| equal_to_ignoring_case("wi")
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'I' is not equal to 'wi' ignoring case


def test_equal_to_ignoring_case_failed2():    
    "I" |should| equal_to_ignoring_case("iw")
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'I' is not equal to 'iw' ignoring case


def test_equal_to_ignoring_case_passed5():    
    "Atenção" |should| equal_to_ignoring_case("ATENÇÃO")
