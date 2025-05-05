import pygame
import sys
import configuracoes.variables as config
import main
import menu.menu as menu
import math
import fases.final_fase as desenha_final

def primeira_fase_iniciar():
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
        "AE": (480, 340)
    }

    # Arestas no formato: (nó1, nó2, peso)
    arestas = { #Mudar para dict...
        "A": [("B", -15), ("D", 5)],
        "B": [("A", -15), ("C", 2), ("D", 3)],
        "C": [("B", 2), ("E", 5), ("J", 3)],
        "D": [("A", 5), ("B", 3), ("E", 3), ("F", 2)],
        "E": [("C", 5), ("D", 3), ("G", 4)],
        "F": [("D", 2), ("G", 2), ("AA", 3)],
        "G": [("E", 4), ("F", 2), ("H", 3), ("AB", 2)],
        "H": [("G", 3), ("I", 1)],
        "I": [("H", 1), ("K", 2), ("L", 2)],
        "J": [("C", 3), ("K", 3)],
        "K": [("I", 2), ("J", 3), ("M", 2)],
        "L": [("I", 2), ("AE", 5)],
        "M": [("K", 2), ("N", 6), ("O", 1), ("AE", 2)],
        "N": [("M", 6), ("P", 4)],
        "O": [("M", 1), ("Q", 4)],
        "P": [("N", 4), ("R", 5)],
        "Q": [("O", 4), ("R", 2), ("S", 3)],
        "R": [("P", 5), ("Q", 2), ("U", 3)],
        "S": [("Q", 3), ("T", 3)],
        "T": [("S", 3), ("V", 3), ("W", 6)],
        "U": [("R", 3), ("V", 5), ("AD", 2), ("AE", 3)],
        "V": [("T", 3), ("U", 5), ("Y", 3)],
        "W": [("T", 6), ("X", 2)],
        "X": [("W", 2), ("Y", 1), ("Z", 1)],
        "Y": [("V", 3), ("X", 1), ("AA", 2)],
        "Z": [("X", 1), ("AA", 4), ("AB", 2), ("AC", 4)],
        "AA": [("F", 3), ("Y", 2), ("Z", 4)],
        "AB": [("G", 2), ("Z", 2)],
        "AC": [("Z", 4), ("AD", 5), ("AE", 4)],
        "AD": [("U", 2), ("AC", 5)],
        "AE": [("L", 5), ("M", 2), ("U", 3), ("AC", 4)]
    }
    
    graph = {
        "A": ["D", "B"],
        "B": ["A", "C", "D"],
        "C": ["B", "E", "J"],
        "D": ["A", "B", "E", "F"],
        "E": ["C", "D", "G"],
        "F": ["D", "G", "AA"],
        "G": ["E", "F", "H", "AB"],
        "H": ["G", "I"],
        "I": ["H", "K", "L"],
        "J": ["C", "K"],
        "K": ["I", "J", "M"],
        "L": ["I", "AE"],
        "M": ["K", "N", "O"],
        "N": ["M", "P"],
        "O": ["M", "Q"],
        "P": ["N", "R"],
        "Q": ["O", "R", "S"],
        "R": ["P", "Q", "U"],
        "S": ["Q", "T"],
        "T": ["S", "V", "W"],
        "U": ["R", "V", "AD", "AE"],
        "V": ["T", "U", "Y"],
        "W": ["T", "X"],
        "X": ["W", "Y", "Z"],
        "Y": ["V", "X", "AA"],
        "Z": ["X", "AA", "AB", "AC"],
        "AA": ["F", "Y", "Z"],
        "AB": ["G", "Z"],
        "AC": ["Z", "AD", "AE"],
        "AD": ["U", "AC"],
        "AE": ["L", "M", "U", "AC"]
    }

    # Estado
    inicial_node = "I"
    final_node = "T"
    current_node = inicial_node
    visited_nodes = [current_node]
    visited_edges = set()
    NODE_RADIUS = 15
    soma_arestas = 0
        
    def desenhar_grafo():
        config.TELA.fill(config.BACKGROUND_JOGO)

        desenha_final.escreve_soma_peso_grafo(soma_arestas)
        
        # Desenha as arestas
        for comeco, vizinhos in arestas.items():
            for fim, peso in vizinhos:
                if (fim, comeco) not in visited_edges and (comeco, fim) not in visited_edges:
                    (x1, y1) = nos[comeco]
                    (x2, y2) = nos[fim]
                    pygame.draw.line(config.TELA, config.CINZA_CLARO, (x1, y1), (x2, y2), 2)

                    # Posição intermediária para o peso
                    px, py = (x1 + x2) // 2, (y1 + y2) // 2
                    texto = config.FONTE_PESO.render(str(peso), True, config.VERDE_ESCURO)
                    config.TELA.blit(texto, (px - texto.get_width() // 2, py - texto.get_height() // 2))

        # Desenhar conexões feitas
        for a, b in visited_edges:
            pygame.draw.line(config.TELA, config.AZUL, nos[a], nos[b], 4)
            desenha_peso(a, b)

        # Desenha os nós
        for nome, (x, y) in nos.items():
            color = config.AZUL_CLARO if nome == inicial_node else config.LARANJA if nome == final_node else config.VERMELHO if nome in visited_nodes else config.AMARELO
            pygame.draw.circle(config.TELA, color, (x, y), NODE_RADIUS)
            pygame.draw.circle(config.TELA, config.BRANCO, (x, y), NODE_RADIUS, 2)

            #validação pra ver se é dev, (pra exibir o nome das vertices...)
            if config.IsDevVar:
                texto = config.FONTE_GRAFO.render(nome, True, config.PRETO)
                config.TELA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

        pygame.display.update()


    def desenha_peso(a, b):
        x1, y1 = nos[a]
        x2, y2 = nos[b] 
        px, py = (x1 + x2) // 2, (y1 + y2) // 2
        peso = next((item for item in arestas[a] if item[0] == (b)), None)[1]
        texto = config.FONTE_PESO.render(str(peso), True, config.VERDE_ESCURO)
        config.TELA.blit(texto, (px - texto.get_width() // 2, py - texto.get_height() // 2))

    def get_node_clicked(pos):
        for node_id, node_pos in nos.items():
            dist = math.hypot(pos[0] - node_pos[0], pos[1] - node_pos[1])
            if dist <= NODE_RADIUS:
                return node_id
        return None


    def all_nodes_visited():
        return len(visited_nodes) == len(nos)
    
    def get_peso_aresta(clicked_node):
        for aresta in arestas[clicked_node]:
            if aresta[0] == current_node:
                return aresta[1]
    
    def letra_para_numero(letra: str) -> int:
        letra = letra.upper()
        resultado = 0
        for i, c in enumerate(reversed(letra)):
            resultado += (ord(c) - 64) * (26 ** i)
        return resultado


    def numero_para_letra(numero: int) -> str:
        resultado = ""
        while numero > 0:
            numero -= 1  # Ajuste para 1-indexado
            resultado = chr((numero % 26) + 65) + resultado
            numero //= 26
        return resultado

    last_clicked_node = visited_nodes[-1]
    rodando = True
    while rodando:
        desenhar_grafo()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.fechar_jogo()

            if all_nodes_visited():
                    rodando = False
                    text = config.FONTE_GRAFO.render("Todos os nós foram visitados!", True, config.BRANCO)
                    config.TELA.blit(text, (config.LARGURA // 2 - 200, 50))
                    pygame.display.flip()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_node = get_node_clicked(event.pos)
                if clicked_node is not None:
                    if clicked_node in graph[current_node]:
                        edge = tuple(sorted((current_node, clicked_node)))
                        if edge not in visited_edges and clicked_node not in visited_nodes:
                            visited_edges.add(edge)
                            soma_arestas += get_peso_aresta(clicked_node)
                        elif clicked_node == last_clicked_node:
                            visited_edges.remove(edge)
                            soma_arestas -= get_peso_aresta(clicked_node)
                        if clicked_node not in visited_nodes:
                            visited_nodes.append(clicked_node)
                            last_clicked_node = current_node
                            current_node = clicked_node
                        elif clicked_node == last_clicked_node:
                            visited_nodes.remove(current_node)
                            current_node = last_clicked_node
                            if last_clicked_node != inicial_node:
                                last_clicked_node = visited_nodes[-2]
                            else:
                                last_clicked_node = inicial_node
                        if clicked_node == final_node:
                            rodando = False
                    else:
                        print("Movimento inválido: esse nó não é vizinho do atual.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.inicar_menu(False)
    
    texto_final_fase = "Aperte ESPAÇO para pular..."
    # main.aguardar(texto_final_fase, cor=config.VERDE_ESCURO, largura=((config.LARGURA // 2) + 300), altura=config.ALTURA-200)
    soma_arestas_cpu = 20
    desenha_final.desenha_final_missao(soma_arestas, soma_arestas_cpu, [texto_final_fase])