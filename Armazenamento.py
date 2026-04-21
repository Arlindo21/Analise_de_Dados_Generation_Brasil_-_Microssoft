import pandas as pd 
#criar um esqueleto 
# Usando dicionarios 
dados ={
    'nome':['Giovanni','Arlindo','Felizardo','Aida '],
    'idade':[36,24,20,22],
    'cidade':['campinas','campinas','Moscovo','Luanda']
}
print(dados)

# A bibliteca panda pode tranformar um dicionario em uma tabela.
#que é chamdo de dataframe
print('='*60)
print('Com o dataframe do panda  na parte de baixo  ')
print('='*60)

df_dados = pd.DataFrame(dados)
print(df_dados)

#criar um arquivo sem nada 
#arquivo csv(Excel)
#para criar precisamos de dados e do pandas 
#chamando dados e atribuindo função 

df_dados.to_csv("teste_de_dados.csv", index=False)

#ler um arquivo  
df_ler_dados=pd.read_csv(r'C:\Users\123\OneDrive\Desktop\Cursos\Generation\Pandas\teste_de_dados.csv')

#lendo as primeiras informações do arquivo.
df_ler_dados.head()

#vamos popular (Adicionando novos dados) a tabela
novos_dados={
    'nome':['josimar','Edmara','Donald'],
    'idade':[35,19,23],
    'cidade':['Canada','Paris','Paris']
}

#transformandondo dicionario em dados 
df_novos_dados=pd.DataFrame(novos_dados)
#unindo o antigo e o novo
#concatenação=junta ou unir 
df_dados_juntos=pd.concat([df_dados,df_novos_dados],ignore_index=True)
print('='*60)
print('\nDados após concatenação:')
print('='*60)
print (df_dados_juntos)