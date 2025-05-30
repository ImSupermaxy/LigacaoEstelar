import configuracoes.variables as config
import main

TEXTO = [
    "Obrigado por jogar Ligação Estelar!! ",
    "Este é um jogo / projeto dedicado ao trabalho da faculdade",
    "Com o tema de grafos para a matéria Teoria dos Grafos",
    "Esperamos que tenha gostado... ",
    "E até uma próxima."
]

CREDITOS = {
    "Jogo feito por: ": "",
    "Desenvolvimento: ": "Matheus Morais",
    "Roteirização: ": "Lucas Dias",
    "Musica e Audio: ": "Gustavo Milanezi, Undertale - (by: Tobby FOX)",
    "Produção Geral: ": "Matheus Morais, Lucas Dias, Gustavo Milanezi",
    "Testes": "Lucas Dias",
    "Documentação: ": "Lucas Dias",
    "Agradecimentos: ": "Professoa Andrea Ono Sakai"
}


def desenha_texto():
    delay_paragrafo = 200
    delay_linha = 50
    
    linhas_mostradas = []
    emit_sound = True
    largura = config.LARGURA // 2
    altura = config.ALTURA // 2 - (len(TEXTO) * 40)
    for i, paragrafo in enumerate(TEXTO):
        pular = main.digitar_lento(paragrafo, linhas_mostradas, delay_linha, config.CINZA_CLARO, altura=altura, largura=largura - 35 * 14, fonte=config.FONTE_FINAL_FASE, som=emit_sound)
        linhas_mostradas.append(paragrafo)
        if pular:
            emit_sound = False
            delay_linha = 0
            delay_paragrafo = 30

        main.pygame.time.delay(delay_paragrafo)


def desenha_creditos():
    padding_creditos = 680
    altura = config.ALTURA - (len(CREDITOS) * 40)
    largura = config.LARGURA
    for tema, paragrafo in CREDITOS.items():
        render = config.FONTE.render(tema, False, config.AMARELO)
        config.TELA.blit(render, (largura - padding_creditos, altura))
        altura = altura + 40
        
    altura = config.ALTURA - (len(CREDITOS) * 40)
    largura = config.LARGURA
    for tema, paragrafo in CREDITOS.items():
        render = config.FONTE.render(paragrafo, False, config.COR_TEXTO)
        config.TELA.blit(render, (largura - padding_creditos + (15 * 13) , altura))
        altura = altura + 40

    main.pygame.display.update()


def desenha_final_jogo():
    config.TELA.fill(config.BACKGROUND_JOGO)
    desenha_texto()
    desenha_creditos()
    main.aguardar_confirmacao(altura=config.ALTURA - 50, largura=config.LARGURA // 2 - (12 * 40), cor=config.AZUL_CLARO2)