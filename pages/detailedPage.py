import tkinter as tk
from CardStruct import Card

def detailedCard(parent, data:Card):
    detailedFrame = tk.Frame(master=parent)
    nameLabel = tk.Label(detailedFrame, text=f"Name: {data.name}")
    regionsLabel = tk.Label(detailedFrame, text=f"Regions: {', '.join(data.regions)}")
    costLabel = tk.Label(detailedFrame, text=f"Cost: {data.cost}")
    attackLabel = tk.Label(detailedFrame, text=f"Attack: {data.attack}")
    healthLabel = tk.Label(detailedFrame, text=f"Health: {data.health}")
    descriptionRawLabel = tk.Label(detailedFrame, text=f"Description: {data.description_raw}")
    levelUpDescriptionRawLabel = tk.Label(detailedFrame, text=f"Level-Up Description: {data.levelup_description_raw}")
    keywordsLabel = tk.Label(detailedFrame, text=f"Keywords: {', '.join(data.keywords)}")
    artistLabel = tk.Label(detailedFrame, text=f"Artist: {data.artist}")
    spellSpeedLabel = tk.Label(detailedFrame, text=f"Spell Speed: {data.spell_speed}")
    rarityLabel = tk.Label(detailedFrame, text=f"Rarity: {data.rarity}")

    subtypesLabel = tk.Label(detailedFrame, text=f"Subtypes: {', '.join(data.subtypes)}")
    supertypeLabel = tk.Label(detailedFrame, text=f"Supertype: {data.supertype}")
    flavorTextLabel = tk.Label(detailedFrame, text=f"Flavor Text: {data.flavor_text}")

    # Pack all the labels into the frame
    nameLabel.pack()
    regionsLabel.pack()
    costLabel.pack()
    attackLabel.pack()
    healthLabel.pack()
    descriptionRawLabel.pack()
    levelUpDescriptionRawLabel.pack()
    keywordsLabel.pack()
    artistLabel.pack()
    spellSpeedLabel.pack()
    rarityLabel.pack()

    subtypesLabel.pack()
    supertypeLabel.pack()
    flavorTextLabel.pack()

    detailedFrame.pack()
    detailedFrame.pack()