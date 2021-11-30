#Importación de bibliotecas
import tkinter
import tk_tools
import serial
import csv
import datetime
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Función para realizar la gráfica
def plot_datos():
    global condicion, datos
    if condicion == True:
        #Lectura de los datos de arduino
        dato = arduino.readline()
        #Con ese código iremos recorriendo la gráfica
        if len(datos) < 100:
            datos = np.append(datos, float(dato[0:len(dato) - 2]))
        else:
            datos[0:99] = datos[1:100]
            datos[99] = float(dato[0:len(dato) - 2])
        linea.set_xdata(np.arange(0, len(datos)))
        linea.set_ydata(datos)
        #Manda llamar a canvas para realizar el dibujo
        canvas.draw()
        valor = int(dato[0:len(dato) - 2].decode('utf-8'))
        display_7seg.set_value(str(valor))
        #Creamos el archivo csv
        with open("datos_p4.csv", "a", newline='') as f:
            escritor = csv.writer(f, delimiter=',')
            escritor.writerow([datetime.datetime.strftime(
                datetime.datetime.now(), '%Y/%m/%d %H:%M:%S ')
                , str(valor)])
    igu.after(1, plot_datos)

#Función para iniciar el graficado
def iniciar_plot():
    global condicion
    condicion = True
    #Bloquea el botón de inicio cuando se pulse
    boton_inicio.config(state='disabled')
    #Activa el botón detención mientras se inicia el plot
    boton_detencion.config(state='normal')
    arduino.reset_input_buffer()


def detener_plot():
    #Se hacen las condiciones contrarias a la función iniciar_plot
    global condicion
    condicion = False
    boton_inicio.config(state='normal')
    boton_detencion.config(state='disable')

#Cerramos la gráfica con esta función para poder finalizar arduino y destruir la interfaz
def cerrar():
    arduino.close()
    igu.destroy()


# Interfaz gráfica de usuario
igu = tkinter.Tk()
igu.title('Graficar datos desde Arduino')
igu.geometry('900x700')
igu.configure(background='white')

fig = Figure(figsize=(8, 4), dpi=100)
ax = fig.add_subplot(111)
ax.set_title('Gráfica de datos del sensor')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Valor')
ax.grid(True, linestyle='-.')
ax.set_xlim(0, 100)
ax.set_ylim(0, 1024)
linea = ax.plot([], [], color='green', marker='o', markersize=6)[0]
canvas = FigureCanvasTkAgg(fig, master=igu)
canvas.draw()

#Código para el botón de inicio
boton_inicio = tkinter.Button(igu, text='Iniciar Graficado',
                              font=('Arial', 14), padx=10, pady=10,
                              bg='green', fg='white',
                              command=lambda: iniciar_plot())

#Código para el botón de detención
boton_detencion = tkinter.Button(igu, text='Detener Graficado',
                                 font=('Arial', 14), padx=10, pady=10,
                                 bg='red', fg='white',
                                 command=lambda: detener_plot())

#Código del botón para cerrar la ventana
boton_cerrar = tkinter.Button(igu, text='Cerrar',
                              font=('Arial', 14), padx=10, pady=10,
                              bg='gray', fg='white',
                              command=cerrar)

#Código de la etiqueta del bcd
etiqueta = tkinter.Label(igu, text='Valor del sensor',
                         font=('arial', 14), bg='white')

#Código para el display de 7 segmentos
display_7seg = tk_tools.SevenSegmentDigits(igu, digits=4,
                                           background='white',
                                           digit_color='black',
                                           height=50)

#Código para la inferfaz
canvas.get_tk_widget().grid(row=0, column=0, rowspan=2,
                            columnspan=2, padx=30, pady=30)
#Distribución de los elementos en la interfaz
etiqueta.grid(row=2, column=0, pady=10)
display_7seg.grid(row=2, column=1, pady=10)

boton_inicio.grid(row=3, column=0, pady=20)
boton_detencion.grid(row=3, column=1, pady=20)
boton_cerrar.grid(row=4, column=0, columnspan=2)

datos = np.array([])

condicion = False

#Configuración del puerto serial de arduino
arduino = serial.Serial('com3', 9600)

igu.after(1, plot_datos)
igu.mainloop()
