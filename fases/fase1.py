import pygame # type: ignore
import math

# pygame.init()
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Ligação Estelar")

def primeira_fase_iniciar(screen, WIDTH, opcoes_logicas_busca, logica_busca_grafo):
    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)
    BLUE = (50, 100, 255)
    GRAY = (180, 180, 180)

    font = pygame.font.SysFont(None, 32)

    # Nós (posições)
    nodes = {
        0: (100, 300),
        1: (250, 150),
        2: (250, 450),
        3: (500, 150),
        4: (500, 450),
        5: (300, 300)
    }

    # Conexões (grafo não-direcionado)
    graph = {
        0: [1, 2],
        1: [0, 3, 5],
        2: [0, 4, 5],
        3: [1, 4],
        4: [2, 3],
        5: [1, 2]
    }

    # Estado
    current_node = 0
    visited_nodes = set([current_node])
    visited_edges = set()
    NODE_RADIUS = 25

    def draw_graph(screen):
        screen.fill(BLACK)

        # Desenhar conexões possíveis
        for start, neighbors in graph.items():
            for end in neighbors:
                if (end, start) not in visited_edges and (start, end) not in visited_edges:
                    pygame.draw.line(screen, GRAY, nodes[start], nodes[end], 2)

        # Desenhar conexões feitas
        for a, b in visited_edges:
            pygame.draw.line(screen, BLUE, nodes[a], nodes[b], 4)

        # Desenhar nós
        for node_id, pos in nodes.items():
            color = GREEN if node_id in visited_nodes else RED
            pygame.draw.circle(screen, color, pos, NODE_RADIUS)
            pygame.draw.circle(screen, BLACK, pos, NODE_RADIUS, 2)

        # Mostrar nó atual
        text = font.render(f"Nó atual: {current_node}", True, BLACK)
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
        draw_graph(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if all_nodes_visited():
                    text = font.render("Todos os nós foram visitados!", True, WHITE)
                    screen.blit(text, (WIDTH // 2 - 200, 50))
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