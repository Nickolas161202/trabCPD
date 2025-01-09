import tkinter as tk
import itertools
from utils.resultCard import resultCard
from Classes import *
def showAssociated(cards, parent):
    sla = []
    for item in cards:
        arvore_codes = Trie()  # Trie para códigos
        arvore_nomes = Trie()  # Trie para nomes
        arquivos = Filenames()
        arvore_codes.carrega_arvore_trie(arquivos.codes)
        arvore_nomes.carrega_arvore_trie(arquivos.nomes)
        resultado = ColecaoDeCartas.carrega_carta_Indexada(arquivos, item, "codigo")
    sla.append(resultado.retorna_colecao())
    sla = list(itertools.chain(*sla)).remove()
    sla = set(sla)

    
def detailedCard(parent, data:Card):
    print(data)
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

    related = tk.Button(text= "cartas relacionadas", command=lambda: showAssociated(data.associated_cards, parent))
    related.grid()

    detailedFrame.grid(sticky="nsew")
