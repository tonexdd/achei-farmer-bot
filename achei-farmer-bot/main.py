from utils.screen import capturar_tela
import cv2
import time
from utils.autoaccept import auto_accept
import os 

def menu():
   print(" ACHEI-FARMER ".center(26, "="))

   print("1 -   AUTO ACCEPT")
   print("2 -   PREVIEW TELA")
   print("3 -   EXIT")
   escolha = int(input(""))
   return escolha
   
def preview_screen():
   print("Iniciando preview ao vivo da tela. Pressione 'z' para sair.")
   while True:
      try:
         frame = capturar_tela()
         cv2.imshow("Preview da Tela", frame)
         if cv2.waitKey(20) & 0xFF == ord('z'):
            print("Preview Encerrado.")
            break
      except Exception as e:
         print (f"[ERRO]: {e}")
      time.sleep(2)
      cv2.destroyAllWindows()

escolha = menu()

if escolha == 1:
   print("[INFO] Iniciando AUTOACCEPT")
   auto_accept()
elif escolha == 2:
   print("[INFO] Iniciando Preview de Tela")
   preview_screen()
