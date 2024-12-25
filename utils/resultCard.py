import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.detailedPage import detailedCard
def resultCard():
    resultFrame = tk.Frame()
    nameLabel =tk.Label(resultFrame, text= "colocar aqui as img da carta")
    btn = tk.Button(resultFrame, text="", command=lambda: switchPage(detailedCard))

    

    nameLabel.pack()
    btn.pack()

    resultFrame.pack()