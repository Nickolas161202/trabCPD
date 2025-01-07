import tkinter as tk
from utils.resultCard import resultCard
from Classes import *


def getSearchData(): 
    data = [Card( #alterar assim que a função de busca estiver pronta
        name="Yuumi",
        regions=["Bandle City", "Targon"],
        cost=3,
        attack=2,
        health=1,
        description_raw="Round Start: Grant the unit I'm Attached to +1|+1. Otherwise, grant me +1|+1 instead.", 
        levelup_description_raw="I or the unit I'm Attached to have attacked 3 times.",
        keywords=["Attatch"],
        artist="SIXMOREVODKA",
        spell_speed="",
        game_absolute_path="http://dd.b.pvp.net/5_12_0/set5/en_us/img/cards/05BC029.png",
        rarity="Champion",
        expansion="Set5",
        card_type="Unit",
        subtypes=["FAE", "CAT"],
        supertype="Champion",
        flavor_text=""
        ),
     Card(
        name="Fiora",
        regions=["Demacia"],
        cost=3,
        attack=3,
        health=3,
        description_raw="When I'm on the board, slay 2 enemies to win the game.",
        levelup_description_raw="I've seen you slay 4 enemies.",
        keywords=["Challenger"],
        artist="SIXMOREVODKA",
        spell_speed="Fast",
        game_absolute_path="http://dd.b.pvp.net/5_12_0/set5/en_us/img/cards/05BC029.png",
        rarity="Champion",
        expansion="Set 1",
        card_type="Unit",
        subtypes=["Elite"],
        supertype="Champion",
        flavor_text="Her strength is rivaled only by her discipline."
    )]
    return data
def resultPage(parent, data:list):
    
    resultFrame = tk.Frame(master=parent)
    resultFrame.grid(row=0, column=0, sticky="nsew")  
    
    canvas = tk.Canvas(resultFrame)
    canvas.grid(row=0, column=0, sticky="nsew")  # Canvas inside the frame
    
    scr = tk.Scrollbar(resultFrame, orient="vertical", command=canvas.yview)
    scr.grid(row=0, column=1, sticky="ns")  # Scrollbar alongside the canvas
    
    canvas.configure(yscrollcommand=scr.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    secondFrame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=secondFrame, anchor="nw")
    
    if len(data) == 0:
        noResult = tk.Label(secondFrame, text="Não há nenhum resultado!")
        noResult.pack()
    else:
        for item in  data: 
            resultCard(secondFrame, item)  
    
    # Make sure the parent can resize properly
    resultFrame.grid_rowconfigure(0, weight=1)
    resultFrame.grid_columnconfigure(0, weight=1)
