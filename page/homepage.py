import streamlit as st
import pandas as pd


# Configurações inicias da página
st.set_page_config(page_title="Dashboard Walmart Vendas", layout="wide")

# Carrega os dados e deixa eles em memória cache
@st.cache_data
def load_data():
    data = pd.read_csv("data/clean/dataset_walmart.csv")
    return data