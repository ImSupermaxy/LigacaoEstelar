
import pygame
from main import aguardar, digitar_lento, desenhar_textos, TELA, BACKGROUND_JOGO, FONTE, LARGURA, opcoes_logicas_busca, FASE_ATUAL, VERDE
from fases.fase1 import primeira_fase_iniciar

def inicar_menu(COR_TEXTO, opcao_atual):
    TELA.fill(BACKGROUND_JOGO)
    # pygame.display.update()
    # desenhar_textos(["Teste, tela para o menu, após a escolha"])
    texto = "Teste, tela para o menu, após a escolha"
    titulo = FONTE.render(texto, True, COR_TEXTO)
    width = LARGURA // 2 - titulo.get_width() // 2
    TELA.blit(titulo, (width, 100))

    digitar_lento(opcoes_logicas_busca.get(opcao_atual + 1), [], 0, 0, VERDE)
    aguardar(largura=width + len(texto) * 10 + 20,altura=100)

    iniciar_fase(FASE_ATUAL, opcoes_logicas_busca.get(opcao_atual))

    pygame.display.update()
    
    
# Chama a fase atual do personagem
def iniciar_fase(fase, logica_busca_grafo):
    match fase:
        case "fase 1":
            primeira_fase_iniciar(TELA, LARGURA, opcoes_logicas_busca, logica_busca_grafo)
        case "fase 2":
            print("Dois")
        case "fase 3":
            print("Três")
        case "fase 4":
            print("Outro número")   
    
    pygame.quit()
    # os.system("python jogo.py")  # ou "python3 jogo.py"