import main
import pygame
import configuracoes.variables as config
import assets.audios.manipuleraudio as maudio
from menu import menu
from fases import fases_menu

TEXTO = "VOCÊ PERDEU ..."

opcao_menu = 1
opcoes_menu = {
    1: "Voltar ao menu",
    2: "Reiniciar Fase",
    3: "Fechar jogo"
}

def desenha_game_over():
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    desenha_texto()
    delay_to_menu = 500
    pygame.time.delay(delay_to_menu)
    desenhar_menu()

def desenha_texto():
    delay_caracter = 300
    
    emit_sound = True
    mixer = maudio.GLOBAL_MIXER
    if emit_sound:
        mixer = maudio.play_efeito_sonoro(config.AUDIO_TEXTO, True)
            
    largura = config.LARGURA // 2 - len(TEXTO) * 12
    altura = config.ALTURA // 2
    
    for caracter in TEXTO:
        render = config.FONTE2.render(caracter, False, config.VERMELHO2)
        config.TELA.blit(render, (largura, altura))
        largura += 30
        pygame.time.delay(delay_caracter)
        pygame.display.update()
        
    if emit_sound:
        mixer.stop()

def desenhar_selecao_menu(is_firts_call=False):
    global opcao_menu
    
    opcoes = opcoes_menu
    for i, texto in opcoes.items():
        cor = config.SELECIONADO if i == opcao_menu else config.CINZA_CLARO
        render = config.FONTE_MENU.render(texto, True, cor)
        linha_posicao = (config.ALTURA - 350) + (i * config.ESPACAMENTO_LINHA_MENU)

        # Obtém o retângulo do texto
        caixa_rect = pygame.Rect(config.LARGURA // 2 - 200, linha_posicao, 200, 200)
        texto_rect = render.get_rect(center=(caixa_rect.center))

        config.TELA.blit(render, texto_rect.center)
        if is_firts_call:
            pygame.time.delay(150)
        pygame.display.update()


def desenhar_menu():
    global opcao_menu
    opcao_menu = 1
    
    # maudio.iniciar_musica_game_over()
    desenhar_selecao_menu(True)
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if (opcao_menu - 1) > 0 :
                        opcao_menu -= 1
                    else:
                        opcao_menu = 1
                elif evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_menu < len(opcoes_menu):
                        opcao_menu += 1
                    else: 
                        opcao_menu = len(opcoes_menu)
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    switch_to_opcao(opcao_menu)
        desenhar_selecao_menu()


def switch_to_opcao(opcao):
    invalido = "opção inválida"
    
    opcoes = opcoes_menu
    match opcoes.get(opcao, invalido):
        case "Voltar ao menu":
            menu.inicar_menu()
        case "Reiniciar Fase":
            fases_menu.iniciar_fase(config.FASE_ATUAL, True)
        case "Fechar jogo":
            main.fechar_jogo()