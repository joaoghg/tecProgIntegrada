import pytest
from valida_telefone import valida_telefone

def test_valida_telefone():
    # Testes para números de telefone válidos
    assert valida_telefone("(11) 9999-9999") == True
    assert valida_telefone("(81) 98765-4321") == True
    assert valida_telefone("(85) 4567-8901") == True

    # Testes para números de telefone inválidos
    assert valida_telefone("11 9999-9999") == False  # sem os parênteses do DDD
    assert valida_telefone("(11) 12345-6789") == False  # primeiro dígito após o DDD deve ser 2-9
    assert valida_telefone("(11) 9999-9a9a") == False  # caracteres não numéricos
