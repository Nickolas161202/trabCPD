
from tkinter import ttk as tk
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
    style = tk.Style()
    style.configure('TLabel', font=("Arial", 15))
    detailedFrame = tk.Frame(master=parent)
    detailedFrame.rowconfigure((0,1,2,3), weight=2, uniform='a')
    detailedFrame.rowconfigure((0,3), weight=1, uniform='a')
    detailedFrame.columnconfigure(1, weight=2, uniform='a')
    detailedFrame.columnconfigure((0,2), weight=1, uniform='a')
    #linha 1
    nameLabel = tk.Label(detailedFrame, text=f"Nome: {data.name}", font=("Arial Black", 18))
    nameLabel.grid(row=0, column= 1 )
    regionsLabel = tk.Label(detailedFrame, text=f"Região: {', '.join(data.regions)}")
    regionsLabel.grid(row=0, column=1, sticky="w")
    costLabel = tk.Label(detailedFrame, text=f"Custo: {data.cost}")
    costLabel.grid(row=0, column=1, sticky="e", padx=20)
    attackLabel = tk.Label(detailedFrame, text=f"Attack: {data.attack} Health: {data.health}")
    attackLabel.grid(row=0, column=1,  sticky="sw")
    keywordsLabel = tk.Label(detailedFrame, text=f"Keywords: {', '.join(data.keywords)}")
    keywordsLabel.grid(row=0, column=1, sticky="s")
    #linha 2
    descriptionRawLabel = tk.Label(detailedFrame, text=f"Description: {data.description_raw}")
    descriptionRawLabel.grid(row=1, column=1, sticky="nw", columnspan=2, pady=20)
    levelUpLabel = tk.Label(detailedFrame, text=f"Level-Up Description: {data.levelup_description_raw}")
    levelUpLabel.grid(row=1, column= 1 , sticky="w") 
    rarityLabel = tk.Label(detailedFrame, text=f"Rarity: {data.rarity}")
    rarityLabel.grid(row=1, column=1, sticky="sw")
    #linha3
    supertypeLabel = tk.Label(detailedFrame, text=f" {data.supertype}")
    supertypeLabel.grid(row=2, column=1, sticky="nw")

    spellSpeedLabel = tk.Label(detailedFrame, text=f"Spell Speed: {data.spell_speed}")
    spellSpeedLabel.grid(row=2, column=1, sticky= "n")
    subtypesLabel = tk.Label(detailedFrame, text=f"Subtypes: {', '.join(data.subtypes)}")
    subtypesLabel.grid(row=2, column=1, sticky="ne")

    flavorTextLabel = tk.Label(detailedFrame, text=f"Flavor Text: {data.flavor_text}")
    flavorTextLabel.grid(row=2, column=1, sticky="w")
    artistLabel = tk.Label(detailedFrame, text=f"Artist: {data.artist}")
    artistLabel.grid(column=1, row=2, sticky="s")

    '''
    related = tk.Button(text= "cartas relacionadas", command=lambda: showAssociated(data.associated_cards, parent))
    related.grid() iimplementação incompleta
    '''
    detailedFrame.grid(sticky="nsew", rowspan=2, columnspan=2)
