def intersecao(lista1, lista2):
    intersecao_lista = []

    for elemento in lista1:

        if elemento in lista2 and elemento not in intersecao_lista:
            intersecao_lista.append(elemento)

    return intersecao_lista


# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = intersecao(lista1, lista2)
print("Interseção das listas:", resultado)
