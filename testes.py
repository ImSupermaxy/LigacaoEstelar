# # # # # # import pygame
# # # # # # import sys

# # # # # # pygame.init()

# # # # # # # Tela
# # # # # # LARGURA, ALTURA = 800, 600
# # # # # # TELA = pygame.display.set_mode((LARGURA, ALTURA))
# # # # # # pygame.display.set_caption("História com Scroll")

# # # # # # # Cores e fontes
# # # # # # PRETO = (0, 0, 0)
# # # # # # BRANCO = (255, 255, 255)
# # # # # # FONTE = pygame.font.SysFont("arial", 28)

# # # # # # # História do jogo
# # # # # # historia = [
# # # # # #     "Em um mundo devastado por sombras...",
# # # # # #     "Um herói solitário surge das cinzas.",
# # # # # #     "Sua missão: restaurar a luz e a esperança.",
# # # # # #     "Mas o caminho será perigoso...",
# # # # # #     "E o tempo está contra você.",
# # # # # #     "Agora, a jornada começa.",
# # # # # #     "Você deve decidir o seu destino.",
# # # # # #     "Cada escolha pode mudar tudo.",
# # # # # #     "Coragem. Esperança. Risco.",
# # # # # #     "Você está pronto para continuar?",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS",
# # # # # #     "ALSKJDALKS"
# # # # # # ]

# # # # # # def digitar_lento(texto, linhas_anteriores, delay=0, offset_y=0):
# # # # # #     texto_atual = ""
# # # # # #     for char in texto:
# # # # # #         texto_atual += char
# # # # # #         desenhar_historia(linhas_anteriores + [texto_atual], offset_y)
# # # # # #         pygame.time.delay(delay)

# # # # # #         for evento in pygame.event.get():
# # # # # #             if evento.type == pygame.QUIT:
# # # # # #                 pygame.quit()
# # # # # #                 sys.exit()
# # # # # #             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
# # # # # #                 return True
# # # # # #     return False

# # # # # # def desenhar_historia(linhas, offset_y):
# # # # # #     TELA.fill(PRETO)
# # # # # #     y = 100 - offset_y
# # # # # #     for linha in linhas:
# # # # # #         render = FONTE.render(linha, True, BRANCO)
# # # # # #         TELA.blit(render, (50, y))
# # # # # #         y += 40
# # # # # #     pygame.display.update()

# # # # # # def mostrar_historia():
# # # # # #     linhas_mostradas = []
# # # # # #     scroll = 0

# # # # # #     for i, paragrafo in enumerate(historia):
# # # # # #         # Aumenta scroll conforme o número de parágrafos cresce
# # # # # #         if i * 40 + 100 > ALTURA - 100:
# # # # # #             scroll += 40  # rola para cima quando ultrapassa a tela

# # # # # #         pular = digitar_lento(paragrafo, linhas_mostradas, offset_y=scroll)
# # # # # #         linhas_mostradas.append(paragrafo)

# # # # # #         if pular:
# # # # # #             break
# # # # # #         pygame.time.delay(500)

# # # # # #     esperar_fim()

# # # # # # def esperar_fim():
# # # # # #     texto_final = FONTE.render("Pressione ENTER para continuar...", True, BRANCO)
# # # # # #     TELA.blit(texto_final, (LARGURA // 2 - texto_final.get_width() // 2, ALTURA - 60))
# # # # # #     pygame.display.update()

# # # # # #     esperando = True
# # # # # #     while esperando:
# # # # # #         for evento in pygame.event.get():
# # # # # #             if evento.type == pygame.QUIT:
# # # # # #                 pygame.quit()
# # # # # #                 sys.exit()
# # # # # #             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
# # # # # #                 esperando = False

# # # # # #     pygame.quit()

# # # # # # if __name__ == "__main__":
# # # # # #     mostrar_historia()


# # # # # #============================-=-=-===========================-=-=-=-===================================-=-=-=-=============================
# # # # # #==========================================================FONTES==========================================================================
# # # # # import pygame
# # # # # import sys

# # # # # # Inicializa o Pygame e o módulo de fontes
# # # # # pygame.init()
# # # # # pygame.font.init()

# # # # # # Tamanho da janela
# # # # # largura, altura = 800, 600
# # # # # tela = pygame.display.set_mode((largura, altura))
# # # # # pygame.display.set_caption("Visualização de Fontes do Pygame")

# # # # # # Cores
# # # # # BRANCO = (255, 255, 255)
# # # # # PRETO = (0, 0, 0)

# # # # # # Texto de exemplo
# # # # # texto_exemplo = "Exemplo de Fonte"

