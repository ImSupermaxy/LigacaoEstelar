import sys
import pygame
import main
from config.variables import *

opcoes_menu = {
    1: "-> Volume: ",
    2: "-> Algo a mais??",
}
opcao_atual = 1

opcoes_volume = {
    1: "Volume Geral: ", #Altera a Variável Master
    2: "Efeitos Sonoros: ",
    3: "Diálogos: ",
    4: "Músicas: "
}
opcao_volume_atual = 0

def iniciar_menu():
    selecao_menu()


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
                    rodando = False
        
        desenhar_selecao_menu()
        


def desenhar_selecao_menu(delay=0):
    TELA.fill(BACKGROUND_JOGO)

    global opcao_atual
    
    for i, texto in opcoes_menu.items():
        cor = SELECIONADO if i == opcao_atual else CINZA_CLARO
        render = FONTE.render(texto, True, cor)
        linha_posicao = PADDING_TOP + i * ESPACAMENTO_LINHA
        # ultima_linha = linha_posicao
        TELA.blit(render, (PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()


def switch_to_opcao(opcao):
    invalido = "opção inválida"
    match opcao:
        case opcoes_menu.get(1, invalido):
            alterar_volume()
        case opcoes_menu.get(2, invalido):
            main.fechar_jogo()


def alterar_volume():
    posicoes_y = exibir_volume()
    valor_to_change = 0
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if (opcao_volume_atual - 1) > 0 :
                        opcao_volume_atual -= 1
                    else:
                        opcao_volume_atual = 1
                elif evento.key == pygame.K_DOWN:
                    if (opcao_volume_atual + 1) < 5:
                        opcao_volume_atual += 1
                    else: 
                        opcao_volume_atual = 4
                elif evento.key == pygame.K_ESCAPE:
                    opcao_volume_atual = 0
                    mudar_volume()
                    rodando = False
        
        desenhar_selecao_menu()
    

def exibir_volume():
    TELA.fill(BACKGROUND_JOGO)
    render = FONTE.render("Volume", True, CINZA_CLARO)
    TELA.blit(render, ((PADDING_LEFT / 2), (PADDING_TOP / 2)))
    
    alturas = []
    
    for i, texto in opcoes_volume.items():
        cor = SELECIONADO if i == opcao_volume_atual else COR_TEXTO
        render = FONTE.render(texto, True, cor)
        linha_posicao = PADDING_TOP + i * ESPACAMENTO_LINHA
        
        alturas.append(linha_posicao)
        TELA.blit(render, (PADDING_LEFT, linha_posicao))

    pygame.display.update()
    return alturas


def exibir_volume_to_change():
    #adicionar essa parte para exibir o volume ao lado da sua opção e conseguir mudá-lo
    opcao_volume_atual = 0
    mudar_volume(100)
    #  elif evento.key == pygame.K_RETURN:
    #     exibir_volume_to_change()


def mudar_volume(volume_to_change):
    volume_master = Volume
    volume_dialogos = Volume_Dialogos
    volume_efeitos = Volume_Efeitos
    voluma_musica = Volume_Musica
    
    voluma_musica = 20
    
    match opcao_volume_atual:
        case 0:
            update_volume(volume_master, volume_dialogos, volume_efeitos, voluma_musica)
        case 1:
            volume_master = volume_to_change
        case 2:
            volume_dialogos = volume_to_change
        case 3:
            volume_efeitos = volume_to_change
        case 4:
            voluma_musica = volume_to_change
    
    update_volume(volume_master, volume_dialogos, volume_efeitos, voluma_musica)
    print(Volume, Volume_Dialogos, Volume_Efeitos, Volume_Musica)