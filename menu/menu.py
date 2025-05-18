
import sys
import random
import pygame
import main
from fases import fases_menu
from menu import configuracoes
import configuracoes.variables as config
import menu.manual as manual

primeira_opcao = "Iniciar" if not config.IsContinuacao else "Continuar"
opcoes_menu = {
    1: primeira_opcao,
    2: "Config",
    3: "Fases",
    4: "Manual",
    5: "Fechar"
}
opcao_atual = 1

opcoes_menu_not_inicial = {
    1: opcoes_menu.get(2, ""),
    2: opcoes_menu.get(3, ""),
    3: opcoes_menu.get(4, ""),
    3: "Voltar ao menu"
}

def inicar_menu(is_calling_initial=True):
    selecao_menu(is_calling_initial)

    pygame.display.update()
    

def selecao_menu(is_calling_initial=True):
    config.TELA.fill(config.BACKGROUND_JOGO)
    global opcao_atual, primeira_opcao
    opcao_atual = 1

    primeira_opcao = "Iniciar" if not config.IsContinuacao else "Continuar"
    opcoes_menu[1] = primeira_opcao
    carregar_menu(is_calling_initial)
    
    rodando = True
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
                    if opcao_atual < len(opcoes_menu):
                        opcao_atual += 1
                    else: 
                        opcao_atual = len(opcoes_menu)
                elif evento.key == pygame.K_RETURN:
                    switch_to_opcao(opcao_atual, is_calling_initial)
                elif not is_calling_initial:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
        # pygame.time.delay(150)
        # carregar_menu(is_calling_initial, True)
        carregar_menu(is_calling_initial)
        

def carregar_menu(is_calling_initial, draw_estrelas=False):
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    desenhar_selecao_menu(is_calling_initial)
    
    if draw_estrelas:
        desenhar_menu()
    
    if is_calling_initial:
        desenhar_imagens_menu()


def desenhar_imagens_menu():
    global opcao_atual
    
    # opcoes = opcoes_menu if is_calling_initial else opcoes_menu_not_inicial
    # for i, texto in opcoes.items():
    #     cor = SELECIONADO if i == opcao_atual else CINZA_CLARO
    #     render = FONTE_MENU.render(texto, True, cor)
    #     linha_posicao = PADDING_TOP + i * ESPACAMENTO_LINHA_MENU
    #     TELA.blit(render, (PADDING_LEFT, linha_posicao))
    #     pygame.time.delay(delay)
    # pygame.display.update()

    
def desenhar_menu():
    # Adiciona estrelas aleatórias
    quantidade_estrelas = 2000
    for _ in range(quantidade_estrelas):
        x = random.randint(0, config.LARGURA - 1)
        y = random.randint(0, config.ALTURA - 1)
        pygame.draw.circle(config.TELA, config.BRANCO, (x, y), 1)

    # Atualiza a tela com os pixels desenhados
    pygame.display.flip()


def desenhar_selecao_menu(is_calling_initial, delay=0):
    # retangulo = pygame.Rect(300, 0, 300, ALTURA)
    # TELA.fill(BACKGROUND_JOGO, retangulo)  # Só preenche dentro do retângulo
    global opcao_atual
    
    opcoes = opcoes_menu if is_calling_initial else opcoes_menu_not_inicial
    for i, texto in opcoes.items():
        cor = config.SELECIONADO if i == opcao_atual else config.CINZA_CLARO
        render = config.FONTE_MENU.render(texto, True, cor)
        linha_posicao = config.PADDING_TOP + i * config.ESPACAMENTO_LINHA_MENU
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()


def switch_to_opcao(opcao, is_calling_initial):
    invalido = "opção inválida"
    
    opcoes = opcoes_menu if is_calling_initial else opcoes_menu_not_inicial
    match opcoes.get(opcao, invalido):
        case "Iniciar":
            fases_menu.iniciar_fase(config.FASE_ATUAL, True)
        case "Continuar":
            fases_menu.iniciar_fase(config.FASE_ATUAL, True)
        case "Config":
            configuracoes.iniciar_menu()
        case "Fases":
            fases_menu.visualizar_fases()
        case "Manual":
            manual.show_manual()
        case "Fechar":
            main.fechar_jogo()
        case "Voltar ao menu":
            inicar_menu()