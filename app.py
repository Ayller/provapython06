import streamlit as st
import pandas as pd
import openpyxl

df = pd.read_excel("dados-educacao.xlsx")


# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Dados educação",
    page_icon="📕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. DADOS HARDCODED (Simulando exatamente a estrutura do CSV da PBH) NESSE CASO VOCÊS DEVERÃO UTILIZAR O PANDAS PARA CARREGAR AS TABELAS
# ==============================================================================

# Filtro exigido na prova: Taquaril e Santa Ines + apenas SERIE HISTORICA
df_filtrado = df[
    (df["escolaridade"].isin(["Mestrado"])) &
    (df["genero"] == "SERIE HISTORICA")
].copy()

df_tabela = df_filtrado[["escolaridade"]]

# ==============================================================================
# 3. BARRA LATERAL E TÍTULO
# ==============================================================================

st.title("Painel Streamlit de dados-educacao")
st.header("Controles")

opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])
