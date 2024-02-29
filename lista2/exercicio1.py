def contaVogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']

    cont = 0
    string = string.lower()

    for i in string:
        if i in vogais:
            cont += 1

    return cont

string = input("Digite o texto: ")
numVogais = contaVogais(string)

print("O número de vogais no texto é", numVogais)