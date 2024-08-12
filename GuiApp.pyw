#from Backend import *
from os import startfile
startfile('Waiting_Screen.exe')
from tkinter import *
#from Widgets import *
from Frontend import Window
from os import system
import time

if __name__ == '__main__':
    v = Window(initalll=True)
    v.build_app()
    system('taskkill /F /IM Waiting_Screen.exe')
    v.display_app()
