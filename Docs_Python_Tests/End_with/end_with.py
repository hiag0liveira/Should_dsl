from should_dsl import *

def test_end_with_passed():
    'hello world' |should| end_with('world')


def test_end_with_failed():    
    'hello motto' |should| end_with('world')
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'hello motto' does not end with 'world'
