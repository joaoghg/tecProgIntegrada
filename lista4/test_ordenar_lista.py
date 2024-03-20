import pytest
from ordenar_lista import ordena_crescente, ordena_decrescente

def test_ordena_crescente():
    lista_desordenada = [3, 1, 5, 2, 4]
    lista_ordenada = [1, 2, 3, 4, 5]
    assert ordena_crescente(lista_desordenada) == lista_ordenada

def test_ordena_decrescente():
    lista_desordenada = [3, 1, 5, 2, 4]
    lista_ordenada = [5, 4, 3, 2, 1]
    assert ordena_decrescente(lista_desordenada) == lista_ordenada
