from fila import Fila


class Historico:
  
    def __init__(self):
        self._fila = Fila()   

    def registrar(self, descricao):
       
        self._fila.enqueue(descricao)

    def listar(self):
       
        if self._fila.esta_vazia():
            print("Nenhuma troca registrada ainda.")
            return
        atual = self._fila._inicio
        while atual is not None:
            print(atual.figurinha)   
            atual = atual.proximo