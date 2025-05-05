import configuracoes.variables as config
import main

#S: 96-100%
#A+: 90-95%
#A: 85-89%
#A-: 80-84%
#B+: 75-79%
#B: 70-74%
#B-: 65-69%
#C+: 60-64%
#C: 55-59%
#C-: 50-54%
#D+: 45-49%
#D: 40-44%
#D-: 35-39%
#E+: 30-34%
#E: 25-29%
#E-: 20-24%
#F+: 15-19%
#F: 10-14%
#F-: 5-9%
#...: 0-4%

def obtem_ranking_by_soma_arestas(soma_usuario, soma_cpu):
    if soma_cpu == 0:
        return "Erro: soma do grafo não pode ser zero."

    porcentagem_real = (soma_usuario / soma_cpu) * 100
    distancia = abs(100 - porcentagem_real)

    # Transformamos essa distância em uma "pontuação invertida"
    # Quanto mais próximo de 100%, maior a pontuação (e melhor o ranking)
    pontuacao = round(max(0, 100 - distancia))

    # Tabela de rankings com base na pontuação (0 a 100)
    rankings = [
        (96, 100, "S"),
        (90, 95, "A+"),
        (85, 89, "A"),
        (80, 84, "A-"),
        (75, 79, "B+"),
        (70, 74, "B"),
        (65, 69, "B-"),
        (60, 64, "C+"),
        (55, 59, "C"),
        (50, 54, "C-"),
        (45, 49, "D+"),
        (40, 44, "D"),
        (35, 39, "D-"),
        (30, 34, "E+"),
        (25, 29, "E"),
        (20, 24, "E-"),
        (15, 19, "F+"),
        (10, 14, "F"),
        (5, 9, "F-"),
        (0, 4, "...")
    ]

    for min_val, max_val, rank in rankings:
        if min_val <= pontuacao <= max_val:
            return rank

    return "Erro: pontuação fora dos limites esperados."  

def escreve_soma_peso_grafo(soma_arestas):
    somaTotal = "Soma total: " + str(soma_arestas)
    main.desenhar_textos([somaTotal], config.AZUL_CLARO, largura=config.LARGURA - len(somaTotal) * 12, atualizaTela=False)
        
def desenha_final_missao(soma_arestas_usuario, soma_arestas_cpu, texto=[], largura_texto=config.LARGURA // 2 - 150, altura_texto=300):
    altura = 30
    config.TELA.fill(config.BACKGROUND_JOGO)
    
    escreve_soma_peso_grafo(soma_arestas_usuario)
    rank = obtem_ranking_by_soma_arestas(soma_arestas_usuario, soma_arestas_cpu)
    texto[-1] += (" " + rank)
    
    #LINHA 1
    pos1_linha = (config.LARGURA // 2 - 400, altura)
    pos2_linha =  (config.LARGURA // 2 - 400, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y
    
    #LINHA 2
    pos1_linha = (config.LARGURA // 2 + 400, altura)
    pos2_linha =  (config.LARGURA // 2 + 400, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y
    
    #LINHA 3
    pos1_linha = (config.LARGURA // 2 - 400, config.ALTURA - altura)
    pos2_linha =  (config.LARGURA // 2 + 400, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y

    cor = config.COR_TEXTO
    prox_cor = config.BACKGROUND_JOGO
    delay = 200
    esperando = True
    i = 0
    while esperando:
        
        if i == delay * 5:
            esperando = False
        texto_atual = ""
        for char in texto:
            texto_atual += char
            linhas_para_mostrar = [] + [texto_atual]
            main.desenhar_textos(linhas_para_mostrar, cor, altura=altura_texto, largura=largura_texto)
            main.pygame.time.delay(100)
        main.pygame.display.update()
        
        tmp = cor
        cor = prox_cor
        prox_cor = tmp
        i += delay
        main.pygame.time.delay(delay)
    
    main.aguardar_confirmacao()
