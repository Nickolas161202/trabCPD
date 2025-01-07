import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage
from tkinter import filedialog
from pathlib import Path
from pages.mainpage import mainPage
from Classes import *

def openFile(arquivos, actualframe, newFrame, parent):
    filename = filedialog.askdirectory() #salva o diretório da pasta
    set1 = ColecaoDeCartas()
    trie_codes = Trie()  # Trie para códigos
    trie_nomes = Trie()  # Trie para nomes
    set1.le_pasta_json(filename)
# Salvando os índices
    set1.salva_cartas_com_indice(arquivos.cards, trie_nomes, trie_codes)
# Salva a Trie para  códigos e nomes
    trie_codes.salva_arvore_trie(arquivos.codes)
    trie_nomes.salva_arvore_trie(arquivos.nomes)
    switchPage(actualframe, newFrame, parent)


def filePage(parent):
    
    arquivos = Filenames() #recebe os nomes

    file_frame = tk.Frame(master=parent)
    file_frame.columnconfigure((0,1,2), weight=1, uniform='a')
    file_frame.rowconfigure((0,1,2), weight=1, uniform='a')


    Label =tk.Label(file_frame, text= "Escolha a pasta de dados json caso queira um novo arquivo binário", font=('Arial', 12) )
    Label.grid(row=0, column=0, sticky='se', padx=20, pady=20, columnspan=2)

    dataBtn = tk.Button(file_frame, text="Extrair dados", command= lambda: openFile(arquivos, file_frame, filePage, parent))
    dataBtn.grid(row=0, column=2, sticky='sw', pady=20)

    codeFilePath = Path(arquivos.codes)
    nameFilePath = Path(arquivos.nomes)
    cardFilePath = Path(arquivos.cards)
    if(codeFilePath.is_file() and nameFilePath.is_file() and cardFilePath.is_file()):
        searchBtn = tk.Button(file_frame, text="Ir para a pesquisa!",  command= lambda: switchPage(file_frame, mainPage, parent))
        searchBtn.grid(row=1, column=1, sticky='n')
    else:
        CautionLabel =tk.Label(file_frame, text= "Crie um arquivo binário válido!")
        CautionLabel.grid(row=1, column=1, sticky='n')
    
    
    file_frame.grid(row= 0, column= 0,sticky="nsew")

    
