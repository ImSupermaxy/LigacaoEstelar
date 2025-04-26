import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Céu Estrelado")

# Cores
azul_ceu = (10, 10, 40)     # Azul escuro para o fundo
estrela = (255, 255, 255)   # Branco para as estrelas

# Preenche o fundo com azul escuro
tela.fill(azul_ceu)

# Adiciona estrelas aleatórias
quantidade_estrelas = 300
for _ in range(quantidade_estrelas):
    x = random.randint(0, largura - 1)
    y = random.randint(0, altura - 1)
    tela.set_at((x, y), estrela)

# Atualiza a tela com os pixels desenhados
pygame.display.flip()

# Loop principal para manter a janela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# Finaliza o Pygame
pygame.quit()
sys.exit()
