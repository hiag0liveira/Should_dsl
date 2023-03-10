import pytest
import test_batata

def test_min():
    values = (2, 3, 1, 4, 6)

    val = test_batata.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = test_batata.max(values)
    assert val == 6