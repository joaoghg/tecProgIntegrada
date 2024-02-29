import csv

def mes_com_mais_vendas(nome_arquivo):
    vendas_por_mes = {}

    with open(nome_arquivo, newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            mes = linha['mes']
            vendas = int(linha['vendas'])
            if mes in vendas_por_mes:
                vendas_por_mes[mes] += vendas
            else:
                vendas_por_mes[mes] = vendas

    mes_mais_vendas = max(vendas_por_mes, key=vendas_por_mes.get)

    return mes_mais_vendas

nome_arquivo_csv = 'dados_vendas.csv'
mes_mais_vendas = mes_com_mais_vendas(nome_arquivo_csv)
print(f"O mês com mais vendas foi: {mes_mais_vendas}")
