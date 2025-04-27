import pygame
import os
from config.variables import *

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

sons = carregar_sons('../assets/musicas')

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Testando Sons")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                sons['Polyphia-Playing_God'].set_volume(Volume_Musica)
                sons['Polyphia-Playing_God'].play()  # Toca o som ao apertar espaço

pygame.quit()
