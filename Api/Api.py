import requests
#Usando Biblioteca requests para ver o codigo de status da api
#status_code
#200- está funcionando
#404 arquivo não encontrado
# as Api Têm uma propriedade chamada de end-point

url ='https://api.open-meteo.com/v1/forecast'

#Usando geolocalização
url_loca ='https://nominatim.openstreetmap.org/reverse'

#clima
latitude = float(input('informe a latitude desejada'))
longitude = float(input('informe a longitude desejada'))
parametros={
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True,    
    
}

#tentando com localização 
parametros_loca={
   "lati":latitude,
   "longi":longitude,
   "format":"json"
 }


# vamos fazer uma requisição para coletar os dados do sistema 
#get para pegar a informação 
# fazendo requisição 
resposta= requests.get(url,params=parametros)

#requesição da localização
resposta_loca = requests.get(
  url_loca,
  params=parametros_loca,
  headers={"user-agent":"meu_app_teste"}
)

#para eu coletar algo, chamamos a biblioteca requests com o atributo get (onde, o que)
# request.get(url,params=parametros)


#Usando Biblioteca requests para ver o codigo de status da api
#status_code
#200- está funcionando
#404 arquivo não encontrado
# as Api Têm uma propriedade chamada de end-point

url ='https://api.open-meteo.com/v1/forecast'

latitude = float(input('informe a latitude desejada'))
longitude = float(input('informe a longitude desejada'))
parametros={
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True,
    
}


# vamos fazer uma requisição para coletar os dados do sistema 
#get para pegar a informação 
# fazendo requisição 
resposta = requests.get(url,params=parametros)

#para eu coletar algo, chamamos a biblioteca requests com o atributo get (onde, o que)
# request.get(url,params=parametros)


if resposta.status_code==200 and resposta_loca.status_code ==200:
  #fazendo funcionar
  #usando Json colocando a 
  dados = resposta.json()
  dados_loca=resposta_loca.json()

  

  temperatura = dados['current_weather']['temperature']
  velocidade_vento = dados['current_weather']

  #proucurando a localização 
  ende=dados_loca.get('adress',{})
  cidade = ende.get('city') or ende.get('town') or ende.get('village') or "Local desconhecido"
  pais = ende.get('country','')

  print(f'A Localização é :{Cidade}-{Pais} ')
  print(f'a temperatura é{temperatura} ºC')
  print(f'a velocidade do vento é{velocidade_vento}km/h')

