import pandas as pd


# Carregando os dados
df = pd.read_csv("data/raw/Walmart_Sales.csv")

# Checando os tipos dos dados
print(df.dtypes)

df = df[["Store", "Date", "Weekly_Sales"]]

# Transformando e padronizando os dados
df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%Y') # Converte para o padrão dia, mês e ano
df["Month"] = df["Date"].dt.month_name() # Cria uma coluna com o nome do mês
df["Year"] = df["Date"].dt.year # Cria uma coluna com o ano

# Checando os tipos dos dados (novamente)
print(df.dtypes)

# Mostra os cinco primeiros resultados
print(df.head(5))

# Manda os dados processados para a pasta clean
df.to_csv("data/clean/dataset_walmart.csv", index=False)
