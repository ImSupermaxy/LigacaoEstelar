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

local_nos = copy.deepcopy(nos)
local_arestas = copy.deepcopy(arestas)
local_graph = copy.deepcopy(graph)

# Estado
inicial_node = "A"
final_node = "AP"
current_node = inicial_node
visited_nodes = [current_node]
visited_edges = set()
NODE_RADIUS = 15
soma_arestas = 0

texto_introducao_fase = [
    "\"Nave B-12, câmbio... Nave B-12, na escuta?... Vamo trabalhar!?\"",
    "\"Você acorda na sua nave com o som do seu companheiro no rádio, chamando para uma provável nova expedição.\"",
    "Na janela da cabine, a mesma visão monótona de sempre: o vasto — e agora incomum — espaço, ",
    "sem nenhuma estrela visível, apenas uma imensidão de lixo. Restos de naves, satélites abandonados e ",
    "resíduos expelidos pelas civilizações. ",
    "",
    "A humanidade agora está espalhada por diversos planetas em todo o espaço, após os acontecimentos ",
    "catastróficos no planeta Terra...",
    "\"Chrr-chrr\" — seus pensamentos são interrompidos pelo rádio e, em seguida, a voz dele de novo:",
    "\"Precisam de você aqui. Temos que abrir caminho pra mais um ricasso de férias. Câmbio.\"",
    "Você suspira, liga sua nave, e parte — mais uma vez — para mais um dia de trabalho.",
]

def reset():
    global inicial_node
    global final_node
    global current_node
    global visited_nodes
    global visited_edges
    global soma_arestas
    
    inicial_node = "A"
    final_node = "AP"
    current_node = inicial_node
    visited_nodes = [current_node]
    visited_edges = set()
    soma_arestas = 0

def desenhar_grafo():
    config.TELA.fill(config.BACKGROUND_JOGO)
    main.desenhar_textos(["FASE 1"], config.ROXO2, 25, config.LARGURA - 140, False, config.FONTE_PESO)
    
    desenha_final.escreve_info_pesos(soma_arestas)
    
    # local_arestas["A"][0] = ("D", 0)
    
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
        # pygame.draw.circle(config.TELA, config.BRANCO, (x, y), NODE_RADIUS, 2)
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


def primeira_fase_iniciar(resetar=True):
    print("Linha 249 - fase1.py: ", config.dados["isContinuacao"])
    if (config.dados["fases"]["atual"] <= 1 or resetar) and not config.SkipHistoria:
        escreve_introducao_final_fase(texto_introducao_fase)
        config.TELA.fill(config.BACKGROUND_JOGO)
    
    global current_node
    global visited_nodes
    global visited_edges
    global soma_arestas

    soma_arestas = config.get_info_resumo_fase("1")["soma"]
    visited_nodes = config.get_info_resumo_fase("1")["visitados"]
    visited_edges = get_linhas_visitadas(visited_nodes)

    if resetar:
        atualiza_dados_fase(1, [], 0, False)
        reset()
    
    last_clicked_node = visited_nodes[-1]
    rodando = True
    while rodando:
        maudio.parar_musica_atual()
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
        "Você concluiu mais uma missão",
        "Seu rendimento hoje ajudou significativamente ",
        "na remoção de todo o lixo nesses arredores, ",
        "quase como se alguns grãos de areia ",
        "fossem removidos de uma praia. ",
        "Você lembra delas? É... acho que não ",
        "Enfim, descanse por hora em sua nave...",
        "Aproveite seus momentos de descanso"
    ]

    caminho, soma_arestas_cpu = dijkstra(local_arestas, inicial_node, final_node)
    print(f'Caminho: {caminho}, Custo: {soma_arestas_cpu}')
    
    atualiza_dados_fase(1, visited_nodes, soma_arestas)
    
    desenha_final.desenha_final_missao(soma_arestas, soma_arestas_cpu, texto_final_missao)
    
    return True