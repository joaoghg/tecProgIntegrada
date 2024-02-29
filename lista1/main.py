#Exercício 1
# lista = []
#
# for i in range(100):
#     lista.append(i+1)
#
# for i in lista:
#     if i % 2 == 0:
#         print(i)

#Exercício 2
# lista1 = ['Teste', 'Jogo', 'Aulas']
# lista2 = []
#
# for i in lista1:
#     lista2.append(len(i))
#
# print(lista2)

#Exercicio 3
# def remove_repetidos(lista):
#     nova_lista = []
#     for i in lista:
#         if i not in nova_lista:
#             nova_lista.append(i)
#     nova_lista.sort()
#     return nova_lista
#
# lista = [1, 1, 2, 3, 3, 4, 3, 8, 7, 6, 7, 8, 10 ,9]
#
# lista = remove_repetidos(lista)
# print (lista)

#Exercicio 4
# def trata_lista(lista):
#     nova_lista = []
#     for i in lista:
#         if i not in nova_lista:
#             nova_lista.append(i)
#     nova_lista.sort()
#     return nova_lista
#
# lista = [100, 200, 10, 2, 150, 5]
#
# lista = trata_lista(lista)
#
# print("Segundo menor número: ")
# print(lista[1])
# print("Segundo maior número: ")
# print(lista[len(lista)-2])

#Exercicio 5
# def lista_comum(lista1, lista2):
#     nova_lista = []
#     for i in lista1:
#         if i in lista2:
#             nova_lista.append(i)
#
#     return nova_lista
#
#
#
# lista1 = [10, 20, 30, 40, 50]
# lista2 = [5, 10, 15, 20, 25, 30]
#
# lista3 = lista_comum(lista1, lista2)
#
# print(lista3)

#Exercicio 6
# def verifica_palindromo(palavra):
#     return palavra == palavra[::-1]
#
# def apenas_palindromos(lista):
#     return [palavra for palavra in lista if verifica_palindromo(palavra)]
#
# lista = ["arara", "banana", "radar", "python", "ovo"]
# palindromos = apenas_palindromos(lista)
# print("Palíndromos:", palindromos)
