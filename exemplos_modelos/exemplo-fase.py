import pygame # type: ignore
import math
import main
from menu import menu
import configuracoes.variables as config

def primeira_fase_iniciar():
    # Nós (posições)
    nodes = {
        0: (100, 300),
        1: (250, 150),
        2: (250, 450),
        3: (500, 150),
        4: (500, 450),
        5: (300, 300),
        6: (200, 650),
        7: (450, 600),
        8: (650, 500),
        9: (650, 250),
        10: (600, 350),
        11: (650, 600),
        12: (750, 550),
        13: (750, 500)
    }

    # Conexões (grafo não-direcionado)
    graph = {
        0: [1, 2, 6],
        1: [0, 3, 5],
        2: [0, 4, 5],
        3: [1, 4, 6, 9],
        4: [2, 3, 6, 8],
        5: [1, 2, 7, 9, 10],
        6: [0, 3, 4, 7],
        7: [5, 6, 8, 10, 12],
        8: [4, 7, 11],
        9: [3, 5],
        10: [5, 7, 10, 12],
        11: [8, 12],
        12: [7, 10, 11, 13],
        13: [12]
    }

    # Estado
    current_node = 0
    visited_nodes = set([current_node])
    visited_edges = set()
    NODE_RADIUS = 14

    def draw_graph(screen):
        config.TELA.fill(config.BACKGROUND_JOGO)

        # Desenhar conexões possíveis
        for start, neighbors in graph.items():
            for end in neighbors:
                if (end, start) not in visited_edges and (start, end) not in visited_edges:
                    pygame.draw.line(screen, config.CINZA, nodes[start], nodes[end], 2)

        # Desenhar conexões feitas
        for a, b in visited_edges:
            pygame.draw.line(screen, config.AZUL, nodes[a], nodes[b], 4)

        # Desenhar nós
        for node_id, pos in nodes.items():
            color = config.VERMELHO if node_id in visited_nodes else config.VERDE
            pygame.draw.circle(screen, color, pos, NODE_RADIUS)
            pygame.draw.circle(screen, config.PRETO, pos, NODE_RADIUS, 2)

        # Mostrar nó atual
        if config.IsDevVar:
            text = config.FONTE_GRAFO.render(f"Nó atual: {current_node}", True, config.COR_TEXTO)
            screen.blit(text, (10, 10))

        pygame.display.flip()

    def get_node_clicked(pos):
        for node_id, node_pos in nodes.items():
            dist = math.hypot(pos[0] - node_pos[0], pos[1] - node_pos[1])
            if dist <= NODE_RADIUS:
                return node_id
        return None

    def all_nodes_visited():
        return len(visited_nodes) == len(nodes)


    running = True
    while running:
        draw_graph(config.TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.fechar_jogo()

            if all_nodes_visited():
                    running = False
                    text = config.FONTE_GRAFO.render("Todos os nós foram visitados!", True, config.BRANCO)
                    config.TELA.blit(text, (config.LARGURA // 2 - 200, 50))
                    pygame.display.flip()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_node = get_node_clicked(event.pos)
                if clicked_node is not None:
                    if clicked_node in graph[current_node]:
                        edge = tuple(sorted((current_node, clicked_node)))
                        if edge not in visited_edges:
                            visited_edges.add(edge)
                        visited_nodes.add(clicked_node)
                        current_node = clicked_node
                    else:
                        print("Movimento inválido: esse nó não é vizinho do atual.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.inicar_menu(False)
                
    
    texto_final_fase = "Aperte ESPAÇO para pular..."      
    main.aguardar(texto_final_fase, largura=((config.LARGURA // 2) - 150), altura=config.ALTURA-200)
    #Mostrar final da primeira fase
    #Ir para a fase 2