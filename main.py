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

def executar_trabalho_nosql():
    try:
        # Teste de Conexão Inicial
        client.admin.command('ping')
        print("✅ Sucesso: Conectado ao MongoDB Atlas!\n")

        print("--- INICIANDO OPERAÇÕES CRUD ---")

        # --- CREATE ---
        print("\n[REQUISIÇÃO] Inserindo novo cliente...")
        novo_cliente = {
            "nome": "Enrique Gil",
            "plano": "Mensal - 4 cortes",
            "status": "Ativo",
            "data_cadastro": "2025-12-19"
        }
        resultado_id = clientes_col.insert_one(novo_cliente).inserted_id
        print(f"[RESPOSTA] Cliente cadastrado com ID: {resultado_id}")

        print("\n[REQUISIÇÃO] Inserindo novo cliente...")
        novo_cliente = {
            "nome": "Jorge Alfredo",
            "plano": "Mensal - 4 cortes",
            "status": "Ativo",
            "data_cadastro": "2025-12-13"
        }
        resultado_id = clientes_col.insert_one(novo_cliente).inserted_id
        print(f"[RESPOSTA] Cliente cadastrado com ID: {resultado_id}")

        # --- READ ---
        print("\n[REQUISIÇÃO] Buscando dados do cliente no banco...")
        cliente_buscado = clientes_col.find_one({"_id": resultado_id})
        print(f"[RESPOSTA] Dados encontrados: {cliente_buscado}")

        # --- UPDATE ---
        print("\n[REQUISIÇÃO] Atualizando plano do cliente...")
        clientes_col.update_one(
            {"_id": resultado_id},
            {"$set": {"plano": "Anual VIP - Ilimitado"}}
        )
        print(f"[RESPOSTA] Plano atualizado com sucesso!")

        # --- DELETE ---
        print("\n[REQUISIÇÃO] Removendo cliente de teste...")
        clientes_col.delete_one({"_id": resultado_id})
        print(f"[RESPOSTA] Cliente removido do sistema.")

        print("\n--- TODAS AS ETAPAS DO CRUD FORAM CONCLUÍDAS ---")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

if __name__ == "__main__":
    executar_trabalho_nosql()