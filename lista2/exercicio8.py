import random

def embaralhar(lista):
    indices_embaralhados = list(range(len(lista)))
    random.shuffle(indices_embaralhados)

    lista_embaralhada = [lista[i] for i in indices_embaralhados]

    return lista_embaralhada

minha_lista = [1, 2, 3, 4, 5]
lista_embaralhada = embaralhar(minha_lista)
print("Lista original:", minha_lista)
print("Lista embaralhada:", lista_embaralhada)
