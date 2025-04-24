# import pygame
# import sys

# pygame.init()

# # Tela
# LARGURA, ALTURA = 800, 600
# TELA = pygame.display.set_mode((LARGURA, ALTURA))
# pygame.display.set_caption("História com Scroll")

# # Cores e fontes
# PRETO = (0, 0, 0)
# BRANCO = (255, 255, 255)
# FONTE = pygame.font.SysFont("arial", 28)

# # História do jogo
# historia = [
#     "Em um mundo devastado por sombras...",
#     "Um herói solitário surge das cinzas.",
#     "Sua missão: restaurar a luz e a esperança.",
#     "Mas o caminho será perigoso...",
#     "E o tempo está contra você.",
#     "Agora, a jornada começa.",
#     "Você deve decidir o seu destino.",
#     "Cada escolha pode mudar tudo.",
#     "Coragem. Esperança. Risco.",
#     "Você está pronto para continuar?",
#     "ALSKJDALKS",
#     "ALSKJDALKS",
#     "ALSKJDALKS",
#     "ALSKJDALKS",
#     "ALSKJDALKS",
#     "ALSKJDALKS",
#     "ALSKJDALKS"
# ]

# def digitar_lento(texto, linhas_anteriores, delay=0, offset_y=0):
#     texto_atual = ""
#     for char in texto:
#         texto_atual += char
#         desenhar_historia(linhas_anteriores + [texto_atual], offset_y)
#         pygame.time.delay(delay)

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
#                 return True
#     return False

# def desenhar_historia(linhas, offset_y):
#     TELA.fill(PRETO)
#     y = 100 - offset_y
#     for linha in linhas:
#         render = FONTE.render(linha, True, BRANCO)
#         TELA.blit(render, (50, y))
#         y += 40
#     pygame.display.update()

# def mostrar_historia():
#     linhas_mostradas = []
#     scroll = 0

#     for i, paragrafo in enumerate(historia):
#         # Aumenta scroll conforme o número de parágrafos cresce
#         if i * 40 + 100 > ALTURA - 100:
#             scroll += 40  # rola para cima quando ultrapassa a tela

#         pular = digitar_lento(paragrafo, linhas_mostradas, offset_y=scroll)
#         linhas_mostradas.append(paragrafo)

#         if pular:
#             break
#         pygame.time.delay(500)

#     esperar_fim()

# def esperar_fim():
#     texto_final = FONTE.render("Pressione ENTER para continuar...", True, BRANCO)
#     TELA.blit(texto_final, (LARGURA // 2 - texto_final.get_width() // 2, ALTURA - 60))
#     pygame.display.update()

#     esperando = True
#     while esperando:
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
#                 esperando = False

#     pygame.quit()

# if __name__ == "__main__":
#     mostrar_historia()
