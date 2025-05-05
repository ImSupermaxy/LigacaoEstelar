import configuracoes.variables as config
import main
from fases import fases_menu

HISOTRIA_FASE_ONE = [
    "\"Nave B-12, câmbio... Nave B-12, na escuta?... Vamo trabalhar!?\"",
    "\"Você acorda na sua nave com o som do seu companheiro no rádio, chamando para uma provável nova expedição.\"",
    "Na janela da cabine, a mesma visão monótona de sempre: o vasto — e agora incomum — espaço, ",
    "sem nenhuma estrela visível, apenas uma imensidão de lixo. Restos de naves, satélites abandonados e ",
    "resíduos expelidos pelas civilizações. ",
    "",
    "A humanidade agora está espalhada por diversos planetas em todo o espaço, após os acontecimentos ",
    "catastróficos no planeta Terra...",
    "\"Chrr-chrr\" — seus pensamentos são interrompidos pelo rádio e, em seguida, a voz dele de novo:",
    "\"Precisam de você aqui. Temos que abrir caminho pra mais um ricasso de férias. Câmbio.\"",
    "Você suspira, liga sua nave, e parte — mais uma vez — para mais um dia de trabalho.",
]

HISOTRIA_FASE_TWO = [
    "\"Nave B-12, câmbio... Nave B-12, na escuta?... Vamo trabalhar!?\"",
    "\"Você acorda na sua nave com o som do seu companheiro no rádio, chamando para uma provável nova expedição.\"",
    "Na janela da cabine, a mesma visão monótona de sempre: o vasto — e agora incomum — espaço, ",
    "sem nenhuma estrela visível, apenas uma imensidão de lixo. Restos de naves, satélites abandonados e ",
    "resíduos expelidos pelas civilizações. ",
    "",
    "A humanidade agora está espalhada por diversos planetas em todo o espaço, após os acontecimentos ",
    "catastróficos no planeta Terra...",
    "\"Chrr-chrr\" — seus pensamentos são interrompidos pelo rádio e, em seguida, a voz dele de novo:",
    "\"Precisam de você aqui. Temos que abrir caminho pra mais um ricasso de férias. Câmbio.\"",
    "Você suspira, liga sua nave, e parte — mais uma vez — para mais um dia de trabalho.",
]

HISTORIAS = {
    config.FASES[0]: HISOTRIA_FASE_ONE,
    config.FASES[1]: HISOTRIA_FASE_TWO,
    # config.FASES[2]: HISOTRIA_FASE_THREE,
    # config.FASES[3]: HISOTRIA_FASE_FOUR,
    # config.FASES[4]: HISOTRIA_FASE_FIVE,
}

# Mostra toda a introdução
def mostrar_historia_fase(fase_atual):
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    TEXTO = HISTORIAS[fase_atual]
    
    altura_historia = config.PADDING_TOP_HISTORIA
    if not config.skipIntroducao:
        linhas_mostradas = []
        delay_linha = 45
        delay_paragrafo = 620
        for i, paragrafo in enumerate(TEXTO):
            pular = main.digitar_lento(paragrafo, linhas_mostradas, delay_linha, altura=altura_historia)
            linhas_mostradas.append(paragrafo)
            if pular:
                delay_linha = 0
                delay_paragrafo = 30

            main.pygame.time.delay(delay_paragrafo)
            
        main.aguardar(largura=(config.PADDING_LEFT + len(TEXTO[len(TEXTO) - 1]) * 11),altura=(altura_historia + (len(TEXTO) * 40 - 40)), cor=config.COR_TEXTO)
    
    fases_menu.iniciar_fase(fase_atual)
