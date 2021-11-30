#Importamos las bibliotecas para trabajar con bases de datos
import sqlite3 
from sqlite3 import Error


#Método al cual le paso mi base de datos para crearla
def conexion_sql(base_datos):
    try:
        conexion=sqlite3.connect(base_datos)
        return conexion
    except Error:
        print(Error)
        
#Función para poder crear una tabla               
def crear_tabla(conexion):
    #Apuntamos, hacemos un cursor 
    cursor=conexion.cursor()
    #Ejecutamos un comando de sql
    #Palabras reservadas en mayúsculas    #Nombres de las columnas y su tipo de dato
    cursor.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, departamento text, puesto text, fecha_contratacion  text)")
    #Ejecutamos en la base de datos
    conexion.commit()
    
#Función para insertar datos en la tabla
def insertar_registro(conexion,registro):
    #Apuntamos, hacemos un cursor 
    cursor=conexion.cursor()
    #Ejecutamos un comando de sql
    cursor.execute("INSERT INTO empleados(id,nombre,salario,departamento,puesto,fecha_contratacion) VALUES(?,?,?,?,?,?)",registro)
    #Ejecutamos en la base de datos
    conexion.commit()
    
#Función para actualizar datos de la base
def actualizar_registro(conexion):
    #Apuntamos, hacemos un cursor
    cursor=conexion.cursor()
    #Ejecutamos un comando de sql, vamos a actualizar el id 2, con un nuevo nombre
    cursor.execute('UPDATE empleados SET nombre="Felipe de Jesus" WHERE id=2')
    #Ejecutamos en la base de datos
    conexion.commit()
     
#Método para consultar información de la base 
def consulta(conexion,comando):
    #Apuntamos, hacemos un cursor
    cursor=conexion.cursor()
    #Ejecutamos un comando  que le vayamos a pasar a la función
    cursor.execute(comando)
    #Imprime la información de cada fila
    filas=cursor.fetchall()
    for fila in filas:
        print(filas)

#Función para borrar la tabla
def borrar_tabla(conexion):
    cursor=conexion.cursor()
    cursor.execute("DROP table IF EXISTS empleados")
    conexion.commit()


       
#Hacemos la conexión con la base de datos
con=conexion_sql("baseempleados.db")

#Creamos la tabla e insertamos los registros
#crear_tabla(con)

#Insertamos los registros con los datos correspondientes
#registro1=(1,"Luis"  ,4000,"Desarrollo","Gerente","2015-09-21")
#registro2=(2,"Felipe",40000,"Desarrollo","Becario","2015-09-21")
#registro3=(3,"Ximena",80000,"Desaroollo","Jefa","2015-09-21")
#registro4=(4,"Leslie",70000,"Desarrollo","Subjefa","2015-09-21")

#insertar_registro(con,registro1)
##insertar_registro(con,registro2)
#insertar_registro(con,registro3)
#insertar_registro(con,registro4)

#Actualizamos los registros
#actualizar_registro(con)

#Hacemos consultas a la base
consulta(con,"SELECT id,nombre FROM empleados WHERE salario>50000")

#   consulta(con,"SELECT * FROM empleados")
#   consulta(con,"SELECT id,nombre FROM empleados")
#   


#Borramos la base

borrar_tabla(con)

con.close()
 