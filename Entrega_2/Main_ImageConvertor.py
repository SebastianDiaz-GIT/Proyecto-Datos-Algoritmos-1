#LIBRERIAS
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import matplotlib.image as img
import numpy as np
import cv2
import imutils
import os

def compression_Algorithm(m):

    mg = img.imread(m)

    w, h = mg.shape[:2]

    xNew = int(w * 1 / 2)
    yNew = int(h * 1 / 2)

    xScale = xNew/(w-1)
    yScale = yNew/(h-1)

    imgData = np.zeros([xNew, yNew, 4])

    for i in range(xNew-1):
        for j in range(yNew-1):
            imgData[i + 1, j + 1]= mg[1 + int(i / xScale),
                                     1 + int(j / yScale)]

    img.imsave('TempImg.jpg', imgData)
    
#Mostrar output de la imagen dependiendo de la seleccion del usuario
def deteccion_Output():
    
    global image

    #Vecino mas cercano
    if selected.get() == 1:
        #Near_img = cv2.INTER_NEAREST
        Near_img = cv2.resize(image,None, fx= 2, fy= 2, interpolation = cv2.INTER_NEAREST)
        imageToShowOutPut = cv2.cvtColor(Near_img, cv2.COLOR_BGR2RGB)
        #imageToShowOutPut = Near_img

    #bilinear
    if selected.get() == 2:
        bilinear_img = cv2.resize(image,None, fx = 2, fy = 2, interpolation = cv2.INTER_LINEAR)
        imageToShowOutPut = cv2.cvtColor(bilinear_img, cv2.COLOR_BGR2RGB)
    #bicubico
    if selected.get() == 3:
        bicubic_img = cv2.resize(image,None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
        imageToShowOutPut = cv2.cvtColor(bicubic_img, cv2.COLOR_BGR2RGB)

    #Mostrar por interfaz la imagen y la informacion
    im = Image.fromarray(imageToShowOutPut)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImg.configure(image=img)
    lblOutputImg.image = img

    #Label IMAGEN SALIDA
    lblInfo3 = Label(root, text= "IMAGEN DE SALIDA ", font="bold")
    lblInfo3.grid(column=1, row=1, padx=8, pady=8)


#Elegir la imagen mediante filedialog
def elegir_imagen():
    #Especificar tipos de archivos
    path_image = filedialog.askopenfilename(filetypes=
    [
        ("image", ".jpg"),
        ("image", ".jpeg"),
        ("image", ".png")
    ])

    #Si longitud de archivos del path es mayor a 0 permitira seguir con la compresion
    if len(path_image) > 0:
        global image

        #leer la imagen de entrada y ubicarla
        image = cv2.imread(path_image)
        image = imutils.resize(image, height= 300)

        #visualizar la imagen de entrada en la GUI
        imageToShow = imutils.resize(image, height=150)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImg.configure(image=img)
        lblInputImg.image = img

        #Label IMAGEN ENTRADA
        lblInfo1 = Label(root, text= "IMAGEN DE ENTRADA")
        lblInfo1.grid(column=0, row = 1, padx= 5, pady= 5)

#Comprimir toda una carpeta de imagenes
def elegir_Directorio():

    #Usuario elige mediante filedialog el directorio a comprimir
    directorio = filedialog.askdirectory()
    pathdir = directorio
    files_names = os.listdir(directorio)
    print(files_names)

    #Si la carpeta no se encuentra vacia seguir con el codigo
    if len(files_names) > 0:

        #Creacion de carpetas para cada compresion de archivos 

        #Carpeta de imagenes comprimidas con el programa
        Compress_Path = "./Compressed_Images"
        if not os.path.exists(Compress_Path):
            os.makedirs(Compress_Path)
            print("directorio creado" + Compress_Path)
        
        #Carpeta para imagenes comprimidas de manera bilinear
        if not os.path.exists(Compress_Path+"/Bilinear"):
            os.makedirs(Compress_Path+"/Bilinear")
            print("directorio creado" + Compress_Path+"/Bilinear")

        #carpeta para imagenes comprimida de manera bicubica
        if not os.path.exists(Compress_Path+"/bicubico"):
            os.makedirs(Compress_Path+"/bicubico")
            print("directorio creado" + Compress_Path+"/bicubico")

        #carpeta para imagenes comprimida de manera bicubica
        if not os.path.exists(Compress_Path+"/Vecino_Cercano"):
            os.makedirs(Compress_Path+"/Vecino_Cercano")
            print("directorio creado" + Compress_Path+"/Vecino_Cercano")

        
        count = 0 #contador para nombrar las imagenes

        #Ciclo para recorrer los archivos del path de la carpeta de imagenes a comprimir
        for files_name in files_names:
            
             #No usara archivos que sean distintos a imagenes v2
                print(files_name) #imprime el path
                carpetaPath = directorio + "/" + files_name
                image = cv2.imread(carpetaPath) #lee las imagenes de la carpeta 
                #print(pathData)
                
                #No usara archivos que sean distintos a imagenes v1
                if image is None:
                    continue
                
                """
                mg = img.imread(files_name)

                w, h = mg.shape[:2]

                xNew = int(w * 1 / 2)
                yNew = int(h * 1 / 2)

                xScale = xNew/(w-1)
                yScale = yNew/(h-1)

                imgData = np.zeros([xNew, yNew, 4])

                for i in range(xNew-1):
                    for j in range(yNew-1):
                        imgData[i + 1, j + 1]= mg[1 + int(i / xScale),
                                                1 + int(j / yScale)]

                img.imsave('TempImg.jpg', imgData)

                #Compresion con algoritmo
                #compression_Algorithm(str(carpetaPath))

                """
                #Compresion de cada variable
                Near_img = cv2.resize(image,None, fx= 2, fy= 2, interpolation = cv2.INTER_NEAREST)
                bilinear_img = cv2.resize(image,None, fx = 2, fy = 2, interpolation = cv2.INTER_LINEAR)
                bicubic_img = cv2.resize(image,None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

                #Guarda las imagenes comprimidas en las carpetas asignadas anteriormente con una nueva extension PNG
                cv2.imwrite(Compress_Path+"/Vecino_Cercano/image_Vecino"+ str(count) + ".jpg", Near_img)
                cv2.imwrite(Compress_Path+"/Bilinear/image_Bilinear"+ str(count) + ".jpg", bilinear_img)
                cv2.imwrite(Compress_Path+"/bicubico/image_Bicubico"+ str(count) + ".jpg", bicubic_img)
                count+=1
                
                
        messagebox.showinfo("Informacion General", "Todas las imagenes se han comprimido con Exito")
        messagebox.showinfo("Informacion General", "Las imagenes se encuentran en la carpeta donde esta ubicado el programa ")
    else: #Si no se encuentran archivos en la carpeta saldra una advertencia al usuario
        messagebox.showinfo("Informacion General", "Error, no se encontraron imagenes en el directorio... Intente nuevamente.")

image = None

#Ventana con tkinter
root = Tk()
root.title("Entrega_2 (Conversion de Imagenes)")


#Label donde se vera la imagen de entrada
lblInputImg = Label(root)
lblInputImg.grid(column=0, row=2)

#label de salida
lblOutputImg = Label(root)
lblOutputImg.grid(column=1, row=1, padx= 20, pady= 20, rowspan=30)

# Label info 2
lblInfo2 = Label(root, text= "Seleccione Tipo de OutPut")
lblInfo2.grid(column=0, row=3, padx=5, pady=5)


#RADIO BUTTONS SELECTION
selected = IntVar()
rad1 = Radiobutton(root, text="Vecino Cercano", width=25, value=1, variable=selected, command= deteccion_Output)
rad2 = Radiobutton(root, text="Bilinear", width=25, value=2, variable=selected, command= deteccion_Output)
rad3 = Radiobutton(root, text="Bicubico", width=25, value=3, variable=selected, command= deteccion_Output)

rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)



#Creamos el botón  para elegir la imagen de entrada
btnVisualizar = Button(root, text="Choose a Image", width=25, command= elegir_imagen)
btnVisualizar.grid(column=0, row=0, padx= 5, pady= 5)

#Boton para Seleccionar directorio
btnVisualizarDirec = Button(root, text="Choose a Directory", width=25, command= elegir_Directorio)
btnVisualizarDirec.grid(column=1, row=0, padx= 5, pady= 5)


#root.iconbitmap("./Icono-NO-ELIMINAR.ico")
root.mainloop()
