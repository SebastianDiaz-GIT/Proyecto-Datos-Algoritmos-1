import os
from os.path import isfile, join
from numpy import genfromtxt
import numpy as np
from timeit import default_timer, timeit
import csv
from matplotlib import pyplot as plt

def carpeta():
    #obtener archivos:
    ruta = 'X:\Sebas-Disk\ST0245-00\Entrega_3/uncompress'
    contenido = os.listdir(ruta)
    archivos = [name for name in contenido]
    print(ruta)
    return archivos


def csv_data(dtCSV):
    #leer el archivo csv
    ruta = 'X:\Sebas-Disk\ST0245-00\Entrega_3/uncompress/' + str(dtCSV)
    data= genfromtxt(ruta, delimiter=',')
    #aplanar el archivo csv 
    csv = data.reshape(-1)
    return str(csv)

#archivo = csv_data()
#print(archivo)

def compression_LZW(csvdata):
    
    size = 256 #tamaño del diccianario con 256 colores en gris
    diccionary = {chr(i): i for i in range(size)} #diccionario a usar para el proceso de compresion

    w="" # Valor a usar para la compresion
    data=[] #salida de compresion del algoritmo


    #k posicion y valor del csv
    for k in csvdata:
        wk = w + k

        #revisar si wk se encuetra en el diccionario
        if wk in diccionary:
            w = wk # w obtendra el valor de wk
        else: 
            #si wk o se encuentra en el diccionario se añadira con su valor a la salida(data)
            #se añade al diccionario el valor de wk
            data.append(diccionary[w])
            diccionary[wk] = size
            size += 1
            w = k 
    
    if w:
        data.append(diccionary[w])
    return data

#print(compression_LZW(archivo))


def desscompression(compressed_csv):
    datasize = 256
    dict = {chr(i): i for i in range(datasize)}

    cod_viejo = ""

    pass

def write_compressed():
    pass

#iniciar contador del programa con timerit
start = default_timer()
def main():

    # ciclo de archivos en la carpeta a comprimir
    for i in carpeta():
        archivo = csv_data(i)
        print(compression_LZW(archivo)) #imprime la compresion sin crear los archivos.
    
main()
end = default_timer()
print(end - start)

