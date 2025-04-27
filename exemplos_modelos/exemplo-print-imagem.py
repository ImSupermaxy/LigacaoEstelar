import pygame

pygame.init()

# Cria a janela
tela = pygame.display.set_mode((1500, 780))
pygame.display.set_caption("Exibindo Imagem")

# Carrega a imagem (suporta .png, .jpg, .bmp, etc.)
imagem = pygame.image.load('Modelo-Menu.png')  # Caminho da imagem

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))  # Limpa a tela (preto)
    tela.blit(imagem, (0, 0))  # Desenha a imagem na posição (100, 100)
    
    pygame.display.update()

pygame.quit()