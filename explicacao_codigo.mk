# Quebra-Cabeça de 8 Peças com Busca em Largura

## Introdução
Este projeto implementa um agente inteligente para resolver o quebra-cabeça de 8 peças. O agente utiliza busca em largura para encontrar a solução, permitindo que o usuário escolha o estado inicial do quebra-cabeça.

## Estrutura do Projeto
O código está dividido em seções distintas, cada uma responsável por uma parte específica do projeto:

### Classes
- **`NoQuebraCabeca`**: Representa um nó no espaço de estados do quebra-cabeça, armazenando informações como o estado atual, o nó pai, a ação tomada e o custo.

### Funções Principais
- **`eh_estado_objetivo`**: Verifica se um determinado estado é o estado objetivo.
- **`obter_vizinhos`**: Gera os estados vizinhos alcançáveis a partir de um determinado estado.
- **`busca_em_largura`**: Realiza a busca em largura para encontrar a solução do quebra-cabeça.

### Funções Auxiliares
- **`obter_caminho_solucao`**: Reconstrói o caminho da solução a partir do nó final.
- **`obter_acao_movimento`**: Determina a ação associada a um movimento entre dois estados.
- **`imprimir_estado_quebra_cabeca`**: Imprime o estado atual do quebra-cabeça em um formato legível.

## Exemplo de Execução
```python
# Exemplo de uso
estado_inicial = obter_estado_inicial()
print("\nEstado Inicial:")
imprimir_estado_quebra_cabeca(estado_inicial)

caminho_solucao, contagem_movimentos = busca_em_largura(estado_inicial, estado_objetivo)

if caminho_solucao:
    print("\nSolução encontrada:")
    for acao, estado in caminho_solucao:
        print(f"Ação: {acao}")
        imprimir_estado_quebra_cabeca(estado)
        print()
else:
    print("\nNão foi possível encontrar uma solução.")

print(f"Número Total de Movimentos: {contagem_movimentos}")