# # # # # # Obtem a lista de fontes disponíveis
# # # # # fontes = pygame.font.get_fonts()
# # # # # fontes.sort()  # organiza em ordem alfabética

# # # # # # Controle de rolagem
# # # # # indice_inicial = 0
# # # # # fontes_por_tela = 10

# # # # # # Função para desenhar as fontes na tela
# # # # # def desenhar_fontes(inicio):
# # # # #     tela.fill(PRETO)

# # # # #     y = 20
# # # # #     for i in range(inicio, min(inicio + fontes_por_tela, len(fontes))):
# # # # #         nome_fonte = fontes[i]
# # # # #         try:
# # # # #             fonte = pygame.font.SysFont(nome_fonte, 28)
# # # # #             texto_renderizado = fonte.render(f"{nome_fonte} - {texto_exemplo}", True, BRANCO)
# # # # #             tela.blit(texto_renderizado, (20, y))
# # # # #             y += 50
# # # # #         except:
# # # # #             # Se der erro com uma fonte, pula
# # # # #             continue

# # # # #     pygame.display.flip()

# # # # # # Loop principal
# # # # # rodando = True
# # # # # print(len(fontes))
# # # # # while rodando:
# # # # #     desenhar_fontes(indice_inicial)

# # # # #     for evento in pygame.event.get():
# # # # #         if evento.type == pygame.QUIT:
# # # # #             rodando = False
# # # # #         elif evento.type == pygame.KEYDOWN:
# # # # #             if evento.key == pygame.K_DOWN:
# # # # #                 indice_inicial = min(indice_inicial + fontes_por_tela, len(fontes) - fontes_por_tela)
# # # # #             elif evento.key == pygame.K_UP:
# # # # #                 indice_inicial = max(indice_inicial - fontes_por_tela, 0)

# # # # # pygame.quit()
# # # # # sys.exit()

# # # # import pygame
# # # # import sys

# # # # # Inicializa o Pygame e o módulo de fontes
# # # # pygame.init()
# # # # pygame.font.init()

# # # # largura, altura = 1520, 750
# # # # TELA = pygame.display.set_mode((largura, altura))
# # # # pygame.display.set_caption("Visualização de Fontes do Pygame")

# # # # PRETO = (0, 0, 0)
# # # # BRANCO = (255, 255, 255)
# # # # VERDE = (0, 200, 0)
# # # # VERDE_ESCURO = (75, 200, 75)
# # # # VERMELHO = (200, 0, 0)
# # # # AZUL = (50, 100, 255)
# # # # AZUL_CLARO = (3, 207, 252)
# # # # CINZA = (180, 180, 180)
# # # # CINZA_CLARO = (210, 210, 210)

# # # # # retangulo = pygame.Rect(100, 100, 200, 150) #substituir pelo (PADDING_LEFT / 2) + len(texto), altura)
# # # # # TELA.fill(PRETO, retangulo)

# # # # retangulo = pygame.Rect(0, 0, 500, 200) #substituir pelo (PADDING_LEFT / 2) + len(texto), altura)
# # # # TELA.fill(VERMELHO, retangulo)

# # # # rodando = True
# # # # while rodando:
# # # #      for evento in pygame.event.get():
# # # #             if evento.type == pygame.QUIT:
# # # #                 pygame.quit()
# # # #                 sys.exit()
# # # #             elif evento.type == pygame.KEYDOWN:
# # # #                 if evento.key == pygame.K_ESCAPE:
# # # #                     rodando = False
# # # #                 if evento.key == pygame.K_RETURN:
# # # #                     rodando = False


# # # import pygame

# # # pygame.init()

# # # # Configurações básicas
# # # largura, altura = 600, 400
# # # tela = pygame.display.set_mode((largura, altura))
# # # clock = pygame.time.Clock()

# # # # Cores
# # # PRETO = (0, 0, 0)
# # # VERMELHO = (255, 0, 0)
# # # AZUL = (0, 0, 255)

# # # # Um retângulo
# # # rect = pygame.Rect(0, 0, 150, 100)

# # # rodando = True
# # # while rodando:
# # #     for evento in pygame.event.get():
# # #         if evento.type == pygame.QUIT:
# # #             rodando = False

# # #     # Primeiro, preenchendo o fundo
# # #     tela.fill(PRETO)

# # #     # Desenhando o retângulo vermelho
# # #     pygame.draw.rect(tela, VERMELHO, rect)

# # #     # Digamos que queremos "substituir" a área com azul
# # #     substituir_area = rect
# # #     pygame.draw.rect(tela, AZUL, substituir_area)

