import main
from fases import fase1
import pygame
import configuracoes.variables as config

def visualizar_fases():
    iniciar_menu()
    
primeira_opcao = config.FASE_ATUAL
opcoes_menu = {
    1: primeira_opcao,
    2: "config (audio? texto? personalização?)",
    3: "fases",
    4: "Fechar"
}
opcao_atual = 1


# Chama a fase atual do personagem
def iniciar_fase(fase):
    match fase:
        case "fase 1":
            config.update_is_continuacao()
            print(config.IsContinuacao)
            fase1.primeira_fase_iniciar()
        case "fase 2":
            print("Dois")
        case "fase 3":
            print("Três")
        case "fase 4":
            print("Outro número")
    
    main.fechar_jogo()


def iniciar_menu():
    main.fechar_jogo()


def selecao_fases():
    
    rodando = True
    while rodando:
        desenhar_selecao_fases()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcao_atual = (opcao_atual - 1) % len(opcoes_menu)
                elif evento.key == pygame.K_DOWN:
                    opcao_atual = (opcao_atual + 1) % len(opcoes_menu)
                elif evento.key == pygame.K_RETURN:
                    rodando = False


def desenhar_selecao_fases():
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    espacamento_linha = 40
    linha_posicao = 200

    for i, texto in enumerate(opcoes_menu):
        cor = config.SELECIONADO if i == opcao_atual else config.CINZA_CLARO
        render = config.FONTE.render(texto, True, cor)
        linha_posicao = 200 + i * espacamento_linha
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
        pygame.time.delay(200)

    pygame.display.update()
    # aguardar_confirmacao(altura=ultima_linha + 60)