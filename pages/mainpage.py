
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import *
from pages.resultPage import resultPage
from Classes import *
def getName(param):
    name = param.get().title()
    # testando carregar as Trie
    arvore_codes = Trie()  # Trie para códigos
    arvore_nomes = Trie()  # Trie para nomes
    arquivos = Filenames()
    arvore_codes.carrega_arvore_trie(arquivos.codes)
    arvore_nomes.carrega_arvore_trie(arquivos.nomes)

    # Testando com nome
    resultado = ColecaoDeCartas.carrega_carta_Indexada(arquivos, name, "nome")
    if resultado is not None:
        resultado = resultado.retorna_colecao()
    else:
        resultado = []
    return  resultado

def getResults(param:tk.Entry, actualFrame, result, parent):
    data = getName(param)
    switchPageWithData(actualFrame, result, parent, data)

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

    searchbtn = tk.Button(mainFrame,  text= "Pesquisar", command=lambda:getResults(inp, mainFrame, resultPage, parent))
    searchbtn.grid(row=1, column=1, sticky="s" )

    btn = tk.Button(mainFrame, text="Busca Avançada", command=lambda: switchPage(mainFrame,AdvancedScreen, parent))
    btn.grid(row=1, column=2, sticky="sw")
    mainFrame.grid(sticky='nsew')
