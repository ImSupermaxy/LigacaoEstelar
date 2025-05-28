
import configuracoes.variables as config
import main

TEXTO = [
    "Após algumas centenas de anos a humanidade vive de forma separada, ",
    "existem colônias espalhadas pela galáxia...  hierarquia, classe, poder, dinheiro, tudo isso ainda existe; ",
    "as pessoas com maior \"status social\" vivem em planetas de luxo, com ar fresco, prias, comida, e água potável, ",
    "enquanto outras, vivem em planetas \"menos desenvolvidos\", sem ordem, separados dassa nova sociedade.",
    "O maior problema dessa evolução é o lixo, o lixo-espacial, ele está por todo lado aqui, ",
    "e para se locomover entre um planeta e outro, é necessário fazer uma varredura pela rota decidida.",
    "Sua missão é limpar esses caminhos para o destino dessas pessoas, ",
    "sendo elas burguesas ou só apenas um jovem casal viajando pelo espaço."
]


# Mostra toda a introdução
def mostrar_introducao():
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    altura_historia = config.PADDING_TOP_HISTORIA
    linhas_mostradas = []
    delay_linha = 50
    delay_paragrafo = 580
    emit_sound = True
    for i, paragrafo in enumerate(TEXTO):
        pular = main.digitar_lento(paragrafo, linhas_mostradas, delay_linha, altura=altura_historia, som=emit_sound)
        linhas_mostradas.append(paragrafo)
        if pular:
            emit_sound = False
            delay_linha = 0
            delay_paragrafo = 30
        
        main.pygame.time.delay(delay_paragrafo)
        
    main.aguardar(largura=(config.PADDING_LEFT + len(TEXTO[len(TEXTO) - 1]) * 11),altura=(altura_historia + (len(TEXTO) * 40 - 40)), cor=config.COR_TEXTO)