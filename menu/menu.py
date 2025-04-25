
import sys
import pygame
import main
from config.variables import *
from fases import fases_menu
from menu import config

primeira_opcao = "Iniciar" if not ISCONTINUACAO else "Continuar"
opcoes_menu = {
    1: primeira_opcao,
    2: "Config?", # (audio? texto? personalização?)
    3: "Fases",
    4: "Fechar"
}
opcao_atual = 1

def inicar_menu():
    selecao_menu()

    pygame.display.update()
    

def selecao_menu():
    TELA.fill(BACKGROUND_JOGO)
    global opcao_atual
    
    rodando = True
    
    desenhar_selecao_menu(50)
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if (opcao_atual - 1) > 0 :
                        opcao_atual -= 1
                    else:
                        opcao_atual = 1
                elif evento.key == pygame.K_DOWN:
                    if (opcao_atual + 1) < 5:
                        opcao_atual += 1
                    else: 
                        opcao_atual = 4
                elif evento.key == pygame.K_RETURN:
                    switch_to_opcao(opcao_atual)
        
        desenhar_selecao_menu()
        


def desenhar_selecao_menu(delay=0):
    TELA.fill(BACKGROUND_JOGO)

    global opcao_atual

    espacamento_linha = 40
    linha_posicao = 200

    # render = FONTE.render("Escolha uma das opções: ", True, BRANCO)
    # TELA.blit(render, (PADDING_LEFT, linha_posicao))
    # linha_posicao += espacamento_linha

    # ultima_linha = 0
    
    for i, texto in opcoes_menu.items():
        cor = SELECIONADO if i == opcao_atual else CINZA_CLARO
        render = FONTE.render(texto, True, cor)
        linha_posicao = 200 + i * espacamento_linha
        # ultima_linha = linha_posicao
        TELA.blit(render, (PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)
        
    # titulo = FONTE.render("O que você deseja fazer?", True, BRANCO)
    # ultima_linha = ultima_linha + 80
    # TELA.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ultima_linha))

    pygame.display.update()
    # aguardar_confirmacao(altura=ultima_linha + 60)


def switch_to_opcao(opcao):
    invalido = "opção inválida"
    
    match opcoes_menu.get(opcao, invalido):
        case "Iniciar":
            fases_menu.iniciar_fase(FASE_ATUAL)
        case "Config?":
            config.iniciar_menu()
        case "Fases":
            fases_menu.visualizar_fases()
        case "Fechar":
            main.fechar_jogo()
            print("???")