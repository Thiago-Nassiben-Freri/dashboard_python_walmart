import streamlit as st
import pandas as pd
import plotly.express as px


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

# Formatação para o formato de moeda em dólar
def format_currency(value):
    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value/1_000:.2f}"
    return f"${value:.2f}"

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

# KPIs
total_sales = df_filtered["Weekly_Sales"].sum()
avg_sales = df_filtered["Weekly_Sales"].mean()
max_sales = df_filtered["Weekly_Sales"].max()
min_sales = df_filtered["Weekly_Sales"].min()

# Colunas das KPIs
col1, col2, col3, col4 = st.columns(4)

# Insere essas KPIs
col1.metric("Total de Vendas", format_currency(total_sales))
col2.metric("Média de Vendas", format_currency(avg_sales))
col3.metric("Maior Venda", format_currency(max_sales))
col4.metric("Menor Venda", format_currency(min_sales))