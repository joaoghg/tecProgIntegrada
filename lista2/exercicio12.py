def menor_string(lista):
    if not lista:
        return None
    menor = lista[0]
    for string in lista:
        if len(string) < len(menor):
            menor = string
    return menor

lista_strings = ["python", "java", "c", "ruby", "javascript"]
menor = menor_string(lista_strings)
print("Menor string na lista:", menor)
