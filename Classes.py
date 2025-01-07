import pickle
import json
import os
class Filenames:
    def __init__(self):
        self.cards = "cartas.pkl"
        self.nomes = "arvore_nomes.pkl"
        self.codes = "arvore_codes.pkl"

    def __repr__(self):
        return f"Filenames(cards={self.cards}, nomes={self.nomes}, codes={self.codes})"

class TrieNode:
    def __init__(self):
        self.children = {}  # Armazena os filhos do nó (cada filho é um caractere)
        self.posicoes = []  # Lista de posições dos dados no arquivo


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Raiz da Trie

    def inserir(self, palavra, posicao):
        no_atual = self.root
        for char in palavra:
            if char not in no_atual.children:
                no_atual.children[char] = TrieNode()
            no_atual = no_atual.children[char]
        no_atual.posicoes.append(posicao)

    def buscar(trie, palavra):
        no_atual: TrieNode = trie.root
        for char in palavra:
            if char not in no_atual.children:
                return None  # Se a palavra não for encontrada
            no_atual = no_atual.children[char]
        return no_atual.posicoes  # Retorna as posições encontradas

    def salva_arvore_trie(self, arquivo_binario):
        with open(arquivo_binario, 'wb') as f:
            pickle.dump(self, f)

    def carrega_arvore_trie(self, arquivo_binario):
        loaded_Trie = Trie()
        with open(arquivo_binario, 'rb') as f:
            # Load the saved Trie object
            loaded_trie = pickle.load(f)
            # Update the current Trie's root with the loaded Trie's root
            self.root = loaded_trie.root

    def __str__(self):
        return f"Trie(root={self.root})"