# # #     # Atualiza a tela
# # #     pygame.display.update()
# # #     clock.tick(60)

# # # pygame.quit()


# # import pygame
# # import sys
# # # import configuracoes.variables as config
# # # import main
# # # import menu.menu as menu
# # import math

# # def primeira_fase_iniciar():
    
# #     NOME_PROJETO = "Teste"
# #     pygame.init()
# #     pygame.font.init()
# #     pygame.display.set_caption(NOME_PROJETO)
    
# #     LARGURA, ALTURA = 1520, 750
# #     IsDevVar = True
# #     TELA = pygame.display.set_mode((LARGURA, ALTURA))
# #     FONTE = pygame.font.SysFont("arial", 28)
# #     FONTE_GRAFO = pygame.font.SysFont(None, 24)
# #     FONTE_PESO = pygame.font.SysFont("arial", 36, bold=True)
    
# #     PRETO = (0, 0, 0)
# #     BRANCO = (255, 255, 255)
# #     VERDE = (0, 200, 0)
# #     VERDE_ESCURO = (75, 200, 75)
# #     VERMELHO = (200, 0, 0)
# #     AZUL = (50, 100, 255)
# #     AZUL_CLARO = (3, 207, 252)
# #     CINZA = (180, 180, 180)
# #     CINZA_CLARO = (210, 210, 210)
# #     AMARELO = (255, 255, 0)
# #     BACKGROUND_JOGO = PRETO
# #     COR_TEXTO = BRANCO
    
# #     # Nós com posições (x, y)
# #     nos = {
# #         "A": (150, 100),
# #         "B": (400, 80),
# #         "C": (650, 150),
# #         "D": (200, 300),
# #         "E": (500, 350)
# #     }

# #     # Arestas no formato: (nó1, nó2, peso)
# #     arestas = { #Mudar para dict...
# #         "A": [("B", 4), ("D", 2)],
# #         "B": [("A", 4), ("C", 6), ("E", 3)],
# #         "C": [("E", 1), ("B", 6)],
# #         "D": [("E", 5), ("A", 2)],
# #         "E": [("B", 3), ("C", 1), ("D", 5)]
# #     }

# #     # Estado
# #     current_node = "A"
# #     visited_nodes = set([current_node])
# #     visited_edges = set()
# #     NODE_RADIUS = 15
    
# #     def desenhar_grafo():
# #         TELA.fill(BACKGROUND_JOGO)

# #         # Desenha as arestas
# #         for comeco, vizinhos in arestas.items():
# #             for fim, peso in vizinhos:
# #                 if (fim, comeco) not in visited_edges and (comeco, fim) not in visited_edges:
# #                     (x1, y1) = nos[comeco]
# #                     (x2, y2) = nos[fim]
# #                     pygame.draw.line(TELA, CINZA_CLARO, (x1, y1), (x2, y2), 2)

# #                     # Posição intermediária para o peso
# #                     px, py = (x1 + x2) // 2, (y1 + y2) // 2
# #                     texto = FONTE_PESO.render(str(peso), True, VERDE_ESCURO)
# #                     TELA.blit(texto, (px - texto.get_width() // 2, py - texto.get_height() // 2))

# #         # Desenhar conexões feitas
# #         for a, b in visited_edges:
# #             pygame.draw.line(TELA, AZUL, nos[a], nos[b], 4)

# #         # Desenha os nós
# #         for nome, (x, y) in nos.items():
# #             color = VERMELHO if nome in visited_nodes else AMARELO
# #             pygame.draw.circle(TELA, color, (x, y), NODE_RADIUS)
# #             pygame.draw.circle(TELA, BRANCO, (x, y), NODE_RADIUS, 2)

# #             #validação pra ver se é dev, (pra exibir o nome das vertices...)
# #             if IsDevVar:
# #                 texto = FONTE_GRAFO.render(nome, True, PRETO)
# #                 TELA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

# #         pygame.display.update()


# #     def get_node_clicked(pos):
# #         for node_id, node_pos in nos.items():
# #             dist = math.hypot(pos[0] - node_pos[0], pos[1] - node_pos[1])
# #             if dist <= NODE_RADIUS:
# #                 return node_id
# #         return None


# #     def all_nodes_visited():
# #         return len(visited_nodes) == len(nos)
    
    
# #     def letra_para_numero(letra: str) -> int:
# #         letra = letra.upper()
# #         resultado = 0
# #         for i, c in enumerate(reversed(letra)):
# #             resultado += (ord(c) - 64) * (26 ** i)
# #         return resultado


