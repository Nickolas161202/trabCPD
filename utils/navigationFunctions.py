import tkinter as tk
from Classes import *

def switchPage(actualFrame, nextFrame, parent): 
    actualFrame.destroy()
    nextFrame(parent)

def switchPageWithData(actualFrame, nextFrame, parent, data): 
    actualFrame.destroy()
    print(data)
    nextFrame(parent, data)


def getName(param):
    name = param.get().title()
    # testando carregar as Trie
    arvore_codes = Trie()  # Trie para códigos
    arvore_nomes = Trie()  # Trie para nomes
    arquivos = Filenames()
    arvore_codes.carrega_arvore_trie(arquivos.codes)
    arvore_nomes.carrega_arvore_trie(arquivos.nomes)
    resultado = ColecaoDeCartas.carrega_carta_Indexada(arquivos, name, "nome")
    return resultado
