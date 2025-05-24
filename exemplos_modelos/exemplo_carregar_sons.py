import pygame
import os
from pathlib import Path

pygame.init()
pygame.mixer.init()

def carregar_sons(pasta):
    sons = {}
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(('.wav', '.ogg', '.mp3')):
            caminho_completo = os.path.join(pasta, nome_arquivo)
            nome_som = os.path.splitext(nome_arquivo)[0]
            sons[nome_som] = pygame.mixer.Sound(caminho_completo)
    return sons

caminho_arquivo = Path(__file__)
RAIZ_PROJETO = caminho_arquivo.parent.parent.resolve()
PASTA_ASSETS = os.path.join(RAIZ_PROJETO, "assets")
PASTA_MUSICA = os.path.join(PASTA_ASSETS, "musicas")
sons = carregar_sons(PASTA_MUSICA)

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Testando Sons")

# rodando = True
# while rodando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_SPACE:
#                 sons['Polyphia-Playing_God'].set_volume(1)
#                 sons['Polyphia-Playing_God'].play()  # Toca o som ao apertar espaço
#                 rodando = False


import time
import sys

# # Inicializa o mixer e o Pygame
# pygame.mixer.init()
# pygame.init()

# Carrega o som
som = sons['Polyphia-Playing_God']
duracao = som.get_length()

# Toca o som
som.play()

# Visualização da progressão
barra_total = 50  # Número de caracteres da barra
inicio = time.time()

while pygame.mixer.get_busy():  # Enquanto o áudio estiver tocando
    agora = time.time()
    decorrido = agora - inicio
    progresso = min(decorrido / duracao, 1.0)

    barras = int(progresso * barra_total)
    barra = "[" + "#" * barras + "-" * (barra_total - barras) + "]"
    tempo = f"{int(decorrido):02}/{int(duracao):02}s"

    sys.stdout.write(f"\r{barra} {tempo}")
    sys.stdout.flush()

    time.sleep(0.1)

print("\nÁudio finalizado!")


# i = 0
# volume = 0.7
# while i < 3:
#     # Reduz o volume para 50% depois de 2 segundos
#     sons['Polyphia-Playing_God'].set_volume(volume)
#     print("Volume reduzido")
#     time.sleep(2)
#     volume = volume - 0.2
    
#     i += 1

# rodando = True
# while rodando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#         if evento.type == pygame.KEYDOWN or evento.type == pygame.K_RETURN:
#             rodando = False
            
pygame.quit()
