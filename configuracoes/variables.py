# Tela
import pygame
import sys
import configuracoes.manipulerjson as mjson
import historia.introducao as introducao

pygame.font.init()

dados = mjson.get_variables_form_json()

IsDevVar = dados["isDev"]
# if IsDevVar:
# else
skipIntroducao = dados["texto"]["skipIntroducao"]
SkipHistoria = dados["texto"]["skipHistoria"]
SkipDialogos = dados["texto"]["skipDialogos"]
IsContinuacao = dados["isContinuacao"]
IsFullSream = dados["isFullScream"]

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
AMARELO = (255, 255, 0)
LARANJA = (254, 127, 0)
ROXO = (137, 44, 220)
ROSA = (220, 44, 217)
AZUL_CLARO2 = (56, 182, 255)
VERMELHO2 = (255, 49, 49)
ROSA2 = (255, 102, 196)
ROXO2 = (140, 82, 255)
VERDE_INICIAL = (93, 219, 90)
CINZA_FINAL = (196, 212, 238)

#--> CONFIGURAÇÕES GERAIS <--
NOME_PROJETO = "Ligação Estelar"
LARGURA, ALTURA = dados["video"]["width"], dados["video"]["heigth"] if not IsFullSream else (0,0)
TELA = pygame.display.set_mode((LARGURA, ALTURA)) if not IsFullSream else pygame.display.set_mode((0,0), pygame.FULLSCREEN)
FONTE = pygame.font.SysFont("arial", 28)
PADDING_LEFT = 50
PADDING_TOP = 200
ESPACAMENTO_LINHA = 40
BACKGROUND_JOGO = PRETO
COR_TEXTO = BRANCO

INFO_DISPLAY = pygame.display.Info()
if IsFullSream:
    LARGURA = INFO_DISPLAY.current_w
    ALTURA = INFO_DISPLAY.current_h


#--> CONFIGURAÇÕES DO MENU <--
FONTE_MENU = pygame.font.SysFont("calibri", 32)
ESPACAMENTO_LINHA_MENU = 45


#--> CONFIGURAÇÕES DO(S) GRAFO(S) <--
FONTE_GRAFO = pygame.font.SysFont(None, 24)
FONTE_PESO = pygame.font.SysFont("arial", 36, bold=True)
FONTE_FINAL_FASE = pygame.font.SysFont("dejavuserif", 28)

#--> CONFIGURAÇÕES DE INTERAÇÃO <--
SELECIONADO = AZUL


#--> CONFIGURAÇÕES DE VOLUME <--
Volume = dados["volume"]["volumeMaster"]
Volume_Efeitos = dados["volume"]["volumeEfeitos"]
Volume_Dialogos = dados["volume"]["volumeDialogos"]
Volume_Musica = dados["volume"]["volumeMusica"]


#--> CONFIGURAÇÕES DE VELOCIDADE <--
VELOCIDADE_DIALOGOS = 100 #em % (alterar o delay e colocar o resto como porcentagem em relacão a esta variavel)
# VELOCIDADE_HISTORIA = 100
# VELOCIDADE_TRASICAO_FASE = 100


#--> CONFIGURAÇÕES HISTÓRIA <--
PADDING_TOP_HISTORIA = PADDING_TOP - 150


#--> INFO HISTÓRIA <-- (transformar em json e buscar de lá)
# HISTORIA = historia.texto
# INTRODUCAO = introducao.texto


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

FASE_ATUAL = FASES[dados["fases"]["atual"] - 1]

def update_variables_json():
    mjson.update_variables_json(dados)
    
def update_is_continuacao(value=True):
    global IsContinuacao
    IsContinuacao = value
    dados["isContinuacao"] = value
    dados["texto"]["skipIntroducao"] = value
    
def update_all_volumes():
    global Volume
    global Volume_Dialogos
    global Volume_Efeitos
    global Volume_Musica
    
    dados["volume"]["volumeMaster"] = Volume 
    dados["volume"]["volumeEfeitos"] = Volume_Efeitos
    dados["volume"]["volumeDialogos"] = Volume_Dialogos
    dados["volume"]["volumeMusica"] = Volume_Musica