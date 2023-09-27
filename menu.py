from times import nomeTimes, timesCadastrados, jogadores, jogadoresCadastrados
from tabela import lerTabela, encherTabela, lerArquivoJoadores, preencherJogadores, arquivoTabela, arquivoJogadores


def menu():
    while True:
        try:
            lines = "-" * 42
            msg = "TABELA BRASILEIRÃO 2023"
            calculo = (len(lines) - len(msg)) // 2
            print("-" * 42)
            print(" " * calculo + msg)
            print("-" * 42)

            print("1 - Ver Tabela")
            print("2 - Cadastrar Time")
            print("3 - Ver Jogadores Cadastrados")
            print("4 - Cadastrar Novo Jogador")
            print("5 - Sair")
            opcoes = int(input("Digite sua opção: "))
            return opcoes
        except ValueError:
            print("Digite apenas números!")


if __name__ == "__main__":
    tabela = lerTabela()
    jogamt = lerArquivoJoadores()
while True:
    teste = menu()
    if teste == 1:
        timesCadastrados(tabela)
        ultimoArquivoModificado = arquivoTabela
    if teste == 2:
        tabela = nomeTimes(tabela)
        encherTabela(tabela)
        ultimoArquivoModificado = arquivoTabela
    if teste == 3:
        jogadoresCadastrados(jogamt)
        ultimoArquivoModificado = arquivoJogadores
    if teste == 4:
        tabela = jogadores(jogamt)
        preencherJogadores(jogamt)
        ultimoArquivoModificado = arquivoJogadores
    if teste == 5:
        print("Obrigado!")
        break
