import os
import main
from fases import fase1, fase2, fase3, fase4, fase5
import pygame
import configuracoes.variables as config
import menu.menu as menu
import assets.imagens.manipulerimg as mimg
import assets.audios.manipuleraudio as maudio

def visualizar_fases():
    iniciar_menu()

opcao_atual = config.dados["fases"]["atual"]
fases_concluidas = []

opcoes_menu = [
    "Voltar",
]

opcao_menu_atual = 0

# Chama a fase atual do personagem
def iniciar_fase(fase, resetar):
    isFaseConcluida = False
    
    match fase:
        case "fase 1":
            if resetar:
                config.reset_fases_of_atual(1)
            isFaseConcluida = fase1.primeira_fase_iniciar(resetar)
            config.update_is_continuacao()
        case "fase 2":
            if resetar:
                config.reset_fases_of_atual(2)
            isFaseConcluida = fase2.segunda_fase_iniciar(resetar)
        case "fase 3":
            if resetar:
                config.reset_fases_of_atual(3)
            isFaseConcluida = fase3.terceira_fase_iniciar(resetar)
        case "fase 4":
            if resetar:
                config.reset_fases_of_atual(4)
            isFaseConcluida = fase4.quarta_fase_iniciar(resetar)
        case "fase 5":
            if resetar:
                config.reset_fases_of_atual(5)
            isFaseConcluida = fase5.quinta_fase_iniciar(resetar)
    
    # if config.dados["jogo_concluido"]:
        # colocar a tela de final de jogo aqui...
    
    if not isFaseConcluida or fase == "fase 5":
        menu.inicar_menu()


def iniciar_menu():
    global opcao_atual
    global opcoes_menu
    global opcao_menu_atual
    global fases_concluidas
    
    opcoes_menu = [
        "Voltar",
    ]
    
    opcao_menu_atual = 0
    opcao_atual = config.dados["fases"]["atual"]
        
    i = 1
    fases_concluidas = []
    while i <= len(config.FASES_CONCLUIDAS):
        fases_concluidas.append(config.FASES[config.FASES_CONCLUIDAS[i - 1] - 1])
        i = i + 1    
        
    selecao_fases()


def switch_to_fase():
    main.fechar_jogo()


def open_resumo_fase():
    global opcoes_menu
    global opcao_menu_atual
    global fases_concluidas
    
    
    
    config.TELA.fill(config.BACKGROUND_JOGO)
    opcoes_menu = [
        "Começar missão",
        "Visualizar",
        "Voltar"
    ]
    
    opcao_menu_atual = 1

    rodando = True
    while rodando:
        desenha_opces_menu()
        desenhar_resumo_missao(True)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    rodando = False
                    opcoes_menu = [
                        "Voltar",
                    ]
                    opcao_menu_atual = 0
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    rodando = not switch_to_opcao()
                elif evento.key == pygame.K_UP:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_menu_atual - 1 < 1:
                        opcao_menu_atual = 1
                    else:
                        if config.FASES[opcao_atual - 1] not in fases_concluidas:
                            opcao_menu_atual = 1
                        else:
                            opcao_menu_atual = opcao_menu_atual - 1
                elif evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_menu_atual + 1 > 3:
                        opcao_menu_atual = 1
                    else:
                        if config.FASES[opcao_atual - 1] not in fases_concluidas and opcao_menu_atual == 1:
                            opcao_menu_atual = opcao_menu_atual + 2
                        else:
                            opcao_menu_atual = opcao_menu_atual + 1

def switch_to_opcao():
    global opcoes_menu
    global opcao_menu_atual
    
    i = 1
    fases_concluidas = []
    while i <= len(config.FASES_CONCLUIDAS):
        fases_concluidas.append(config.FASES[config.FASES_CONCLUIDAS[i - 1] - 1])
        i = i + 1
    
    if opcao_menu_atual > 0:
        match opcoes_menu[opcao_menu_atual - 1]:
            case "Voltar":
                opcoes_menu = [
                    "Voltar",
                ]
                opcao_menu_atual = 0
    
                return True
            case "Visualizar":
                iniciar_fase(config.FASES[opcao_atual - 1], False)
            case "Começar missão":
                iniciar_fase(config.FASES[opcao_atual - 1], True)
    else:  
        open_resumo_fase()
    
    return False
    

