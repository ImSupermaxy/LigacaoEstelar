import pygame
import sys
from menu import menu
from config.variables import *

# Inicializa o pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption(NOME_PROJETO)

# Renderiza todos os parágrafos atuais
def desenhar_textos(linhas, offset_y, cor=COR_TEXTO, altura=100,largura=PADDING_LEFT):
    y = altura - offset_y
    for linha in linhas:
        render = FONTE.render(linha, False, cor)
        TELA.blit(render, (largura, y))
        y += 40  # espaço entre linhas
    pygame.display.update()


# Escreve uma linha com efeito de digitação
def digitar_lento(linha, linhas_anteriores, delay=50, offset_y=0, cor=COR_TEXTO, altura=100, largura=PADDING_LEFT):
    texto_atual = ""
    for char in linha:
        texto_atual += char
        linhas_para_mostrar = linhas_anteriores + [texto_atual]
        desenhar_textos(linhas_para_mostrar, offset_y, cor, altura=altura, largura=largura)
        pygame.time.delay(delay)

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return True
            elif evento.type == pygame.QUIT:
                fechar_jogo()
    return False
    
# def desenhar_selecao_logica():
#     TELA.fill(BACKGROUND_JOGO)
    
#     espacamento_linha = 40
#     linha_posicao = 160

#     render = FONTE.render("Escolha uma das opções: ", True, BRANCO)
#     TELA.blit(render, (PADDING_LEFT, linha_posicao))
    
#     linha_posicao += espacamento_linha
    
#     ultima_linha = 0
#     for i, texto in enumerate(opcoes_jogo):
#         cor = SELECIONADO if i == opcao_atual else CINZA_CLARO
#         render = FONTE.render(texto, True, cor)
#         linha_posicao = 200 + i * espacamento_linha
#         ultima_linha = linha_posicao
#         TELA.blit(render, (PADDING_LEFT, linha_posicao))
        
#     titulo = FONTE.render("O que você deseja fazer?", True, BRANCO)
#     ultima_linha = ultima_linha + 80
#     TELA.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ultima_linha))

#     pygame.display.update()
#     # aguardar_confirmacao(altura=ultima_linha + 60)

# def selecao_logica():
#     global opcao_atual
#     rodando = True
#     while rodando:
#         desenhar_selecao_logica()

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 fechar_jogo()
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_UP:
#                     opcao_atual = (opcao_atual - 1) % len(opcoes_jogo)
#                 elif evento.key == pygame.K_DOWN:
#                     opcao_atual = (opcao_atual + 1) % len(opcoes_jogo)
#                 elif evento.key == pygame.K_RETURN:
#                     rodando = False
 

# Mostra toda a introdução
def mostrar_historia():
    TELA.fill(BACKGROUND_JOGO)
    
    if not SKIP_HISTORIA:
        linhas_mostradas = []
        delay_linha = 30
        delay_paragrafo = 500
        scroll = 0
        for i, paragrafo in enumerate(HISTORIA):
            if i * 40 + 100 > ALTURA - 100:
                scroll += 40 
            pular = digitar_lento(paragrafo, linhas_mostradas, delay_linha, offset_y=scroll)
            linhas_mostradas.append(paragrafo)
            if pular:
                delay_linha = 0
                delay_paragrafo = 60

            pygame.time.delay(delay_paragrafo)
            
        aguardar(largura=(PADDING_LEFT + len(HISTORIA[len(HISTORIA) - 1]) * 10 + 5),altura=(100 + (len(HISTORIA) * 40 - 40)), cor=COR_TEXTO)
    
    menu.inicar_menu()


def aguardar_confirmacao(texto="Pressione ENTER para continuar...",largura=0,altura=0, cor=BRANCO):
    # TELA.fill(BACKGROUND_JOGO)
    if altura == 0:
        altura = ALTURA // 2
    if largura == 0:
        largura = LARGURA // 2 - texto.get_width() // 2

    texto = FONTE.render(texto, True, cor)
    TELA.blit(texto, (largura, altura))
    pygame.display.update()
        
    # Loop para manter a tela ativa
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_jogo()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                esperando = False
                

def aguardar(texto="...",largura=0,altura=0, cor=COR_TEXTO):
    # TELA.fill(BACKGROUND_JOGO)
    if altura == 0:
        altura = ALTURA // 2
    if largura == 0:
        largura = LARGURA // 2 - texto.get_width() // 2
        
    prox_cor = BACKGROUND_JOGO
    
    # Loop para manter a tela ativa
    esperando = True
    while esperando:
        # fonte = FONTE.render(texto, True, cor)
        # TELA.blit(fonte, (largura, altura))
        esperando = not digitar_lento(texto, [], 150, offset_y=0, cor=cor, altura=altura, largura=largura)
        pygame.display.update()
        
        tmp = cor
        cor = prox_cor
        prox_cor = tmp
        pygame.time.delay(200)


def fechar_jogo():
    pygame.quit()
    sys.exit()


# Início
def main():
    TELA.fill(BACKGROUND_JOGO)
    pygame.display.update()
    mostrar_historia()


if __name__ == "__main__":
    main()