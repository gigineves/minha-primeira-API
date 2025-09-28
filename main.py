from fastapi import FastAPI, HTTPException
import pandas as pd


try:
    dados = pd.read_csv("dados/cardapio.csv")
    dados_dict = dados.to_dict("records")
except Exception as e:
    print("Erro ao carregar dataset:", e)
    dados_dict = []


app = FastAPI(
    title="Minha Primeira API com FastAPI",
    description="API para servir dados de um cardápio de restaurante 🍕🍔🥗",
    version="1.0.0"
)


@app.get("/")
def home():
    """
    Endpoint inicial com informações da API
    """
    return {
        "projeto": "Minha API",
        "autor": "Giovanna",
        "descricao": "API para servir dados de um cardápio de restaurante",
        "total_registros": len(dados_dict)
    }


@app.get("/dados")
def listar_todos():
    """
    Retorna TODOS os itens do dataset
    """
    return dados_dict


@app.get("/dados/{item_id}")
def buscar_por_id(item_id: int):
    """
    Busca um item específico pelo ID
    Exemplo: /dados/3
    """
    resultado = next((item for item in dados_dict if item["id"] == item_id), None)
    if resultado:
        return resultado
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.get("/categoria/{categoria}")
def buscar_por_categoria(categoria: str):
    """
    Filtra os itens do cardápio por categoria
    Exemplo: /categoria/Pizza
    """
    resultados = [item for item in dados_dict if item["categoria"].lower() == categoria.lower()]
    if resultados:
        return {
            "categoria": categoria,
            "total": len(resultados),
            "itens": resultados
        }
    raise HTTPException(status_code=404, detail="Categoria não encontrada")
