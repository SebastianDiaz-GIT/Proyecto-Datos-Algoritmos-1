from tkinter import filedialog
from tkinter import *
import os

import cv2


directorio = filedialog.askdirectory()
    
files_name = os.listdir(directorio)
print(files_name)

for files_name in files_name:
    print(files_name)

    carpetaPath = directorio + "/" + files_name
    image = cv2.imread(carpetaPath)
        
    cv2.imshow("imagen", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()