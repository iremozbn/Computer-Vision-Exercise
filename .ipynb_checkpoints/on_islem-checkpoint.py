import cv2
import matplotlib.pyplot as plt

#görüntü boyutlandırma
def boyutlandirma(img,x,y):
    return cv2.resize(img,(x,y))