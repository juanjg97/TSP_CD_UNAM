import time
import requests
import threading
import concurrent.futures

hilo_local = threading.local()

def get_sesion():
    if not hasattr(hilo_local,"session"):
        hilo_local.session=requests.Session()
    return hilo_local.session

def descargar_sitio(url):
    sesion=get_sesion()
    with sesion.get(url) as respuesta:
        print("Leyendo {} de {}".format(len((respuesta.content)),url))

def descargar_todo(sitios):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as ejecutor:
            ejecutor.map(descargar_sitio,sitios)

if __name__ == '__main__':
    sitios = ["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
    "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
    
    hora_inicio=time.time()
    descargar_todo(sitios)
    duracion=time.time()-hora_inicio
    print("Se descargaron {} sitios en {} segundos".
          format(len(sitios),duracion))