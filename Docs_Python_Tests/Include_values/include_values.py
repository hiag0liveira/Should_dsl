from should_dsl import should, should_not


def test_include_values_passed():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(1)


def test_include_values_passed2():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(1, 3)


def test_include_values_passed3():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(1, 2, 3)


def test_include_values_falid():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(1, 4)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include value 4


def test_include_values_falid2():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(1, 4, 5)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include values 4 and 5


def test_include_values_falid3():
    {'a': 1, 'b': 2, 'c': 3} | should | include_values(6, 1, 4, 5)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to include values 6, 4 and 5


def test_should_not_include_values_passed():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_values(4, 5)


def test_should_not_include_values_falid():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_values(1, 2, 4)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to not include values 1 and 2


def test_should_not_include_values_falid2():
    {'a': 1, 'b': 2, 'c': 3} | should_not | include_values(3, 4)
    # Traceback(most recent call last):
    #     ...
    # ShouldNotSatisfied: expected target to not include value 3


def test_should_not_include_values_no_values_falid():
    ['a', 'b', 'c'] | should | include_values('does not matter')
    # Traceback(most recent call last):
    #     ...
    # TypeError: target must be a dictionary
