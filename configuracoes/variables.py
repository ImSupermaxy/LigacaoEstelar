# Tela
import pygame
import sys
import configuracoes.manipulerjson as mjson
import historia.introducao as introducao
import os
from pathlib import Path

def init_pygame():
    pygame.font.init()
    pygame.mixer.init()

init_pygame()
dados = mjson.get_variables_form_json()

def atualiza_dados():
    dados = mjson.get_variables_form_json()

IsDevVar = dados["isDev"]
# if IsDevVar:
# else
skipIntroducao = dados["texto"]["skipIntroducao"]
SkipHistoria = dados["texto"]["skipHistoria"]
SkipDialogos = dados["texto"]["skipDialogos"]
IsContinuacao = dados["isContinuacao"]
IsFullSream = dados["isFullScream"]
fases_auto_atualiza = dados["fases"]["auto_atualiza"]

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
CIANO = (51, 219, 204)
LINHA_FASES_MENU = (79, 137, 236)

#--> CONFIGURAÇÕES GERAIS <--
NOME_PROJETO = "Ligação Estelar"
LARGURA, ALTURA = dados["video"]["width"], dados["video"]["heigth"] if not IsFullSream else (0,0)
TELA = pygame.display.set_mode((LARGURA, ALTURA)) if not IsFullSream else pygame.display.set_mode((0,0), pygame.FULLSCREEN)
FONTE = pygame.font.SysFont("arial", 28)
FONTE2 = pygame.font.SysFont("arial", 40)
FONTE_RESUMO_FASE = pygame.font.SysFont("arial", 23)
PADDING_LEFT = 50
PADDING_TOP = 200
ESPACAMENTO_LINHA = 40
BACKGROUND_JOGO = PRETO
COR_TEXTO = BRANCO
    
caminho_arquivo = Path(__file__)
RAIZ_PROJETO = caminho_arquivo.parent.parent.resolve()
PASTA_ASSETS = os.path.join(RAIZ_PROJETO, "assets")
PASTA_IMAGENS = os.path.join(PASTA_ASSETS, "imagens")
PASTA_AUDIOS = os.path.join(PASTA_ASSETS, "audios")
PASTA_MUSICA = os.path.join(PASTA_ASSETS, "musicas")

INFO_DISPLAY = pygame.display.Info()
if IsFullSream:
    LARGURA = INFO_DISPLAY.current_w
    ALTURA = INFO_DISPLAY.current_h

#--> AUDIO <--
AUDIO_SELECAO_FASE = "som_selecao_undertale.mp3"
AUDIO_DESELECAO_FASE = "som_deselecionado_undertale.mp3"
AUDIO_SELECAO_MENU = "som_selecao_teste.mp3"
AUDIO_TEXTO = "som_texto_toriel.mp3"


#--> CONFIGURAÇÕES DO MENU <--
FONTE_MENU = pygame.font.SysFont("calibri", 32)
ESPACAMENTO_LINHA_MENU = 45


#--> CONFIGURAÇÕES DO(S) GRAFO(S) <--
FONTE_GRAFO = pygame.font.SysFont(None, 24)
FONTE_PESO = pygame.font.SysFont("arial", 36, bold=True)
FONTE_FINAL_FASE = pygame.font.SysFont("dejavuserif", 28)

#--> CONFIGURAÇÕES DE INTERAÇÃO <--
SELECIONADO = AZUL

Volume = 0
Volume_Efeitos = 0
Volume_Dialogos = 0
Volume_Musica = 0

#--> CONFIGURAÇÕES DE VOLUME <--
def get_all_volumes():
    global Volume
    global Volume_Efeitos
    global Volume_Dialogos
    global Volume_Musica
    
    Volume  = dados["volume"]["volumeMaster"]
    Volume_Efeitos = dados["volume"]["volumeEfeitos"]
    Volume_Dialogos = dados["volume"]["volumeDialogos"]
    Volume_Musica = dados["volume"]["volumeMusica"]
    
get_all_volumes()

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
OPEN_FASE_TWO = False
OPEN_FASE_THREE = False
OPEN_FASE_FOUR = False
OPEN_FASE_FIVE = False


