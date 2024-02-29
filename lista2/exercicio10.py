def calcular_frequencia(texto):
    palavras = texto.split()

    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


texto = input("Digite o texto?:")
frequencia_palavra = calcular_frequencia(texto)
print("Frequência de cada palavra:")
for palavra, frequencia in frequencia_palavra.items():
    print(f"{palavra}: {frequencia}")
