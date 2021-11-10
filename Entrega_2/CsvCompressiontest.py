from numpy import genfromtxt
from matplotlib import pyplot as plt
from os import remove, path
import tempfile 


f = "test.csv" # Aqui ponen donde esta el csv

f = genfromtxt(f,delimiter=",") # Convierten el csv a array de numpy

imgplot = plt.imsave("Dataimg" + ".jpg", f, cmap= "gray") #Setea la imagen que se 
print("archivo creado")

if path.exists("./Dataimg.jpg"):
    remove("./Dataimg.jpg")
print("archivo eliminado")

plt.show() #Mostrara la imagen