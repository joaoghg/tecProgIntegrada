def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

nome_arquivo = "exemplo.txt"
conteudo_arquivo = ler_arquivo(nome_arquivo)
if conteudo_arquivo:
    print("Conteúdo do arquivo:")
    print(conteudo_arquivo)
