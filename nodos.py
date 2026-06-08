class NodoLista:
    """Um elo da lista encadeada do álbum."""

    def __init__(self, figurinha):
        self.figurinha = figurinha   
        self.proximo = None         

class NodoFila:
    """Um elo das filas (trocas e histórico)."""

    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None