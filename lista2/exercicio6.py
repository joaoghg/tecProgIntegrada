def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None

    soma = []

    for i in range(len(matriz1)):
        linha_soma = []
        for j in range(len(matriz1[0])):
            linha_soma.append(matriz1[i][j] + matriz2[i][j])
        
        soma.append(linha_soma)

    return soma


matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)

if resultado:
    print("Matriz resultante da soma:")
    for linha in resultado:
        print(linha)
else:
    print("As matrizes não podem ser somadas.")