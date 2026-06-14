from nodos import NodoLista


class Album:
    """O álbum da Copa"""

    def __init__(self):
        self._cabeca = None   
        self._tamanho = 0     
    def buscar(self, id):
        """Procura uma figurinha pelo número. Retorna a figurinha ou não achou"""
        atual = self._cabeca         
        while atual is not None:      
            if atual.figurinha.id == id:
                return atual.figurinha  
            atual = atual.proximo    
        return None                   

    def adicionar(self, figurinha):
        """Adiciona uma figurinha no fim do álbum."""
        if self.buscar(figurinha.id) is not None:
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

    def listar(self):
        """Mostra todas as figurinhas do álbum."""
        if self._cabeca is None:
            print("Álbum vazio.")
            return
        atual = self._cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo
            
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
                return True
            anterior = atual          
            atual = atual.proximo     
        return False                  

    def porcentagem(self, total):
        """Calcula quanto do álbum já foi preenchido (0 a 100)."""
        if total <= 0:
            return 0.0
        return (self._tamanho / total) * 100