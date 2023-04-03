from should_dsl import should, should_not


def test_close_to_passed():
    1 |should| close_to(0.9, delta=0.1)


def test_close_to_passed2():    
    0.8 |should| close_to(0.9, delta=0.1)


def test_close_to_failed():    
    1 |should| close_to(0.89, delta=0.1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected to be close to 0.89 (within +/- 0.1), got 1


def test_close_to_should_not_passed():    
    1 |should_not| close_to(0.89, delta=0.1)


def test_close_to_should_not_failed():   
    0.91 |should_not| close_to(0.9, delta=0.01)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: expected not to be close to 0.9 (within +/- 0.01), got 0.91


def test_close_to_passed3():   
    4.9 |should| close_to(4, delta=0.9)