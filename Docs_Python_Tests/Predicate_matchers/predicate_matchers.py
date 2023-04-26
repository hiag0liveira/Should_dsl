from should_dsl import should, should_not, add_predicate_regex

class Foo(object):
    def __init__(self, valid=True):
        self.valid = valid
        self.sleeping = True
        self._doing_some_private_things = False
    def __str__(self):
      return '<foo object>'
    
def test_predicate_matchers_true():    
    Foo() |should| be_valid


def test_predicate_matchers_should_not_false():    
    Foo() |should_not| be_valid
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: expected valid to be False, got True


def test_predicate_matchers_false():    
    Foo(False) |should| be_valid
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: expected valid to be True, got False


def test_predicate_matchers_should_not_true():    
    Foo(False) |should_not| be_valid


def test_predicate_matchers_true_2():    
    Foo() |should| be_sleeping

def test_predicate_matchers_should_not_false_2():      
    Foo() |should_not| be_sleeping
# Traceback (most recent call last):
#     ...
# ShouldNotSatisfied: expected sleeping to be False, got True



def test_predicate_matchers_error():       
     be_valid
# Traceback (most recent call last):
#     ...
# NameError: name 'be_valid' is not defined


def test_predicate_matchers_should_true_3():    
    Foo() |should| be_valid


def test_predicate_matchers_error2():    
    be_valid
# Traceback (most recent call last):
#     ...
# NameError: name 'be_valid' is not defined



def test_predicate_matchers_false_2():    
    Foo() |should| be_doing_some_private_things
# Traceback (most recent call last):
#     ...
# NameError: name 'be_doing_some_private_things' is not defined


def test_predicate_matchers_false_3():    
    Foo() |should| be__doing_some_private_things
# Traceback (most recent call last):
#     ...
# NameError: name 'be__doing_some_private_things' is not defined


def be_valid():       
    be_valid = 'hey, i exist!!'
def test_predicate_matchers_true_3():      
    Foo() |should| be_valid

# >>> be_valid
# 'hey, i exist!!'



add_predicate_regex(r'is_really_(.+)')
class Integer(int):
    def __init__(self, value):
        self.is_really_positive = value >= 0
        self.isodd = (value % 2 == 1) 

def test_predicate_matchers_int_true():    
    Integer(10) |should| be_positive

def test_predicate_matchers_int_true_2():    
    Integer(1) |should| be_odd


class Float(float):
    def __init__(self, value):
        self.is_negative = value < 0

def test_predicate_matchers_float_true():    
    Float(-1) |should| be_negative


from should_dsl import should_not
class EmptyObject(object):
     def __len__(self):
         return 0

     def __zero__(self):
         return True

obj = EmptyObject()

def test_predicate_matchers_obj_true():        
    obj |should| be_empty

def test_predicate_matchers_obj_should_not_true():        
    obj.empty = False
    obj |should_not| be_empty

def test_predicate_matchers_obj_true_2():        
    del obj.empty
    obj |should| be_empty