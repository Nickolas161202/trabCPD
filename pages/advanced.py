import tkinter as tk



def AdvancedScreen():
    adv_frame = tk.Frame()

    manaLabel =tk.Label(adv_frame, text= "digite o custo de mana")
    manaSearch = tk.Entry(adv_frame)

    kwLabel = tk.Label(adv_frame, text = "digite as palavras-chaves")
    kwSearch = tk.Entry(adv_frame)
    
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
    setLabel.pack()
    adv_frame.pack()
