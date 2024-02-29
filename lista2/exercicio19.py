import csv

def soma_vendas_por_vendedor(nome_arquivo):
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

    return vendas_por_vendedor

nome_arquivo_csv = 'dados_vendas.csv'
vendas_por_vendedor = soma_vendas_por_vendedor(nome_arquivo_csv)
print("Soma de vendas por vendedor:")
for vendedor, soma_vendas in vendas_por_vendedor.items():
    print(f"{vendedor}: {soma_vendas}")
