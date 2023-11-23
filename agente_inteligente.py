from collections import deque

#A CLASSE NÓ QUEBRA CABECA CONTEM AS INFORMAÇÕES NECESSÁRIAS
class NoQuebraCabeca:
    def __init__(self, estado, pai=None, acao=None, custo=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

# VERIFICA SE O ESTADO É O ESTADO OBJETIVO
def eh_estado_objetivo(estado, estado_objetivo):
    return estado == estado_objetivo

# GERA OS VIZINHOS ALCANÇAVEIS A PARTIR DE UM DETERMINADO ESTADO
def obter_vizinhos(estado):
    vizinhos = []
    indice_vazio = estado.index(0)
    linha, coluna = indice_vazio // 3, indice_vazio % 3
    acoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in acoes:
        nova_linha, nova_coluna = linha + dr, coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_estado = estado[:]
            novo_indice = nova_linha * 3 + nova_coluna
            novo_estado[indice_vazio], novo_estado[novo_indice] = novo_estado[novo_indice], novo_estado[indice_vazio]
            vizinhos.append(novo_estado)

    return vizinhos

# A FUNCAO REALIZA UMA BUSCA EM LARGURA PARA ENCONTRAR A SOLUÇÃO DO QUEBRA-CABEÇA
def busca_em_largura(estado_inicial, estado_objetivo):
    fronteira = deque([NoQuebraCabeca(estado_inicial)])
    explorado = set()
    contagem_movimentos = 0

    while fronteira:
        no_atual = fronteira.popleft()
        estado_atual = no_atual.estado

        if eh_estado_objetivo(estado_atual, estado_objetivo):
            return obter_caminho_solucao(no_atual), no_atual.custo

        explorado.add(tuple(estado_atual))

        for proximo_estado in obter_vizinhos(estado_atual):
            if tuple(proximo_estado) not in explorado and not any(no.estado == proximo_estado for no in fronteira):
                novo_no = NoQuebraCabeca(proximo_estado, no_atual, obter_acao_movimento(estado_atual, proximo_estado), no_atual.custo + 1)
                fronteira.append(novo_no)
                contagem_movimentos += 1

    return None, 0

# FUNÇÃO QUE RECONSTROI O CAMINHO DA SOLUÇÃO A PARTIR DO NÓ FINAL
def obter_caminho_solucao(no):
    caminho = []
    while no.pai:
        caminho.append((no.acao, no.estado))
        no = no.pai
    return list(reversed(caminho))

# DETERMINA A AÇÃO ASSOCIADA A UM MOVIMENTO ENTRE DOIS ESTADOS
def obter_acao_movimento(estado_anterior, proximo_estado):
    indice_vazio_anterior = estado_anterior.index(0)
    indice_vazio_proximo = proximo_estado.index(0)
    linha_anterior, coluna_anterior = indice_vazio_anterior // 3, indice_vazio_anterior % 3
    linha_proximo, coluna_proximo = indice_vazio_proximo // 3, indice_vazio_proximo % 3

    if linha_proximo < linha_anterior:
        return "Moveu para cima"
    elif linha_proximo > linha_anterior:
        return "Moveu para baixo"
    elif coluna_proximo < coluna_anterior:
        return "Moveu para a esquerda"
    elif coluna_proximo > coluna_anterior:
        return "Moveu para a direita"

# IMPRIME O ESTADO ATUAL DO QUEBRA CABEÇA
def imprimir_estado_quebra_cabeca(estado):
    for i in range(0, len(estado), 3):
        print(estado[i:i+3])

#ESTADO DO QUEBRA CABECA
estado_inicial = [0, 1, 3, 7, 4, 6, 5, 8, 2]
estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# CHAMA A FUNÇÃO BUSCA LARGURA E ARMAZENA A CONTAGEM DOS MOVIMENTOS
caminho_solucao, contagem_movimentos = busca_em_largura(estado_inicial, estado_objetivo)

print("\nEstado Inicial:")
imprimir_estado_quebra_cabeca(estado_inicial)

if caminho_solucao:
    print("\nSolução encontrada:")
    for acao, estado in caminho_solucao:
        print(f"Ação: {acao}")
        imprimir_estado_quebra_cabeca(estado)
        print()
else:
    print("\nNão foi possível encontrar uma solução.")

print(f"Número Total de Movimentos: {contagem_movimentos}")