import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.detailedPage import detailedCard
from gera_arquivo_e_arvore import carta
def resultCard(parent, data:carta):

    resultFrame = tk.Frame(master=parent)
    nameLabel =tk.Label(resultFrame, text= data.name)
    btn = tk.Button(resultFrame, text="detalhes", command=lambda: switchPage(resultFrame, detailedCard, parent))

    

    nameLabel.pack()
    btn.pack()

    resultFrame.pack()