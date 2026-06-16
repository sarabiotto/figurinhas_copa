from nodos import NodoFila


class Fila:
    

    def __init__(self):
        self._inicio = None    
        self._fim = None       
        self._tamanho = 0

    def esta_vazia(self):
        return self._inicio is None

    def enqueue(self, figurinha):
       
        novo = NodoFila(figurinha)
        if self._fim is None:          
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo   l
            self._fim = novo           
        self._tamanho += 1

    def dequeue(self):
        
        if self._inicio is None:
            return None
        no = self._inicio
        self._inicio = self._inicio.proximo
        if self._inicio is None:       m
            self._fim = None
        self._tamanho -= 1
        return no.figurinha

    def peek(self):
        
        if self._inicio is None:
            return None
        return self._inicio.figurinha

    def limpar(self):
      
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def tamanho(self):
        return self._tamanho

    def listar(self):
      
        if self._inicio is None:
            print("Fila vazia.")
            return
        atual = self._inicio
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo