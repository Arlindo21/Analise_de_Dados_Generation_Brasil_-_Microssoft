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