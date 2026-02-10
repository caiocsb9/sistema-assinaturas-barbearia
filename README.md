# ✂️ Sistema de Assinaturas para Barbearia Barros

Sistema desenvolvido para a disciplina **Banco de Dados NoSQL** (UFU), focado na gestão de clientes, planos de assinatura e análise de faturamento em tempo real.

## 📋 Descrição

Este projeto utiliza o **MongoDB** para gerenciar o ecossistema de uma barbearia, explorando a flexibilidade do modelo orientado a documentos para lidar com históricos de atendimentos e diferentes categorias de assinaturas. A arquitetura é composta por um Backend em **FastAPI** e um Frontend em **Streamlit**.

## 🚀 Tarefas Implementadas (Cronograma UFU)

### 🔹 Tarefa 3: Popular via API
- Implementação do endpoint `POST /popular/` utilizando o método **insert_many** do PyMongo para inserção em massa de dados de teste.

### 🔹 Tarefa 4: Data Analytics (Aggregation Pipeline)
Desenvolvimento de relatórios gerenciais automáticos processados diretamente no banco de dados:
- **Distribuição de Planos**: Uso de `$group` e `$sum` para contabilizar a popularidade de cada plano de assinatura.
- **Faturamento Estimado**: Pipeline utilizando `$match` (para filtrar apenas clientes ativos) e `$group` com `$sum` (baseado no campo valor) para calcular a receita real.

### 🔹 Tarefa 5: Dashboard Visual
- Interface desenvolvida em **Streamlit** que consome os dados da API e apresenta gráficos de barras e métricas de desempenho para o gestor.

## 🛠 Tecnologias

- **Linguagem**: Python 3.14
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Banco de Dados**: MongoDB Atlas (Cloud)
- **Bibliotecas**: `pymongo`, `pandas`, `requests`, `uvicorn`

---

## 🔧 Como Executar

O sistema depende de dois serviços rodando simultaneamente:

1. **Backend (Terminal 1)**:
   ```bash
   uvicorn api_barbearia:app --reload
   Documentação interativa disponível em: https://www.google.com/search?q=http://127.0.0.1:8000/docs
Frontend (Terminal 2):

Bash
streamlit run dashboard.py

📝 Estrutura de Dados (Exemplo)
JSON
{
  "nome": "Enrique Gil",
  "plano": "VIP",
  "valor": 120.0,
  "status": "Ativo",
  "data_cadastro": "2026-02-10"
}
