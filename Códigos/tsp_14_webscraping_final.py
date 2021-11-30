import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from bs4.element import Comment
from IPython.display import clear_output

palabras_excluidas = set(['a','de','y','el','La','Las','Los','La','un','se','es','o'
                          ,'en','este','esto','esta','que','tu','para','por','con',
                          'son','si','pero','asi','aunque','su','del','más','ver','>'
                          ,'una','+','lo','al','no','y','México','méxico','ese','eso',
                          'esos','pero','anque'])

def filtrar_etiquetas(elemento):
    if elemento.parent.name in ['style','script','head','title','meta','[document]']:
        return False
    if isinstance(elemento,Comment):
        return False
    return True

def scrape(sitio,palabras_excluidas):
    pagina=requests.get(sitio)
    soup=BeautifulSoup(pagina.content,'html.parser')
    texto=soup.find_all(text=True)
    texto_visible=filter(filtrar_etiquetas,texto)
    conteo_palabras={}
    print("\nEsta es la lista de palabras exlcluidas\n")
    print(palabras_excluidas)
    for texto in texto_visible:
        
        palabras=texto.replace('\n','').replace('\t','').split(' ')
        palabras=list(filter(lambda p:True if p.lower() not in 
                              palabras_excluidas else False,palabras))
        
        for palabra in palabras:
            if palabra != '':
                if palabra in conteo_palabras:
                    conteo_palabras[palabra]+=1
                else:
                    conteo_palabras[palabra]=1

    conteo_palabras=sorted(conteo_palabras.items(),
                           key=(lambda kv:kv[1]),reverse=True)
    return conteo_palabras


try:
    clear_output()
    sitio=input("Ingresa el sitio web que quieres analizar: ")
    palabras=scrape(sitio,palabras_excluidas)
    
    print("\n-----------------------------------------------------------------")
    print("Las palabras más comunes son\n")
    print(palabras[0:10])

    while(True):
        print("----------------------------------------------------------------")
        res=input("Deseas agregar alguna palabra a la lista de palabras excluidas y/n: ")
        if res == 'y':
            word=input("Ingresa palabra en minúsculas: ")
            palabras_excluidas.add(word)
            palabras=scrape(sitio,palabras_excluidas)
        elif res=='n':
            palabras=scrape(sitio,palabras_excluidas)
            break
        else:
            print("Ingresa la respuesta correctamente")
        
        
    palabra_mas_comun=palabras[0]
    print("\n********************************************************")
    print("La palabra más común fue: {}".format(palabra_mas_comun))
    
except:
    print("Algo ha salido mal")
print("\nFin del programa")