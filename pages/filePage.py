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

    Label =tk.Label(file_frame, text= "escolha a pasta de dados json caso queira um novo arquivo binário")
    dataBtn = tk.Button(file_frame, text="Extrair dados", command= lambda: openFile())
    Label.pack()
    dataBtn.pack()

    filepath = Path("./colecao_cartas_com_indice.bin")
    if(filepath.is_file()):
        searchBtn = tk.Button(file_frame, text="Ir para a pesquisa!", command= lambda: switchPage(file_frame, mainPage, parent))
        searchBtn.pack()
    else:
        CautionLabel =tk.Label(file_frame, text= "Crie um arquivo binário válido!")
        CautionLabel.pack()
    
    
    file_frame.pack()
    
