from should_dsl import *

def test_matcher_as_functions_should_not_true():    
    'abc' |should_not| equal_to('cba')


def test_matcher_as_functions_true():    
    1 |should| be_into([1, 2, 3])



def test_matcher_as_functions_true_2():
    (1, 2, 3) |should| include_in_any_order([2, 1])


import math
@matcher
def be_the_square_root_of():
    return (lambda x, y: x == math.sqrt(y), "%s is %sthe square root of %s")


def test_matcher_as_functions_true_3():
    3 |should| be_the_square_root_of(9)



def test_matcher_as_functions_false():
    2 |should| be_the_square_root_of(4.1)
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: 2 is not the square root of 4.1


# >>> equal_to
# Traceback (most recent call last):
#     ...
# NameError: ... 'equal_to' ...


def test_matcher_as_functions_should_not_true2():    
    'abc' |should_not| equal_to('cba')

# >>> equal_to
# Traceback (most recent call last):
#     ...
# NameError: ... 'equal_to' ...

def equal_to():
    print('hey, it works')

# equal_to()
# hey, it works
def test_matcher_as_functions_should_not_true3():    
    'abc' |should_not| equal_to('cba')


# def equal_to():
#     hey, it works
