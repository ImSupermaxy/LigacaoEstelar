import heapq
import configuracoes.variables as config

# Nós com posições (x, y)
nos = {
    "A": (100, 30),
    "B": (230, 90),
    "C": (270, 190),
    "D": (120, 130),
    "E": (180, 220),
    "F": (110, 400),
    "G": (200, 380),
    "H": (250, 300),
    "I": (320, 260),
    "J": (330, 100),
    "K": (450, 160),
    "L": (450, 220),
    "M": (550, 200),
    "N": (650, 150),
    "O": (610, 240),
    "P": (780, 160),
    "Q": (730, 350),
    "R": (710, 240),
    "S": (680, 420),
    "T": (800, 530),
    "U": (560, 420),
    "V": (680, 580),
    "W": (540, 510),
    "X": (450, 540),
    "Y": (450, 640),
    "Z": (300, 570),
    "AA": (120, 620),
    "AB": (210, 480),
    "AC": (300, 400),
    "AD": (410, 430),
    "AE": (480, 340),
    "AF": (500, 50),
    "AG": (710, 30),
    "AH": (860, 100),
    "AI": (820, 270),
    "AJ": (950, 40),
    "AK": (1090, 80),
    "AL": (930, 320),
    "AM": (830, 440),
    "AN": (1000, 410),
    "AO": (960, 190),
    "AP": (1100, 220),
    "AQ": (1120, 520),
    "AR": (980, 620),
    "AS": (820, 660),
    "AT": (630, 700),
    "AU": (340, 690)
}

arestas = {
    "A": [("D", 7)],
    "B": [("C", 4), ("D", 5)],
    "C": [("B", 4), ("E", 7), ("J", 5)],
    "D": [("A", 7), ("B", 5), ("E", 5), ("F", 4)],
    "E": [("C", 7), ("D", 5), ("G", 6)],
    "F": [("D", 4), ("G", 4), ("AA", 5)],
    "G": [("E", 6), ("F", 4), ("H", 5), ("AB", 4)],
    "H": [("G", 5), ("I", 3)],
    "I": [("H", 3), ("K", 4), ("L", 4)],
    "J": [("C", 5), ("K", 5), ("AF", 6)],
    "K": [("I", 4), ("J", 5), ("M", 4)],
    "L": [("I", 4), ("AE", 7)],
    "M": [("K", 4), ("N", 8), ("O", 3), ("AE", 4), ("AG", 7)],
    "N": [("M", 8), ("P", 6), ("AF", 8)],
    "O": [("M", 3), ("Q", 6)],
    "P": [("N", 6), ("R", 7), ("AH", 6)],
    "Q": [("O", 6), ("R", 4), ("S", 5), ("AN", 7)],
    "R": [("P", 7), ("Q", 4), ("U", 5), ("AI", 5)],
    "S": [("Q", 5), ("T", 5), ("AM", 6)],
    "T": [("S", 5), ("V", 5), ("W", 8), ("AS", 6)],
    "U": [("R", 5), ("V", 7), ("AD", 4), ("AE", 5)],
    "V": [("T", 5), ("U", 7), ("Y", 5), ("AS", 8)],
    "W": [("T", 8), ("X", 4)],
    "X": [("W", 4), ("Y", 3), ("Z", 3)],
    "Y": [("V", 5), ("X", 3), ("AA", 4), ("AT", 6), ("AU", 5)],
    "Z": [("X", 3), ("AA", 6), ("AB", 4), ("AC", 6)],
    "AA": [("F", 5), ("Y", 4), ("Z", 6)],
    "AB": [("G", 4), ("Z", 4)],
    "AC": [("Z", 6), ("AD", 7), ("AE", 6)],
    "AD": [("U", 4), ("AC", 7)],
    "AE": [("L", 7), ("M", 4), ("U", 5), ("AC", 6)],
    "AF": [("J", 6), ("N", 8)],
    "AG": [("M", 7), ("AH", 8), ("AJ", 7)],
    "AH": [("P", 6), ("AG", 8), ("AK", 5)],
    "AI": [("R", 5), ("AL", 5), ("AO", 6)],
    "AJ": [("AG", 7), ("AK", 4)],
    "AK": [("AH", 5), ("AJ", 4), ("AO", 5)],
    "AL": [("AI", 5), ("AP", 4)],
    "AM": [("S", 6), ("AN", 5), ("AQ", 6)],
    "AN": [("Q", 7), ("AM", 5), ("AP", 6)],
    "AO": [("AI", 6), ("AK", 5)],
    "AP": [("AL", 4), ("AN", 6)],
    "AQ": [("AM", 6), ("AR", 5)],
    "AR": [("AQ", 5), ("AS", 7)],
    "AS": [("T", 6), ("V", 8), ("AR", 7), ("AT", 6)],
    "AT": [("Y", 6), ("AS", 6), ("AU", 7)],
    "AU": [("Y", 5), ("AT", 7)]
}

