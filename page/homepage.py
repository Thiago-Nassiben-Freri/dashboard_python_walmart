import streamlit as st
import pandas as pd


# Configurações inicias da página
st.set_page_config(page_title="Dashboard Walmart Vendas", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv("")