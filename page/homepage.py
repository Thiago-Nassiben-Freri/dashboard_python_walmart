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

# Ordem correta dos meses
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Define a coluna Month como categórica ordenada
df["Month"] = pd.Categorical(
    df["Month"],
    categories=month_order,
    ordered=True
)

# Título do menu de seleção
st.sidebar.title("Menu de Seleção")

# Meses disponíveis respeitando a ordem correta
available_months = [m for m in month_order if m in df["Month"].unique()]

# Caixa de seleção de mês
month = st.sidebar.selectbox(
    "Selecione o mês",
    ["Todos"] + available_months
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

# Filtragem inicial do gráfico de linhas
sales_month = (
    df_filtered.groupby("Month")["Weekly_Sales"]
    .sum()
    .reset_index()
    .sort_values("Month")
)

# Gráfico de linhas
fig_line = px.line(
    sales_month,
    x="Month",
    y="Weekly_Sales",
    title="Evolução das Vendas por Mês",
    markers=True
)

# Filtragem inicial do gráfico de barras
sales_store = df_filtered.groupby("Store")["Weekly_Sales"].sum().reset_index()

# Gráfico de barras
fig_bar = px.bar(
    sales_store,
    x="Store",
    y="Weekly_Sales",
    title="Total de Vendas por Loja"
)

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(fig_line, width="stretch")
with col6:
    st.plotly_chart(fig_bar, width="stretch")
