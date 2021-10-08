#Import the tkinter library
from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import Image
from PIL import ImageTk
import numpy as np
import cv2
import imutils

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


    im = Image.fromarray(imageToShowOutPut)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImg.configure(image=img)
    lblOutputImg.image = img

    lblInfo3 = Label(root, text= "IMAGEN DE SALIDA ", font="bold")
    lblInfo3.grid(column=1, row=0, padx=5, pady=5)




def elegir_imagen():
    #Especificar tipos de archivos
    path_image = filedialog.askopenfilename(filetypes=
    [
        ("image", ".jpg"),
        ("image", ".jpeg"),
        ("image", ".png")
    ])

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


image = None


root = Tk()
root.title("Entrega_2 (Conversion de Imagenes)")


#Label donde se vera la imagen de entrada
lblInputImg = Label(root)
lblInputImg.grid(column=0, row=2)

#label de salida
lblOutputImg = Label(root)
lblOutputImg.grid(column=1, row=1, rowspan=6)

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


root.mainloop()
