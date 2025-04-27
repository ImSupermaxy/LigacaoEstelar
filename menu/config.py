import sys
import pygame
import main
from config.variables import *

opcoes_menu = {
    1: "Volume",
    2: "Texto", #Aparecer a configuração da velocidade dos diálogos / fonte do texto...
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

    desenhar_selecao_menu(50)
    is_switch_to_opcao = False
    
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
                    if (opcao_atual + 1) < len(opcoes_menu):
                        opcao_atual += 1
                    else: 
                        opcao_atual = len(opcoes_menu)
                elif evento.key == pygame.K_ESCAPE:
                    rodando = False
                    break
                elif evento.key == pygame.K_RETURN:
                    rodando = False
                    is_switch_to_opcao = True
        desenhar_selecao_menu()
    
    if is_switch_to_opcao:
        switch_to_opcao(opcao_atual)
        selecao_menu()
    
        


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
    match opcao:
        case 1:
            alterar_volume()
        case 2:
            main.fechar_jogo()


def alterar_volume():
    global opcao_volume_atual
    posicoes_y = desenhar_selecao_menu_volume(50)
    valor_to_change = get_volume_to_change(opcao_volume_atual)
    
    rodando_volume = True
    while rodando_volume:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if opcao_volume_atual == 0:
                        opcao_volume_atual = 1
                    elif (opcao_volume_atual - 1) > 0 :
                        opcao_volume_atual -= 1
                    else:
                        opcao_volume_atual = 1
                    valor_to_change = get_volume_to_change(opcao_volume_atual)
                elif evento.key == pygame.K_DOWN:
                    if opcao_volume_atual == 0:
                        opcao_volume_atual = 1
                    elif (opcao_volume_atual + 1) < len(opcoes_volume):
                        opcao_volume_atual += 1
                    else: 
                        opcao_volume_atual = len(opcoes_volume)
                    valor_to_change = get_volume_to_change(opcao_volume_atual)
                elif evento.key == pygame.K_RETURN:
                    change_volume(valor_to_change, posicoes_y)
                elif evento.key == pygame.K_ESCAPE:
                    opcao_volume_atual = 0
                    rodando_volume = False
        
        desenhar_selecao_menu_volume()
    

def desenhar_selecao_menu_volume(delay=0):
    TELA.fill(BACKGROUND_JOGO)
    render = FONTE.render("Configurações Volume: ", True, AZUL_CLARO)
    TELA.blit(render, ((PADDING_LEFT / 2), (PADDING_TOP / 2)))
    
    global opcao_volume_atual
    alturas = []
    
    for i, texto in opcoes_volume.items():
        cor = SELECIONADO if i == opcao_volume_atual else COR_TEXTO
        render = FONTE.render(texto, True, cor)
        linha_posicao = PADDING_TOP + i * ESPACAMENTO_LINHA
        
        alturas.append(linha_posicao)
        TELA.blit(render, (PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()
    return alturas


def change_volume(valor_to_change, alturas):
    altura, texto = alturas[opcao_volume_atual - 1], opcoes_volume.get(opcao_volume_atual)

    rodando = True
    while rodando:
        exibir_volume_to_change(altura, texto, str(valor_to_change))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    if valor_to_change > 0:
                        valor_to_change -= 5
                elif evento.key == pygame.K_RIGHT:
                    if valor_to_change < 100:
                        valor_to_change += 5
                elif evento.key == pygame.K_RETURN:
                    mudar_volume(valor_to_change)
                elif evento.key == pygame.K_ESCAPE:
                    exibir_volume_to_change(altura, "", "")
                    rodando = False    


def exibir_volume_to_change(altura, texto, valor_to_exibir):
    all_texto = valor_to_exibir + "%"
    posicao_texto = len(texto) * 16
    retangulo = pygame.Rect((PADDING_LEFT // 2) + posicao_texto, altura, len(all_texto) + 60, 50)

    # Desenhando o retângulo vermelho
    pygame.draw.rect(TELA, BACKGROUND_JOGO, retangulo)
    
    render = FONTE.render(all_texto, True, BRANCO)
    TELA.blit(render, ((PADDING_LEFT // 2) + posicao_texto, altura))
    pygame.display.update()   


def get_volume_to_change(opcao):
    
    match opcao:
        case 1:
            return Volume
        case 2:
            return Volume_Efeitos * 100
        case 3:
            return Volume_Dialogos * 100
        case 4:
            return Volume_Musica * 100
        
    return 0



def mudar_volume(volume_to_change):
    volume_master = Volume
    volume_dialogos = Volume_Dialogos
    volume_efeitos = Volume_Efeitos
    voluma_musica = Volume_Musica
    
    voluma_musica = 20
    global opcao_volume_atual
    
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