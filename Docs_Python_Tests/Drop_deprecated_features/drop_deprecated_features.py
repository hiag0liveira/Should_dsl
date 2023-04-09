from should_dsl import *

def test_drop_deprecated_should_be_failed():    
    1 |should_be| 1
    # Traceback (most recent call last):
    #     ...
    # NameError: name 'should_be' is not defined


def test_drop_deprecated_should_not_be_failed(): 
    1 |should_not_be| 2
    # Traceback (most recent call last):
    #     ...
    # NameError: name 'should_not_be' is not defined


def test_drop_deprecated_have_all_failed():
    [1, 2, 3] |should_have.all_of| [2, 3]
    # Traceback (most recent call last):
    #     ...
    # NameError: name 'should_have' is not defined


def test_drop_deprecated_not_have_failed():    
    [1, 2, 3] |should_not_have.any_of| [5, 6]
    # Traceback (most recent call last):
    #     ...
    # NameError: name 'should_not_have' is not defined


def test_drop_deprecated_end_with_failed():    
    "Brasil" |should.end_with| "sil"
    # Traceback (most recent call last):
    #     ...
    # AttributeError: ...
