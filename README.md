4.1. DESCRIÇÃO DO PROBLEMA PRÁTICO

Imagine-se um jogo em que uma personagem está no canto superior esquerdo de um tabuleiro e quer chegar ao tesouro, no canto inferior direito. Existe uma parede no meio, por onde não pode passar. A personagem move-se um quadrado de cada vez (para cima, para baixo, para a esquerda ou para a direita), e cada passo custa 1.
O problema consiste em descobrir o caminho mais curto até ao tesouro, sem explorar quadrados desnecessários. O tabuleiro tem 6 linhas e 6 colunas (36 quadrados), dos quais 4 são parede e 32 são livres. Os símbolos usados são: S (partida), G (chegada), # (parede) e . (chão livre).

O A* seguiu pela margem superior e pela margem direita do tabuleiro, contornando a parede sem hesitar, e explorou apenas 11 dos 32 quadrados livres. Um caminho igualmente curto pela esquerda e por baixo também existiria, pois há vários caminhos óptimos com 10 passos; o algoritmo escolhe um deles devido à regra de desempate.
