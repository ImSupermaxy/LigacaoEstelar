import pygame
import sys
from menu import menu
import configuracoes.variables as config
import historia.introducao as introducao
import assets.audios.manipuleraudio as maudio
from datetime import datetime, timedelta
from historia import game_over as go 
from fases import final_jogo

# Inicializa o pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption(config.NOME_PROJETO)

# Renderiza todos os parágrafos atuais
def desenhar_textos(linhas, cor=config.COR_TEXTO, altura=config.PADDING_TOP,largura=config.PADDING_LEFT, atualizaTela=True, fonte=config.FONTE, espacamento=config.ESPACAMENTO_LINHA):
    y = altura
    for linha in linhas:
        render = fonte.render(linha, False, cor)
        config.TELA.blit(render, (largura, y))
        y += espacamento  # espaço entre linhas
    if atualizaTela:
        pygame.display.update()


# Escreve uma linha com efeito de digitação
def digitar_lento(linha, linhas_anteriores, delay=50, cor=config.COR_TEXTO, altura=config.PADDING_TOP, largura=config.PADDING_LEFT, fonte=config.FONTE, som=False):
    texto_atual = ""
    mixer = maudio.GLOBAL_MIXER
    if som:
        mixer = maudio.play_efeito_sonoro(config.AUDIO_TEXTO, True)
    
    for char in linha:
        texto_atual += char
        linhas_para_mostrar = linhas_anteriores + [texto_atual]
        desenhar_textos(linhas_para_mostrar, cor, altura=altura, largura=largura, fonte=fonte)
            
        pygame.time.delay(delay)

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                    if som:
                        mixer.stop()
                    return True
            elif evento.type == pygame.QUIT:
                fechar_jogo()

    if som:
        mixer.stop()
    return False


def aguardar_confirmacao(texto="Pressione [ENTER] para continuar...",largura=0,altura=0, cor=config.BRANCO):
    # TELA.fill(BACKGROUND_JOGO)
    if altura == 0:
        altura = config.ALTURA // 2
    if largura == 0:
        largura = config.LARGURA // 2 - len(texto) // 2

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
        largura = config.LARGURA // 2 - len(texto) // 2
        
    prox_cor = config.BACKGROUND_JOGO
    
    esperando = True
    while esperando:
        # fonte = FONTE.render(texto, True, cor)
        # TELA.blit(fonte, (largura, altura))
        esperando = not digitar_lento(texto, [], 150, cor=cor, altura=altura, largura=largura, som=False)
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
    
    # final_jogo.desenha_final_jogo()
    # return
    
    # if config.IsDevVar:
    #   go.desenha_final_jogo()
    #   return;
    
    pygame.display.update()
    
    if not config.skipIntroducao:
        introducao.mostrar_introducao()
    
    menu.inicar_menu()


if __name__ == "__main__":
    main()