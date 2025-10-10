import pyautogui
import webbrowser
import time

# 1) Abrir o Youtube com uma música especifica
url = 'https://www.youtube.com/watch?v=wmin5WkOuPw'
webbrowser.open(url)

# 2) Aguardar o carregamento da página
time.sleep(15) # Ajustar de acordo com a velocidade da internet utilizada

# 3) Garantir que o vídeo comece (aprete o espaço para "play")
pyautogui.press('space')