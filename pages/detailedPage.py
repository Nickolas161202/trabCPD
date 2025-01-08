import tkinter as tk

from Classes import Card

def detailedCard(parent, data:Card):
    detailedFrame = tk.Frame(master=parent)
    detailedFrame.rowconfigure((0,1,2), weight=1)
    detailedFrame.columnconfigure((0,1,2), weight=1)

    nameLabel = tk.Label(detailedFrame, text=f"Nome: {data.name}")
    nameLabel.grid(row=0, column=0)

    regionsLabel = tk.Label(detailedFrame, text=f"Região: {', '.join(data.regions)}")
    regionsLabel.grid(row=0, column=0, sticky="e")
    
    costLabel = tk.Label(detailedFrame, text=f"Custo: {data.cost}")
    costLabel.grid(row= 0, column=0, sticky="s")
    
    attackLabel = tk.Label(detailedFrame, text=f"Attack: {data.attack} Health: {data.health}")
    attackLabel.grid(row=1, column=0, pady=20, sticky="n")

    descriptionRawLabel = tk.Label(detailedFrame, text=f"Description: {data.description_raw}")
    descriptionRawLabel.grid(row=1, column=0, sticky="ne", pady=20, columnspan=2)

    levelUpLabel = tk.Label(detailedFrame, text=f"Level-Up Description: {data.levelup_description_raw}")
    levelUpLabel.grid(row=0, column= 1 )

    keywordsLabel = tk.Label(detailedFrame, text=f"Keywords: {', '.join(data.keywords)}")
    keywordsLabel.grid(row=0, column=1, sticky="e", padx=20)
    
    artistLabel = tk.Label(detailedFrame, text=f"Artist: {data.artist}")
    artistLabel.grid(row=0, column=1, sticky="s")

    spellSpeedLabel = tk.Label(detailedFrame, text=f"Spell Speed: {data.spell_speed}")
    spellSpeedLabel.grid(row=0, column=1, sticky= "se")

    rarityLabel = tk.Label(detailedFrame, text=f"Rarity: {data.rarity}")

    subtypesLabel = tk.Label(detailedFrame, text=f"Subtypes: {', '.join(data.subtypes)}")
    subtypesLabel.grid(row=1, column=1)

    supertypeLabel = tk.Label(detailedFrame, text=f"Supertype: {data.supertype}")
    supertypeLabel.grid(row=1, column=1, sticky="e")

    flavorTextLabel = tk.Label(detailedFrame, text=f"Flavor Text: {data.flavor_text}")
    flavorTextLabel.grid(row=1, column=1, sticky="s")

    detailedFrame.grid(sticky="nsew")
