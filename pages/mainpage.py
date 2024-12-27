
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage
def mainPage(parent):
    mainFrame = tk.Frame(master= parent)
    w = tk.Label(mainFrame, text='Bem Vindo ao LoR Finder!')
    inputLabel = tk.Label(mainFrame, text= "Busca por nome:")
    inp = tk.Entry(mainFrame)
    searchbtn = tk.Button(mainFrame,  text= "Pesquisar", command=lambda:switchPage(mainFrame, resultPage, parent))
    btn = tk.Button(mainFrame, text="Busca Avançada", command=lambda: switchPage(mainFrame,AdvancedScreen, parent))
    w.pack()
    inp.pack()
    searchbtn.pack()
    inputLabel.pack()
    btn.pack()
    mainFrame.pack()
