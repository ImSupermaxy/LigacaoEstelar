# Tela
import pygame
import sys

IS_DEV_VAR = True
SKIP_HISTORIA = IS_DEV_VAR
SKIP_DIALOGOS = IS_DEV_VAR

pygame.font.init()
LARGURA, ALTURA = 1420, 720
PADDING_LEFT = 50
PADDING_TOP = 200
ESPACAMENTO_LINHA = 40

TELA = pygame.display.set_mode((LARGURA, ALTURA))
NOME_PROJETO = "Ligação Estelar"
ISCONTINUACAO = False

# Cores e fonte
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERDE_ESCURO = (75, 200, 75)
VERMELHO = (200, 0, 0)
AZUL = (50, 100, 255)
AZUL_CLARO = (3, 207, 252)
CINZA = (180, 180, 180)
CINZA_CLARO = (210, 210, 210)
FONTE = pygame.font.SysFont("arial", 28)
# FONTE = pygame.font.SysFont("calibri", 32)
    
FONTE_GRAFO = pygame.font.SysFont(None, 32)
SELECIONADO = AZUL
BACKGROUND_JOGO = PRETO
COR_TEXTO = BRANCO

# História do jogo
HISTORIA = [
    "Em um mundo onde existem dezenas de colônias de seres humanos espalhados pela galáxia",
    "Nosso objetivo é restaurar a única e íntegra memória de nossos antepassados",
    "Juntando todas essas civilizações que viveram separadas de seus irmãos por tanto tempo",
    "Você fará isso, mas do seu jeito",
    # "Escolha uma dessas opções de jogo: "
]

# opcoes_jogo = [
#     # "",
#     # "",
#     "1 -  Grafo não direcionado (sem poderamento) indo até um ponto b",
#     "2 -  Grafo não direcionado (com poderamento) indo até um ponto b",
#     "3 -  Grafo não direcionado ligando todos os pontos"
# ]
# opcao_atual = 0
# opcoes_logicas_busca = {
#     1: "BFS",
#     2: "Dijkstra",
#     3: "Prim" #ou kruskal (sem muitas arestas (linhas), e o Prim (para muitas arestas, (linhas)))
# }

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

Volume = 100 #em %
Volume_Efeitos = 100
Volume_Dialogos = 100
Volume_Musica = 100

# VELOCIDADE_TEXTOS = 100 #em % (alterar o delay e colocar o resto como porcentagem em relacão a esta variavel)
# VELOCIDADE_HISTORIA = 100
# VELOCIDADE_TRASICAO_FASE = 100

def update_volume(volume, volume_efeitos, volume_dialogos, volume_musica):
    Volume = volume
    Volume_Efeitos = volume_efeitos * (volume / 100)
    Volume_Dialogos = volume_dialogos * (volume / 100)
    Volume_Musica = volume_musica * (volume / 100)
    