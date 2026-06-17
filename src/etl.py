import pandas as pd


# Carregando os dados
df = pd.read_csv("data/raw/Walmart_Sales.csv")

# Checando os tipos dos dados
print(df.dtypes)

# Transformando e padronizando os dados
df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%Y') # Converte para o padrão dia, mês e ano
df["Temperature"] = (df["Temperature"] - 32) * (5/9) # Converte de Fahrenheit para Celsius

# Checando os tipos dos dados (novamente)
print(df.dtypes)

# Mostra os cinco primeiros resultados
print(df.head(5))

# Manda os dados processados para a pasta clean
df.to_csv("data/clean/dataset_walmart.csv", index=False)
