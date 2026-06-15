from nodos import NodoLista


class Album:
    """O álbum da Copa, guardado como uma lista encadeada."""

    def __init__(self):
        self._cabeca = None        # primeiro nó do álbum
        self._tamanho = 0          # quantas figurinhas no álbum
        self._rep_cabeca = None    # primeira repetida (lista separada)
        self._rep_tamanho = 0      # quantas repetidas no total

    def buscar(self, id):
        """Procura uma figurinha pelo número. Retorna a figurinha ou None."""
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def adicionar(self, figurinha):
        """Adiciona no álbum. Se já existe, vai pra pilha de repetidas.
        Retorna True se entrou no álbum, False se era repetida."""
        if self.buscar(figurinha.id) is not None:
            self._adicionar_repetida(figurinha)
            return False

        novo = NodoLista(figurinha)
        if self._cabeca is None:
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1
        return True

    def remover(self, id):
        """Remove a figurinha pelo número. Retorna True se removeu."""
        if self._cabeca is None:
            return False

        if self._cabeca.figurinha.id == id:
            self._cabeca = self._cabeca.proximo
            self._tamanho -= 1
            return True

        anterior = self._cabeca
        atual = self._cabeca.proximo
        while atual is not None:
            if atual.figurinha.id == id:
                anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar(self):
        """Mostra todas as figurinhas do álbum."""
        if self._cabeca is None:
            print("Álbum vazio.")
            return
        atual = self._cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def porcentagem(self, total):
        """Calcula quanto do álbum já foi preenchido (0 a 100)."""
        if total <= 0:
            return 0.0
        return (self._tamanho / total) * 100

    def _adicionar_repetida(self, figurinha):
        """Guarda uma figurinha repetida no fim da lista de repetidas."""
        novo = NodoLista(figurinha)
        if self._rep_cabeca is None:
            self._rep_cabeca = novo
        else:
            atual = self._rep_cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._rep_tamanho += 1

    def listar_repetidas(self):
        """Mostra todas as figurinhas repetidas."""
        if self._rep_cabeca is None:
            print("Nenhuma figurinha repetida.")
            return
        atual = self._rep_cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def contar_repetidas(self):
        """Retorna quantas figurinhas repetidas existem."""
        return self._rep_tamanho