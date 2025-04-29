import json
import os

# Pegar a pasta onde está o main.py
pasta_atual = os.path.dirname(__file__)

# Voltar uma pasta
pasta_anterior = os.path.abspath(os.path.join(pasta_atual, '..'))

# Construir o caminho até o arquivo JSON
caminho_json = os.path.join(pasta_anterior, 'config/volume', 'exemplo-volume.json')

# 1. Tentar ler o arquivo
if os.path.exists(caminho_json):
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formatado!")
        dados = {}  # Começar com um dicionário vazio
else:
    print("Aviso: Arquivo não encontrado, criando novo...")
    dados = {}

print(dados)

# 2. Modificar ou adicionar dados
# Atualizar idade
if 'idade' in dados:
    dados['idade'] += 1
else:
    dados['idade'] = 1  # Começar com 1 se não existir

# Adicionar profissão
dados.setdefault('profissao', 'Engenheira')

# Adicionar hobbies
if 'hobbies' not in dados or not isinstance(dados['hobbies'], list):
    dados['hobbies'] = []

dados['hobbies'].append('ciclismo')

# 3. Salvar as alterações
try:
    with open(caminho_json, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print("Arquivo salvo com sucesso!")
    print(dados)
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")



# #===============================Exemplo com lógica do sistema=========================================
# import json
# import os

# nomeArquivo = "volume.json"
# localConfiguracao = "Volume Configuração: "
# dados = {}

# # Pegar a pasta onde está o .py
# pasta_atual = os.path.dirname(__file__)

# # # Voltar uma pasta
# # pasta_anterior = os.path.abspath(os.path.join(pasta_atual, '..'))

# # Construir o caminho até o arquivo JSON
# caminho_json = os.path.join(pasta_atual, nomeArquivo)


# def getDadosFromArquivo():
#     global caminho_json
#     global localConfiguracao
#     global dados
    
#     # 1. Tentar ler o arquivo
#     if os.path.exists(caminho_json): # nome do arquivo ou caminho do arquivo..
#         try:
#             with open(caminho_json, 'r', encoding='utf-8') as f: # nome do arquivo ou caminho do arquivo..
#                 dados = json.load(f)
#         except json.JSONDecodeError:
#             print(localConfiguracao + "Erro: O arquivo JSON está mal formatado!")
#             dados = {
#                 "Volume": 100, #em %
#                 "Volume_Efeitos": 1,
#                 "Volume_Dialogos": 1,
#                 "Volume_Musica": 1
#             }  # Começar com um dicionário vazio
#     else:
#         print(localConfiguracao +"Aviso: Arquivo não encontrado, criando novo...")
#         dados = {
#             "Volume": 100, #em %
#             "Volume_Efeitos": 1,
#             "Volume_Dialogos": 1,
#             "Volume_Musica": 1
#         }  # Começar com um dicionário vazio

# def get_volume(nome):
#     return dados[nome]

# def update_volume(volume, volume_efeitos, volume_dialogos, volume_musica):
#     print(localConfiguracao + str(volume) + " " + str(volume_dialogos) + " " + str(volume_efeitos) + " " + str(volume_musica))
    
#     # Atualizar json
#     if 'Volume' in dados:
#         dados['Volume'] = volume
#     if 'Volume' in dados:
#         dados['Volume_Efeitos'] = volume_efeitos
#     if 'Volume' in dados:
#         dados['Volume_Dialogos'] = volume_dialogos
#     if 'Volume' in dados:
#         dados['Volume_Musica'] = volume_musica

#     # # Adicionar no json
#     # dados.setdefault('profissao', 'Engenheira')

#     # # Adicionar em array ou o próprio array no json
#     # if 'hobbies' not in dados or not isinstance(dados['hobbies'], list):
#     #     dados['hobbies'] = []
#     # dados['hobbies'].append('ciclismo')

#     # Salvar as alterações
#     try:
#         with open(caminho_json, 'w', encoding='utf-8') as f: # nome do arquivo ou caminho do arquivo..
#             json.dump(dados, f, ensure_ascii=False, indent=4)
#         print("Arquivo salvo com sucesso!")
#         print(localConfiguracao + str(dados["Volume"]) + " " + str(dados["Volume_Dialogos"]) + " " + str(dados["Volume_Efeitos"]) + " " + str(dados["Volume_Musica"]))
#     except Exception as e:
#         print(f"Erro ao salvar o arquivo: {e}")

# getDadosFromArquivo()