class NoBPlus:
    def __init__(self, grau, is_folha=True):
        self.grau = grau              # Grau mínimo do nó
        self.is_folha = is_folha      # Indica se o nó é folha
        self.chaves = []              # Lista de chaves
        self.dados = []               # Lista de dados por chave (só para nós folhas)
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
            # Encontre a posição onde a chave deve ser inserida
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1

            # Verifique se a chave já existe
            if i >= 0 and no.chaves[i] == chave:
                # Se a chave existe, anexe o dado à lista de dados correspondente
                no.dados[i].append(dado)
            else:
                # Insira a chave e inicialize a lista de dados
                no.chaves.insert(i + 1, chave)
                no.dados.insert(i + 1, [dado])
        else:
            # Encontre o filho onde a chave deve ser inserida
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1

            # Divida o nó filho se estiver cheio
            if len(no.filhos[i].chaves) == (2 * self.grau) - 1:
                self._dividir_no(no, i, no.filhos[i])
                if chave > no.chaves[i]:
                    i += 1

            # Continue a inserção no nó filho
            self._inserir_nao_cheio(no.filhos[i], chave, dado)

    def _dividir_no(self, pai, indice, no):
        grau = self.grau
        novo_no = NoBPlus(grau, is_folha=no.is_folha)

        # Atualize as chaves e filhos do nó pai
        pai.chaves.insert(indice, no.chaves[grau - 1])
        pai.filhos.insert(indice + 1, novo_no)

        # Divida as chaves entre os dois nós
        novo_no.chaves = no.chaves[grau:]
        no.chaves = no.chaves[:grau - 1]

        if not no.is_folha:
            # Divida os filhos entre os dois nós
            novo_no.filhos = no.filhos[grau:]
            no.filhos = no.filhos[:grau]
        else:
            # Divida os dados entre os dois nós
            novo_no.dados = no.dados[grau:]
            no.dados = no.dados[:grau - 1]

            # Atualize os ponteiros dos nós folha
            novo_no.proximo = no.proximo
            no.proximo = novo_no

    def salva_arvore_b_plus(self, arquivo_binario):
        with open(arquivo_binario, 'wb') as f:
          pickle.dump(self, f)

    def carrega_arvore_b_plus(arquivo_binario):
      with open(arquivo_binario, 'rb') as f:
          arvore_b_plus = pickle.load(f)
      return arvore_b_plus

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

class ColecaoDeCartas:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta_obj):
        self.cartas.append(carta_obj)

    def retorna_colecao(self):
        return self.cartas

    def listar_cartas(self):
        for carta_obj in self.cartas:
            print(f"Nome: {carta_obj.name}, Custo: {carta_obj.cost}, Descrição: {carta_obj.description_raw}")
    
    def salva_cartas_com_indice(self, arquivo_binario, arvore_b_plus):
        with open(arquivo_binario, 'wb') as f:
            i = 1
            for carta_obj in self.cartas:
                pickle.dump(carta_obj, f)
    
                # Insere a chave (nome da carta) e a posição no índice (árvore B+)
                arvore_b_plus.inserir(carta_obj.name, i)
                i += 1
                
    def carrega_carta_por_nome_Indexada(arquivo_binario, arquivo_indice, nome_carta):
        arvore_b_plus = ArvoreBPlus.carrega_arvore_b_plus(arquivo_indice)
        posicao_no_arquivo = arvore_b_plus.buscar(nome_carta)
        nova_colecao = ColecaoDeCartas()
    
        if posicao_no_arquivo is None:
            # Se a carta não for encontrada no índice, retorna None
            print(f"Carta com nome '{nome_carta}' não encontrada no índice.")
            return None

        for posicao in posicao_no_arquivo:
        # Abre o arquivo binário para leitura
          with open(arquivo_binario, 'rb') as f:
              for i in range(posicao):
                carta_obj = pickle.load(f)
          nova_colecao.adicionar_carta(carta_obj)
        return nova_colecao

    def carrega_carta(self,dados_json):
        carta = Card(
            name=dados_json.get('name'),
            regions=dados_json.get('regions', []),
            cost=dados_json.get('cost', 0),
            attack=dados_json.get('attack', 0),
            health=dados_json.get('health', 0),
            description_raw=dados_json.get('descriptionRaw', ''),
            levelup_description_raw=dados_json.get('levelupDescriptionRaw', ''),
            keywords=dados_json.get('keywords', []),
            artist=dados_json.get('artistName', ''),
            spell_speed=dados_json.get('spellSpeed', ''),
            game_absolute_path=dados_json['assets'][0].get('gameAbsolutePath', '') if 'assets' in dados_json and len(dados_json['assets']) > 0 else '',
            rarity=dados_json.get('rarity', ''),
            expansion=dados_json.get('set', ''),
            card_type=dados_json.get('type', ''),
            subtypes=dados_json.get('subtypes', []),
            supertype=dados_json.get('supertype', ''),
            flavor_text=dados_json.get('flavorText', ''),
            card_code=dados_json.get('cardCode', ''),
            associated_cards=dados_json.get('associatedCardRefs',[])
            )
        return carta

    def le_arquivo_json(self,arquivo):
        try:
          with open(arquivo, 'r') as arquivo:
              json_data = json.load(arquivo)
        except Exception as e:
          print(f"Erro abrir json: {e}")
    
        for obj in json_data:
            carta_obj = self.carrega_carta(obj)
            self.adicionar_carta(carta_obj)

    def __repr__(self):
        return f"ColecaoDeCartas(cartas={self.cartas})"
