import pytest
from conversor import dolar_para_euro, real_para_dolar

def test_dolar_para_euro():
    assert dolar_para_euro(100) == 91
    assert dolar_para_euro(0) == 0      
    assert dolar_para_euro(50) == 45.5 

def test_real_para_dolar():
    assert real_para_dolar(100) == 20
    assert real_para_dolar(0) == 0      
    assert real_para_dolar(50) == 10 
