import os

def consolidar_arquivos(diretorio, arquivo_destino):
    try:
        with open(arquivo_destino, 'w') as arquivo_destino:
            for nome_arquivo in os.listdir(diretorio):
                if nome_arquivo.endswith(".txt"):
                    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                    with open(caminho_arquivo, 'r') as arquivo_origem:
                        conteudo_arquivo = arquivo_origem.read()
                    arquivo_destino.write(conteudo_arquivo + "\n")
        print(f"A consolidação dos arquivos do diretório '{diretorio}' foi concluída com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao consolidar os arquivos: {e}")

diretorio = "C:/"
arquivo_destino = "consolidado.txt"
consolidar_arquivos(diretorio, arquivo_destino)