graph = {
    "A": ["D"],
    "B": ["C", "D"],
    "C": ["B", "E", "J"],
    "D": ["A", "B", "E", "F"],
    "E": ["C", "D", "G"],
    "F": ["D", "G", "AA"],
    "G": ["E", "F", "H", "AB"],
    "H": ["G", "I"],
    "I": ["H", "K", "L"],
    "J": ["C", "K", "AF"],
    "K": ["I", "J", "M"],
    "L": ["I", "AE"],
    "M": ["K", "N", "O", "AE", "AG"],
    "N": ["M", "P", "AF"],
    "O": ["M", "Q"],
    "P": ["N", "R", "AH"],
    "Q": ["O", "R", "S", "AN"], 
    "R": ["P", "Q", "U", "AI"],
    "S": ["Q", "T", "AM"],
    "T": ["S", "V", "W", "AS"],
    "U": ["R", "V", "AD", "AE"],
    "V": ["T", "U", "Y", "AS"],
    "W": ["T", "X"],
    "X": ["W", "Y", "Z"],
    "Y": ["V", "X", "AA", "AT", "AU"],
    "Z": ["X", "AA", "AB", "AC"],
    "AA": ["F", "Y", "Z"],
    "AB": ["G", "Z"],
    "AC": ["Z", "AD", "AE"],
    "AD": ["U", "AC"],
    "AE": ["L", "M", "U", "AC"],
    "AF": ["J", "N"],
    "AG": ["M", "AH", "AJ"],
    "AH": ["P", "AG", "AK"],
    "AI": ["R", "AL", "AO"],
    "AJ": ["AG", "AK"],
    "AK": ["AH", "AJ", "AO"],
    "AL": ["AI", "AP"],
    "AM": ["S", "AN", "AQ"],
    "AN": ["Q", "AM", "AP"],
    "AO": ["AI", "AK"],
    "AP": ["AL", "AN"],
    "AQ": ["AM", "AR"],
    "AR": ["AQ", "AS"],
    "AS": ["T", "V", "AR", "AT"],
    "AT": ["Y", "AS", "AU"],
    "AU": ["Y", "AT"]
}


def dijkstra(grafo, inicio, destino):
    fila = [(0, inicio, [inicio])]  # (custo_acumulado, nó_atual, caminho)
    visitado = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)

        if atual == destino:
            return caminho, custo  #Caminho e custo total

        if atual in visitado:
            continue
        visitado.add(atual)

        for vizinho, peso in grafo[atual]:
            if vizinho not in visitado:
                heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))

    return None, float('inf')  # Caso não encontre caminho


def calcula_peso_arestas(grafo, visitados, v_final):
    soma = 0
    
    # Desenha as arestas
    for i, item in enumerate(grafo.items()):
        (comeco, vizinhos) = item
        if comeco in visitados:
            if comeco != v_final:
                for item2 in vizinhos:
                    (vertice, peso) = item2
                    soma += peso
    return soma


def get_linhas_visitadas(vertices_visitados):
    edges = set()
    
    for i, vertice in enumerate(vertices_visitados):
        if vertice != vertices_visitados[-1]:
            edge = tuple(sorted((vertice, vertices_visitados[i + 1])))
            edges.add(edge)
    
    return edges
    

def atualiza_dados_fase(fase_atual, visitados, soma, change_fase_atual=True):
    config.update_vertices_visitados(fase_atual, visitados)
    config.update_soma_fase(fase_atual, soma)
    config.update_total(fase_atual)
    
    if config.fases_auto_atualiza and change_fase_atual:
        config.update_fase_atual(fase_atual + 1)