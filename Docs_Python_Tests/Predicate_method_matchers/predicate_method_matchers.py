#Predicate_method_matchers

from should_dsl import should, should_not, add_predicate_regex

class Foo(object):
     def always_true(self):
         return True
     def always_false(self):
         return False
     def face_of(self, fruit):
         return fruit == 'banana'
     def head_of(self, state, fruit):
         return state == 'rotten' and fruit == 'apple'
     def a_kind_of(self, *dead_end):
         return dead_end == ['nothing', 'senseless label']
     def _str_(self):
         return '<foo object>'


def test_preditace_method_matchers_should_not_always_true():
	Foo() |should_not| be_always_false


def test_preditace_method_matchers_always_true():
	Foo() |should| be_always_true


def test_preditace_method_matchers_always_false():
	Foo() |should| be_always_false
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected always_false() to return True, got False


def test_preditace_method_matchers_should_not_always_false():
	Foo() |should_not| be_always_true
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected always_true() to return False, got True


def test_preditace_method_matchers_face_true():
    Foo() |should| be_face_of('banana')


def test_preditace_method_matchers_should_not_face_true():
	Foo() |should_not| be_face_of('pineapple')


def test_preditace_method_matchers_face_false():
	Foo() |should| be_face_of('pineapple')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected face_of('pineapple') to return True, got False


def test_preditace_method_matchers_head_true():
	Foo() |should| be_head_of('rotten', 'apple')


def test_preditace_method_matchers_head_false():
	Foo() |should| be_head_of('fair', 'apple')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected head_of('fair', 'apple') to return True, got False


def test_preditace_method_matchers_kind_false():
	Foo() |should| be_a_kind_of('craziness', 'wasting of time', 'buzzword')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected a_kind_of('craziness', 'wasting of time', 'buzzword') to return True, got False



add_predicate_regex(r'is_really_(.+)')
class Integer(int):
     def is_really_positive(self):
         return self >= 0

def test_preditace_method_matchers_positive_true():
	Integer(10) |should| be_positive