import pytest
from valida_telefone import valida_telefone

def test_valida_telefone():
    # Testes para n�meros de telefone v�lidos
    assert valida_telefone("(11) 9999-9999") == True
    assert valida_telefone("(81) 98765-4321") == True
    assert valida_telefone("(85) 4567-8901") == True

    # Testes para n�meros de telefone inv�lidos
    assert valida_telefone("11 9999-9999") == False  # sem os par�nteses do DDD
    assert valida_telefone("(11) 12345-6789") == False  # primeiro d�gito ap�s o DDD deve ser 2-9
    assert valida_telefone("(11) 9999-9a9a") == False  # caracteres n�o num�ricos
