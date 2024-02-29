def contar_ocorrencias(frase, palavra):
    frase = frase.strip()
    palavras = frase.split(' ')

    contador = 0

    for char in palavras:
        if char.strip() == palavra.strip():
            contador += 1

    return contador

frase = input("Insira uma frase:")
palavra = input("Insira a palavra que será contada:")
ocorrencias = contar_ocorrencias(frase, palavra)
print(f"A palavra '{palavra.strip()}' ocorre {ocorrencias} vezes na frase.")