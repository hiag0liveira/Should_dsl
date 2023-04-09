from should_dsl import *


def test_equal_to_passed():    
    1 |should| equal_to(1)


def test_equal_to_failed():    
    2 |should| equal_to(3)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 2 is not equal to 3


def test_equal_to_should_not_passed():    
    1 |should_not| equal_to(2)


def test_equal_to_variable_passed():
    name = 'dsl'
    name |should| equal_to('dsl')


def test_equal_to_variable_should_not_failed():
    name = 'dsl'
    name |should_not| equal_to('dsl')
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'dsl' is equal to 'dsl'


def test_equal_to_string_failed():
    name = 'dsl'
    name |should| equal_to('dsl\ntest', diff=True)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: the strings are different, see the diff below:
    # --- actual
    # +++ expected
    # @@ -1 +1,2 @@
    # -dsl+dsl
    # +test


def test_equal_to_case_passed():
    'CaSe' |should| equal_to('case', case_sensitive=False)


def test_equal_to_case_failed():
    'CaSe' |should| equal_to('case', case_sensitive=True)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: 'CaSe' is not equal to 'case'


def test_equal_to_case_failed2():    
    'CaSE' |should| equal_to('CasE\nInsensitive', diff=True, case_sensitive=False)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: the strings are different, see the diff below:
    # --- actual
    # +++ expected
    # @@ -1 +1,2 @@
    # -case+case
    # +insensitive