FASES = [
    FASE_ONE,
    FASE_TWO,
    FASE_THREE,
    FASE_FOUR,
    FASE_FIVE
]

FASE_ATUAL = FASES[dados["fases"]["atual"] - 1]

#Passar para o json
Primeira_Fase_Vertices_Visitados = []
Segunda_Fase_Vertices_Visitados = []
Terceira_Fase_Vertices_Visitados = []
Quarta_Fase_Vertices_Visitados = []
Quinta_Fase_Vertices_Visitados = []

total_peso_fases = dados["fases"]["total"]

ARQUIVO_INFO_FASE = "info_fases.json"

def get_all_vertices_visitados():
    global Primeira_Fase_Vertices_Visitados
    global Segunda_Fase_Vertices_Visitados
    global Terceira_Fase_Vertices_Visitados
    global Quarta_Fase_Vertices_Visitados
    global Quinta_Fase_Vertices_Visitados
    
    info = mjson.get_variables_form_json(ARQUIVO_INFO_FASE)
    
    Primeira_Fase_Vertices_Visitados = info["1"]["visitados"]
    Segunda_Fase_Vertices_Visitados = info["2"]["visitados"]
    Terceira_Fase_Vertices_Visitados = info["3"]["visitados"]
    Quarta_Fase_Vertices_Visitados = info["4"]["visitados"]
    Quinta_Fase_Vertices_Visitados = info["5"]["visitados"]


def update_total(fase):
    global total_peso_fases
    
    info = mjson.get_variables_form_json(ARQUIVO_INFO_FASE)
    
    total = 0
    
    i = 1
    while i <= fase:
        total += info[str(i)]["soma"]
        i += 1

    dados["fases"]["total"] = total
    total_peso_fases = total
    mjson.update_variables_json(dados)


def update_soma_fase(fase, soma):
    info = mjson.get_variables_form_json(ARQUIVO_INFO_FASE)
    info[str(fase)]["soma"] = soma
    mjson.update_variables_json(info, ARQUIVO_INFO_FASE)


def update_vertices_visitados(fase, visitados):
    info = mjson.get_variables_form_json(ARQUIVO_INFO_FASE)
    info[str(fase)]["visitados"] = visitados
    mjson.update_variables_json(info, ARQUIVO_INFO_FASE)
    
    get_all_vertices_visitados()
    

def update_fase_atual(fase):
    global FASE_ATUAL
    dados["fases"]["atual"] = fase
    
    FASE_ATUAL = FASES[dados["fases"]["atual"] - 1]


def get_info_resumo_fase(opcao):
    return mjson.get_variables_form_json(ARQUIVO_INFO_FASE)[str(opcao)]

    
def update_variables_json():
    mjson.update_variables_json(dados)

    
def update_is_continuacao(value=True):
    global IsContinuacao
    IsContinuacao = value
    dados["isContinuacao"] = value
    dados["texto"]["skipIntroducao"] = value


def get_volume_musica() -> float:
    teste = (Volume_Musica * (Volume / 100)) / 100
    print("Volume Música: " + str(teste))
    return teste


def get_volume_efeitos():
    teste = (Volume_Efeitos * (Volume / 100)) / 100
    return teste

    
def update_all_volumes():
    global Volume
    global Volume_Dialogos
    global Volume_Efeitos
    global Volume_Musica
    
    dados["volume"]["volumeMaster"] = Volume
    dados["volume"]["volumeEfeitos"] = Volume_Efeitos
    dados["volume"]["volumeDialogos"] = Volume_Dialogos
    dados["volume"]["volumeMusica"] = Volume_Musica
    update_variables_json()
    atualiza_dados()
    get_all_volumes()
    
def update_all_texto():
    global skipIntroducao
    global SkipDialogos
    global SkipHistoria
    
    dados["texto"]["skipIntroducao"] = skipIntroducao 
    dados["texto"]["skipDialogos"] = SkipDialogos
    dados["texto"]["skipHistoria"] = SkipHistoria
    
get_all_vertices_visitados()