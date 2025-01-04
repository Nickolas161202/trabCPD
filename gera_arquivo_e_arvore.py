import json
import struct
import pickle

class NoBPlus:
    def __init__(self, grau, is_folha=True):
        self.grau = grau              # Grau mínimo do nó
        self.is_folha = is_folha      # Indica se o nó é folha
        self.chaves = []              # Lista de chaves
        self.ponteiros = []           # Ponteiros para dados ou nós filhos
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
            no_atual = no_atual.ponteiros[i]

        # Buscar a chave no nó folha
        if chave in no_atual.chaves:
            return no_atual.ponteiros[no_atual.chaves.index(chave)]
        return None

    def inserir(self, chave, ponteiro):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.grau) - 1:
            nova_raiz = NoBPlus(self.grau, is_folha=False)
            nova_raiz.ponteiros.append(self.raiz)
            self._dividir_no(nova_raiz, 0, self.raiz)
            self.raiz = nova_raiz

        self._inserir_nao_cheio(self.raiz, chave, ponteiro)

    def _inserir_nao_cheio(self, no, chave, ponteiro):
        if no.is_folha:
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            no.chaves.insert(i + 1, chave)
            no.ponteiros.insert(i + 1, ponteiro)
        else:
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.ponteiros[i].chaves) == (2 * self.grau) - 1:
                self._dividir_no(no, i, no.ponteiros[i])
                if chave > no.chaves[i]:
                    i += 1
            self._inserir_nao_cheio(no.ponteiros[i], chave, ponteiro)

    def _dividir_no(self, pai, indice, no):
        grau = self.grau
        novo_no = NoBPlus(grau, is_folha=no.is_folha)
        pai.chaves.insert(indice, no.chaves[grau - 1])
        pai.ponteiros.insert(indice + 1, novo_no)

        novo_no.chaves = no.chaves[grau:]
        no.chaves = no.chaves[:grau - 1]

        if not no.is_folha:
            novo_no.ponteiros = no.ponteiros[grau:]
            no.ponteiros = no.ponteiros[:grau]
        else:
            novo_no.proximo = no.proximo
            no.proximo = novo_no

class carta:
    def __init__(self,associated_card_refs,game_absolute_path,region_refs,attack,cost,health,description_raw,levelup_description_raw,artist_name,name,card_code,
                 keyword_refs,spell_speed_ref,rarity_ref,subtypes,supertype,card_type,card_set,formats):
        self.associated_card_refs = associated_card_refs
        self.game_absolute_path = game_absolute_path
        self.region_refs = region_refs
        self.attack = attack
        self.cost = cost
        self.health = health
        self.description_raw = description_raw
        self.levelup_description_raw = levelup_description_raw
        self.artist_name = artist_name
        self.name = name
        self.card_code = card_code
        self.keyword_refs = keyword_refs
        self.spell_speed_ref = spell_speed_ref
        self.rarity_ref = rarity_ref
        self.subtypes = subtypes
        self.supertype = supertype
        self.card_type = card_type
        self.card_set = card_set
        self.formats = formats

    def gera_carta(json_data):

      return carta(
        associated_card_refs=json_data.get("associatedCardRefs", []),
        game_absolute_path=json_data["assets"][0]["gameAbsolutePath"] if json_data.get("assets") else "",
        region_refs=json_data.get("regionRefs", []),
        attack=json_data.get("attack", 0),
        cost=json_data.get("cost", 0),
        health=json_data.get("health", 0),
        description_raw=json_data.get("descriptionRaw", ""),
        levelup_description_raw=json_data.get("levelupDescriptionRaw", ""),
        artist_name=json_data.get("artistName", ""),
        name=json_data.get("name", ""),
        card_code=json_data.get("cardCode", ""),
        keyword_refs=json_data.get("keywordRefs", []),
        spell_speed_ref=json_data.get("spellSpeedRef", ""),
        rarity_ref=json_data.get("rarityRef", ""),
        subtypes=json_data.get("subtypes", []),
        supertype=json_data.get("supertype", ""),
        card_type=json_data.get("type", ""),
        card_set=json_data.get("set", ""),
        formats=json_data.get("formats", [])
    )

    def print_carta(self):
        print(f"Nome: {self.name}")
        print(f"Descrição: {self.description_raw}")
        print(f"Ataque: {self.attack}")
        print(f"Custo: {self.cost}")
        print(f"Saúde: {self.health}")
        print(f"Artista: {self.artist_name}")
        print(f"Raridade: {self.rarity_ref}")
        print(f"Código da Carta: {self.card_code}")
        print(f"Tipos: {', '.join(self.subtypes)}")
        print(f"Formato(s): {', '.join(self.formats)}")

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

def salva_cartas_com_indice(arquivo_binario, colecao_cartas, arvore_b_plus):
    with open(arquivo_binario, 'wb') as f:
        for carta_obj in colecao_cartas.retorna_colecao():
            # Serializa a carta
            dados_serializados = pickle.dumps(carta_obj)
            # Escreve os dados no arquivo
            posicao_atual = f.tell()
            f.write(dados_serializados)

            # Insere a chave (card_code) e a posição no índice (árvore B+)
            arvore_b_plus.inserir(carta_obj.card_code, posicao_atual)

def carrega_carta_por_indice(arquivo_binario, arvore_b_plus, card_code):
    posicao = arvore_b_plus.buscar(card_code)
    if posicao is not None:
        with open(arquivo_binario, 'rb') as f:
            f.seek(posicao)  # Vai até a posição onde o dado da carta está armazenado
            dados_serializados = f.read()
            carta_obj = pickle.loads(dados_serializados)
            return carta_obj
    return None

colecao = ColecaoDeCartas()
arvore_b_plus = ArvoreBPlus(grau=3)

caminho_arquivo = '/content/exj.json'

with open(caminho_arquivo, 'r') as arquivo:
    json_data = json.load(arquivo)

for obj in json_data:
    carta_obj = carta.gera_carta(obj)
    colecao.adicionar_carta(carta_obj)

arquivo_binario = "colecao_cartas_com_indice.bin"

salva_cartas_com_indice(arquivo_binario, colecao, arvore_b_plus)

card_code_procurado = "01IO028T1"
carta_encontrada = carrega_carta_por_indice(arquivo_binario, arvore_b_plus, card_code_procurado)

carta_encontrada.print_carta()
