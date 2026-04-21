import pandas as pd 

# Criar dados iniciais
dados = {
    'nome': ['Giovanni', 'Arlindo', 'Felizardo', 'Aida'],
    'idade': [36, 24, 20, 22],
    'cidade': ['Campinas', 'Campinas', 'Moscovo', 'Luanda']
}

print(dados)

print('='*60)
print('Com o DataFrame do pandas')
print('='*60)

df_dados = pd.DataFrame(dados)
print(df_dados)

# Salvar em CSV
df_dados.to_csv("teste_de_dados.csv", index=False)

# Ler o CSV
df_ler_dados = pd.read_csv('teste_de_dados.csv')

print('\nPrimeiras linhas do CSV:')
print(df_ler_dados.head())  # ⚠️ aqui faltava print

# Novos dados (população)
novos_dados = {
    'nome': ['Josimar', 'Edmara', 'Donald'],
    'idade': [35, 19, 23],
    'cidade': ['Canada', 'Paris', 'Paris']
}

# Transformar em DataFrame
df_novos_dados = pd.DataFrame(novos_dados)

# Concatenar (juntar)
df_dados_juntos = pd.concat([df_dados, df_novos_dados], ignore_index=True)

print('\nDados após concatenação:')
print(df_dados_juntos)

# 📊 População por cidade
populacao = df_dados_juntos['cidade'].value_counts()

print('\nPopulação por cidade:')
print(populacao)