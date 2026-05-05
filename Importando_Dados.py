#1 entrada manual - usuario informa dados 
#raspagem de dados web scrapin 
#importção e automação 
import pandas as pd 
import requests
from datetime import datetime
#web scraping 
from bs4 import BeautifulSoup

def coletar_noticias_g1():
    url_g1= 'https://g1.globo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
    }
    #condicionando o uso
    #try
    try:
        respostas=requests.get(url=url_g1, headers=headers)
        respostas.raise_for_status()
        soup=BeautifulSoup(respostas.text, 'html.parser')
        posts=soup.find_all('a')
        noticias=[]
        for i in posts:
            titulo=i.get_text(strip=True)
            link= i.get('href')
            noticias.append({'titulo':titulo,
                             'link':link,
                             'Data': datetime.now().strftime('%d/%m/%y ')})
        df_noticias=pd.DataFrame(noticias)
        return df_noticias
    except Exception as e:
        print('Não consegui ler as noticias')
        return None
noticias1= coletar_noticias_g1()
if noticias1 is not None:
    print(noticias1.head(10))
else:
    print('Não consegui ler as noticias')
    from re import X
# Grafico com Valor medio de gasolina 
import matplotlib.pyplot as plt
# Eixos 
x_mes = ['Janeiro','Fevereiro','Março','Abril','Maio']
y_preco = [5.76,6.50,6.43,6.41,6.20]

#Gerando grafico biblioteca
plt.figure(figsize=(8,4))
plt.plot(x_mes, y_preco, marker='o', linestyle='-',color='blue')
plt.title('Media do Preço da Gasolina')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Valors', fontsize=12)
plt.grid(True)
plt.show()