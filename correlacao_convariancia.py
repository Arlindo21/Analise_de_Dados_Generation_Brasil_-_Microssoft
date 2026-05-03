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
