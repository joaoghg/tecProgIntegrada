import heapq

def buscar_maiores(lista, k):
    maiores_elementos = heapq.nlargest(k, lista)

    indices = set()

    for num in maiores_elementos:
        indices.add(lista.index(num))

    maiores_lista = [lista[i] for i in indices]

    return maiores_lista

lista = [4, 7, 1, 9, 3, 8, 5, 2, 6]
k = int(input("Informe a quantidade de elementos que serão retornados:"))
maiores = buscar_maiores(lista, k)
print(f"Os {k} maiores elementos na lista são: {maiores}")