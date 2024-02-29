def substituirLetras(string, substituida, substituta):
    return string.replace(substituida, substituta)

string = input("Digite o texto:")
substituida = input("Qual letra você quer substituir?")
substituta = input("Por qual letra você quer trocar?")

novaString = substituirLetras(string, substituida, substituta)
print("O novo texto é:", novaString)