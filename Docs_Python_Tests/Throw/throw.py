from should_dsl import *

def divide_one_by_zero():
    return 1 / 0
def divide_x_by_y(x, y):
     return x / y


def test_throw_true():
    divide_one_by_zero |should| throw(ZeroDivisionError)


def test_throw_should_not_false():
	divide_one_by_zero |should_not| throw(ZeroDivisionError)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected not to throw 'ZeroDivisionError', but got it


def test_throw_true_2():
	(divide_x_by_y, 5, 0) |should| throw(ZeroDivisionError)

def test_throw_false():
	[divide_x_by_y, 2, 1] |should| throw(ZeroDivisionError)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected to throw 'ZeroDivisionError', got no exception


def test_throw_should_not_true():
	(divide_x_by_y, 1, 0) |should_not| throw(AttributeError)




class Foo(Exception): pass
def raise_foo(message):
    raise Foo(message)


def test_throw_raise_true():
	(raise_foo, 'cool! it works!') |should| throw(Foo, message='cool! it works!')


def test_throw_raise_true_2():
	(raise_foo, 'cool! it works! ble') |should| throw(Foo('cool! it works! ble'))


def test_throw_raise_false():
	(lambda: raise_foo('what a pro!')) |should| throw(Foo, message='cool! it works!')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected to throw 'Foo' with the message 'cool! it works!', got 'Foo' with 'what a pro!'


def test_throw_raise_false_2():
	(lambda: raise_foo('what a pro!')) |should| throw(Foo('cool! it works! ble'))
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected to throw 'Foo' with the message 'cool! it works! ble', got 'Foo' with 'what a pro!'


def test_throw_raise_should_not_false():
	(lambda: raise_foo('who?')) |should_not| throw(Foo, message='who?')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected not to throw 'Foo' with the message 'who?', but got it


def test_throw_raise_should_not_true():
	(lambda: raise_foo('who?')) |should_not| throw(Foo, message='what?')



#The expected message may also be expressed as a regular expression:


def test_throw_raise_regular_expression_true():
	(raise_foo, 'what a pro!') |should| throw(Foo, message_regex=r'what a .+!')

def test_throw_raise_regular_expression_true_2():
	(raise_foo, 'what a jerk!') |should| throw(Foo, message_regex=r'what a .+!')

def test_throw_raise_regular_expression_should_not_true():
	(raise_foo, 'what a pro?') |should_not| throw(Foo, message_regex=r'what a .+!')

def test_throw_raise_regular_expression_should_not_true_2():
	(raise_foo, 'what da hell!') |should_not| throw(Foo, message_regex=r'what a .+!')

def test_throw_raise_regular_expression_false():
	(raise_foo, 'what a pro!') |should| throw(Foo, message_regex="what a .+ yeah")
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected to throw 'Foo' with a message that matches 'what a .+ yeah', got 'Foo' with no match for 'what a pro!'

def test_throw_raise_regular_expression_should_not_false_2():
	(raise_foo, 'what a pro!') |should_not| throw(Foo, message_regex=r'what a .+!')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected not to throw 'Foo' with a message that matches 'what a .+!', but got it