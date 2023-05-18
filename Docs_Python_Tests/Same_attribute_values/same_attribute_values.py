from should_dsl import should, should_not

class Foo(object):
   def __init__(self, a, b):
       self.a = a
       self.b = b

a = Foo(1,2)
b = Foo(1,2)
c = Foo(1,3)
#Simple test

def test_same_attribute_values_true(a = Foo(1,2), b = Foo(1,2), c = Foo(1,3)):	
	a |should| have_same_attribute_values_as(b)



def test_same_attribute_values_false(a = Foo(1,2), b = Foo(1,2), c = Foo(1,3)):
	a |should| have_same_attribute_values_as(c)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> to have the same attribute values as <...Foo ... at ...>


def test_same_attribute_values_false_2(a = Foo(1,2), b = Foo(1,2), c = Foo(1,3)):
	a |should_not| have_same_attribute_values_as(b)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> to have not the same attribute values as <...Foo ... at ...>




def test_same_attribute_values_true_2():	
#Adding attributes to each object
	setattr(a,'c',3)
	setattr(b,'c',3)
	a |should| have_same_attribute_values_as(b)


def test_same_attribute_values_true_3():
#Deleting one attribute of the object
	del a.c
	a |should_not| have_same_attribute_values_as(b)