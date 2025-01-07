import tkinter as tk
from utils.navigationFunctions import switchPage
from pages.resultPage import resultPage



def getEntries(region:tk.Entry = None,cost:tk.Entry = None ,atk:tk.Entry = None, hp:tk.Entry= None, keyW:tk.Entry= None, rarity:str = "NONE", exp:tk.Entry= None ):
        filtros_carta = {
    'regions': [region.get()],
    'cost': cost.get(),
    'attack': atk.get(),
    'health': hp.get(),
    'keywords': keyW.get().split(" "),
    'rarity': rarity.get(),
    'expansion': exp.get(),
}
        
        print(filtros_carta)

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
    inputLabel = tk.Label(adv_frame, text= "Busca por nome:")
    inputLabel.pack()

    inp = tk.Entry(adv_frame)
    inp.pack()

    manaLabel =tk.Label(adv_frame, text= "digite o custo de mana")
    manaLabel.pack()

    manaSearch = tk.Entry(adv_frame)
    manaSearch.pack()


    kwLabel = tk.Label(adv_frame, text = "digite as palavras-chaves")
    kwLabel.pack()

    kwSearch = tk.Entry(adv_frame, )
    kwSearch.pack()

    
    statsLabel = tk.Label(adv_frame, text = "digite os status da carta (vida/ataque)")
    statsLabel.pack()

    healthSearch = tk.Entry(adv_frame)
    healthSearch.pack()

    dmgSearch = tk.Entry(adv_frame)
    dmgSearch.pack()

    regionVar = tk.StringVar(value="Selecione a região")
    regionDropdown = tk.OptionMenu(adv_frame, regionVar, *regions)
    regionDropdown.pack()


    expansionVar = tk.StringVar(value="Selecione a expansão")
    expansionDropdown = tk.OptionMenu(adv_frame, expansionVar, *expansions)
    expansionDropdown.pack()

    rarityLabel  = tk.Label(adv_frame, text="Selecione a raridade (existem cartas sem raridade, neste caso selecionar NONE)")
    rarityLabel.pack()
    rarityVar = tk.StringVar(value="Selecionar")
    rarityDropdown = tk.OptionMenu(adv_frame, rarityVar, *rarities)
    rarityDropdown.pack()

    btn = tk.Button(adv_frame, text="pesquisar", command=lambda: getEntries(regionVar, manaSearch, dmgSearch, healthSearch, kwSearch, rarityVar, expansionVar ))
    btn.pack()
    adv_frame.pack()
