import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.detailedPage import detailedCard
def resultCard(parent):
    resultFrame = tk.Frame(master=parent)
    nameLabel =tk.Label(resultFrame, text= "colocar aqui as img da carta")
    btn = tk.Button(resultFrame, text="detalhes", command=lambda: switchPage(resultFrame, detailedCard, parent))

    

    nameLabel.pack()
    btn.pack()

    resultFrame.pack()