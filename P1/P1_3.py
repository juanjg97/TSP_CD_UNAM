#Asignación 11, alumno: Juan José Jasso Garduño

#Se importa la biblioteca time, se usa para medir el tiempo
#Se importa la biblioteca requests, se usa para enviar peticiones HTTP
#Se importa la biblioteca threading para el uso de hilos
#Se importa la biblioteca concurrent.futures que provee una interfaz para ejecutar scripts de forma asincrónica
#Se importa la biblioteca matplotlib para el uso de gráficas
import time
import requests
import threading
import concurrent.futures
import matplotlib.pyplot as plt

#Se crea un objeto de la clase threading.local
hilo_local = threading.local()

#Se crean 2 listas vacías para almacenar la duración de cada iteración dependiendo del método para descarga
lista_1=[]
lista_2=[]

#Se crea un ciclo con 10 iteraciones para descargar sitios de manera paralela usando hilos
#Se guarda en una lista la duración que tuvo cada iteración 
#Se imprime el número de sitios descargados junto con su duración

for i in range(10):
    print("-------------------------------------------")
    print("Paralela iteración {}".format(i))
    print("-------------------------------------------")
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
        lista_1.append(duracion)
        print("Se descargaron {} sitios en {} segundos".
              format(len(sitios),duracion))


#Se crea un ciclo con 10 iteraciones para descargar sitios de manera secuencial
#Se guarda en una lista la duración que tuvo cada iteración 
#Se imprime el número de sitios descargados junto con su duración

for j in range(10):
    print("-------------------------------------------")
    print("Secuencial iteración {}".format(j))
    print("-------------------------------------------")
    def descargar_sitio(url,sesion):
        with sesion.get(url) as respuesta:
            print("Leyendo {} de {}".format(len((respuesta.content)),url))
    
    def descargar_todo(sitios):
        with requests.Session() as sesion:
                for url in sitios:
                    descargar_sitio(url,sesion)
    
    if __name__ == '__main__':
        sitios = ["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
        "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
        
        hora_inicio=time.time()
        descargar_todo(sitios)
        duracion=time.time()-hora_inicio
        lista_2.append(duracion)
        print("Se descargaron {} sitios en {} segundos".
              format(len(sitios),duracion))

#Al terminar ambos procesos se muestran las listas con los tiempos que tuvo cada método, respectivamente

print("\n")
print("Termino de ejecuciones \n")
print("Tiempos de manera paralela [s]: ")
print(lista_1)
print("\nTiempos de manera secuencial [s] : ")
print(lista_2)

#Se muestra un boxplot para los tiempos de duración que tuvo cada método, respectivamente.

plt.boxplot(lista_1)
plt.boxplot(lista_2)
plt.show()