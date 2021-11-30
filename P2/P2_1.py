import requests
from bs4 import BeautifulSoup


pagina=requests.get("https://arthurLeej.com/e-history.html")
print(pagina)

print(pagina.content)

soup=BeautifulSoup(pagina.content,'html.parser')

print(soup.prettify())
titulo = soup.find('b')
print(titulo)
print(titulo.get_text())

cuerpo = soup.find('body')
print(cuerpo.get_text())

texto_parrafos = soup.find_all('b')
for texto in texto_parrafos:
    print(texto.get_text())
    
pagina = requests.get('https://github.com/MiguelSerranoReyes')
soup   = BeautifulSoup(pagina.content,'html.parser')

nombre = soup.find('span', attrs={'class':'vcard-fullname'})
print(nombre.get_text())

pagina = requests.get('https://github.com/MiguelSerranoReyes')
soup   = BeautifulSoup(pagina.content,'html.parser')

nombre = soup.find('span', attrs={'class':'vcard-username'})
print(nombre.get_text())

pagina=requests.get("https://arthurLeej.com/e-history.html")
soup   = BeautifulSoup(pagina.content,'html.parser')

print(soup)
print(soup.children)

for child in soup.children:
    print(type(child))

html = list(soup.children)[2]
for seccion in html:
    print("\n\n Nueva Sección")
    print(seccion)
    
head = list(html.children)[1]
for etiqueta in head:
    print("\n\n Nueva Etiqueta")
    print(etiqueta)
    
titulo = list(head.children)[1]
print(titulo.get_text())
    
    
