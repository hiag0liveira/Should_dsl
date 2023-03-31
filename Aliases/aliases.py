from should_dsl import aliases, should
import pytest

# Aliases are useful when the code is in another language than English, avoiding
# mixed languages. The following examples are in Portuguese.

deve = should

aliases(equal_to='ser_igual_a', include='incluir', have='ter')


def test_equal_to_passed():
    1 | deve | ser_igual_a(1)


def test_equal_to_failed():
    1 | deve | ser_igual_a(2)


def test_include_passed():
    'asas' | deve | incluir('sa')


def test_include_failed():
    'asas' | deve | incluir('su')


def test_have_passed():
    [1, 2, 3] | deve | ter(3).elementos


def test_have_failed():
    [1, 2, 3] | deve | ter(4).elementos


def test_have2_passed():
    class Campo:
        pass

    campo = Campo()
    campo.jogadores = range(22)
    campo | deve | ter(22).jogadores


def test_have2_failed():
    class Campo:
        pass

    campo = Campo()
    campo.jogadores = range(22)
    campo | deve | ter(24).jogadores
