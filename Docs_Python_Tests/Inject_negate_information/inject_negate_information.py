
from should_dsl import should, should_not, matcher


class FooMatcher(object):
    name = 'be_a_foo_object'

    def match(self, right_object):
        print("Ran with negate? %s" % self.run_with_negate)
        return not self.run_with_negate


matcher(FooMatcher)
# <class 'FooMatcher' >


def test_inject_negate_information():
    1 | should | be_a_foo_object
    # Ran with negate? False


def test_should_not_inject_negate_information():
    1 | should_not | be_a_foo_object
    # Ran with negate? True
    # Matchers which __slots__ attribute will not cause AttributeError.


class BarMatcher(object):
    __slots__ = []
    name = 'be_a_bar_object'

    def match(self, right_object):
        return True


matcher(BarMatcher)
# <class 'BarMatcher' >


def test_inject_negate_information3():
    1 | should | be_a_bar_object
