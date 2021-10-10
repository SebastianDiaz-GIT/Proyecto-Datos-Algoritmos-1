from os import path
import cv2
import imutils
from tkinter import *
from tkinter import filedialog
import numpy as np
from PIL import Image
from PIL import ImageTk

import matplotlib.pyplot as plt


pathimg = "X:\Sebas-Disk\ST0245-00\Entrega_2" + "/" + "apple.jpg"
img = cv2.imread(pathimg)

bilinear_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_LINEAR)
bicubic_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_CUBIC)
near_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST)


cv2.imshow("Road", near_img)
cv2.imshow("Road3", bicubic_img)
cv2.imshow("Road4", bilinear_img)

cv2.imshow("Road", near_img)
cv2.imshow("Road2", img)
cv2.waitKey(0)
