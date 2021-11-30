
import time     #Se importa la biblioteca time, se usa para medir el tiempo
import requests #Se importa la biblioteca requests, se usa para enviar peticiones HTTP

#Se crea una función para descargar información de un sitio
#Se imprime el número de archivo que se está leyendo y el sitio de donde proviene
def descargar_sitio(url,sesion):
    with sesion.get(url) as respuesta:
        print("Leyendo {} de {}".format(len((respuesta.content)),url))

#Se crea una función que recibe algunas url
#Después para cada url en sitios, se usa el método descargar sitio
def descargar_todo(sitios):
    with requests.Session() as sesion:
            for url in sitios:
                descargar_sitio(url,sesion)

#Si estamos en main, crea una lista con un par de sitios
#La lista de sitios se multiplica por 100 para tener 200 sitios para descargar
#Se establece un tiempo de inicio y se usa la función descargar todo, se le pasa como
#argumento la lista generada previamente
#Se crea una variable duración al finalizar la descarga
#Se imprime el número de sitios descargados y el tiempo que tardó
if __name__ == '__main__':
    sitios = [
    "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
    "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"
    ]*100
    
    hora_inicio=time.time()
    descargar_todo(sitios)
    duracion=time.time()-hora_inicio
    print("Se descargaron {} sitios en {} segundos".
          format(len(sitios),duracion))
    
