import json
import os

NOMEJSON = "variables.json"

# Pegar a pasta onde está o .py
pasta_atual = os.path.dirname(__file__)

def get_variables_form_json():
    global pasta_atual
    localConfiguracao = "mainpuler json GET: "
    
    # # Voltar uma pasta
    # pasta_anterior = os.path.abspath(os.path.join(pasta_atual, '..'))

    # Construir o caminho até o arquivo JSON
    caminho_json = os.path.join(pasta_atual, NOMEJSON)

    # 1. Tentar ler o arquivo
    if os.path.exists(caminho_json): # nome do arquivo ou caminho do arquivo..
        try:
            with open(caminho_json, 'r', encoding='utf-8') as f: # nome do arquivo ou caminho do arquivo..
                return json.load(f)
        except json.JSONDecodeError:
            print(localConfiguracao + "Erro: O arquivo JSON está mal formatado!")
            return { }
    else:
        print(localConfiguracao +"Aviso: Arquivo não encontrado, criando novo...")
        return { }  


def update_variables_json(dados):
    global pasta_atual
    localConfiguracao = "mainpuler json PUT: "
    print(localConfiguracao, dados)
    
    caminho_json = os.path.join(pasta_atual, NOMEJSON)
    
    try:
        with open(caminho_json, 'w', encoding='utf-8') as f: # nome do arquivo ou caminho do arquivo..
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Arquivo salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")