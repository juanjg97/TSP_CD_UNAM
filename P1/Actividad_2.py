#Actividad 2, Alumno: Juan José Jasso Garduño

import time     #Se importa la biblioteca time, se usa para medir el tiempo
import requests #Se importa la biblioteca requests, se usa para enviar peticiones HTTP
import threading #Se importa la biblioteca threading para el uso de hilos
import concurrent.futures #Provee una interfaz para ejecutar scripts de forma asincrónica

#Se crea un objeto de la clase threading.local
hilo_local = threading.local()

#Se crea una función para el uso de hilos con peticiones
def get_sesion():
    if not hasattr(hilo_local,"session"):
        hilo_local.session=requests.Session()
    return hilo_local.session

#Se crea una función para descargar información de un sitio, se le debe pasar una url
#Se obtiene una sesión
#Con la sesión se imprime el número de archivo que se está leyendo y el sitio de donde proviene
def descargar_sitio(url):
    sesion=get_sesion()
    with sesion.get(url) as respuesta:
        print("Leyendo {} de {}".format(len((respuesta.content)),url))

#Se crea una función que recibe una lista de urls
#Se usan caracteristicas concurrentes con 5 trabajadores
#Se usa el método descargar sitio junto con el ejecutor creado previamente para descargar los sitios
def descargar_todo(sitios):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as ejecutor:
            ejecutor.map(descargar_sitio,sitios)


#Si estamos en main, crea una lista con un par de sitios
#La lista de sitios se multiplica por 100 para tener 200 sitios para descargar
#Se establece un tiempo de inicio y se usa la función descargar todo, se le pasa como
#argumento la lista generada previamente
#Se crea una variable duración al finalizar la descarga
#Se imprime el número de sitios descargados y el tiempo que tardó
if __name__ == '__main__':
    sitios = ["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
    "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
    
    hora_inicio=time.time()
    descargar_todo(sitios)
    duracion=time.time()-hora_inicio
    print("Se descargaron {} sitios en {} segundos".
          format(len(sitios),duracion))