import tkinter as tk
from tkinter import ttk
from utils.navigationFunctions import *
from pages.resultPage import resultPage
from Classes import *
from utils.navigationFunctions import switchPageWithData

def strToInt(ent):
    if ent != '':
        return int(ent)
    return None

def getEntries(name:tk.Entry, region:tk.Entry = None,cost:tk.Entry = None ,atk:tk.Entry = None, hp:tk.Entry= None, keyW:tk.Entry= None, rarity:str = "NONE", exp:tk.Entry= None, actualFrame = None, nextFrame = None, parent = None ):
    filtros_carta = {
    'regions': [region.get()],
    'cost': strToInt(cost.get()),
    'attack': strToInt(atk.get()),
    'health': strToInt(hp.get()),
    'keywords': keyW.get().split(" "),
    'rarity': rarity.get(),
    'expansion': exp.get(),
    }
    print(filtros_carta)
    data = getName(name)
    data = data.filtra_colecao_simples(filtros_carta)
    switchPageWithData(actualFrame, nextFrame, parent, data)
    
    
            

def AdvancedScreen(parent):
    expansions =["Set" + str(i) for i in range(1,8)]
    rarities = ["COMMON", "RARE", "EPIC", "CHAMPION", "NONE"]
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
    adv_frame.rowconfigure((0,1,2,3), weight=1, uniform="a")
    adv_frame.columnconfigure((0,1,2,3), weight=1, uniform="a")
    style = ttk.Style()
    style.configure('TLabel', font=(("Arial", 12)))
    
    inputLabel = tk.Label(adv_frame, text= "Nome:")
    inputLabel.grid(row=1, column=1, sticky="n")
    inp = tk.Entry(adv_frame)
    inp.grid(row=1, column=2, sticky="nw")

    manaLabel =tk.Label(adv_frame, text= "Custo de mana")
    manaLabel.grid(row=1, column=1)
    manaSearch = tk.Entry(adv_frame)
    manaSearch.grid(row=1, column=2, sticky="w")


    kwLabel = tk.Label(adv_frame, text = "Palavras-chaves:")
    kwLabel.grid(row=1, column=1, sticky="s")
    kwSearch = tk.Entry(adv_frame, )
    kwSearch.grid(row=1, column=2, sticky="sw")

    
    statsLabel = tk.Label(adv_frame, text = "Status da carta (vida/ataque):")
    statsLabel.grid(row=2, column=1, sticky="n", pady=20 )
    healthSearch = tk.Entry(adv_frame)
    healthSearch.grid(row=2, column=2, sticky="nw", pady=20)
    dmgSearch = tk.Entry(adv_frame)
    dmgSearch.grid(row=2, column=2,  padx=10, columnspan=2, pady=20, sticky="n")

    regionVar = tk.StringVar(value="Região")
    regionDropdown = tk.OptionMenu(adv_frame, regionVar, *regions)
    regionDropdown.grid(row=2, column=2, sticky="w")

    expansionVar = tk.StringVar(value="Expansão")
    expansionDropdown = tk.OptionMenu(adv_frame, expansionVar, *expansions)
    expansionDropdown.grid(row=2, column=1)

    rarityLabel  = tk.Label(adv_frame, text="Raridade ( cartas com raridade NONE são cartas derivadas dos campeões)")
    rarityLabel.grid(row=2, column=0, columnspan=2, sticky="s", pady=20 )
    rarityVar = tk.StringVar(value="Selecionar")
    rarityDropdown = tk.OptionMenu(adv_frame, rarityVar, *rarities)
    rarityDropdown.grid(row=2, column=2, sticky= "sw", pady=20)

    btn = tk.Button(adv_frame, text="pesquisar", command=lambda: getEntries(inp, regionVar, manaSearch, dmgSearch, healthSearch, kwSearch, rarityVar, expansionVar, adv_frame, resultPage, parent))
    btn.grid(row=3, column=1, sticky="ne", pady=20)
    adv_frame.grid(sticky="nsew")
