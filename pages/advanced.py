import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage



def salve(etr1:tk.Entry,etr2:tk.Entry ,etr3:tk.Entry, etr4:tk.Entry, checkButtons:list ):
        etr1 = etr1.get()
        etr2 = etr2.get()
        etr3 = etr3.get()
        etr4 = etr4.get()
        
        print(etr1, etr2, etr3, etr4)
        for region in checkButtons:
              print(region.get())

def AdvancedScreen(parent):
    regions = [ #array utilizado para gerar dinâmicamente os checkbuttons e seus respectivos valores
    "Bandle City",
    "Bilgewater",
    "Demacia",
    "Freljord",
    "Ionia",
    "Piltover & Zaun",
    "Runeterra",
    "Shurima",
    "Targon",
    "The Shadow Isles"
]
    adv_frame = tk.Frame(master=parent)

    manaLabel =tk.Label(adv_frame, text= "digite o custo de mana")
    manaSearch = tk.Entry(adv_frame)

    kwLabel = tk.Label(adv_frame, text = "digite as palavras-chaves")
    kwSearch = tk.Entry(adv_frame, )
    
    statsLabel = tk.Label(adv_frame, text = "digite os status da carta (vida/ataque)")
    healthSearch = tk.Entry(adv_frame)
    dmgSearch = tk.Entry(adv_frame)
    
    regionLabel = tk.Label(adv_frame, text="selecione a região")
    

    setLabel = tk.Label(adv_frame, text="selecione o  set")
    
   
    manaLabel.pack()
    manaSearch.pack()
    kwLabel.pack()
    kwSearch.pack()
    statsLabel.pack()
    healthSearch.pack()
    dmgSearch.pack()
    regionLabel.pack()
    regionVal = []
    for region in regions:
          checkvar  = tk.StringVar()
          checkbtn = tk.Checkbutton(adv_frame, text=region, onvalue=region, offvalue="", variable=checkvar)
          regionVal.append(checkvar) 
          checkbtn.pack()   
    setLabel.pack()
    btn = tk.Button(adv_frame, text="pesquisar", command=lambda: salve(manaSearch, kwSearch, dmgSearch, healthSearch, regionVal))
    btn.pack()
    adv_frame.pack()
