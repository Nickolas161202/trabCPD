
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import *
from pages.resultPage import resultPage

def getResults(param:tk.Entry, actualFrame,  parent, useImg):
    data = getName(param)
    
    switchPageWithData(actualFrame, resultPage, parent, [data ,useImg ])

def mainPage(parent):
    
    mainFrame = tk.Frame(master= parent)
    mainFrame.rowconfigure((0,1,2,3), weight= 1, uniform='a')
    mainFrame.columnconfigure((0,1,2,3), weight= 1, uniform='a')

    w = tk.Label(mainFrame, text='Bem Vindo ao LoR Finder!', font=('Arial Black', 20))
    w.grid(row=0, column=1, columnspan=2)

    inputLabel = tk.Label(mainFrame, text= "Busca por nome:", font=("Arial", 12))
    inputLabel.grid(row=1, column=1) 


    inp = tk.Entry(mainFrame)
    inp.grid(row=1, column=2, sticky="w")

    searchbtn = tk.Button(mainFrame,  text= "Pesquisar", command=lambda:getResults(inp, mainFrame, parent, imVar))
    searchbtn.grid(row=1, column=1, sticky="s" )

    btn = tk.Button(mainFrame, text="Busca Avançada", command=lambda: switchPage(mainFrame,AdvancedScreen, parent))
    btn.grid(row=1, column=2, sticky="sw")
    imVar = tk.BooleanVar()
    img = tk.Checkbutton(mainFrame, onvalue=True, offvalue=False, variable=imVar, text="Mostrar imagem? (requer conexão de rede)")
    img.grid(row=2, column= 2)

    mainFrame.grid(sticky='nsew')
