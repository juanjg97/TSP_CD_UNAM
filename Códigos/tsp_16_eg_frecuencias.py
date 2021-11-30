import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

#datos=loadmat('EEG-inconsciente.mat')
datos=loadmat('C:/Users/User/Google Drive/UNAM/9no Semestre/TSP II - Ciencia de datos/Códigos Spyder y Prácticas/Códigos/EEG-inconsciente.mat')

EEG = datos['EEG']
tiempo=datos['t'][0]

plt.figure(figsize=(15,3))
plt.plot(tiempo,EEG,'-o')
plt.xlabel('Tiempo[s]')
plt.ylabel('Voltaje[$\mu$V]')
plt.title('EEG')
plt.show()


plt.figure(figsize=(15,3))
plt.plot(tiempo[:100],EEG[:100],'-o')
plt.xlabel('Tiempo[s]')
plt.ylabel('Voltaje[$\mu$V]')
plt.title('EEG')
plt.show()



x = EEG
dt = tiempo[1]-tiempo[0]
N = x.shape[0]
T = N*dt

np.mean(x)
x.mean()

x.var()
x.std()

lags = np.arange(-len(x)+1,len(x))
x=x.flatten()

ac = (1/N)*np.correlate(x-x.mean(),x-x.mean(),mode='full')

indices = abs(lags)<=100

plt.figure(figsize=(15,3))
plt.plot(lags[indices]*dt,ac[indices])
plt.xlabel('Lags[s]')
plt.ylabel('Autocovarianza')
plt.title('EEG')
plt.show()

from numpy.fft import fft,rfft

xf = fft(x-x.mean())
#Espectro de potencia
Sxx=(2*dt**2/T)*(xf*np.conj(xf))
#Ignorando las frecuencias negativas
Sxx=Sxx[:int(len(x)/2)]
#Resolución de la frecuencia
df=1/T
#Frecuencia de Nyquist
fNQ=1/dt/2
#Eje de frcuencia
eje_f=np.arange(0,fNQ,df)

plt.figure(figsize=(12,3))
plt.plot(eje_f,np.real(Sxx))
plt.xlabel('Frecuencia[Hz]')
#plt.ylabel('Potencia [$\muV^2$/Hz]')
plt.xlim([0,100])
plt.show()