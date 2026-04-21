import pandas as pd 
janeiro=pd.read_csv(r'desafio/vendas_janeiro.csv')
fevereiro=pd.read_csv(r'C:\Users\123\OneDrive\Desktop\Cursos\Generation\desafio\vendas_fevereiro.csv')
marco=pd.read_csv(r'desafio/vendas_marco.csv')

print(janeiro)
df_janeiro= pd.DataFrame(janeiro)
de_fevereiro= pd.DataFrame(fevereiro)
df_marco= pd.DataFrame(marco)
df_tricomplto.to_csv('vendas_tri_complto.csv',index=False)
print(df_tricomplto)