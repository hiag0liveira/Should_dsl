from should_dsl import should, should_not, matcher
import math

@matcher
def be_the_square_root_of():
    return (lambda x, y: x == math.sqrt(y), "%s is %sthe square root of %s")

def test_custom_square_passed():    
    3 |should| be_the_square_root_of(9)


def test_custom_square_failed():    
    2 |should| be_the_square_root_of(4.1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not the square root of 4.1


def test_custom_square_should_not_passed():    
    2 |should_not| be_the_square_root_of(3)


def test_custom_square_should_not_failed():
    3 |should_not| be_the_square_root_of(9)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 3 is the square root of 9


# The order of "actual", "expected", and an eventual "not" can be specified within
# the message itself. If not specified, default actual->not->expected order is
# assumed.

# By default, the word 'not ' is added to should error messages. If you want
# the word 'not ' shown as part of should_not error messages rather than as part
# of the should error messages, you must pass should_not as the third element of
# the tuple returned by your custom matcher.

@matcher
def be_triple():
    return (lambda x, y: x == y * 3,
        "expected %(not)striple %(expected)s, got %(actual)s",
        should_not)

def test_custom_triple_failed():    
    3.1 |should| be_triple(1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected triple 1, got 3.1


def test_custom_triple_should_not_failed():  
    3 |should_not| be_triple(1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected not triple 1, got 3


# For readability purposes, a function called matcher_configuration is provided,
# with same effects than passing a regular tuple.

from should_dsl import matcher_configuration

@matcher
def be_triple():
    return matcher_configuration(
        verifier=lambda x, y: x == y * 3,
        message="expected %(not)striple %(expected)s, got %(actual)s",
        word_not_for=should_not)


def test_custom_triple_failed2():   
    3.1 |should| be_triple(1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected triple 1, got 3.1


# If information about the word "not" is not given, the word "not" is applied to
# should error messages by default.

@matcher
def be_the_square_root_of():
    return (lambda x, y: x == math.sqrt(y),
             "%(actual)s is %(not)sthe square root of %(expected)s")


def test_custom_square_failed2():    
    2 |should| be_the_square_root_of(4.1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not the square root of 4.1


def test_custom_square_should_not_failed2():    
    3 |should_not| be_the_square_root_of(9)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 3 is the square root of 9



# But 'should' can be informed.

@matcher
def be_the_square_root_of():
    return (lambda x, y: x == math.sqrt(y),
            "%(actual)s is %(not)sthe square root of %(expected)s", should)


def test_custom_square_failed3():    
    2 |should| be_the_square_root_of(4.1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not the square root of 4.1


def test_custom_square_should_not_failed3():   
    3 |should_not| be_the_square_root_of(9)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 3 is the square root of 9