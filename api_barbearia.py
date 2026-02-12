from fastapi import FastAPI
from pymongo import MongoClient, TEXT, GEOSPHERE
from typing import List

app = FastAPI()

uri = "mongodb+srv://caiocsb9_db_user:9fbFwK4zZ4r0OKlS@clusterbarbearia.25wqtrb.mongodb.net/?appName=ClusterBarbearia"
client = MongoClient(uri)
db = client['barbearia_db']
collection = db['clientes']

#DADOS PARA AUTOPOPULAÇÃO
MASSA_DADOS = [
    {"nome": "Enrique Gil", "plano": "VIP", "valor": 120.0, "status": "Ativo", "localizacao": {"type": "Point", "coordinates": [-48.275, -18.918]}},
    {"nome": "Caio Barros", "plano": "Mensal", "valor": 60.0, "status": "Ativo", "localizacao": {"type": "Point", "coordinates": [-48.280, -18.920]}},
    {"nome": "Carlos Oliveira", "plano": "Mensal", "valor": 60.0, "status": "Ativo", "localizacao": {"type": "Point", "coordinates": [-48.270, -18.910]}},
    {"nome": "Ricardo Santos", "plano": "Trimestral", "valor": 150.0, "status": "Inativo", "localizacao": {"type": "Point", "coordinates": [-48.260, -18.900]}},
    {"nome": "Felipe Matos", "plano": "VIP", "valor": 120.0, "status": "Ativo", "localizacao": {"type": "Point", "coordinates": [-48.285, -18.925]}},
    {"nome": "Bruno Souza", "plano": "Mensal", "valor": 60.0, "status": "Ativo", "localizacao": {"type": "Point", "coordinates": [-48.290, -18.930]}}
]

@app.on_event("startup")
def inicializar_sistema():
    """Automatiza as Tarefas 3 e 6 ao iniciar a aplicação"""
    print("\n[STARTUP] Limpando e Populando Banco (Tarefa 3)...")
    collection.delete_many({})
    collection.insert_many(MASSA_DADOS)
    
    print("[STARTUP] Criando Índices (Tarefa 6)...")
    # 1. Índice Simples
    collection.create_index([("plano", 1)])
    # 2. Índice de Texto
    collection.create_index([("nome", TEXT)])
    # 3. Índice Geosphere2d
    collection.create_index([("localizacao", GEOSPHERE)])
    
    print("✅ Sistema pronto: Dados populados e índices criados!")

#ROTAS DE BUSCA

@app.get("/buscar/nome/{termo}")
async def buscar_por_nome(termo: str):
    """Testa o Índice de Texto"""
    return list(collection.find({"$text": {"$search": termo}}, {"_id": 0}))

@app.get("/buscar/perto/")
async def buscar_proximidade(lat: float = -18.918, lon: float = -48.275, raio_metros: int = 2000):
    """Testa o Índice Geoespacial"""
    query = {
        "localizacao": {
            "$nearSphere": {
                "$geometry": {"type": "Point", "coordinates": [lon, lat]},
                "$maxDistance": raio_metros
            }
        }
    }
    return list(collection.find(query, {"_id": 0}))

#ROTAS DE ANÁLISE

@app.get("/analise/planos")
async def analise_planos():
    pipeline = [{"$group": {"_id": "$plano", "total": {"$sum": 1}}}, {"$sort": {"total": -1}}]
    return list(collection.aggregate(pipeline))

@app.get("/analise/faturamento")
async def analise_faturamento():
    pipeline = [{"$match": {"status": "Ativo"}}, {"$group": {"_id": None, "total": {"$sum": "$valor"}}}]
    res = list(collection.aggregate(pipeline))
    return res[0] if res else {"total": 0}