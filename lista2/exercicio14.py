import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            dados = []
            for linha in leitor_csv:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
        return None

nome_arquivo_csv = "dados.csv"
dados_csv = ler_arquivo_csv(nome_arquivo_csv)
if dados_csv:
    print("Conteúdo do arquivo CSV:")
    for linha in dados_csv:
        print(linha)
