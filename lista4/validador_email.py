import pytest
from validador_email import valida_email

def test_valida_email():
    # Testes para e-mails válidos
    assert valida_email("usuario@example.com") == True
    assert valida_email("usuario123@example.com") == True
    assert valida_email("usuario.123@example.com") == True
    assert valida_email("usuario_123@example.com") == True
    assert valida_email("usuario+123@example.com") == True
    assert valida_email("usuario-123@example.com") == True

    # Testes para e-mails inválidos
    assert valida_email("usuario@com") == False
    assert valida_email("usuario@example") == False
    assert valida_email("usuarioexample.com") == False
    assert valida_email("usuario@.com") == False
    assert valida_email("usuario@com.") == False
    assert valida_email("usuario@ex ample.com") == False
