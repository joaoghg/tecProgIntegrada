def encontrar_pares(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

minha_lista = [1, 2, 3, 4, 5, 6]
alvo = int(input("Informe o valor alvo:"))
pares = encontrar_pares(minha_lista, alvo)
print(f"Pares cuja soma é {alvo}: {pares}")
