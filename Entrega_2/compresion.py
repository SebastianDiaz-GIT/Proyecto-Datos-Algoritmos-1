# using matplotlib and numpy

import matplotlib.image as img
import numpy as npy
 

m = img.imread("X:\Sebas-Disk\ST0245-00\Entrega_2.\Imagene_de_Prueba/anime.png");

w, h = m.shape[:2];
 
xNew = int(w * 1 / 2);
yNew = int(h * 1 / 2);

xScale = xNew/(w-1);
yScale = yNew/(h-1);
 
newImage = npy.zeros([xNew, yNew, 4]);
 
for i in range(xNew-1):
   for j in range(yNew-1):
       newImage[i + 1, j + 1]= m[1 + int(i / xScale),
                                 1 + int(j / yScale)]
 
img.imsave('scaled.png', newImage);

