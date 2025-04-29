import pygame
import sys
from menu import menu
import configuracoes.variables as config

# Inicializa o pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption(config.NOME_PROJETO)

# Renderiza todos os parágrafos atuais
def desenhar_textos(linhas, cor=config.COR_TEXTO, altura=config.PADDING_TOP,largura=config.PADDING_LEFT):
    y = altura
    for linha in linhas:
        render = config.FONTE.render(linha, False, cor)
        config.TELA.blit(render, (largura, y))
        y += config.ESPACAMENTO_LINHA  # espaço entre linhas
    pygame.display.update()


# Escreve uma linha com efeito de digitação
def digitar_lento(linha, linhas_anteriores, delay=50, cor=config.COR_TEXTO, altura=config.PADDING_TOP, largura=config.PADDING_LEFT):
    texto_atual = ""
    for char in linha:
        texto_atual += char
        linhas_para_mostrar = linhas_anteriores + [texto_atual]
        desenhar_textos(linhas_para_mostrar, cor, altura=altura, largura=largura)
        pygame.time.delay(delay)

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return True
            elif evento.type == pygame.QUIT:
                fechar_jogo()
    return False
 

# Mostra toda a introdução
def mostrar_historia():
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    altura_historia = config.PADDING_TOP_HISTORIA
    if not config.SkipHistoria:
        linhas_mostradas = []
        delay_linha = 30
        delay_paragrafo = 500
        for i, paragrafo in enumerate(config.HISTORIA):
            pular = digitar_lento(paragrafo, linhas_mostradas, delay_linha, altura=altura_historia)
            linhas_mostradas.append(paragrafo)
            if pular:
                delay_linha = 0
                delay_paragrafo = 30

            pygame.time.delay(delay_paragrafo)
            
        aguardar(largura=(config.PADDING_LEFT + len(config.HISTORIA[len(config.HISTORIA) - 1]) * 10 + 5),altura=(altura_historia + (len(config.HISTORIA) * 40 - 40)), cor=config.COR_TEXTO)
    
    menu.inicar_menu()


def aguardar_confirmacao(texto="Pressione ENTER para continuar...",largura=0,altura=0, cor=config.BRANCO):
    # TELA.fill(BACKGROUND_JOGO)
    if altura == 0:
        altura = config.ALTURA // 2
    if largura == 0:
        largura = config.LARGURA // 2 - texto.get_width() // 2

    texto = config.FONTE.render(texto, True, cor)
    config.TELA.blit(texto, (largura, altura))
    pygame.display.update()
        
    # Loop para manter a tela ativa
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_jogo()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                esperando = False
                

def aguardar(texto="...",largura=0,altura=0, cor=config.COR_TEXTO, delay=200):
    if altura == 0:
        altura = config.ALTURA // 2
    if largura == 0:
        largura = config.LARGURA // 2 - texto.get_width() // 2
        
    prox_cor = config.BACKGROUND_JOGO
    
    esperando = True
    while esperando:
        # fonte = FONTE.render(texto, True, cor)
        # TELA.blit(fonte, (largura, altura))
        esperando = not digitar_lento(texto, [], 150, cor=cor, altura=altura, largura=largura)
        pygame.display.update()
        
        tmp = cor
        cor = prox_cor
        prox_cor = tmp
        pygame.time.delay(delay)


def transicao(delay = 200):
    config.TELA.fill(config.BACKGROUND_JOGO)
    texto = "..."
    altura = config.ALTURA // 2
    largura = config.LARGURA // 2
    
    cor = config.COR_TEXTO
    prox_cor = config.BACKGROUND_JOGO
    
    esperando = True
    i = 0
    while esperando:
        
        if i == delay * 5:
            esperando = False
        texto_atual = ""
        for char in texto:
            texto_atual += char
            linhas_para_mostrar = [] + [texto_atual]
            desenhar_textos(linhas_para_mostrar, cor, altura=altura, largura=largura)
            pygame.time.delay(100)
        pygame.display.update()
        
        tmp = cor
        cor = prox_cor
        prox_cor = tmp
        i += delay
        pygame.time.delay(delay)


def fechar_jogo():
    config.update_variables_json()
    pygame.quit()
    sys.exit()


# Início
def main():
    config.TELA.fill(config.BACKGROUND_JOGO)
    pygame.display.update()
    mostrar_historia()


if __name__ == "__main__":
    main()