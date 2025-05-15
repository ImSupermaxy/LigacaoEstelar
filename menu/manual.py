import main
import configuracoes.variables as config

def show_manual():
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    desenha_infos_vertices()
    desenha_resumo_jogo()
        
    rodando = True
    while rodando:
        main.desenhar_textos(["Pressione qualquer tecla para voltar"], config.VERMELHO2, config.ALTURA // 2, config.LARGURA - 400, True)
        config.pygame.time.delay(500)
        main.desenhar_textos(["Pressione qualquer tecla para voltar"], config.BACKGROUND_JOGO, config.ALTURA // 2, config.LARGURA - 400, True)
        config.pygame.time.delay(500)
        for evento in config.pygame.event.get():
            if evento.type == config.pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == config.pygame.KEYDOWN:
                rodando = False
    
    # main.aguardar_confirmacao("Pressione [ENTER] para voltar", config.LARGURA // 2,config.ALTURA // 2, config.LARANJA)
    
    
def desenha_infos_vertices():
    NODE_RADIUS = 15
    
    render = config.FONTE_PESO.render("Vértices: ", False, config.AMARELO)
    config.TELA.blit(render, (40, 20))
    
    pos_vertice_inicial = (40 + NODE_RADIUS, 80)    
    config.pygame.draw.circle(config.TELA, config.VERDE_INICIAL, pos_vertice_inicial, NODE_RADIUS)
    largura, altura = pos_vertice_inicial
    render = config.FONTE.render("Este é o vértice inicial, ou o seu ponto de partida para concluir a missão", False, config.COR_TEXTO)
    config.TELA.blit(render, (largura + 20, altura - 15))
    
    pos_vertice_final = (40 + NODE_RADIUS, 120)
    config.pygame.draw.circle(config.TELA, config.CINZA_FINAL, pos_vertice_final, NODE_RADIUS)
    largura, altura = pos_vertice_final
    render = config.FONTE.render("Este é o seu detino final, o vértice que você deve chegar", False, config.COR_TEXTO)
    config.TELA.blit(render, (largura + 20, altura - 15))
    
    
    #LINHA 1
    pos1_linha = (0, altura + 30)
    pos2_linha =  (config.LARGURA // 2 + 50, altura + 30)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)
    
    #LINHA 2
    pos1_linha = (config.LARGURA // 2 + 50, altura + 30)
    pos2_linha =  (config.LARGURA // 2 + 50, 20)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)
    
    config.pygame.display.update()


def desenha_resumo_jogo():
    TEXTO = [
        "\"Em uma galáxia onde os seres humanos estão espalhados em colônias",
        "e todo e qualquer meio de locomoção entre os planetas é incapacitado",
        "por uma densa névoa de lixo espacial",
        "você, trabalha em uma empresa de limpeza espacial, que cuida de limpar",
        "locais inviáveis.\"",
        "",
        "-> Selecione os vértices com menor peso para alcançar o final com a",
        "   melhor pontuação possível;",
        "-> Não ultrapasse a quantidade máxima de lixo que seu equipamento",
        "   aguenta",
        "-> A cada fase o os valores dos pesos diminuirão conforme a sua rota",
        "-> Caso precise rejogue cada fase individualmente no \"menu de fases\""
    ]
    
    altura_historia = 170
    
    render = config.FONTE_PESO.render("Objetivo: ", False, config.AMARELO)
    config.TELA.blit(render, (40, altura_historia))
    
    #LINHA 1
    pos1_linha = (0, altura_historia + (40 * len(TEXTO)) + 50)
    pos2_linha =  (config.LARGURA // 2 + 50, altura_historia + (40 * len(TEXTO)) + 50)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)
    
    #LINHA 2
    pos1_linha = (config.LARGURA // 2 + 50, altura_historia + (40 * len(TEXTO)) + 50)
    pos2_linha =  (config.LARGURA // 2 + 50, altura_historia + 10)
    main.pygame.draw.line(config.TELA, config.LINHA_FASES_MENU, pos1_linha, pos2_linha, 4)

    linhas_mostradas = []
    for i, paragrafo in enumerate(TEXTO):
        pular = main.digitar_lento(paragrafo, linhas_mostradas, 0, altura=altura_historia + 40, largura=40)
        linhas_mostradas.append(paragrafo)
    

    
    config.pygame.display.update()