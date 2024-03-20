import pytest
from verifica_senha import verifica_seguranca_senha

def test_verifica_seguranca_senha():
    # Senhas inválidas
    assert verifica_seguranca_senha("") == False
    assert verifica_seguranca_senha("abcde") == False
    assert verifica_seguranca_senha("ABCDE") == False
    assert verifica_seguranca_senha("12345678") == False
    assert verifica_seguranca_senha("abcd1234") == False
    assert verifica_seguranca_senha("ABCD1234") == False
    assert verifica_seguranca_senha("!@#$%^&*()") == False
    assert verifica_seguranca_senha("abcdefgh!") == False

    # Senhas válidas
    assert verifica_seguranca_senha("Abcd123!") == True
    assert verifica_seguranca_senha("P@ssw0rd") == True
    assert verifica_seguranca_senha("SecureP@ssw0rd") == True
