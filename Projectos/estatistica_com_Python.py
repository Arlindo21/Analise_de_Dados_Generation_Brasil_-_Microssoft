import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

#usando seaborn para configurar o visual dos graficos 

sns.set_theme(style="whitegrid")

#carregando o arquivo 
df_shoes = pd.read_csv('Projectos/shoes_sales_dataset.csv')

#Bloco de funções

#Visulisação de dados
  #bloco de funções
  #Função ver dados
def ver_dados():
    #usario escolhe quantos dados ele quer ver
    resposta= int(input('Quantos Linhas de dados quer ver? '))

    return df_shoes.head(resposta)

  #Medidas de tendencia
  #media- moda - mediana
def medidas_tendencia():
  # UNÇÕES DE TENDENCIA
  #mean()-media
  #median()-mediana
  #mode()[0]- moda

  #calculo de media
    media_preco = df_shoes['Price_USD'].mean()
    media_qtd_produtos = df_shoes['Units_Sold'].mean()
    media_total_vendas=df_shoes['Revenue_USD'].mean()
    #calculo de moda
    moda_cor=df_shoes['Color'].mode()[0]
    moda_marca=df_shoes['Brand'].mode()[0]

    #calculo mediana
    mediana_receita=df_shoes['Price_USD'].median()
    mediana_qtd_produtos=df_shoes['Units_Sold'].median()
    mediana_total_vendas=df_shoes['Revenue_USD'].median()

   #exibindo resultados 
    print("📊 Medidas de Tendência:\n")
    print(f"Média de preços: {media_preco:.2f}")
    print(f"Média de unidades vendidas: {media_qtd_produtos:.2f}")
    print(f"Média de receita: {media_total_vendas:.2f}\n")

    print(f"Moda (cor): {moda_cor}")
    print(f"Moda (marca): {moda_marca}\n")

    print(f"Mediana de preços: {mediana_receita:2f}")
    print(f"Mediana de unidades: {mediana_qtd_produtos:.2f}")
    print(f"Mediana de receita: {mediana_total_vendas:.2f}")


# Função de dispersão
def dispersao_variabilidade():
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df_shoes['Revenue_USD'])
    plt.title("Distribuição da Receita (Boxplot)")
    plt.show()
  #Histograma
  def histograma():
        plt.figure(figsize=(8, 5))
        sns.histplot(df_shoes['Price_USD'], kde=True, color='red', bins=30)
        plt.title("Histograma da Receita")
        plt.xlabel("Receita")
        plt.ylabel("Frequência")

medidas_tendencia()
dispersao_variabilidade()
histograma()
