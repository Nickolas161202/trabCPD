import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage
from tkinter import filedialog
from pathlib import Path
from pages.mainpage import mainPage
def openFile():
    filename = filedialog.askdirectory() #salva o diretório da pasta
    print(filename)


def filePage(parent):
    file_frame = tk.Frame(master=parent)
    file_frame.rowconfigure(0, weight=1)
    file_frame.columnconfigure(0, weight=1)

    Label =tk.Label(file_frame, text= "escolha a pasta de dados json caso queira um novo arquivo binário")
    dataBtn = tk.Button(file_frame, text="Extrair dados", command= lambda: openFile())
    Label.grid(row=0, column=1,pady=2)
    dataBtn.grid(row=1, column=1)

    filepath = Path("./colecao_cartas_com_indice.bin")
    if(filepath.is_file()):
        searchBtn = tk.Button(file_frame, text="Ir para a pesquisa!", command= lambda: switchPage(file_frame, mainPage, parent))
        searchBtn.grid(row=2, column=1)
    else:
        CautionLabel =tk.Label(file_frame, text= "Crie um arquivo binário válido!")
        CautionLabel.grid(row=2, column=1)
    
    
    file_frame.grid(row= 0, column= 0,sticky="nsew", padx=10)
    
    
