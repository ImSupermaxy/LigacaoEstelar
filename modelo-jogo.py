import pygame

pygame.init()

TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
FONTE = pygame.font.SysFont("arial", 32)

def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        TELA.fill(PRETO)
        texto = FONTE.render("O jogo começou! Boa sorte!", True, BRANCO)
        TELA.blit(texto, (150, 250))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()