import pygame
import os
import configuracoes.variables as config

def get_imagem(nome_imagem):
    pasta_atual = config.PASTA_IMAGENS
    caminho = os.path.join(pasta_atual, nome_imagem)
    imagem = pygame.image.load(caminho)
    return imagem