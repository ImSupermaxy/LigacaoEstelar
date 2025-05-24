import pygame
import os
import configuracoes.variables as config
from mutagen.mp3 import MP3
from datetime import datetime, timedelta
import time
import sys

MUSICA_MENU = "MusicaMenu.mp3"
SOM_ATUAL = ""
GLOBAL_MIXER = pygame.mixer.Sound(os.path.join(config.PASTA_AUDIOS, MUSICA_MENU))
DATA_INICIAL_SOM = datetime.now()

def iniciar_musica_menu():
    global GLOBAL_MIXER
    global DATA_INICIAL_SOM
    
    caminho_musica = os.path.join(config.PASTA_AUDIOS, MUSICA_MENU)
    mixer = pygame.mixer.Sound(caminho_musica)
    GLOBAL_MIXER = mixer
    GLOBAL_MIXER.get_length()
    update_volume_musica_atual(config.get_volume_musica())
    DATA_INICIAL_SOM = datetime.now()
    GLOBAL_MIXER.play()
    update_som_atual(caminho_musica)


def change_audio_to_loop(volume_atual):
    change_volume = True
    while change_volume:
        GLOBAL_MIXER.set_volume(volume_atual)
        volume_atual = volume_atual - 5
        change_volume = volume_atual == 0
        pygame.time.delay(50)


def get_data_to_loop(inicial_date):
    audio = MP3(SOM_ATUAL)
    data_to_loop = inicial_date + timedelta(seconds=audio.info.length)
    return data_to_loop


def update_som_atual(som):
    global SOM_ATUAL
    SOM_ATUAL = som


def update_volume_musica_atual(volume:float):
    print("Valor para atualizar: " + str(volume))
    print("Antes: " + str(GLOBAL_MIXER.get_volume()))
    GLOBAL_MIXER.set_volume(volume)
    print("Atualizado: " + str(GLOBAL_MIXER.get_volume()))
    

def parar_musica_atual():
    GLOBAL_MIXER.set_volume(0)
    GLOBAL_MIXER.stop()


# def carregar_sons(pasta):
#     sons = {}
#     for nome_arquivo in os.listdir(pasta):
#         if nome_arquivo.endswith(('.wav', '.ogg', '.mp3')):
#             caminho_completo = os.path.join(pasta, nome_arquivo)
#             nome_som = os.path.splitext(nome_arquivo)[0]
#             sons[nome_som] = pygame.mixer.Sound(caminho_completo)
#     return sons
# sons = carregar_sons('../assets/musicas')
# # tela = pygame.display.set_mode((400, 300))
# # pygame.display.set_caption("Testando Sons")
# rodando = True
# while rodando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_SPACE:
#                 sons['Polyphia-Playing_God'].set_volume(Volume_Musica)
#                 sons['Polyphia-Playing_God'].play()  # Toca o som ao apertar espaço

# pygame.quit()
