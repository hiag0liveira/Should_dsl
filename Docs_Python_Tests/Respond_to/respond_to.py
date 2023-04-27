#Respond_to

from should_dsl import should, should_not

class Foo(object):
     def bar(self):
        pass
     def _internal_bar(self):
        pass
     def __name_clashing_bar(self):
        pass


f = Foo()


def test_respond_to_true():
	f |should| respond_to('bar')


def test_respond_to_false():
	f |should_not| respond_to('bar')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> not to respond to 'bar'


def test_respond_to_false_2():
	f |should| respond_to('unexisting_bar')
	#Traceback (most recent call last):
    	#...
	#ShouldNotSatisfied: expected <...Foo ... at ...> to respond to 'unexisting_bar'


def test_respond_to_true_2():
	f |should| respond_to('_internal_bar')


def test_respond_to_true_3():
	f |should| respond_to('_Foo__name_clashing_bar')