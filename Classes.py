class NoBPlus:
    def __init__(self, grau, is_folha=True):
        self.grau = grau              # Grau mínimo do nó
        self.is_folha = is_folha      # Indica se o nó é folha
        self.chaves = []              # Lista de chaves
        self.dados = []               # Lista de dados (só para nós folhas)
        self.filhos = []              # Lista de ponteiros para filhos (usado em nós internos)
        self.proximo = None           # Ponteiro para o próximo nó folha (usado em nós folhas)

class ArvoreBPlus:
    def __init__(self, grau=3):
        self.raiz = NoBPlus(grau)
        self.grau = grau

    def buscar(self, chave):
        no_atual = self.raiz
        while not no_atual.is_folha:
            i = 0
            while i < len(no_atual.chaves) and chave >= no_atual.chaves[i]:
                i += 1
            no_atual = no_atual.filhos[i]

        # Buscar a chave no nó folha
        if chave in no_atual.chaves:
            return no_atual.dados[no_atual.chaves.index(chave)]
        return None

    def inserir(self, chave, dado):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.grau) - 1:
            nova_raiz = NoBPlus(self.grau, is_folha=False)
            nova_raiz.filhos.append(self.raiz)
            self._dividir_no(nova_raiz, 0, self.raiz)
            self.raiz = nova_raiz

        self._inserir_nao_cheio(self.raiz, chave, dado)

    def _inserir_nao_cheio(self, no, chave, dado):
        if no.is_folha:
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            no.chaves.insert(i + 1, chave)
            no.dados.insert(i + 1, dado)
        else:
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == (2 * self.grau) - 1:
                self._dividir_no(no, i, no.filhos[i])
                if chave > no.chaves[i]:
                    i += 1
            self._inserir_nao_cheio(no.filhos[i], chave, dado)

    def _dividir_no(self, pai, indice, no):
        grau = self.grau
        novo_no = NoBPlus(grau, is_folha=no.is_folha)
        pai.chaves.insert(indice, no.chaves[grau - 1])
        pai.filhos.insert(indice + 1, novo_no)

        novo_no.chaves = no.chaves[grau:]
        no.chaves = no.chaves[:grau - 1]

        if not no.is_folha:
            novo_no.filhos = no.filhos[grau:]
            no.filhos = no.filhos[:grau]
        else:
            novo_no.dados = no.dados[grau:]
            no.dados = no.dados[:grau - 1]
            novo_no.proximo = no.proximo
            no.proximo = novo_no

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
        card_type: str = "",
        subtypes: list = None,
        supertype: str = "",
        flavor_text: str = "",
        card_code: str = "",
        associated_cards: list = None,
        associated_indexes: list = None
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
        self.expansion = expansion
        self.card_type = card_type
        self.subtypes = subtypes if subtypes is not None else []
        self.supertype = supertype
        self.flavor_text = flavor_text
        self.card_code = card_code
        self.associated_cards = associated_cards if associated_cards is not None else []
        self.associated_indexes = associated_indexes if associated_indexes is not None else []

    def __repr__(self):
        return (
            f"Carta(\n Name = {self.name!r},\n Regions = {self.regions!r},\n Cost = {self.cost},\n "
            f"Attack=  {self.attack},\n Health = {self.health},\n Description = {self.description_raw!r},\n "
            f"Level Up = {self.levelup_description_raw!r},\n Keywords = {self.keywords!r},\n "
            f"Artist = {self.artist!r},\n Spell Speed = {self.spell_speed!r},\n Image Link = {self.game_absolute_path!r},\n "
            f"Rarity = {self.rarity!r},\n Expansion = {self.expansion!r},\n Card Type = {self.card_type!r},\n Subtypes = {self.subtypes!r},\n "
            f"Supertype = {self.supertype!r},\n Flavor Text = {self.flavor_text!r},\n Card Code = {self.card_code!r},\n "
            f"Associated Cards = {self.associated_cards!r},\n Associated Indexes = {self.associated_indexes!r} \n)"
        )

