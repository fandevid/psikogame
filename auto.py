from http.cookies import BaseCookie
from pyexpat import native_encoding
from time import sleep
from tkinter.messagebox import YESNOCANCEL
import pyautogui as auto
from urllib3 import disable_warnings

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

# auto.write("Selamat ya", 0.05)
# sleep(1.5)
# auto.press('enter')
# # auto.press('backspace',10,0.05)
# auto.write("Jaga dirimu disana", 0.05)
# sleep(1.5)
# auto.press('enter')
# # auto.press('backspace',18,0.05)
# auto.write('Dan jangan lupa SHOLAT!!!', 0.05)
# sleep(1.5)
# auto.press('enter')
# # auto.press('backspace',25,0.05)
# auto.write('Jangan sering begadang juga, nggak baik', 0.05)
# sleep(1.5)
# auto.press('enter')
# # auto.press('backspace',40, 0.05)
# auto.write('Sampai jumpa lagi nanti', 0.05)
# sleep(1.5)
# auto.press('enter')
# # auto.press('backspace',30, 0.05)
# auto.write('Dari @jalu', 0.05)

auto.alert('Woi, udah dulu ya ngodingnya ','Your Computer - @jalu')
auto.alert('Jaga dirimu disana dan jangan lupa SHOLAT!!!','Your Computer - @jalu')
auto.alert('Jangan sering begadang juga, nggak baik','Your Computer - @jalu')
auto.alert('Sampai jumpa lagi nanti, Byee >_<','Your Computer - @jalu')
# auto.alert('Byee','Your Computer - @jalu')