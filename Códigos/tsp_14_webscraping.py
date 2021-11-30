#Aplicación que regresa las palabras más comunes de un sitio web

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from bs4.element import Comment
from IPython.display import clear_output


def desplegar_resultados(palabras,sitio):
    pass

def filtrar_etiquetas(elemento):
    #Si el elemento que te estoy dando tiene alguna de estás etiquetas, dame falso
    if elemento.parent.name in ['style','script','head','title','meta','[document]']:
        return False
    #Si el elemento que me tienes, es instancia de Comment, tampoco lo quiero
    if isinstance(elemento,Comment):
        return False
    return True

def scrape(sitio): #Rascar
    #Obtenemos la información de la página web
    pagina=requests.get(sitio)
    soup=BeautifulSoup(pagina.content,'html.parser')
    #En texto hay ciertas etiquetas
    texto=soup.find_all(text=True)
    #De todas las etiquetas las voy a filtrar para que sólo me muestre las etiquetas visibles
    #Recibe una lista
    texto_visible=filter(filtrar_etiquetas,texto)
    #Hacemos la lista de palabras que será un diccionario vacío
    conteo_palabras={}
    #El set es un tipo de lista, no tiene índices y sus elementos están desordenados, sólo se accesa por valor
    #En el sitio hay palabras que no me interesan, por ejemplo: a, etc
    palabras_excluidas = set(['a','de','y','el','La','Las','Los','La','un','se','es','o'
                              ,'en','este','esto','esta','que','tu','para','por','con',
                              'son','si','pero','asi','aunque','su','del','más','ver','>'
                              ,'una','+','lo','al','no','y','México'])
#,'ese','eso','esos','pero','anque'
    print("Esta es una lista de palabras exlcluidas: ")
    print(palabras_excluidas)

    
    #Para cada texto en texto visible
    for texto in texto_visible:
        palabras=texto.replace('\n','').replace('\t','').split(' ')
        palabras=list(filter((lambda p:True if p.lower() not in palabras_excluidas else False),palabras))
        for palabra in palabras:
            if palabra != '':
                if palabra in conteo_palabras:
                    conteo_palabras[palabra]+=1
                else:
                    conteo_palabras[palabra]=1
    #Conteo palabras lo ordenamos, sus elementos son los que vamos a ordenar
    #con una llave que es una expresión lambda que recibe la llave y me regresa el valor de la llave
    #Lo queremos de mayor a menor
    conteo_palabras=sorted(conteo_palabras.items(),
                           key=(lambda kv:kv[1]),reverse=True)
    return conteo_palabras


#Código principal
try:
    clear_output()
    sitio=input("Ingresa el sitio web que quieres analizar: ")
    palabras=scrape(sitio)
    '''
    print("Las palabras más comunes son: ")
    print(palabras[0:10])
    res=input(print("Deseas agregar alguna palabra a la lista de palabras excluidas y/n"))
    if res == 'y'
    '''
    palabra_mas_comun=palabras[0]
    print("\nLa palabra más común fue: {}".format(palabra_mas_comun))
    desplegar_resultados(palabras,sitio)
    
except:
    print("Algo ha salido mal")
print("\nFin del programa")