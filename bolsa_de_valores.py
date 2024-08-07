import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

acao = input("Digite o codigo da ação desejada: ")

dados = yfinance.Ticker(acao).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

fechamento.plot()

maximo = round(fechamento.max() ,2)
minimo = round(fechamento.min() ,2)
media = round(fechamento.mean() , 2)


destinatario = "seuemaildesejado@gmail.com"
assunto = "Bolsa de valores"

mensagem = f"""Prezado(a), segue as análises solicitadas da ação {acao}: 

Cotação Max: R$ {maximo}
Cotação Min: R$ {minimo}
Valor Médio: R$ {media}

para mais informações entrar em contato"""


# Abrir o navegador e ir par ao Gmail
webbrowser.open("www.gmail.com")
time.sleep(7)

# Pause de 5 segundos
pyautogui.PAUSE = 3

# Clicar no botão escrever
pyautogui.click(x=67, y=216)

# Digitar o email do destinatário 
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão de enviar
pyautogui.click(x=847, y=696)

# Fechar gmail
pyautogui.click("ctrl", "f4")