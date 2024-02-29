def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def identificar_primos(lista):
    primos = []
    for numero in lista:
        if is_primo(numero):
            primos.append(numero)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primos = identificar_primos(numeros)
print("Números primos na lista:", primos)
