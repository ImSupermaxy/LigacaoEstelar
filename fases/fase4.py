import pygame
import sys
import configuracoes.variables as config
import main
import menu.menu as menu
import math
import fases.final_fase as desenha_final
import copy
from fases.grafo import nos, arestas, graph, dijkstra, atualiza_dados_fase, calcula_peso_arestas, get_linhas_visitadas
import assets.audios.manipuleraudio as maudio
from historia import game_over as go

local_nos = copy.deepcopy(nos)
local_arestas = copy.deepcopy(arestas)
local_graph = copy.deepcopy(graph)

# Estado
# inicial_node = fase2.final_node
inicial_node = "AJ"
final_node = "Y"
current_node = inicial_node
visited_nodes = [current_node]
visited_edges = set()
NODE_RADIUS = 15
soma_arestas = 0
atual_fase = 4

texto_introducao_fase = [
    "\"Sabe... nunca entendi direito como a humanidade chegou onde está hoje. Nem nas aulas de história isso fazia sentido.\"",
    "Você dá uma risada curta. ",
    "\"Eu posso te contar. Sei um pouco por causa do meu antigo trabalho.\" No início, não existia esse ",
    "domínio do espaço e nem a divisão entre planetas. Mas a falta de cuidado com o próprio lar sempre ",
    "esteve lá. O que vemos agora no espaço já acontecia — em escala maior — e num só planeta. ",
    "Depois de muito tempo negligenciando a Terra, ela entrou num estado irreversível, praticamente ",
    "inabitável. As grandes potências mundiais, então, começaram a construir foguetes para evacuar o ",
    "planeta. Mas, como sempre, as divergências políticas falaram mais alto. Cada nação decidiu colonizar ",
    "um planeta diferente, e assim a humanidade acabou espalhada — e em constante conflito. ",
    "Mas, obviamente, em poucos lugares isso é contado dessa forma. Revelar que as raízes da sociedade ",
    "atual destruíram o primeiro planeta habitado pela humanidade gera desconfiança demais no sistema ",
    "em que todos vivem. ",
    "Bip. Bip. Bip. ",
    "Algo apita do outro lado do rádio. Dá pra ouvir Raphael empurrando a cadeira, deslizando até o outro ",
    "lado da cabine, e logo depois retornando ao comunicador. \"Vamos ter que deixar a hora da história ",
    "pra depois.\" — ele diz, em tom de desapontamento. — \"Temos mais uma missão pra fazer.\" ",
    "Você liga a nave. Os sistemas ganham vida e, sem pensar muito, parte para mais um dia de trabalho. "
]

def reset():
    global inicial_node
    global final_node
    global current_node
    global visited_nodes
    global visited_edges
    global soma_arestas
    
    # inicial_node = fase2.final_node
    inicial_node = "AJ"
    final_node = "Y"
    current_node = inicial_node
    visited_nodes = [current_node]
    visited_edges = set()
    soma_arestas = 0
   
    
def update_grafo(vertices_visitados, end=False):
    global local_arestas
    if not config.OPEN_FASE_FOUR:
        for i, vertice in enumerate(vertices_visitados):
            ligacao_vertices = local_arestas[vertice]
            for j, dict in enumerate(ligacao_vertices):
                (vertice2, peso) = dict
                if vertice2 != vertices_visitados[-1] and peso >= 1:
                    if i + 1 < len(vertices_visitados) and vertice2 == vertices_visitados[i + 1]:
                        local_arestas[vertice][j] = (vertice2, peso - 1)
                        for u, dict2 in enumerate(local_arestas[vertice2]):
                            (vertice3, peso2) = dict2
                            if vertice3 == vertice:
                                local_arestas[vertice2][u] = (vertice3, peso - 1)
        if end:
            config.OPEN_FASE_FOUR = True 


def desenhar_grafo():
    config.TELA.fill(config.BACKGROUND_JOGO)
    main.desenhar_textos(["FASE 4"], config.ROXO2, 25, config.LARGURA - 140, False, config.FONTE_PESO)
    
    desenha_final.escreve_info_pesos(soma_arestas)
    
    # Desenha as arestas
    for comeco, vizinhos in local_arestas.items():
        for fim, peso in vizinhos:
            if (fim, comeco) not in visited_edges and (comeco, fim) not in visited_edges:
                (x1, y1) = local_nos[comeco]
                (x2, y2) = local_nos[fim]
                pygame.draw.line(config.TELA, config.CINZA_CLARO, (x1, y1), (x2, y2), 2)
                # Posição intermediária para o peso
                px, py = (x1 + x2) // 2, (y1 + y2) // 2
                texto = config.FONTE_PESO.render(str(peso), True, config.VERDE_ESCURO)
                config.TELA.blit(texto, (px - texto.get_width() // 2, py - texto.get_height() // 2))
    # Desenhar conexões feitas
    for a, b in visited_edges:
        pygame.draw.line(config.TELA, config.ROXO2, local_nos[a], local_nos[b], 4)
        desenha_peso(a, b)
    # Desenha os nós
    for nome, (x, y) in local_nos.items():
        color = config.VERDE_INICIAL if nome == inicial_node else config.CINZA_FINAL if nome == final_node else config.ROSA2 if nome in visited_nodes else config.AZUL_CLARO2
        pygame.draw.circle(config.TELA, color, (x, y), NODE_RADIUS)
        
        #validação pra ver se é dev, (pra exibir o nome das vertices...)
        if config.IsDevVar:
            texto = config.FONTE_GRAFO.render(nome, True, config.PRETO)
            config.TELA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))
    pygame.display.update()


