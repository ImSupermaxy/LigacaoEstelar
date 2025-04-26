import pygame
import os

# Inicializar Pygame e mixer
pygame.init()
pygame.mixer.init()

# Função para carregar sons
def carregar_sons(pasta):
    sons = {}
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.wav') or nome_arquivo.endswith('.ogg') or nome_arquivo.endswith('.mp3'):
            caminho_completo = os.path.join(pasta, nome_arquivo)
            nome_som = os.path.splitext(nome_arquivo)[0]  # tira a extensão
            sons[nome_som] = pygame.mixer.Sound(caminho_completo)
    return sons

# Carregar todos os sons da pasta 'sons'
sons = carregar_sons('sons')

# Exemplo de como usar:
sons['explosao'].play()  # Toca o som chamado 'explosao.wav'
sons['pulo'].play()      # Toca o som chamado 'pulo.wav'
