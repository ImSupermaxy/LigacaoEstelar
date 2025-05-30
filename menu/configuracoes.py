import sys
import pygame
import main
import configuracoes.variables as config
import menu.menu as menu
import assets.audios.manipuleraudio as maudio

opcoes_menu = {
    1: "Volume",
    2: "Textos",
    3: "Voltar",
}
opcao_atual = 1

opcoes_volume = {
    1: "Volume Geral: ",
    2: "Efeitos Sonoros: ",
    3: "Diálogos: ",
    4: "Músicas: "
}
opcao_volume_atual = 1

opcoes_textos = {
    1: "Pular histórias: ",
    2: "Pular ???: ",
    3: "... "
}
opcao_texto_atual = 1


def iniciar_menu():
    selecao_menu()


def selecao_menu():
    config.TELA.fill(config.BACKGROUND_JOGO)
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
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if (opcao_atual - 1) > 0 :
                        opcao_atual -= 1
                    else:
                        opcao_atual = 1
                elif evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if (opcao_atual + 1) < len(opcoes_menu):
                        opcao_atual += 1
                    else: 
                        opcao_atual = len(opcoes_menu)
                elif evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    rodando = False
                    break
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    rodando = False
                    is_switch_to_opcao = True
        desenhar_selecao_menu()
    
    if is_switch_to_opcao:
        show_menu_again = not switch_to_opcao(opcao_atual)
        
        if show_menu_again:
            selecao_menu()
        

def desenhar_selecao_menu(delay=0):
    config.TELA.fill(config.BACKGROUND_JOGO)
    global opcao_atual
    
    for i, texto in opcoes_menu.items():
        cor = config.SELECIONADO if i == opcao_atual else config.CINZA_CLARO
        render = config.FONTE_MENU.render(texto, True, cor)
        linha_posicao = config.PADDING_TOP + i * config.ESPACAMENTO_LINHA_MENU
        # ultima_linha = linha_posicao
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()


def switch_to_opcao(opcao):
    match opcao:
        case 1:
            alterar_volume()
        case 2:
            alterar_textos()
        case 3:
            return True
        
    return False


def alterar_volume():
    global opcao_volume_atual
    posicoes_y = desenhar_selecao_menu_volume(50)
    
    rodando_volume = True
    while rodando_volume:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_volume_atual == 0:
                        opcao_volume_atual = 1
                    elif (opcao_volume_atual - 1) > 0 :
                        opcao_volume_atual -= 1
                    else:
                        opcao_volume_atual = 1
                elif evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_volume_atual == 0:
                        opcao_volume_atual = 1
                    elif (opcao_volume_atual + 1) < len(opcoes_volume):
                        opcao_volume_atual += 1
                    else: 
                        opcao_volume_atual = len(opcoes_volume)
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    change_volume(posicoes_y)
                elif evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    opcao_volume_atual = 1
                    rodando_volume = False
        
        desenhar_selecao_menu_volume()


def desenhar_selecao_menu_volume(delay=0):
    config.TELA.fill(config.BACKGROUND_JOGO)
    render = config.FONTE_MENU.render("Configurações Volume: ", True, config.AZUL_CLARO)
    config.TELA.blit(render, ((config.PADDING_LEFT / 2) + 20, (config.PADDING_TOP / 2)))
    
    global opcao_volume_atual
    alturas = []
    
    for i, texto in opcoes_volume.items():
        cor = config.SELECIONADO if i == opcao_volume_atual else config.COR_TEXTO
        render = config.FONTE_MENU.render(texto, True, cor)
        linha_posicao = config.PADDING_TOP + i * config.ESPACAMENTO_LINHA_MENU
        
        alturas.append(linha_posicao)
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()
    return alturas


def change_volume(alturas):
    if opcao_volume_atual == 0:
        return
    altura, texto = alturas[opcao_volume_atual - 1], opcoes_volume.get(opcao_volume_atual)
    valor_to_change = get_volume_to_change(opcao_volume_atual)

    rodando = True
    while rodando:
        exibir_volume_to_change(altura, texto, str(valor_to_change))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if valor_to_change > 0:
                        valor_to_change -= 5
                elif evento.key == pygame.K_RIGHT:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if valor_to_change < 100:
                        valor_to_change += 5
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    mudar_volume(valor_to_change)
                    rodando = False
                elif evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    exibir_volume_to_change(altura, "", "")
                    rodando = False    


def exibir_volume_to_change(altura, texto, valor_to_exibir):
    all_texto = valor_to_exibir + "%"
    posicao_texto = len(texto) * 14
    retangulo = pygame.Rect(config.PADDING_LEFT + posicao_texto, altura, len(all_texto) + 60, 50)

    # Desenhando o retângulo vermelho
    pygame.draw.rect(config.TELA, config.BACKGROUND_JOGO, retangulo)
    
    render = config.FONTE.render(all_texto, True, config.BRANCO)
    config.TELA.blit(render, (config.PADDING_LEFT + posicao_texto, altura))
    pygame.display.update()   


