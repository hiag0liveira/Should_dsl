from should_dsl import *
import math

@matcher
def be_the_square_root_of():
    return (lambda x, y: x == math.sqrt(y), "%s is %sthe square root of %s")


def test_deprecated_passed():
    3 |should| be_the_square_root_of(9)