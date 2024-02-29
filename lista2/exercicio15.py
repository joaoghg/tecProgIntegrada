import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")
        return None

nome_arquivo_json = "dados.json"
dados_json = ler_arquivo_json(nome_arquivo_json)
if dados_json:
    print("Conteúdo do arquivo JSON:")
    print(dados_json)
