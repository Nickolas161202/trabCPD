
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
    w = tk.Label(mainFrame, text='Bem Vindo ao LoR Finder!')
    inputLabel = tk.Label(mainFrame, text= "Busca por nome:")
    inp = tk.Entry(mainFrame)
    searchbtn = tk.Button(mainFrame,  text= "Pesquisar", command=lambda:getResults(inp, mainFrame, resultPage, parent))
    btn = tk.Button(mainFrame, text="Busca Avançada", command=lambda: switchPage(mainFrame,AdvancedScreen, parent))
    w.pack()
    inputLabel.pack()
    inp.pack()
    searchbtn.pack()
    btn.pack()
    mainFrame.pack(fill="both")
