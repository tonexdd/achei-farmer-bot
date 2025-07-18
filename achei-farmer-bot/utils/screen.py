import mss  #Isso vai server para capturar a tela mais rapido
import numpy as np #Para lidar com array de pixels
import cv2 #Processar as imagens

CAPTURE_REGION = {
    "top": 300,
    "left": 600,
    "width": 800,
    "height": 500
}
def capturar_tela():
    with mss.mss() as sct:
        img = np.array(sct.grab(CAPTURE_REGION)) #Captura a imagem
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR) #BGRA > BGR
    