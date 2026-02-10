from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# 1. Configuração da Conexão (Sua URI específica)
uri = "mongodb+srv://caiocsb9_db_user:9fbFwK4zZ4r0OKlS@clusterbarbearia.25wqtrb.mongodb.net/?appName=ClusterBarbearia"

# Criando o cliente e conectando ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Definindo o Banco de Dados e a Coleção
db = client['barbearia_db']
clientes_col = db['clientes']

def popular_banco_teste():
    """Insere dados para termos o que agregar"""
    print("\n[STEP 1] Populando banco com dados de teste...")
    clientes_col.delete_many({}) # Limpa o banco antes de começar
    
    massa_dados = [
        {"nome": "Enrique Gil", "plano": "Premium", "valor": 80.0, "status": "Ativo"},
        {"nome": "Caio Barros", "plano": "Basico", "valor": 50.0, "status": "Ativo"},
        {"nome": "João Silva", "plano": "Premium", "valor": 80.0, "status": "Inativo"},
        {"nome": "Maria Souza", "plano": "VIP", "valor": 120.0, "status": "Ativo"},
        {"nome": "Pedro Oliveira", "plano": "Basico", "valor": 50.0, "status": "Ativo"}
    ]
    clientes_col.insert_many(massa_dados)
    print("✅ Dados inseridos com sucesso!")

def executar_agregacoes():
    print("\n--- INICIANDO AGGREGATION PIPELINES ---")

    # TESTE 1: Contagem de clientes por tipo de plano ($group)
    print("\n[PIPELINE 1] Contando clientes por plano...")
    pipeline_planos = [
        {
            "$group": {
                "_id": "$plano", 
                "quantidade": {"$sum": 1}
            }
        }
    ]
    res1 = list(clientes_col.aggregate(pipeline_planos))
    for item in res1:
        print(f"RESPOSTA: Plano {item['_id']} possui {item['quantidade']} clientes.")

    # TESTE 2: Faturamento total de clientes ATIVOS ($match + $group)
    print("\n[PIPELINE 2] Calculando faturamento de clientes ativos...")
    pipeline_faturamento = [
        {"$match": {"status": "Ativo"}},
        {
            "$group": {
                "_id": None, 
                "total": {"$sum": "$valor"}
            }
        }
    ]
    res2 = list(clientes_col.aggregate(pipeline_faturamento))
    if res2:
        print(f"RESPOSTA: O faturamento total ativo é R$ {res2[0]['total']:.2f}")

if __name__ == "__main__":
    popular_banco_teste()
    executar_agregacoes()
