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
