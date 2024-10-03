# Importação das bibliotecas necessárias
import pandas as pd

# Caminho para o arquivo CSV (ajuste se necessário)
caminho_arquivo = '/kaggle/input/dataset/climate_change_impact_on_agriculture_2024.csv'

# Carregar o dataset em um DataFrame do pandas
dados_agricultura = pd.read_csv(caminho_arquivo)

# Perguntar ao usuário se ele deseja visualizar todos os dados
mostrar_todos = input("Você gostaria de visualizar todos os dados? (s/n): ").strip().lower()

if mostrar_todos == 's':
    # Exibir todos os dados de forma bonita
    from IPython.display import display
    display(dados_agricultura)
else:
    # Perguntar quantas linhas o usuário gostaria de ver
    try:
        numero_linhas = int(input("Quantas linhas você gostaria de visualizar? "))
        print(f"\nVisualizando {numero_linhas} linhas aleatórias dos dados:")
        display(dados_agricultura.sample(numero_linhas))
    except ValueError:
        print("Entrada inválida. Exibindo 5 linhas por padrão.")
        display(dados_agricultura.head())

# Análise de valores vazios (NaN) em cada coluna
print("\n\nAnálise de valores faltantes em cada coluna:\n")
valores_vazios = dados_agricultura.isnull().sum()
display(valores_vazios)

# Verificar a porcentagem de valores faltantes por coluna
print("\n\nPorcentagem de valores faltantes por coluna:\n")
percentual_valores_vazios = (dados_agricultura.isnull().mean() * 100).round(2)
display(percentual_valores_vazios)

import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o gráfico
plt.figure(figsize=(15, 12))

# Gráfico de barras para temperatura média por região
plt.subplot(3, 1, 1)  # 3 linhas, 1 coluna, primeiro gráfico
sns.barplot(
    x='Region',  # Variável categórica no eixo x
    y='Average_Temperature_C',  # Variável numérica no eixo y
    data=dados_agricultura,  # DataFrame contendo os dados
    estimator='mean',  # Função de estimativa: calcula a média
    palette='rocket',  # Paleta de cores para o gráfico
    errorbar=None
)
plt.title('Temperatura média por região', fontsize=16)
plt.xlabel('Região', fontsize=14)
plt.ylabel('Temperatura média (°C)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico de barras para precipitação total por região
plt.subplot(3, 1, 2)  # 3 linhas, 1 coluna, segundo gráfico
sns.barplot(
    x='Region',  # Variável categórica no eixo x
    y='Total_Precipitation_mm',  # Variável numérica no eixo y
    data=dados_agricultura,  # DataFrame contendo os dados
    estimator='sum',  # Função de estimativa: calcula a soma
    palette='viridis',  # Paleta de cores para o gráfico
    errorbar=None
)
plt.title('Precipitação total por região', fontsize=16)
plt.xlabel('Região', fontsize=14)
plt.ylabel('Precipitação total (mm)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico de barras para rendimento por região em relação à temperatura
plt.subplot(3, 1, 3)  # 3 linhas, 1 coluna, terceiro gráfico
sns.barplot(
    x='Region',  # Variável categórica no eixo x
    y='Crop_Yield_MT_per_HA',  # Variável numérica no eixo y
    data=dados_agricultura,  # DataFrame contendo os dados
    estimator='mean',  # Função de estimativa: calcula a média
    palette='magma',  # Paleta de cores para o gráfico
    errorbar=None
)
plt.title('Rendimento das colheitas por região', fontsize=16)
plt.xlabel('Região', fontsize=14)
plt.ylabel('Rendimento (MT/HA)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

# Ajustando o layout
plt.tight_layout()
plt.show()
