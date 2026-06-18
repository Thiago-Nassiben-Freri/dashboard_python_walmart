import streamlit as st
import pandas as pd


# Configurações inicias da página
st.set_page_config(
    page_title="Dashboard Walmart Vendas", 
    layout="wide"
)

# Carrega os dados e deixa eles em memória cache
@st.cache_data
def load_data():
    data = pd.read_csv("data/clean/dataset_walmart.csv")
    return data

# Armaneza os dados na variável df
df = load_data()

# Título do menu de seleção
st.sidebar.title("Menu de Seleção")

# Caixa de seleção de mês
month = st.sidebar.selectbox(
    "Selecione o mês",
    ["Todos"] + sorted(df["Month"].unique().tolist())
)

# Caixa de seleção do ano
year = st.sidebar.selectbox(
    "Selecione o ano",
    ["Todos"] + sorted(df["Year"].unique().tolist())
)

# Caixa de seleção da loja/unidade
store = st.sidebar.selectbox(
    "Selecione a loja",
    ["Todos"] + sorted(df["Store"].unique().tolist())
)

# Aplica os filtros de forma dinâmica
df_filtered = df.copy()

# Caso a opção "Todos" não esteja selecionada 
if month != "Todos":
    df_filtered = df_filtered[df_filtered["Month"] == month]

if year != "Todos":
    df_filtered = df_filtered[df_filtered["Year"] == year]

if store != "Todos":
    df_filtered = df_filtered[df_filtered["Store"] == store]

st.dataframe(df_filtered)