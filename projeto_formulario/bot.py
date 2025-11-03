import pyautogui
import time

pyautogui.PAUSE = 0.3


# Abrir o navegador
pyautogui.moveTo(x=37, y=300, duration=1)
pyautogui.click(x=37, y=300)
time.sleep(2)

# Clica na barra de pesquisa, escreve o nome de domínio e pressiona enter para entrar no site
pyautogui.moveTo(x=290, y=95, duration=1)
pyautogui.click(x=290, y=95, duration=1)
pyautogui.write('https://desecsecurity.com/')
time.sleep(1)
pyautogui.press('enter')

# Clina no menu fale conoco
pyautogui.click(x=1694, y=206, duration=1)

# Rola a barra em -7
pyautogui.moveTo(x=1708, y=254)
time.sleep(2)
pyautogui.scroll(-3)

# Move o mouse para assunto(treinamento) e clica para marcar
pyautogui.moveTo(x=352, y=503, duration=1)
pyautogui.click(x=352, y=503)

# Move o mouve para o campo nome clica
pyautogui.moveTo(x=839, y=451, duration=1)
pyautogui.click(x=839, y=451)
time.sleep(2)

# Prenche todos os campos do formulário
pyautogui.write('João Silva', interval=0.10)
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('joao@email.com')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('98989769087')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Desenvolvedor backend')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(
    'Gostaria de ter mais informação sobre o curso de Pentest Profissional e sobre o treinamento em Web Dev Security', interval=0.10)
time.sleep(1)
pyautogui.press('tab')

# Presiona enter para enviar a mensagem
pyautogui.press('enter')
