import tkinter 
import tk_tools
import serial
import csv
import datetime
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_datos():
    global condicion,datos
    if condicion == True:
        dato=arduino.readline()
        if len(datos)<100:
            datos = np.append(datos,float(dato[0:len(dato)-2]))
        else:
            datos[0:99]=datos[1:100]
            datos[99]=float(dato[0:len(dato)-2])
            
        linea.set_xdata(np.arange(0,len(datos)))
        linea.set_ydata(datos)
        canvas.draw()
    igu.after(1,plot_datos)

def iniciar_plot():
    global condicion
    condicion= True
    boton_inicio.config(state='disabled')
    boton_detencion.config(state='normal')
    arduino.reset_input_buffer()
    
    
def detener_plot():
    global condicion
    condicion= False
    boton_inicio.config(state='normal')
    boton_detencion.config(state='disable')

def cerrar():
    arduino.close()
    igu.destroy()

#Interfaz gráfica de usuario
igu = tkinter.Tk()
igu.title('Graficar datos desde Arduino')
igu.geometry('900x700')
igu.configure(background='white')

fig = Figure(figsize=(8,4),dpi=100)
ax  = fig.add_subplot(111)
ax.set_title('Gráfica de datos del sensor')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Valor')
ax.grid(True,linestyle='-.')
ax.set_xlim(0,100)
ax.set_ylim(0,1024)
linea=ax.plot([],[],color='green',marker='o',markersize=6)[0]
canvas = FigureCanvasTkAgg(fig,master=igu)
canvas.draw()


boton_inicio = tkinter.Button(igu,text='Iniciar Graficado',
                              font=('Arial',14),padx=10,pady=10,
                              bg='green',fg='white',
                              command=lambda:iniciar_plot())


boton_detencion = tkinter.Button(igu,text='Detener Graficado',
                              font=('Arial',14),padx=10,pady=10,
                              bg='red',fg='white',
                              command=lambda:detener_plot())


boton_cerrar = tkinter.Button(igu,text='Cerrar',
                              font=('Arial',14),padx=10,pady=10,
                              bg='gray',fg='white',
                              command=cerrar)

 
etiqueta = tkinter.Label(igu,text='Valor del sensor',
                         font=('arial',14),bg='white')

display_7seg=tk_tools.SevenSegmentDigits(igu,digits=4,
                                         background='white',
                                         digit_color='black',
                                         height=50) 


canvas.get_tk_widget().grid(row=0,column=0,rowspan=2,
                            columnspan=2,padx=30,pady=30)


etiqueta.grid(row=2,column=0,pady=10)
display_7seg.grid(row=2,column=1,pady=10)

boton_inicio.grid(row=3,column=0,pady=20)
boton_detencion.grid(row=3,column=1,pady=20)
boton_cerrar.grid(row=4,column=0,columnspan=2)

datos=np.array([])

condicion= False
arduino = serial.Serial('com3',9600)

igu.after(1,plot_datos)
igu.mainloop()