from should_dsl import aliases, should
import pytest

# Aliases are useful when the code is in another language than English, avoiding
# mixed languages. The following examples are in Portuguese.


deve = should

aliases(equal_to='ser_igual_a', include='incluir', have='ter')


1 | deve | ser_igual_a(1)
'asas' | deve | incluir('sa')
[1, 2, 3] | deve | ter(3).elementos


class Campo:
    pass


campo = Campo()
campo.jogadores = range(22)
campo | deve | ter(22).jogadores
