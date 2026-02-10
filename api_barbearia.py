from fastapi import FastAPI
from pymongo import MongoClient
from typing import List

app = FastAPI()


uri = "mongodb+srv://caiocsb9_db_user:9fbFwK4zZ4r0OKlS@clusterbarbearia.25wqtrb.mongodb.net/?appName=ClusterBarbearia"
client = MongoClient(uri)
db = client['barbearia_db']
collection = db['clientes']

# --- TAREFA 3: POPULAR ---
@app.post("/popular/")
async def popular_banco(clientes: List[dict]):
    collection.delete_many({}) 
    resultado = collection.insert_many(clientes)
    return {"status": "sucesso", "ids_inseridos": [str(id) for id in resultado.inserted_ids]}

# --- TAREFA 4: AGGREGATION PIPELINES ---
@app.get("/analise/planos")
async def analise_planos():
    pipeline = [{"$group": {"_id": "$plano", "total": {"$sum": 1}}}]
    return list(collection.aggregate(pipeline))

@app.get("/analise/faturamento")
async def analise_faturamento():
    pipeline = [
        {"$match": {"status": "Ativo"}},
        {"$group": {"_id": None, "total": {"$sum": "$valor"}}}
    ]
    res = list(collection.aggregate(pipeline))
    return res[0] if res else {"total": 0}