class Card:
    def __init__(
        self,
        name: str = "",
        regions: list = None,
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

    def carrega_carta(self, dados_json):
        self.name = dados_json.get('name')
        self.regions = dados_json.get('regions', [])
        self.cost = dados_json.get('cost', 0)
        self.attack = dados_json.get('attack', 0)
        self.health = dados_json.get('health', 0)
        self.description_raw = dados_json.get('descriptionRaw', '')
        self.levelup_description_raw = dados_json.get('levelupDescriptionRaw', '')
        self.keywords = dados_json.get('keywords', [])
        self.artist = dados_json.get('artistName', '')
        self.spell_speed = dados_json.get('spellSpeed', '')
        self.game_absolute_path = (
            dados_json['assets'][0].get('gameAbsolutePath', '')
            if 'assets' in dados_json and len(dados_json['assets']) > 0
            else ''
        )
        self.rarity = dados_json.get('rarity', '')
        self.expansion = dados_json.get('set', '')
        self.card_type = dados_json.get('type', '')
        self.subtypes = dados_json.get('subtypes', [])
        self.supertype = dados_json.get('supertype', '')
        self.flavor_text = dados_json.get('flavorText', '')
        self.card_code = dados_json.get('cardCode', '')
        self.associated_cards = dados_json.get('associatedCardRefs', [])

    def __repr__(self):
        return (
            f"Carta(\n Name = {self.name!r},\n Regions = {self.regions!r},\n Cost = {self.cost},\n "
            f"Attack=  {self.attack},\n Health = {self.health},\n Description = {self.description_raw!r},\n "
            f"Level Up = {self.levelup_description_raw!r},\n Keywords = {self.keywords!r},\n "
            f"Artist = {self.artist!r},\n Spell Speed = {self.spell_speed!r},\n Image Link = {self.game_absolute_path!r},\n "
            f"Rarity = {self.rarity!r},\n Expansion = {self.expansion!r},\n Card Type = {self.card_type!r},\n Subtypes = {self.subtypes!r},\n "
            f"Supertype = {self.supertype!r},\n Flavor Text = {self.flavor_text!r},\n Card Code = {self.card_code!r},\n "
            f"Associated Cards = {self.associated_cards!r}\n)"
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

    def salva_cartas_com_indice(self, arquivo_binario, arvore_nome, arvore_code):
        try:
            with open(arquivo_binario, 'wb') as f:
                for carta_obj in self.retorna_colecao():
                    dados_serializados = pickle.dumps(carta_obj)
                    posicao_atual = f.tell()  # Captura a posição onde o dado será armazenado
                    f.write(dados_serializados)

                    # Insere o índice (chave) no índice B+ para código
                    arvore_code.inserir(carta_obj.card_code, posicao_atual)

                    # Insere o índice (chave) na Trie para nome
                    arvore_nome.inserir(carta_obj.name, posicao_atual)
        except Exception as e:
            print(f"Erro ao salvar cartas com índice: {e}")

    def carrega_carta_Indexada(filenames, parametro, nome_ou_codigo):
        arvore_trie = Trie()
        # Se a busca for pelo nome, usamos a Trie
        if nome_ou_codigo == "nome":
            arvore_trie.carrega_arvore_trie(filenames.nomes)
        elif nome_ou_codigo == "codigo":
            arvore_trie.carrega_arvore_trie(filenames.codes)
        posicao_no_arquivo = arvore_trie.buscar(parametro)
        print(posicao_no_arquivo)
        nova_colecao = ColecaoDeCartas()


        if posicao_no_arquivo is None:
            # Se a carta não for encontrada no índice, retorna None
            print(f"Carta com {nome_ou_codigo} '{parametro}' não encontrada no índice.")
            print(f"Carta com {nome_ou_codigo} '{parametro}' não encontrada no índice.")
            return None

        # Se houver várias posições para a chave, percorre todas
        if isinstance(posicao_no_arquivo, list):  # Caso seja uma lista de posições
            for posicao in posicao_no_arquivo:
                with open(filenames.cards, 'rb') as f:
                    f.seek(posicao)  # Vai até a posição onde o dado da carta está armazenado
                    dados_serializados = f.read()
                    carta_obj = pickle.loads(dados_serializados)
                    nova_colecao.adicionar_carta(carta_obj)
        else:
            # Se houver apenas uma posição, carrega a carta diretamente
            with open(filenames.cards, 'rb') as f:
                f.seek(posicao_no_arquivo)  # Vai até a posição
                dados_serializados = f.read()
                carta_obj = pickle.loads(dados_serializados)
                nova_colecao.adicionar_carta(carta_obj)

        # Se houver várias posições para a chave, percorre todas
        if isinstance(posicao_no_arquivo, list):  # Caso seja uma lista de posições
            for posicao in posicao_no_arquivo:
                with open(filenames.cards, 'rb') as f:
                    f.seek(posicao)  # Vai até a posição onde o dado da carta está armazenado
                    dados_serializados = f.read()
                    carta_obj = pickle.loads(dados_serializados)
                    nova_colecao.adicionar_carta(carta_obj)
        else:
            # Se houver apenas uma posição, carrega a carta diretamente
            with open(filenames.cards, 'rb') as f:
                f.seek(posicao_no_arquivo)  # Vai até a posição
                dados_serializados = f.read()
                carta_obj = pickle.loads(dados_serializados)
                nova_colecao.adicionar_carta(carta_obj)

        return nova_colecao

    def le_arquivo_json(self, arquivo):
      try:
          with open(arquivo, 'r', encoding="utf-8") as f:
              json_data = json.load(f)
      except Exception as e:
          print(f"Erro ao abrir JSON: {e}")
          return None

      for obj in json_data:
          carta_obj = Card()
          carta_obj.carrega_carta(obj)
          self.adicionar_carta(carta_obj)



    def __str__(self):
        print("Coleção de Cartas:\n")
        for carta in self.cartas:
            print(carta)
        return ""

    def le_pasta_json(self,pasta):
      try:
        arquivos = [f for f in os.listdir(pasta) if f.endswith('.json')]

        if not arquivos:
          print("Nenhum arquivo encontrado!")
          return
        
        for arq in arquivos:
          caminho_arq = os.path.join(pasta, arq)
          print(f"Lendo arquivo: {caminho_arq}")
          self.le_arquivo_json(caminho_arq)
      except Exception as e:
        print(f"Erro ao abrir pasta: {e}")