def desenha_peso(a, b):
    x1, y1 = local_nos[a]
    x2, y2 = local_nos[b] 
    px, py = (x1 + x2) // 2, (y1 + y2) // 2
    peso = next((item for item in local_arestas[a] if item[0] == (b)), None)[1]
    texto = config.FONTE_PESO.render(str(peso), True, config.BRANCO)
    config.TELA.blit(texto, (px - texto.get_width() // 2, py - texto.get_height() // 2))


def get_node_clicked(pos):
    for node_id, node_pos in local_nos.items():
        dist = math.hypot(pos[0] - node_pos[0], pos[1] - node_pos[1])
        if dist <= NODE_RADIUS:
            return node_id
    return None


def all_nodes_visited():
    return len(visited_nodes) == len(local_nos)


def get_peso_aresta(clicked_node):
    global current_node
    
    for aresta in local_arestas[clicked_node]:
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


def escreve_introducao_final_fase(texto):
    config.TELA.fill(config.BACKGROUND_JOGO)
    main.pygame.display.update()
    main.pygame.time.delay(600)
    
    altura_historia = config.PADDING_TOP_HISTORIA
    linhas_mostradas = []
    delay_linha = 40
    delay_paragrafo = 580
    emit_sound = True
    for i, paragrafo in enumerate(texto):
        pular = main.digitar_lento(paragrafo, linhas_mostradas, delay_linha, altura=altura_historia, som=emit_sound)
        linhas_mostradas.append(paragrafo)
        if pular:
            emit_sound = False
            delay_linha = 0
            delay_paragrafo = 30
        main.pygame.time.delay(delay_paragrafo)
        
    main.aguardar(largura=(config.PADDING_LEFT + len(texto[len(texto) - 1]) * 11),altura=(altura_historia + (len(texto) * 40 - 40)), cor=config.COR_TEXTO)


def quarta_fase_iniciar(resetar=True):
    global soma_arestas
    global current_node
    global visited_nodes
    global visited_edges
    
    if atual_fase not in config.FASES_CONCLUIDAS and resetar and not config.SkipHistoria:
        escreve_introducao_final_fase(texto_introducao_fase)
        config.TELA.fill(config.BACKGROUND_JOGO)

    tmpI = 1
    while tmpI <= atual_fase:
        visited_nodes = config.get_info_resumo_fase(tmpI)["visitados"]
        visited_edges = get_linhas_visitadas(visited_nodes)
        soma_arestas = config.get_info_resumo_fase(tmpI)["soma"]
        
        if tmpI > atual_fase and resetar:
            atualiza_dados_fase(tmpI, [], 0, False)
        
        update_grafo(visited_nodes, not (tmpI + 1) <= atual_fase)
        # soma_arestas = calcula_peso_arestas(local_arestas, vertices_fases[tmpI - 1], final_node)
        
        tmpI += 1
        
    if resetar:
        reset()

    last_clicked_node = visited_nodes[-1]
    rodando = True
    while rodando:
        maudio.parar_musica_atual()
        desenhar_grafo()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.fechar_jogo()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_node = get_node_clicked(event.pos)
                if clicked_node is not None:
                    if clicked_node in local_graph[current_node]:
                        edge = tuple(sorted((current_node, clicked_node)))
                        if edge not in visited_edges and clicked_node not in visited_nodes:
                            maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
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
                            maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                            visited_nodes.remove(current_node)
                            current_node = last_clicked_node
                            if last_clicked_node != inicial_node:
                                last_clicked_node = visited_nodes[-2]
                            else:
                                last_clicked_node = inicial_node
                        if clicked_node == final_node:
                            if config.total_peso_fases + soma_arestas > config.MAX_PESOS_VERTICES:
                                go.desenha_game_over()
                            rodando = False
                    else:
                        maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                        print("Movimento inválido: esse nó não é vizinho do atual.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.inicar_menu(False)
    
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    # escreve_introducao_final_fase(texto_final_fase)
        
    texto_final_missao = [
        "Mais uma missão concluída",
        "Uma sensação estranha te envade,",
        "como se fosse um súbito sopro de esperança...",
        "Talvez nem tudo tenha sido em vão,",
        "ou talvez, sejam apenas as alucinações do cansaço,",
        "falando mais alto do que a razão... ",
        "Neste momento quem sabe,",
        "o melhor seja descansar mesmo..."
    ]

    caminho, soma_arestas_cpu = dijkstra(local_arestas, inicial_node, final_node)
    print(f'Caminho: {caminho}, Custo: {soma_arestas_cpu}')
    
    atualiza_dados_fase(atual_fase, visited_nodes, soma_arestas)
    
    desenha_final.desenha_final_missao(soma_arestas, soma_arestas_cpu, texto_final_missao)
    return True