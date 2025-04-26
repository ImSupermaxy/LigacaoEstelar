import main
from config.variables import *
from fases import fase1

def visualizar_fases():
    iniciar_menu()
    
primeira_opcao = FASE_ATUAL
opcoes_menu = {
    1: primeira_opcao,
    2: "config (audio? texto? personalização?)",
    3: "fases",
    4: "Fechar"
}
opcao_atual = 1

# Chama a fase atual do personagem
def iniciar_fase(fase):
    match fase:
        case "fase 1":
            fase1.primeira_fase_iniciar()
        case "fase 2":
            print("Dois")
        case "fase 3":
            print("Três")
        case "fase 4":
            print("Outro número")
    
    pygame.quit()
    # os.system("python jogo.py")  # ou "python3 jogo.py"


def iniciar_menu():
    main.fechar_jogo()


def selecao_fases():
    
    rodando = True
    while rodando:
        desenhar_selecao_fases()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                main.fechar_jogo()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcao_atual = (opcao_atual - 1) % len(opcoes_menu)
                elif evento.key == pygame.K_DOWN:
                    opcao_atual = (opcao_atual + 1) % len(opcoes_menu)
                elif evento.key == pygame.K_RETURN:
                    rodando = False


def desenhar_selecao_fases():
    TELA.fill(BACKGROUND_JOGO)
    
    espacamento_linha = 40
    linha_posicao = 200

    for i, texto in enumerate(opcoes_menu):
        cor = SELECIONADO if i == opcao_atual else CINZA_CLARO
        render = FONTE.render(texto, True, cor)
        linha_posicao = 200 + i * espacamento_linha
        TELA.blit(render, (PADDING_LEFT, linha_posicao))
        pygame.time.delay(200)

    pygame.display.update()
    # aguardar_confirmacao(altura=ultima_linha + 60)