def get_volume_to_change(opcao):
    
    match opcao:
        case 1:
            return config.Volume
        case 2:
            return config.Volume_Efeitos
        case 3:
            return config.Volume_Dialogos
        case 4:
            return config.Volume_Musica
        
    return 0


def mudar_volume(volume_to_change):
    global opcao_volume_atual
    # print(volume_to_change)
    
    match opcao_volume_atual:
        case 1:
            config.Volume = volume_to_change
        case 2:
            config.Volume_Efeitos = volume_to_change
        case 3:
            config.Volume_Dialogos = volume_to_change
        case 4:
            config.Volume_Musica = volume_to_change
        case 0:
            config.Volume = config.Volume
            config.Volume_Efeitos = config.Volume_Efeitos
            config.Volume_Dialogos = config.Volume_Dialogos
            config.Volume_Musica = config.Volume_Musica
    
    config.update_all_volumes()

    main.transicao(50)
    menu.reiniciar_musica()


def alterar_textos():
    global opcao_texto_atual
    posicoes_y = desenhar_selecao_menu_textos(50)
    
    rodando_texto = True
    while rodando_texto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_texto_atual == 0:
                        opcao_texto_atual = 1
                    elif (opcao_texto_atual - 1) > 0 :
                        opcao_texto_atual -= 1
                    else:
                        opcao_texto_atual = 1
                elif evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_texto_atual == 0:
                        opcao_texto_atual = 1
                    elif (opcao_texto_atual + 1) < len(opcoes_textos):
                        opcao_texto_atual += 1
                    else: 
                        opcao_texto_atual = len(opcoes_textos)
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    change_texto(posicoes_y)
                elif evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    opcao_texto_atual = 1
                    rodando_texto = False
        
        desenhar_selecao_menu_textos()


def desenhar_selecao_menu_textos(delay=0):
    config.TELA.fill(config.BACKGROUND_JOGO)
    render = config.FONTE_MENU.render("Configurações de Texto: ", True, config.AZUL_CLARO)
    config.TELA.blit(render, ((config.PADDING_LEFT / 2) + 20, (config.PADDING_TOP / 2)))
    
    global opcao_texto_atual
    alturas = []
    
    for i, texto in opcoes_textos.items():
        cor = config.SELECIONADO if i == opcao_texto_atual else config.COR_TEXTO
        render = config.FONTE_MENU.render(texto, True, cor)
        linha_posicao = config.PADDING_TOP + i * config.ESPACAMENTO_LINHA_MENU
        
        alturas.append(linha_posicao)
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
        pygame.time.delay(delay)

    pygame.display.update()
    return alturas


def change_texto(alturas):
    if opcao_texto_atual == 0:
        return
    altura, texto = alturas[opcao_texto_atual - 1], opcoes_textos.get(opcao_texto_atual)
    valor_to_change = get_texto_to_change(opcao_texto_atual)

    rodando = True
    while rodando:
        exibir_textos_to_change(altura, texto, str(valor_to_change))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    valor_to_change = not valor_to_change
                elif evento.key == pygame.K_RIGHT:
                    valor_to_change = not valor_to_change
                elif evento.key == pygame.K_RETURN:
                    mudar_textos(valor_to_change)
                    rodando = False
                elif evento.key == pygame.K_ESCAPE:
                    exibir_textos_to_change(altura, "", "")
                    rodando = False
                    
def get_texto_to_change(opcao):
    match opcao:
        case 1:
            return config.SkipHistoria
        case 2:
            return config.SkipDialogos
        case 3:
            return False
        case 4:
            return False
        
    return 0

def exibir_textos_to_change(altura, texto, valor_to_exibir):
    all_texto = str(valor_to_exibir)
    posicao_texto = len(texto) * 14
    retangulo = pygame.Rect(config.PADDING_LEFT + posicao_texto, altura, len(all_texto) + 60, 50)

    # Desenhando o retângulo vermelho
    pygame.draw.rect(config.TELA, config.BACKGROUND_JOGO, retangulo)
    
    render = config.FONTE.render(all_texto, True, config.BRANCO)
    config.TELA.blit(render, (config.PADDING_LEFT + posicao_texto, altura))
    pygame.display.update()  
    

def mudar_textos(texto_to_change):
    global opcao_texto_atual
    
    match opcao_volume_atual:
        case 1:
            config.SkipHistoria = texto_to_change
        case 2:
            config.SkipDialogos = texto_to_change
        case 3:
            return False
        case 4:
            return False
        case 0:
            config.Volume = config.Volume
            config.Volume_Efeitos = config.Volume_Efeitos
            config.Volume_Dialogos = config.Volume_Dialogos
            config.Volume_Musica = config.Volume_Musica
    
    config.update_all_texto()

    main.transicao(50)