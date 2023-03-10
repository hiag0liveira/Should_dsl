import pytest
# import html.pytest
from batata import *

def test_max():
    lista = [0, 1, 2]
    assert max(lista) == 1

def test2_max():
    lista = [0, 1, 2]
    assert max(lista) == 2
