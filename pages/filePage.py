import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage
from tkinter import filedialog
from pathlib import Path
from pages.mainpage import mainPage
from Classes import *
def openFile(arquivos):
    filename = filedialog.askopenfilename() #salva o diretório da pasta
    set1 = ColecaoDeCartas()
    trie_codes = Trie()  # Trie para códigos
    trie_nomes = Trie()  # Trie para nomes
    set1.le_arquivo_json(filename)
# Salvando os índices
    set1.salva_cartas_com_indice(arquivos.cards, trie_nomes, trie_codes)
# Salva a Trie para  códigos e nomes
    trie_codes.salva_arvore_trie(arquivos.codes)
    trie_nomes.salva_arvore_trie(arquivos.nomes)


def filePage(parent):
    arquivos = Filenames() #recebe os nomes 
    file_frame = tk.Frame(master=parent)
    file_frame.rowconfigure(0, weight=1)
    file_frame.columnconfigure(0, weight=1)

    Label =tk.Label(file_frame, text= "escolha a pasta de dados json caso queira um novo arquivo binário")
    dataBtn = tk.Button(file_frame, text="Extrair dados", command= lambda: openFile(arquivos))
    Label.grid(row=0, column=1,pady=2)
    dataBtn.grid(row=1, column=1)

    codeFilePath = Path(arquivos.codes)
    nameFilePath = Path(arquivos.nomes)
    cardFilePath = Path(arquivos.cards)
    if(codeFilePath.is_file() and nameFilePath.is_file() and cardFilePath.is_file()):
        searchBtn = tk.Button(file_frame, text="Ir para a pesquisa!", command= lambda: switchPage(file_frame, mainPage, parent))
        searchBtn.grid(row=2, column=1)
    else:
        CautionLabel =tk.Label(file_frame, text= "Crie um arquivo binário válido!")
        CautionLabel.grid(row=2, column=1)
    
    
    file_frame.grid(row= 0, column= 0,sticky="nsew", padx=10)
    
    
