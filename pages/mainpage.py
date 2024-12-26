
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import switchPage

def mainPage(parent):
    mainFrame = tk.Frame(master= parent)
    w = tk.Label(mainFrame, text='Bem Vindo ao LoR Finder!')
    inp = tk.Entry(mainFrame)
    btn = tk.Button(mainFrame, text="Busca Avançada", command=lambda: switchPage(mainFrame,AdvancedScreen, parent))
    w.pack()
    inp.pack()
    btn.pack()
    mainFrame.pack()