def selecao_fases():
    global opcao_atual
    global opcao_menu_atual
    
    rodando = True
    while rodando:
        desenha_opces_menu()
        desenhar_selecao_fases(True)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_menu_atual == 0:
                        if opcao_atual + 3 > config.dados["fases"]["atual"]:
                            opcao_atual = config.dados["fases"]["atual"]
                        else:
                            opcao_atual = opcao_atual + 3
                if evento.key == pygame.K_UP:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_menu_atual == 0:
                        if opcao_atual - 3 < 1:
                            opcao_atual = 1
                        else:
                            opcao_atual = opcao_atual - 3
                elif evento.key == pygame.K_LEFT:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    if opcao_atual - 1 < 1:
                        if opcao_atual == 1:
                            opcao_atual = opcao_atual - 1
                        opcao_menu_atual = 1
                    else:
                        opcao_atual = opcao_atual - 1
                elif evento.key == pygame.K_RIGHT:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_MENU)
                    opcao_menu_atual = 0
                    if opcao_atual + 1 > config.dados["fases"]["atual"]:
                        opcao_atual = config.dados["fases"]["atual"]
                    else:
                        opcao_atual = opcao_atual + 1
                elif evento.key == pygame.K_RETURN:
                    maudio.play_efeito_sonoro(config.AUDIO_SELECAO_FASE)
                    rodando = not switch_to_opcao()
                elif evento.key == pygame.K_ESCAPE:
                    maudio.play_efeito_sonoro(config.AUDIO_DESELECAO_FASE)
                    rodando = False


def desenha_opces_menu(update_tela = False):
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    for i, texto in enumerate(opcoes_menu):
        cor = config.SELECIONADO if i == opcao_menu_atual - 1 else config.CINZA_FASES_MENU if i == 1 and config.FASES[opcao_atual - 1] not in fases_concluidas else config.COR_TEXTO
        render = config.FONTE.render(texto, True, cor)
         
        posicao_inicial = 320
        espacamento_linha = 50
        linha_posicao = posicao_inicial + i * espacamento_linha
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
    
    if update_tela:
        pygame.display.update()


def desenhar_resumo_missao(is_update_tela):
    largura_caixa_fase = 320
    altura_caixa_fase = 120
       
    render = config.FONTE.render(config.FASES[opcao_atual - 1], True, config.CIANO)
    config.TELA.blit(render, (largura_caixa_fase, altura_caixa_fase))
    
    desenha_caixa_fases(largura_caixa_fase, altura_caixa_fase, config.CIANO)

    largura_caixa_descricao = 1100
    altura_caixa_descricao = 380
    padding_top_caixa_descricao = 90
    desenha_caixa_fases(largura_caixa_descricao, (config.ALTURA // 2) - 50, config.LINHA_FASES_MENU, altura_caixa_descricao, padding_top_caixa_descricao, 4)
    
    padding_top_caixa_imagem = 60
    #LINHA 1
    pos1_linha = (largura_caixa_descricao + 128, padding_top_caixa_descricao - 20)
    pos2_linha =  (largura_caixa_descricao + 128, altura_caixa_descricao - padding_top_caixa_imagem)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)
    
    #LINHA 2
    pos1_linha = (largura_caixa_descricao + 128, altura_caixa_descricao - padding_top_caixa_imagem)
    pos2_linha =  (largura_caixa_descricao + 128 + 300, altura_caixa_descricao - padding_top_caixa_imagem)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)

    #desenhar infos da tela...
    info_fase = {
        "resumo": [],
        "cliente": "",
        "planeta": "",
        "destino": "",
        "dificuldade": "?",
        "arquivo_cliente": "",
        "arquivo_planeta": ""
    }
    
    info_fase = config.get_info_resumo_fase(opcao_atual)

    imagem = info_fase["arquivo_planeta"]
    imagem_original = mimg.get_imagem(imagem)

    imagem = imagem_original
    # Redimensionar a imagem (por exemplo, para 50% do tamanho original)
    if imagem_original.get_width() > 560:
        largura = imagem_original.get_width() // 4
        altura = imagem_original.get_height() // 4
        imagem = pygame.transform.scale(imagem_original, (largura, altura))
    else:
        largura = imagem_original.get_width() // 2
        altura = imagem_original.get_height() // 2
        imagem = pygame.transform.scale(imagem_original, (largura, altura))
    
    config.TELA.blit(imagem, (largura_caixa_descricao + 134, padding_top_caixa_descricao - 23))
        
    padding_resumo = largura_caixa_fase + 420
    main.desenhar_textos(info_fase["resumo"], config.COR_TEXTO, padding_top_caixa_descricao - 20, padding_resumo, False, config.FONTE_RESUMO_FASE, 30)
    
    nome_cliente = info_fase["cliente"]
    nome_planeta = info_fase["planeta"]
    destino = info_fase["destino"]
    dificuldade = info_fase["dificuldade"]

    desenha_resumo_geral_missao("Cliente: ", nome_cliente, padding_resumo, config.ALTURA - (70 + 30 * 4))
    desenha_resumo_geral_missao("planeta: ", nome_planeta, padding_resumo, config.ALTURA - (70 + 30 * 3))
    desenha_resumo_geral_missao("destino: ", destino, padding_resumo, config.ALTURA - (70 + 30 * 2))
    desenha_resumo_geral_missao("dificuldade: ", dificuldade, padding_resumo, config.ALTURA - (70 + 30 * 1), config.VERDE)
    
    #DESENHA TÍTULO
    main.desenhar_textos(["D e s c r i ç ã o   d a   m i s s ã o"], config.AMARELO, padding_top_caixa_descricao - 65, padding_resumo, False, config.FONTE2)
    
    if is_update_tela:
        config.pygame.display.update()
    

