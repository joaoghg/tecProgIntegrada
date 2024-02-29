import csv

def encontrar_maior_e_menor_vendas(nome_arquivo):
    vendas_por_vendedor = {}

    with open(nome_arquivo, newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            vendedor = linha['Vendedor']
            venda = int(linha['Venda'])
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += venda
            else:
                vendas_por_vendedor[vendedor] = venda

    vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)

    vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)

    return vendedor_mais_vendeu, vendedor_menos_vendeu

nome_arquivo_csv = 'dados_vendas.csv'
mais_vendeu, menos_vendeu = encontrar_maior_e_menor_vendas(nome_arquivo_csv)
print(f"O vendedor que mais vendeu foi: {mais_vendeu}")
print(f"O vendedor que menos vendeu foi: {menos_vendeu}")
