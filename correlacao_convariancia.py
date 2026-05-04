import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

alturas =np.array([160,170,175,163,180 ])

#peak-topeak Calcula a diferança entre o ,maior e o menor valor do array 
print(alturas)


#Criando uma variavel nova 
#o codigo abaixo pode ser executado dessa forma 
#amplitude=np.ptp(alturas)
#print(amplitude)

#Chamaando a biblioteca já no print 
print(f'A Amplitude do é {np.ptp(alturas)}')
# amplitude = maior e menor valor
print(f'O valor Minimo é', {np.min(alturas)})
print(f'O valor Maximo  é', {np.max(alturas)})

#Desvio de padrão
print(f'O Desvio de Padrão é {np.std(alturas):.2f}')
 
# Calculando a media das alturas 
#2 formas de o fazer 
#1ª Forma 
#media_alturas = np.mean(alturas)
#print(media_alturas)
# 2ª Forma chamando já no print 
print(f'A média das alturas  é : {np.mean(alturas)}')


#covariencia positiva
#Duas Coisas crescem ou decrescem ao mesmo tempo 

#negativa
#quando uma variavel cresce e a outra decresce
# covariencia zero 
# nadda muda 

dados_equipamentos ={
    'Consumo ':[10,20,30,40,50,60,70,80],
    'tempratura':[25,32,45,48,60,72,85,0]

}
# Transformçãos dos dados para a leitura em Pandas 
df_dados = pd.DataFrame(dados_equipamentos)

# fazendo o calculo da covariância
#criar uma base para a covariança
cov_matrix =df_dados.cov()

print(f'A covariencia foi :{cov_matrix.iloc[0,1]}')

# correlação


print(df_dados.corr())