def desenha_caixa_fases(largura, altura, cor, raio = 80, padding_top = 40, largura_linha = 2):
    padding_text = 50
    
    #LINHA 1
    pos1_linha = (largura - raio, altura - (raio - padding_top))
    pos2_linha =  (largura - raio, altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, largura_linha)
    
    #LINHA 2
    pos1_linha = (largura + (raio + padding_text), altura - (raio - padding_top))
    pos2_linha =  (largura + (raio + padding_text), altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, largura_linha)
    
    #LINHA 3
    pos1_linha = (largura - raio, altura + raio)
    pos2_linha =  (largura + (raio + padding_text), altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, largura_linha)


def desenhar_selecao_fases(update_tela = False):    
    espacamento_caixa_fase = 320
    espacamento_linha = 150
    linha_posicao = 350
    padding_left_caixa_fase = 250

    i2 = 1
    for i, texto in enumerate(config.FASES):
        cor = config.SELECIONADO if (i + 1) == opcao_atual else config.AMARELO if texto in fases_concluidas else config.CINZA_FASES_MENU if i + 1 > config.dados["fases"]["atual"] else config.COR_TEXTO
        render = config.FONTE.render(texto, True, cor)
         
        linha_posicao = padding_left_caixa_fase + (i + 1) * espacamento_caixa_fase
        
        # #adicionar a cor branca pra quando a fase for possível de selecionar
        # cor_linha = config.AMARELO if texto in fases_concluidas else config.CINZA_CLARO
        
        #detalhe não vai funcionar caso precise de 3 linhas ou mais... (altrar a lógica)
        if linha_posicao > config.LARGURA:
            linha_posicao = padding_left_caixa_fase + i2 * espacamento_caixa_fase
            altura_texto = espacamento_linha * 3
            
            config.TELA.blit(render, (linha_posicao, altura_texto))
            i2 += 1
            
            desenha_caixa_fases(linha_posicao, altura_texto, cor)
        else: 
            config.TELA.blit(render, (linha_posicao, espacamento_linha))
            desenha_caixa_fases(linha_posicao, espacamento_linha, cor)

    if update_tela:
        pygame.display.update()
    # aguardar_confirmacao(altura=ultima_linha + 60)
    
    
def desenha_resumo_geral_missao(texto, valor, altura, largura, cor_secundaria=config.COR_TEXTO):
    main.desenhar_textos([texto], config.SELECIONADO, largura, altura, False, config.FONTE_RESUMO_FASE)
    main.desenhar_textos([valor], cor_secundaria, largura, altura + len(texto) * 8, False, config.FONTE_RESUMO_FASE)