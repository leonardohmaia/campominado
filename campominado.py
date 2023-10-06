import random

def criar_tabuleiro(linhas, colunas, minas):
    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]
    for _ in range(minas):
        while True:
            linha = random.randint(0, linhas - 1)
            coluna = random.randint(0, colunas - 1)
            if tabuleiro[linha][coluna] != "*":
                tabuleiro[linha][coluna] = "*"
                break
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * len(linha) - 1))

def contar_minas_vizinhas(tabuleiro, linha, coluna):
    minas_vizinhas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= linha + i < len(tabuleiro) and 0 <= coluna + j < len(tabuleiro[0]) and tabuleiro[linha + i][coluna + j] == "*":
                minas_vizinhas += 1
    return minas_vizinhas

def revelar_celulas_vizinhas(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] != " ":
        return
    minas_vizinhas = contar_minas_vizinhas(tabuleiro, linha, coluna)
    tabuleiro[linha][coluna] = str(minas_vizinhas)
    if minas_vizinhas == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= linha + i < len(tabuleiro) and 0 <= coluna + j < len(tabuleiro[0]):
                    revelar_celulas_vizinhas(tabuleiro, linha + i, coluna + j)

def jogar_campo_minado():
    linhas = int(input("Digite o número de linhas do tabuleiro: "))
    colunas = int(input("Digite o número de colunas do tabuleiro: "))
    minas = int(input("Digite o número de minas: "))

    tabuleiro = criar_tabuleiro(linhas, colunas, minas)
    imprimir_tabuleiro(tabuleiro)

    while True:
        linha = int(input("Digite a linha para revelar: "))
        coluna = int(input("Digite a coluna para revelar: "))

        if tabuleiro[linha][coluna] == "*":
            print("Você perdeu! Fim de jogo.")
            break
        else:
            revelar_celulas_vizinhas(tabuleiro, linha, coluna)
            imprimir_tabuleiro(tabuleiro)

if __name__ == "__main__":
    jogar_campo_minado()
