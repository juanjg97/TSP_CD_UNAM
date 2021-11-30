import requests
from bs4 import BeautifulSoup

#Solicitamos entrar a la pagina y descargar la información
pagina=requests.get("https://www.arthurLeej.com/e-history.html")

#Me da el código que devuelve la página web, 200 es que funciona bien
print(pagina)

#Me da el código html de este sitio web
print(pagina.content)

#Para organizar el código html, creamos un objeto y lo imprimimos
soup=BeautifulSoup(pagina.content,'html.parser')
print(soup.prettify())

#Accedemos a algunas regiones usando soup

#Encuentrame la primera coincidencia que tena la letra b
#Me regresa toda la etiqueta
titulo=soup.find('b')
print(titulo)

#Si solo quiero el texto dentro de la etiqueta
print(titulo.get_text())

#Obtenemos todo el texto que tiene el cuerpo
cuerpo=soup.find('body')
print(cuerpo.get_text())

#Si queremos encontrar todas las coincidencias dentro de una etiqueta
#Nos devuelve el texto que esté entre etiquetas b -> <b> ----</b>
texto_parrafos=soup.find_all('b')
for texto in texto_parrafos:
    print(texto.get_text())
    
#Podemos guardar los datos que estamos trabajando

pagina=requests.get("https://www.github.com/MiguelSerranoReyes")
#Para organizar el código html, creamos un objeto y lo imprimimos
soup=BeautifulSoup(pagina.content,'html.parser')

#Sabemos que el nombre está en una etiqueta llamada span
#Quiero un span en particular, con cirtos atributos
nombre=soup.find('span',attrs={'class':'vcard-fullname'})
print(nombre.get_text())

#En lugar del nombre quiero el nombre de usuario
nombre_usuario=soup.find('span',attrs={'class':'vcard-username'})
print(nombre_usuario.get_text())

#--------------------------------------------------------------
#--------------------------------------------------------------
#Otra forma de navegar en el sitio web
pagina=requests.get("https://www.arthurLeej.com/e-history.html")
soup=BeautifulSoup(pagina.content,'html.parser')

#Me da la idea que es una lista y puedo acceder a sus elementos
print(soup.children) 

#Ahora quiero ver el tipo de archivos que contiene esa lista
#Me dice que en el tercer elemento son clase bs4.element.Tag
for child in soup.children:
    print(type(child))


html=list(soup.children)[2] #También es una lista
#Podemos ver como estamos navegando para ver cómo está estructurado el código html
for section in html:
    print('\n\nNueva Sección')
    print(section)

#De la salida del ciclo podemos ver que la cabecera <head> está en la sección 1
head=list(html.children)[1]
#Veamos las etiquetas que hay en la cabecera
for tag in head:
    print('\n\nNueva Etiqueta')
    print(tag)

#Si quisiera sacar el título, sé que está en el elemento 1
titulo=list(head.children)[1]
print(titulo.get_text())