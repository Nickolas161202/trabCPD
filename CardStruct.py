import pickle

class Card:
    def __init__(
        self, 
        name: str, 
        regions: list, 
        cost: int = 0, 
        attack: int = 0, 
        health: int = 0, 
        description_raw: str = "", 
        levelup_description_raw: str = "", 
        keywords: list = None, 
        artist: str = None, 
        spell_speed: str = "", 
        game_absolute_path: str = "", 
        rarity: str = "", 
        expansion: str = "", 
        cardType: str = "", 
        subtypes: list = None, 
        supertype: str = "", 
        flavor_text: str = None
    ):
        self.name = name
        self.regions = regions
        self.cost = cost
        self.attack = attack
        self.health = health
        self.description_raw = description_raw
        self.levelup_description_raw = levelup_description_raw
        self.keywords = keywords if keywords is not None else []
        self.artist = artist
        self.spell_speed = spell_speed
        self.game_absolute_path = game_absolute_path
        self.rarity = rarity
        self.set = expansion
        self.type = cardType
        self.subtypes = subtypes if subtypes is not None else []
        self.supertype = supertype
        self.flavor_text = flavor_text

    def __repr__(self):
        return (
            f"Carta(name={self.name!r}, regions={self.regions!r}, cost={self.cost}, "
            f"attack={self.attack}, health={self.health}, description_raw={self.description_raw!r}, "
            f"levelup_description_raw={self.levelup_description_raw!r}, keywords={self.keywords!r}, "
            f"artist={self.artist!r}, spell_speed={self.spell_speed!r}, game_absolute_path={self.game_absolute_path!r}, "
            f"rarity={self.rarity!r}, set={self.set!r}, type={self.type!r}, subtypes={self.subtypes!r}, "
            f"supertype={self.supertype!r}, flavor_text={self.flavor_text!r})"
        )

def carregar_cartas_de_pickle(arquivo):
    with open(arquivo, "rb") as f:
        return pickle.load(f)
    
def salvar_cartas_em_pickle(cartas, arquivo):
    with open(arquivo, "wb") as f:
        pickle.dump(cartas, f)

def exibir_pickle(nomeArquivo):
    cartas_restauradas = carregar_cartas_de_pickle(nomeArquivo)
    for carta in cartas_restauradas:
        print(carta)

def main():
    Yuumi = Card(
                "Yuumi",("Bandle City", "Targon"), 3, 2, 1,
				 "Round Start: Grant the unit I'm Attached to +1|+1. Otherwise, grant me +1|+1 instead.", 
                 "I or the unit I'm Attached to have attacked 3 times.",
                 ("Attatch"), "SIXMOREVODKA", "",
                 "http://dd.b.pvp.net/5_12_0/set5/en_us/img/cards/05BC029.png",
                 "Champion", "Set5", "Unit", ("FAE", "CAT"), "Champion", ""
                 )
    Fiora = Card(
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
        game_absolute_path="path/to/image.jpg",
        rarity="Champion",
        expansion="Set 1",
        cardType="Unit",
        subtypes=["Elite"],
        supertype="Champion",
        flavor_text="Her strength is rivaled only by her discipline."
    )

    nomeArquivo = "Teste.pkl"

    cartas = [Yuumi, Fiora]

    salvar_cartas_em_pickle(cartas, nomeArquivo)

# Exemplo de uso

	# !!!!!!!!!!!!!DOCUMENTATION!!!!!!!!!!!!!!!!
	# '    0 caso não aplicável
	# ''   string vazia caso não aplicável
	# '''	opcional, visível apenas via "detalhes"
