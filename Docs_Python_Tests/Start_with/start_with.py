#Start_with

from should_dsl import *

def test_start_with_true():
	'Hello world' |should| start_with('Hello')


def test_start_with_false():
	'Hello world' |should| start_with('Hola')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: 'Hello world' does not start with 'Hola'