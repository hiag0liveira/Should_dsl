from should_dsl import should, should_not, matcher

import math
class SquareRootMatcher(object):
     name = 'be_the_square_root_of'
     def __call__(self, arg):
         self._arg = arg
         return self
     def match(self, lvalue):
         self._lvalue = lvalue
         return lvalue == math.sqrt(self._arg)
     def message_for_failed_should(self):
         return "expected %s be the square root of %s, but it is not" % (
                     self._lvalue, self._arg)
     def message_for_failed_should_not(self):
         return "expected %s not be the square root of %s, but it is" % (
                     self._lvalue, self._arg)
SquareRootMatcher = matcher(SquareRootMatcher)

def test_matcher_classes_true():
    3 |should| be_the_square_root_of(9)


def test_matcher_classes_false():    
    1 |should| be_the_square_root_of(3)
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: expected 1 be the square root of 3, but it is not


def test_matcher_classes_true_2():   
    4 |should_not| be_the_square_root_of(11)


def test_matcher_classes_should_not_false():       
    4 |should_not| be_the_square_root_of(16)
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: expected 4 not be the square root of 16, but it is


# If a matcher class has a constructor, it must have no other parameters than self
class ParameterizedInit(object):
    name = 'anything'
    def __init__(self, lvalue): pass
    def __call__(self): return self
    def match(self): return True
    def message_for_failed_should(self): return ""
    def message_for_failed_should_not(self): return ""
# ...
# >>> ParameterizedInit = matcher(ParameterizedInit)
# Traceback (most recent call last):
#     ...
# TypeError: matcher class constructor cannot have arguments

# Other TypeError exceptions on constructors behave normally:
# >>> class AnotherOne(object):
# ...     name = 'another one'
# ...     def __init__(self):
# ...         1 + 'a'
# ...


# >>> AnotherOne = matcher(AnotherOne)
# Traceback (most recent call last):
#     ...
# TypeError: unsupported operand type(s) for ...
