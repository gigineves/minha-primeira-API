
# 🍽️ API de Cardápio de Restaurante — FastAPI

Este projeto é uma API REST desenvolvida com **FastAPI**, que serve dados de um cardápio fictício de restaurante. Ela foi criada como parte da Tarefa 4 da disciplina, com foco em aplicar os conceitos de criação de endpoints, manipulação de dados e documentação automática.

A API é simples, funcional e bem estruturada — ideal para quem está começando no mundo das APIs com Python.


## 📦 O que essa API faz?

A API permite:

- Ver informações gerais sobre o projeto
- Listar todos os pratos disponíveis no cardápio
- Buscar um prato específico pelo seu ID
- Filtrar pratos por categoria (como "Pizza", "Lanches", "Saladas")


## 📁 Estrutura do Projeto

Minha_Primeira_API/
├── main.py               # Código principal da API
├── README.md             # Documentação do projeto
├── requirements.txt      # Lista de dependências
├── dados/
│   └── cardapio.csv      # Dataset com os pratos do restaurante
```

⚠️ O dataset foi criado manualmente, por isso **não há necessidade de fonte.txt**.

## 🔧 Tecnologias Utilizadas

- **FastAPI**: framework moderno e rápido para APIs com Python
- **Uvicorn**: servidor leve e eficiente para rodar a aplicação
- **Pandas**: biblioteca para manipulação de dados tabulares

Instalação das dependências:

```bash
pip install fastapi uvicorn pandas
```

---

## 🔗 Endpoints Disponíveis

### 1. Informações da API

```http
GET /
```

Retorna informações básicas sobre o projeto, autor e número total de registros.

---

### 2. Listar todos os pratos

```http
GET /dados
```

Retorna todos os itens do cardápio em formato JSON.

---

### 3. Buscar prato por ID

```http
GET /dados/{item_id}
```

Exemplo: `/dados/3` → retorna o prato com ID 3.

Se o ID não existir, retorna erro 404 com mensagem "Item não encontrado".

---

### 4. Filtrar por categoria

```http
GET /categoria/{categoria}
```

Exemplo: `/categoria/Pizza` → retorna todos os pratos da categoria "Pizza".

Se a categoria não existir, retorna erro 404 com mensagem "Categoria não encontrada".

---

## ▶️ Como Executar a API

1. Certifique-se de estar na pasta do projeto.
2. Execute o servidor com:

```bash
uvicorn main:app --reload
```

3. Acesse a documentação interativa gerada automaticamente:

```
http://localhost:8000/docs
```

Você poderá testar todos os endpoints diretamente por essa interface.

