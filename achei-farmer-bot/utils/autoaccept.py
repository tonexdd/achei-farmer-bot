import pyautogui
import time
from pyautogui import ImageNotFoundException
import cv2

def auto_accept():
    while True:
        try:
            aceitar = pyautogui.locateOnScreen("achei-farmer-bot/utils/accept.png", confidence= 0.8)
            if aceitar:
                print("Partida encontrada")
            pyautogui.moveTo(aceitar, duration= 0.3)
            pyautogui.click(aceitar)

            break
        except ImageNotFoundException:
            print("Procurando partida...")
        time.sleep(3)

