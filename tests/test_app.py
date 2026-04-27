import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import soma

def test_soma_inteiros():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-2, -3) == -5

def test_soma_com_zero():
    assert soma(0, 5) == 5

def test_soma_float():
    assert soma(2.5, 3.5) == 6.0

def test_soma_valor_grande():
    assert soma(1000000, 2000000) == 3000000