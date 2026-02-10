import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Dashboard Barbearia Barros", layout="wide")

st.title("✂️ Dashboard Gerencial - Sistema de Assinaturas")
st.markdown("---")


API_URL = "http://127.0.0.1:8000"


col1, col2 = st.columns(2)

try:
    # --- TAREFA 4: CONSUMINDO AGGREGATION PIPELINE (FATURAMENTO) ---

    res_fat = requests.get(f"{API_URL}/analise/faturamento").json()
    
    with col1:
        st.subheader("💰 Faturamento Ativo")

        valor = res_fat.get('total', 0)
        st.metric(label="Receita Estimada (Clientes Ativos)", value=f"R$ {valor:.2f}")

    # --- TAREFA 4: CONSUMINDO AGGREGATION PIPELINE (PLANOS) ---

    res_planos = requests.get(f"{API_URL}/analise/planos").json()
    
    with col2:
        st.subheader("📊 Distribuição de Planos")
        if res_planos:

            df = pd.DataFrame(res_planos)

            df.columns = ['Plano', 'Quantidade']
            st.bar_chart(df.set_index('Plano'))
        else:
            st.info("Aguardando dados para gerar o gráfico...")

except Exception as e:

    st.error("ERRO: Não foi possível conectar à API.")
    st.warning("Verifique se o comando 'uvicorn api_barbearia:app --reload' está rodando no Terminal 1.")

st.divider()
st.info("💡 Dados processados via Aggregation Pipeline no MongoDB Atlas.")