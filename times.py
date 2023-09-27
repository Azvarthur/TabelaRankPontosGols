def isValidPontos(pontos):
    if pontos.startswith('-') and pontos[1:].isdigit():
        return True
    elif pontos.isdigit():
        return True
    else:
        return False


def nomeTimes(tabela):
    try:
        linhas = "-" * 42
        msg = "Novo cadastro".upper()
        calculo = (len(linhas) - len(msg)) // 2
        print("-" * 42)
        print(" " * calculo + msg)
        print("-" * 42)

        while True:
            nome = str(input("Nome do time: "))
            if all(x.isalpha() or x.isspace() for x in nome):
                break
            else:
                print("Apenas letras!")

        tabela.append(nome)

        while True:
            pontos = input("Pontos atuais: ")
            if pontos.isdigit():
                break
            else:
                print("Apenas números ou '-' para pontos negativos!")

        pontos = int(pontos)
        tabela.append(pontos)

        while True:
            gols = input("Saldo de Gols: ")
            if isValidPontos(gols):
                break
            else:
                print("Apenas números!")

        gols = int(gols)
        tabela.append(gols)

        print(f"{nome} foi adicionado à tabela!")
        return tabela

    except ValueError as error:
        print(error)
    return tabela


def timesCadastrados(tabela):
    if not tabela:
        print("Ainda não existe nenhum time cadastrado!")
    else:
        timePontos = list(zip(tabela[::3], tabela[1::3], tabela[2::3]))
        timePontos.sort(
            key=lambda x: (-int(x[1]), -int(x[2])))  # lambda para especificar que a ordenação deve ser feita com
        # base no segundo elemento de cada sublista. A função lambda recebe um argumento x (que representa um elemento da
        # lista timePontos) e retorna x[1], ou seja, o segundo elemento desse elemento da lista. Isso significa que a lista
        # será ordenada com base nos valores do segundo elemento de cada sublista.
        # O -int(x[1]) e -int(x[2]) são os valores que serão buscados dentro da lista de forma ordenada decrescente - é usado para inverter a ordem.
        # o x[2] é para em caso de emparte por pontos x[1] o x[2] ordenara por saldo de gols.
        # não preciso usar rever=True pois a ordem já é tratada pela função key.
        lines = "-" * 42
        msg = "TABELA ATUAL"
        calculo = (len(lines) - len(msg)) // 2
        print("-" * 42)
        print(" " * calculo + msg)
        print("-" * 42)
        print("Tabela Atual: ")
        for nome, pontos, gols in timePontos:
            print(f"Time: {nome}. Pontos {pontos}. Saldo de Gols: {gols}")


def jogadores(jogamt):
    linhas = "-" * 42
    msg = "Novo jogador: ".upper()
    calculo = (len(linhas) - len(msg)) // 2
    print("-" * 42)
    print(" " * calculo + msg)
    print("-" * 42)
    try:
        while True:
            jogadorTime = input("Time: ").title()
            if all(y.isalpha() or y.isspace for y in jogadorTime):
                break
            else:
                print("Apenas letras!")
        jogamt.append(jogadorTime)

        while True:
            nomeJogador = str(input("Nome do jogador: "))
            if all(z.isalpha() or z.isspace for z in nomeJogador):
                break
            else:
                print("Apenas letras!")

        jogamt.append(nomeJogador)

        while True:
            golsJoador = input("Gols marcados: ")
            if golsJoador.isdigit():
                break
            else:
                print("Apenas números!")

        golsJoador = int(golsJoador)
        jogamt.append(golsJoador)

        return jogamt
    except ValueError as error:
        print(error)

    return jogamt


def jogadoresCadastrados(jogamt):
    if not jogamt:
        print("Ainda não existe nenhum jogador cadastrado!")
    else:
        jogadorGols = list(zip(jogamt[::3], jogamt[1::3], jogamt[2::3]))
        jogadorGols.sort(key=lambda x: int(x[2]), reverse=True)
        lines = "-" * 42
        msg = "TABELA ATUAL"
        calculo = (len(lines) - len(msg)) // 2
        print("-" * 42)
        print(" " * calculo + msg)
        print("-" * 42)
        for time, nome, gols in jogadorGols:
            print(f"Time: {time}. Nomes: {nome}. Gols: {gols}")
