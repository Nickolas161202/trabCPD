import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage


def AdvancedScreen(parent):
    adv_frame = tk.Frame(master=parent)

    manaLabel =tk.Label(adv_frame, text= "digite o custo de mana")
    manaSearch = tk.Entry(adv_frame)

    kwLabel = tk.Label(adv_frame, text = "digite as palavras-chaves")
    kwSearch = tk.Entry(adv_frame)
    
    statsLabel = tk.Label(adv_frame, text = "digite os status da carta (vida/ataque)")
    healthSearch = tk.Entry(adv_frame)
    dmgSearch = tk.Entry(adv_frame)
    
    regionLabel = tk.Label(adv_frame, text="selecione a região")
    setLabel = tk.Label(adv_frame, text="selecione o  set")
    btn = tk.Button(adv_frame, text="pesquisar", command=lambda: switchPage(adv_frame, resultPage, parent))

    manaLabel.pack()
    manaSearch.pack()
    kwLabel.pack()
    kwSearch.pack()
    statsLabel.pack()
    healthSearch.pack()
    dmgSearch.pack()
    regionLabel.pack()
    setLabel.pack()
    btn.pack()
    adv_frame.pack()
