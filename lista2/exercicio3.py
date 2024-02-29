def contaPalavras(frase):
    frase = frase.strip()
    palavras = frase.split(' ')
    return len(palavras)

frase = input("Insira uma frase:")
numPalavras = contaPalavras(frase)

print("O número de palavras na frase é:", numPalavras)