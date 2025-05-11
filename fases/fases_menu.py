import main
from fases import fase1, fase2#, fase3, fase4, fase5
import pygame
import configuracoes.variables as config

def visualizar_fases():
    iniciar_menu()

opcao_atual = config.dados["fases"]["atual"]
fases_concluidas = []

opcoes_menu = [
    "Voltar",
]

opcao_menu_atual = 0

# Chama a fase atual do personagem
def iniciar_fase(fase):
    match fase:
        case "fase 1":
            fase1.primeira_fase_iniciar()
            config.update_is_continuacao()
        case "fase 2":
            print("Dois")
        case "fase 3":
            print("Três")
        case "fase 4":
            print("Outro número")
    
    main.fechar_jogo()


def iniciar_menu():
    global fases_concluidas
    global opcao_atual
    global opcoes_menu
    global opcao_menu_atual
    
    opcoes_menu = [
        "Voltar",
    ]
    
    opcao_menu_atual = 0
    
    if not config.dados["fases"]["isAllCompleted"]:
        for i in range(len(config.FASES), 0, -1):
            if i < opcao_atual:
                fases_concluidas.append(config.FASES[i - 1])
    else:
        fases_concluidas = config.FASES
    
    selecao_fases()


def switch_to_fase():
    main.fechar_jogo()


def open_resumo_fase():
    global opcoes_menu
    global opcao_menu_atual
    
    config.TELA.fill(config.BACKGROUND_JOGO)
    opcoes_menu = [
        "Começar missão",
        "Voltar"
    ]
    
    opcao_menu_atual = 1
        
    info_fase = {
        "resumo": [],
        "cliente": "",
        "planeta": "",
        "Destino": "",
        "dificuldade": "?",
        "arquivo_cliente": "",
        "arquivo_planeta": ""
    }
    
    info_fase = config.get_info_resumo_fase(config.FASES[opcao_atual -1])

    #desenhar quadrado do lado direito com as infos de resumo da missão / o quadradinho da fase também...

    rodando = True
    while rodando:
        desenha_opces_menu(True)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                    opcoes_menu = [
                        "Voltar",
                    ]
                    opcao_menu_atual = 0
                elif evento.key == pygame.K_RETURN:
                    rodando = not switch_to_opcao()
                elif evento.key == pygame.K_UP:
                    if opcao_menu_atual - 1 < 1:
                        opcao_menu_atual = 1
                    else:
                        opcao_menu_atual = opcao_menu_atual - 1
                elif evento.key == pygame.K_DOWN:
                    if opcao_menu_atual + 1 > 2:
                        opcao_menu_atual = 1
                    else:
                        opcao_menu_atual = opcao_menu_atual + 1

def switch_to_opcao():
    global opcoes_menu
    global opcao_menu_atual
    
    if opcao_menu_atual > 0:
        match opcoes_menu[opcao_menu_atual - 1]:
            case "Voltar":
                opcoes_menu = [
                    "Voltar",
                ]
                opcao_menu_atual = 1
    
                return True
            case "Começar missão":
                iniciar_fase(config.FASES[opcao_atual - 1])
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
                    if opcao_menu_atual == 0:
                        if opcao_atual + 3 > 5:
                            opcao_atual = 5
                        else:
                            opcao_atual = opcao_atual + 3
                if evento.key == pygame.K_UP:
                    if opcao_menu_atual == 0:
                        if opcao_atual - 3 < 1:
                            opcao_atual = 1
                        else:
                            opcao_atual = opcao_atual - 3
                elif evento.key == pygame.K_LEFT:
                    if opcao_atual - 1 < 1:
                        if opcao_atual == 1:
                            opcao_atual = opcao_atual - 1
                        opcao_menu_atual = 1
                    else:
                        opcao_atual = opcao_atual - 1
                elif evento.key == pygame.K_RIGHT:
                    opcao_menu_atual = 0
                    if opcao_atual + 1 > 5:
                        opcao_atual = 5
                    else:
                        opcao_atual = opcao_atual + 1
                elif evento.key == pygame.K_RETURN:
                    rodando = not switch_to_opcao()
                elif evento.key == pygame.K_ESCAPE:
                    rodando = False


def desenha_opces_menu(update_tela = False):
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    for i, texto in enumerate(opcoes_menu):
        cor = config.SELECIONADO if i == opcao_menu_atual - 1 else config.CINZA_CLARO
        render = config.FONTE.render(texto, True, cor)
         
        posicao_inicial = 320
        espacamento_linha = 50
        linha_posicao = posicao_inicial + i * espacamento_linha
        config.TELA.blit(render, (config.PADDING_LEFT, linha_posicao))
    
    if update_tela:
        pygame.display.update()


def desenha_caixa_fases(largura, altura, cor):
    raio = 80
    padding_text = 50
    padding_top = 40
    
    #LINHA 1
    pos1_linha = (largura - raio, altura - (raio - padding_top))
    pos2_linha =  (largura - raio, altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, 2)
    
    #LINHA 2
    pos1_linha = (largura + (raio + padding_text), altura - (raio - padding_top))
    pos2_linha =  (largura + (raio + padding_text), altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, 2)
    
    #LINHA 3
    pos1_linha = (largura - raio, altura + raio)
    pos2_linha =  (largura + (raio + padding_text), altura + raio)
    main.pygame.draw.line(config.TELA, cor, pos1_linha, pos2_linha, 2)


def desenhar_selecao_fases(update_tela = False):    
    espacamento_caixa_fase = 320
    espacamento_linha = 150
    linha_posicao = 350
    padding_left_caixa_fase = 250

    i2 = 1
    for i, texto in enumerate(config.FASES):
        cor = config.SELECIONADO if (i + 1) == opcao_atual else config.AMARELO if texto in fases_concluidas else config.CINZA_CLARO
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