import sqlite3 

from sqlite3 import Error

#Método al cual le paso mi base de datos
def conexion_sql(base_datos):
    try:
        conexion=sqlite3.connect(base_datos)
        return conexion
    except Error:
        print(Error)
        
#Función para poder crear una tabla
               
def crear_tabla(conexion):
    cursor=conexion.cursor() #Apuntamos, hacemos un cursor 
    #Ejecutamos un comando de sql
    #Palabras reservadas en mayúsculas    #Nombres de las columnas y su tipo de dato
    cursor.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, departamento text, puesto text, fecha_contratacion  text)")
    #Ejecutamos en la base de datos
    conexion.commit()
    
def insertar_registro(conexion,registro):
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO empleados(id,nombre,salario,departamento,puesto,fecha_contratacion) VALUES(?,?,?,?,?,?)",registro)
    conexion.commit()
    
    
def actualizar_registro(conexion):
    cursor=conexion.cursor()
    cursor.execute('UPDATE empleados SET nombre="Felipe de Jesus" WHERE id=2')
    conexion.commit()
     

def consulta(conexion,comando):
    cursor=conexion.cursor()
    cursor.execute(comando)
    filas=cursor.fetchall()
    for fila in filas:
        print(filas)

def borrar_tabla(conexion):
    cursor=conexion.cursor()
    cursor.execute("DROP table IF EXISTS empleados")
    conexion.commit()


registro1=(1,"Luis"  ,4000,"Desarrollo","Gerente","2015-09-21")
registro2=(2,"Felipe",40000,"Desarrollo","Becario","2015-09-21")
registro3=(3,"Ximena",80000,"Desaroollo","Jefa","2015-09-21")
registro4=(4,"Leslie",70000,"Desarrollo","Subjefa","2015-09-21")
       
con=conexion_sql("baseempleados.db")

"""
crear_tabla(con)
insertar_registro(con,registro1)
insertar_registro(con,registro2)
insertar_registro(con,registro3)
insertar_registro(con,registro4)
"""

#actualizar_registro(con)

#   consulta(con,"SELECT * FROM empleados")
#   consulta(con,"SELECT id,nombre FROM empleados")
#   consulta(con,"SELECT id,nombre FROM empleados WHERE salario>50000")
#   consulta(con,"SELECT id,nombre FROM empleados WHERE salario>50000")

#   borrar_tabla(con)

con.close()
 