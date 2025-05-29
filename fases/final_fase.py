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

max_peso_fases = 200

def obtem_ranking_by_soma_arestas(soma_usuario, soma_cpu):
    if soma_cpu == 0:
        return "Erro: soma do grafo não pode ser zero."

    porcentagem_real = (soma_usuario / soma_cpu) * 100
    distancia = abs(100 - porcentagem_real)

    # Transformamos essa distância em uma "pontuação invertida"
    # Quanto mais próximo de 100%, maior a pontuação (e melhor o ranking)
    pontuacao = round(max(0, 100 - distancia))

    #Atualizar essa lógica (trazer o valor máximo possível na fase também, 
    # ou seja calcular em cima da distância do valor da cpu(MIN) e o valor máximo da fase (MAX) 
    # verificar onde está o valor do usuário)

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
    somaTotal = "Soma total: "
    main.desenhar_textos([somaTotal], config.AZUL_CLARO, largura=config.LARGURA - 200, atualizaTela=False)
    main.desenhar_textos([str(soma_arestas)], config.VERDE, largura=config.LARGURA - 200 + len(somaTotal) * 13, atualizaTela=False)

def escreve_total_peso_grafo(total):
    somaTotal = "Soma fases: "
    main.desenhar_textos([somaTotal], config.ROSA2, altura=config.PADDING_TOP + 50, largura=config.LARGURA - 200, atualizaTela=False)
    main.desenhar_textos([str(total)], config.VERDE, altura=config.PADDING_TOP + 50, largura=config.LARGURA - 200 + len(str(somaTotal)) * 13, atualizaTela=False)

def escreve_limite_peso_fases():
    somaTotal = "Max: "
    main.desenhar_textos([somaTotal], config.AMARELO, altura=config.PADDING_TOP + 100, largura=config.LARGURA - 200, atualizaTela=False)
    main.desenhar_textos([str(max_peso_fases)], config.VERDE, altura=config.PADDING_TOP + 100, largura=config.LARGURA - 200 + len(str(somaTotal)) * 15, atualizaTela=False)
    
def escreve_info_pesos(soma_arestas_usuario):
    escreve_soma_peso_grafo(soma_arestas_usuario)
    escreve_total_peso_grafo(config.total_peso_fases)
    escreve_limite_peso_fases()

def imprime_relatorio_fase(texto, valor, cor_principal, cor_valor, largura_texto, altura, delay=350):
    render = config.FONTE.render(texto, False, cor_principal)
    config.TELA.blit(render, (largura_texto, altura))
    
    render = config.FONTE.render(" " + valor, False, cor_valor)
    config.TELA.blit(render, (largura_texto + (len(texto) * 10), altura))
    main.pygame.display.update()
    
    main.pygame.time.delay(delay)


def desenha_final_missao(soma_arestas_usuario, soma_arestas_cpu, texto=[], largura_texto=config.LARGURA // 2, altura_texto=50):
    altura = 30
    config.TELA.fill(config.BACKGROUND_JOGO)
    main.pygame.display.update()
    main.pygame.time.delay(600)
    
    escreve_info_pesos(soma_arestas_usuario)
    
    rank = obtem_ranking_by_soma_arestas(soma_arestas_usuario, soma_arestas_cpu)
    texto.append("")
    texto.append("")
    
    raio = 400
    largura_texto = (largura_texto - raio) + 50
    #LINHA 1
    pos1_linha = (config.LARGURA // 2 - raio, altura)
    pos2_linha =  (config.LARGURA // 2 - raio, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha, 3) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y
    
    #LINHA 2
    pos1_linha = (config.LARGURA // 2 + raio, altura)
    pos2_linha =  (config.LARGURA // 2 + raio, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha, 3) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y
    
    #LINHA 3
    pos1_linha = (config.LARGURA // 2 - raio, config.ALTURA - altura)
    pos2_linha =  (config.LARGURA // 2 + raio, config.ALTURA - altura)
    main.pygame.draw.line(config.TELA, config.AZUL_CLARO, pos1_linha, pos2_linha, 3) #desenhar um retângulo sem a parte de cima, mais lardo no eixo y

    delay_paragrafo = 200
    delay_linha = 50
    
    linhas_mostradas = []
    emit_sound = True
    for i, paragrafo in enumerate(texto):
        pular = main.digitar_lento(paragrafo, linhas_mostradas, delay_linha, config.CINZA_CLARO, altura=altura_texto, largura=largura_texto, fonte=config.FONTE_FINAL_FASE, som=emit_sound)
        linhas_mostradas.append(paragrafo)
        if pular:
            emit_sound = False
            delay_linha = 0
            delay_paragrafo = 30

        main.pygame.time.delay(delay_paragrafo)

    soma_total_texto = "Sua soma total: "
    altura_soma_total = 160
    imprime_relatorio_fase(soma_total_texto, str(config.total_peso_fases), config.BRANCO, config.VERDE, largura_texto, config.ALTURA - altura - altura_soma_total)
    
    max_total_texto = "Máximo valor: "
    altura_max_total = 120
    imprime_relatorio_fase(max_total_texto, str(max_peso_fases), config.BRANCO, config.VERDE, largura_texto, config.ALTURA - altura - altura_max_total)

    ranking_texto = "Seu ranking: "
    altura_ranking = 80
    imprime_relatorio_fase(ranking_texto, rank, config.BRANCO, config.VERDE, largura_texto, config.ALTURA - altura - altura_ranking)
    
    # render = config.FONTE.render(ranking_texto, False, config.ROXO)
    # config.TELA.blit(render, (largura_texto, config.ALTURA - altura - altura_ranking))
    
    # render = config.FONTE.render(" " + rank, False, config.VERDE)
    # config.TELA.blit(render, (largura_texto + (len(ranking_texto) * 10), config.ALTURA - altura - altura_ranking))
    
    main.aguardar_confirmacao(altura=config.ALTURA - altura - altura_ranking)
    # config.TELA.fill(config.BACKGROUND_JOGO)