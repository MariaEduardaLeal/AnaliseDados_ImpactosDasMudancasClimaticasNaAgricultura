# Importação das bibliotecas necessárias
import pandas as pd

# Caminho para o arquivo CSV (ajuste se necessário)
caminho_arquivo = 'base_dados/climate_change_impact_on_agriculture_2024.csv'

# Carregar o dataset em um DataFrame do pandas
dados_agricultura = pd.read_csv(caminho_arquivo)

# Exibir as primeiras 5 linhas do dataset para uma visão geral
print("Visualização inicial dos dados:")
print(dados_agricultura.head())

# Análise de valores vazios (NaN) em cada coluna
print("\nAnálise de valores faltantes em cada coluna:")
valores_vazios = dados_agricultura.isnull().sum()
print(valores_vazios)

# Verificar a porcentagem de valores faltantes por coluna
print("\nPorcentagem de valores faltantes por coluna:")
percentual_valores_vazios = (dados_agricultura.isnull().mean() * 100).round(2)
print(percentual_valores_vazios)
