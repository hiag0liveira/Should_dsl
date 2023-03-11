from should_dsl import aliases, should
import pytest

# Aliases are useful when the code is in another language than English, avoiding
# mixed languages. The following examples are in Portuguese.


def test_should_equal_to_passed():
    1 | should | equal_to(1)


def test_should_equal_to_failed():
    1 | should | equal_to(2)


def test_should_include():
    'asas' | should | include('sa')


def test_should_have():
    class Campo:
        pass

    campo = Campo()
    campo.jogadores = range(22)
    campo | should | have(22).jogadores
