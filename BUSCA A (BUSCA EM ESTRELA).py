import heapq

mapa = ["S.....",
        "......",
        "..##..",
        "..##..",
        "......",
        ".....G"]
inicio, fim = (0, 0), (5, 5)

def h(p):                                  # quantos quadrados faltam
    return abs(p[0] - fim[0]) + abs(p[1] - fim[1])

fila = [(h(inicio), h(inicio), inicio)]    # (f, h, posição)
veio_de = {inicio: None}
custo = {inicio: 0}

while fila:
    f, _, atual = heapq.heappop(fila)      # pega o melhor quadrado
    if atual == fim:
        break
    g = custo[atual]
    for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        l, c = atual[0] + dl, atual[1] + dc
        if 0 <= l < 6 and 0 <= c < 6 and mapa[l][c] != "#":
            if (l, c) not in custo or g + 1 < custo[(l, c)]:
                custo[(l, c)] = g + 1
                veio_de[(l, c)] = atual
                heapq.heappush(fila, (g + 1 + h((l, c)), h((l, c)), (l, c)))

caminho = []                               # volta de G até S
p = fim
while p:
    caminho.append(p)
    p = veio_de[p]

print("Passos:", len(caminho) - 1)
for l in range(6):
    print(" ".join("*" if (l, c) in caminho and mapa[l][c] == "." else mapa[l][c] for c in range(6)))