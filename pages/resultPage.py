import tkinter as tk
from utils.resultCard import resultCard
from CardStruct import Card


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
        cardType="Unit",
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
        cardType="Unit",
        subtypes=["Elite"],
        supertype="Champion",
        flavor_text="Her strength is rivaled only by her discipline."
    )]
    return data
def resultPage(parent):
    data = getSearchData()
    resultFrame = tk.Frame(master=parent)
    if len(data) == 0:
        noResult =tk.Label(resultFrame, text="Não há nenhum resultado!")
        noResult.pack()
    else:
        for i in data:
            resultCard(resultFrame, i)




    resultFrame.pack()