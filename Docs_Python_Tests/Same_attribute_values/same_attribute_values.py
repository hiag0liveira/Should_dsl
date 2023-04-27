from should_dsl import should, should_not

class Foo(object):
   def __init__(self, a, b):
       self.a = a
       self.b = b

a = Foo(1,2)
b = Foo(1,2)
c = Foo(1,3)
#Simple test

def test_same_attribute_values_true():	
	a |should| have_same_attribute_values_as(b)


def test_same_attribute_values_false():
	a |should| have_same_attribute_values_as(c)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> to have the same attribute values as <...Foo ... at ...>


def test_same_attribute_values_false_2():
	a |should_not| have_same_attribute_values_as(b)
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> to have not the same attribute values as <...Foo ... at ...>


#Adding attributes to each object

a.c = 3
b.c = 3


def test_same_attribute_values_true_2():
	a |should| have_same_attribute_values_as(b)



#Deleting one attribute of the object

del a.c

def test_same_attribute_values_true_3():
	a |should_not| have_same_attribute_values_as(b)