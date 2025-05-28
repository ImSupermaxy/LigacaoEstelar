# 🚀 Ligação Estelar

**Resumo:** Ligação Estelar é um jogo que busca oferecer entretenimento ao usuário enquanto estimula o raciocínio lógico e aborda temas como poluição e meio ambiente. O jogo se passa em uma distopia futurista, onde o protagonista é um piloto de nave espacial que trabalha em uma empresa especializada em limpeza de rotas interplanetárias e segurança. Seu objetivo principal é limpar os caminhos no espaço — agora cobertos por resíduos — para garantir que seus clientes cheguem com segurança ao destino desejado.

---

## 🎯 Objetivo

Nosso projeto tem como principais objetivos conscientizar e criticar práticas relacionadas ao descarte de lixo, ao mesmo tempo em que oferece entretenimento ao jogador. Além disso, busca estimular o raciocínio lógico por meio de desafios envolvendo cálculos de peso total das rotas (arestas) e premiar o desempenho com uma pontuação proporcional à eficiência da escolha do caminho.
Embora ambientado em um universo fictício, o projeto aborda um problema real: o descarte massivo de lixo no espaço, agravado pelo avanço tecnológico e pela falta de responsabilidade ambiental. A narrativa imagina um futuro onde o excesso de resíduos gerou até mesmo novas profissões, como a construção de naves com partes reaproveitadas e a limpeza de corredores espaciais, essenciais para garantir viagens seguras entre planetas. Essa ficção permite uma crítica social sobre os rumos da humanidade em relação ao meio ambiente, incentivando o jogador a refletir sobre sustentabilidade e consequências a longo prazo das ações humanas.
O jogo se baseia em conceitos de grafo com o espaço sendo representado como um grafo conexo, ponderado e não direcionado, onde os vértices representam planetas e as arestas, os caminhos possíveis entre eles. Como o lixo espacial tornou alguns caminhos mais perigosos ou inviáveis, é necessário encontrar a rota mais segura e eficiente. Para isso, o sistema utiliza o Algoritmo de Dijkstra, que permite identificar o trajeto com menor peso (menor quantidade de destroços), validando o desempenho do jogador com base na escolha do caminho e sua semelhança com o trajeto tomado pelo Dijkstra.


---

## 👨‍💻 Tecnologias Utilizadas

Liste as principais tecnologias, linguagens, frameworks e bibliotecas utilizadas:

- Python 3.12
- pip keyboard 0.13.5
- pip mutagen  1.47.0
- pip pygame   2.6.1
- Streamlit / FastAPI / Flask
- SQLite / PostgreSQL
- React / HTML + CSS + JS
- Graphviz / NetworkX (caso use grafos)
- Outros...


---

## 🗂️ Estrutura do Projeto

Caso o projeto tenha uma estrutura de pastas significativa, insira aqui um diagrama com os diretórios principais:

A estrutura a seguir é um exemplo. Vocês devem usar a estrutura do seu projeto obrigatóriamente. 
```
📦 nome-do-projeto
├── 📁 app
│   ├── main.py
│   ├── models/
│   ├── views/
│   └── utils/
├── README.md
└── requirements.txt
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-projeto.git
cd nome-do-projeto
```

2. Crie o ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python main.py
```

---

## 📸 Demonstrações

Inclua aqui prints, gifs ou vídeos mostrando a interface ou o funcionamento do sistema:

- Tela inicial
- Exemplo de funcionalidade
- Resultados esperados

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Fulano da Silva | [@fulano](https://github.com/fulano) |
| Ciclano Souza | [@ciclano](https://github.com/ciclano) |

---

## 🧠 Disciplinas Envolvidas

- Estrutura de Dados I
- Teoria dos Grafos
- Linguagens Formais e Autômatos

---

## 🏫 Informações Acadêmicas

- Universidade: **Universidade Braz Cubas**
- Curso: **Ciência da Computação / Análise e Desenvolvimento de Sistemas**
- Semestre: 3º
- Período: Noite
- Professora orientadora: **Dra. Andréa Ono Sakai**
- Evento: **Mostra de Tecnologia 1º Semestre de 2025**
- Local: Laboratório 12
- Datas: 05 e 06 de junho de 2025

---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.
