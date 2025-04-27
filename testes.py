# # # import pygame
# # # import sys

# # # pygame.init()

# # # # Tela
# # # LARGURA, ALTURA = 800, 600
# # # TELA = pygame.display.set_mode((LARGURA, ALTURA))
# # # pygame.display.set_caption("História com Scroll")

# # # # Cores e fontes
# # # PRETO = (0, 0, 0)
# # # BRANCO = (255, 255, 255)
# # # FONTE = pygame.font.SysFont("arial", 28)

# # # # História do jogo
# # # historia = [
# # #     "Em um mundo devastado por sombras...",
# # #     "Um herói solitário surge das cinzas.",
# # #     "Sua missão: restaurar a luz e a esperança.",
# # #     "Mas o caminho será perigoso...",
# # #     "E o tempo está contra você.",
# # #     "Agora, a jornada começa.",
# # #     "Você deve decidir o seu destino.",
# # #     "Cada escolha pode mudar tudo.",
# # #     "Coragem. Esperança. Risco.",
# # #     "Você está pronto para continuar?",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS",
# # #     "ALSKJDALKS"
# # # ]

# # # def digitar_lento(texto, linhas_anteriores, delay=0, offset_y=0):
# # #     texto_atual = ""
# # #     for char in texto:
# # #         texto_atual += char
# # #         desenhar_historia(linhas_anteriores + [texto_atual], offset_y)
# # #         pygame.time.delay(delay)

# # #         for evento in pygame.event.get():
# # #             if evento.type == pygame.QUIT:
# # #                 pygame.quit()
# # #                 sys.exit()
# # #             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
# # #                 return True
# # #     return False

# # # def desenhar_historia(linhas, offset_y):
# # #     TELA.fill(PRETO)
# # #     y = 100 - offset_y
# # #     for linha in linhas:
# # #         render = FONTE.render(linha, True, BRANCO)
# # #         TELA.blit(render, (50, y))
# # #         y += 40
# # #     pygame.display.update()

# # # def mostrar_historia():
# # #     linhas_mostradas = []
# # #     scroll = 0

# # #     for i, paragrafo in enumerate(historia):
# # #         # Aumenta scroll conforme o número de parágrafos cresce
# # #         if i * 40 + 100 > ALTURA - 100:
# # #             scroll += 40  # rola para cima quando ultrapassa a tela

# # #         pular = digitar_lento(paragrafo, linhas_mostradas, offset_y=scroll)
# # #         linhas_mostradas.append(paragrafo)

# # #         if pular:
# # #             break
# # #         pygame.time.delay(500)

# # #     esperar_fim()

# # # def esperar_fim():
# # #     texto_final = FONTE.render("Pressione ENTER para continuar...", True, BRANCO)
# # #     TELA.blit(texto_final, (LARGURA // 2 - texto_final.get_width() // 2, ALTURA - 60))
# # #     pygame.display.update()

# # #     esperando = True
# # #     while esperando:
# # #         for evento in pygame.event.get():
# # #             if evento.type == pygame.QUIT:
# # #                 pygame.quit()
# # #                 sys.exit()
# # #             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
# # #                 esperando = False

# # #     pygame.quit()

# # # if __name__ == "__main__":
# # #     mostrar_historia()


# # #============================-=-=-===========================-=-=-=-===================================-=-=-=-=============================
# # #==========================================================FONTES==========================================================================
# # import pygame
# # import sys

# # # Inicializa o Pygame e o módulo de fontes
# # pygame.init()
# # pygame.font.init()

# # # Tamanho da janela
# # largura, altura = 800, 600
# # tela = pygame.display.set_mode((largura, altura))
# # pygame.display.set_caption("Visualização de Fontes do Pygame")

# # # Cores
# # BRANCO = (255, 255, 255)
# # PRETO = (0, 0, 0)

# # # Texto de exemplo
# # texto_exemplo = "Exemplo de Fonte"

# # # Obtem a lista de fontes disponíveis
# # fontes = pygame.font.get_fonts()
# # fontes.sort()  # organiza em ordem alfabética

# # # Controle de rolagem
# # indice_inicial = 0
# # fontes_por_tela = 10

# # # Função para desenhar as fontes na tela
# # def desenhar_fontes(inicio):
# #     tela.fill(PRETO)

# #     y = 20
# #     for i in range(inicio, min(inicio + fontes_por_tela, len(fontes))):
# #         nome_fonte = fontes[i]
# #         try:
# #             fonte = pygame.font.SysFont(nome_fonte, 28)
# #             texto_renderizado = fonte.render(f"{nome_fonte} - {texto_exemplo}", True, BRANCO)
# #             tela.blit(texto_renderizado, (20, y))
# #             y += 50
# #         except:
# #             # Se der erro com uma fonte, pula
# #             continue

# #     pygame.display.flip()

# # # Loop principal
# # rodando = True
# # print(len(fontes))
# # while rodando:
# #     desenhar_fontes(indice_inicial)

# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             rodando = False
# #         elif evento.type == pygame.KEYDOWN:
# #             if evento.key == pygame.K_DOWN:
# #                 indice_inicial = min(indice_inicial + fontes_por_tela, len(fontes) - fontes_por_tela)
# #             elif evento.key == pygame.K_UP:
# #                 indice_inicial = max(indice_inicial - fontes_por_tela, 0)

# # pygame.quit()
# # sys.exit()

# import pygame
# import sys

# # Inicializa o Pygame e o módulo de fontes
# pygame.init()
# pygame.font.init()

# largura, altura = 1520, 750
# TELA = pygame.display.set_mode((largura, altura))
# pygame.display.set_caption("Visualização de Fontes do Pygame")

# PRETO = (0, 0, 0)
# BRANCO = (255, 255, 255)
# VERDE = (0, 200, 0)
# VERDE_ESCURO = (75, 200, 75)
# VERMELHO = (200, 0, 0)
# AZUL = (50, 100, 255)
# AZUL_CLARO = (3, 207, 252)
# CINZA = (180, 180, 180)
# CINZA_CLARO = (210, 210, 210)

# # retangulo = pygame.Rect(100, 100, 200, 150) #substituir pelo (PADDING_LEFT / 2) + len(texto), altura)
# # TELA.fill(PRETO, retangulo)

# retangulo = pygame.Rect(0, 0, 500, 200) #substituir pelo (PADDING_LEFT / 2) + len(texto), altura)
# TELA.fill(VERMELHO, retangulo)

# rodando = True
# while rodando:
#      for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_ESCAPE:
#                     rodando = False
#                 if evento.key == pygame.K_RETURN:
#                     rodando = False


import pygame

pygame.init()

# Configurações básicas
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Um retângulo
rect = pygame.Rect(0, 0, 150, 100)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Primeiro, preenchendo o fundo
    tela.fill(PRETO)

    # Desenhando o retângulo vermelho
    pygame.draw.rect(tela, VERMELHO, rect)

    # Digamos que queremos "substituir" a área com azul
    substituir_area = rect
    pygame.draw.rect(tela, AZUL, substituir_area)

    # Atualiza a tela
    pygame.display.update()
    clock.tick(60)

pygame.quit()
