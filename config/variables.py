# Tela
import pygame
import sys

pygame.font.init()

#--> CONFIG DEV/ BANCO - JOGO <--
IS_DEV_VAR = True
SKIP_HISTORIA = IS_DEV_VAR
SKIP_DIALOGOS = IS_DEV_VAR
ISCONTINUACAO = False #Obter de um arquivo json que vai ser alterado com as informações da gameplay do jogador (fase, continuação, etc..)
IS_FULL_SCREAM = False

#--> CORES <--
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERDE_ESCURO = (75, 200, 75)
VERMELHO = (200, 0, 0)
AZUL = (50, 100, 255)
AZUL_CLARO = (3, 207, 252)
CINZA = (180, 180, 180)
CINZA_CLARO = (210, 210, 210)


#--> CONFIGURAÇÕES GERAIS <--
NOME_PROJETO = "Ligação Estelar"
LARGURA, ALTURA = 1520, 750 if not IS_FULL_SCREAM else (0,0)
TELA = pygame.display.set_mode((LARGURA, ALTURA)) if not IS_FULL_SCREAM else pygame.display.set_mode((0,0), pygame.FULLSCREEN)
FONTE = pygame.font.SysFont("arial", 28)
PADDING_LEFT = 50
PADDING_TOP = 200
ESPACAMENTO_LINHA = 40
BACKGROUND_JOGO = PRETO
COR_TEXTO = BRANCO

INFO_DISPLAY = pygame.display.Info()
if IS_FULL_SCREAM:
    LARGURA = INFO_DISPLAY.current_w
    ALTURA = INFO_DISPLAY.current_h


#--> CONFIGURAÇÕES DO MENU <--
FONTE_MENU = pygame.font.SysFont("calibri", 32)
ESPACAMENTO_LINHA_MENU = 45


#--> CONFIGURAÇÕES DO(S) GRAFO(S) <--
FONTE_GRAFO = pygame.font.SysFont(None, 32)


#--> CONFIGURAÇÕES DE INTERAÇÃO <--
SELECIONADO = AZUL


#--> CONFIGURAÇÕES DE VOLUME <--
Volume = 100 #em %
Volume_Efeitos = 100
Volume_Dialogos = 100
Volume_Musica = 100


def update_volume(volume, volume_efeitos, volume_dialogos, volume_musica):
    Volume = volume
    Volume_Efeitos = volume_efeitos * (volume / 100)
    Volume_Dialogos = volume_dialogos * (volume / 100)
    Volume_Musica = volume_musica * (volume / 100)


#--> CONFIGURAÇÕES DE VELOCIDADE <--
VELOCIDADE_DIALOGOS = 100 #em % (alterar o delay e colocar o resto como porcentagem em relacão a esta variavel)
# VELOCIDADE_HISTORIA = 100
# VELOCIDADE_TRASICAO_FASE = 100


#--> CONFIGURAÇÕES HISTÓRIA <--
PADDING_TOP_HISTORIA = PADDING_TOP - 150


#--> INFO HISTÓRIA <-- (transformar em json e buscar de lá)
HISTORIA = [
    "Em um mundo onde existem dezenas de colônias de seres humanos espalhados pela galáxia",
    "Nosso objetivo é restaurar a única e íntegra memória de nossos antepassados",
    "Juntando todas essas civilizações que viveram separadas de seus irmãos por tanto tempo",
    "Você fará isso, mas do seu jeito",
]


#--> CONFIGURAÇÕES DAS FASES <--
FASE_ONE = "fase 1"
FASE_TWO = "fase 2"
FASE_THREE = "fase 3"
FASE_FOUR = "fase 4"
FASE_FIVE = "fase 5"

FASES = [
    FASE_ONE,
    FASE_TWO,
    FASE_THREE,
    FASE_FOUR,
    FASE_FIVE
]

FASE_ATUAL = FASE_ONE

    