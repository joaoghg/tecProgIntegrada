import pytest
from conta_palavras import conta_palavras

def test_conta_palavras():
    texto = "Isso e uma frase simples."
    assert conta_palavras(texto) == 5

    texto = "Esta e uma frase, com pontuacao"
    assert conta_palavras(texto) == 6

    texto = ""
    assert conta_palavras(texto) == 0
