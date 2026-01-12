import pytest

from project.main import isEven

def test_isEven():
    assert isEven(4) == True
    assert isEven(3) == False
    assert isEven(0) == True