# #     def numero_para_letra(numero: int) -> str:
# #         resultado = ""
# #         while numero > 0:
# #             numero -= 1  # Ajuste para 1-indexado
# #             resultado = chr((numero % 26) + 65) + resultado
# #             numero //= 26
# #         return resultado

    
# #     rodando = True
# #     while rodando:
# #         desenhar_grafo()
        
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 main.fechar_jogo()

# #             if all_nodes_visited():
# #                     rodando = False
# #                     text = config.FONTE_GRAFO.render("Todos os nós foram visitados!", True, config.BRANCO)
# #                     config.TELA.blit(text, (config.LARGURA // 2 - 200, 50))
# #                     pygame.display.flip()

# #             elif event.type == pygame.MOUSEBUTTONDOWN:
# #                 clicked_node = get_node_clicked(event.pos)
# #                 if clicked_node is not None:
# #                     if clicked_node in arestas[letra_para_numero(current_node)]:
# #                         edge = tuple(sorted((current_node, clicked_node)))
# #                         if edge not in visited_edges:
# #                             visited_edges.add(edge)
# #                         visited_nodes.add(clicked_node)
# #                         current_node = clicked_node
# #                     else:
# #                         print("Movimento inválido: esse nó não é vizinho do atual.")
# #             elif event.type == pygame.KEYDOWN:
# #                 if event.key == pygame.K_ESCAPE:
# #                     rodando = False


# # primeira_fase_iniciar()

# def obtem_ranking_by_soma_arestas(soma_usuario, soma_cpu):
#     if soma_cpu == 0:
#         return "Erro: soma do grafo não pode ser zero."

#     porcentagem_real = (soma_usuario / soma_cpu) * 100
#     distancia = abs(100 - porcentagem_real)

#     # Transformamos essa distância em uma "pontuação invertida"
#     # Quanto mais próximo de 100%, maior a pontuação (e melhor o ranking)
#     pontuacao = round(max(0, 100 - distancia))

#     # Tabela de rankings com base na pontuação (0 a 100)
#     rankings = [
#         (96, 100, "S"),
#         (90, 95, "A+"),
#         (85, 89, "A"),
#         (80, 84, "A-"),
#         (75, 79, "B+"),
#         (70, 74, "B"),
#         (65, 69, "B-"),
#         (60, 64, "C+"),
#         (55, 59, "C"),
#         (50, 54, "C-"),
#         (45, 49, "D+"),
#         (40, 44, "D"),
#         (35, 39, "D-"),
#         (30, 34, "E+"),
#         (25, 29, "E"),
#         (20, 24, "E-"),
#         (15, 19, "F+"),
#         (10, 14, "F"),
#         (5, 9, "F-"),
#         (0, 4, "...")
#     ]

#     for min_val, max_val, rank in rankings:
#         if min_val <= pontuacao <= max_val:
#             return f"Porcentagem real: {porcentagem_real:.2f}%, Ranking: {rank}"

#     return "Erro: pontuação fora dos limites esperados."

# print(obtem_ranking_by_soma_arestas(102, 100))


import pygame
import time
from pathlib import Path
import os

# Inicialização
pygame.init()
pygame.mixer.init()


caminho_arquivo = Path(__file__)
RAIZ_PROJETO = caminho_arquivo.parent.resolve()
PASTA_ASSETS = os.path.join(RAIZ_PROJETO, "assets")
PASTA_IMAGENS = os.path.join(PASTA_ASSETS, "imagens")
PASTA_AUDIOS = os.path.join(PASTA_ASSETS, "audios")
PASTA_MUSICA = os.path.join(PASTA_ASSETS, "musicas")

AUDIO_TEXTO = "som_texto_undertale_editado.mp3"

# Configurações da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Texto com som")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carregar o som
sound = pygame.mixer.Sound(os.path.join(PASTA_AUDIOS, AUDIO_TEXTO))  # ou .wav

# Função para exibir o texto com som
def type_text(text, x, y, sound):
    displayed_text = ""
    sound.play(-1)  # Reproduz o som em loop contínuo

    for char in text:
        displayed_text += char
        render = font.render(displayed_text, True, WHITE)
        screen.fill(BLACK)
        screen.blit(render, (x, y))
        pygame.display.update()
        time.sleep(50)  # Delay entre caracteres
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    sound.stop()  # Parar o som quando o texto terminar

# Loop principal
running = True
while running:
    screen.fill(BLACK)
    type_text("Este é um exemplo com som contínuo.", 50, 250, sound)

    # Espera para encerrar
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False

pygame.quit()