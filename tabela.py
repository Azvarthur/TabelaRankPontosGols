import os

arquivoTabela = "tabela.txt"
arquivoJogadores = "jogadores.txt"
ultimoArquivoModificado = None

def lerTabela():
    if os.path.exists(arquivoTabela):
        with open(arquivoTabela, 'r') as arquivo:
            return arquivo.read().splitlines()
    else:
        return []


def encherTabela(tabela):
    if ultimoArquivoModificado == arquivoTabela: #verificar se o arquivo está certo
        listToString = map(str, tabela)

        with open(arquivoTabela, 'w') as arquivo:
            arquivo.write("\n".join(listToString))



def lerArquivoJoadores():
    if os.path.exists(arquivoJogadores):
        with open(arquivoJogadores, "r") as jogadores:
            return jogadores.read().splitlines()
    else:
        return []



def preencherJogadores(jogamt):
    if ultimoArquivoModificado == arquivoJogadores: #verificar se o arquivo está certo
        listaParaString = map(str, jogamt)

        with open(arquivoJogadores, "w") as jogadores:
            jogadores.write("\n".join(listaParaString))
