import requests
from bs4 import BeautifulSoup

#Solicitamos entrar a la pagina y descargar la información
pagina=requests.get("https://es.wikipedia.org/wiki/Anexo:Estadios_de_f%C3%BAtbol_en_M%C3%A9xico")
soup=BeautifulSoup(pagina.content,'html.parser')



lista_attrs=['Estadio Azteca','Estadio Olímpico Universitario','Estadio Jalisco','Estadio BBVA',
            'Estadio Cuauhtémoc','Estadio Akron','Estadio Universitario (UANL)','Estadio Corregidora',
            'Estadio Nemesio Diez','Estadio León','Estadio Corona (TSM)','Estadio Hidalgo','Estadio Caliente',
            'Estadio Alfonso Lastras Ramírez','Estadio de Mazatlán','Estadio Victoria (Aguascalientes)',
            'Estadio Olímpico Benito Juárez']

lista_capacidad=[87000,72000,55020,51348,51726,46232,41886,33,162,31000,31297,29273,27512,27333,25111,25000,23851,19703]

lista_nombres=[]

for i in range(len(lista_attrs)):
    nombre=soup.find('a',attrs={'title':lista_attrs[i]})
    lista_nombres.append(nombre.get_text())
    print("El estadio: {} tiene una capacidad de: {} personas".format(lista_nombres[i],lista_capacidad[i]))
    
    
