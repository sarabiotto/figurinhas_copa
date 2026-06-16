from nodos import NodoLista


class Album:


    def __init__(self):
        self._cabeca = None        
        self._tamanho = 0          
        self._rep_cabeca = None    
        self._rep_tamanho = 0      

    def buscar(self, id):

        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def adicionar(self, figurinha):

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

        if self._cabeca is None:
            print("Álbum vazio.")
            return
        atual = self._cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def porcentagem(self, total):

        if total <= 0:
            return 0.0
        return (self._tamanho / total) * 100

    def _adicionar_repetida(self, figurinha):

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

        if self._rep_cabeca is None:
            print("Nenhuma figurinha repetida.")
            return
        atual = self._rep_cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def contar_repetidas(self):

        return self._rep_tamanho

    def buscar_por_jogador(self, nome):

        resultado_cabeca = None
        resultado_fim = None

        atual = self._cabeca
        while atual is not None:
            if nome.lower() in atual.figurinha.nome.lower():
                novo = NodoLista(atual.figurinha)
                if resultado_cabeca is None:
                    resultado_cabeca = novo
                    resultado_fim = novo
                else:
                    resultado_fim.proximo = novo
                    resultado_fim = novo
            atual = atual.proximo

        return resultado_cabeca

    def buscar_por_selecao(self, pais):

        resultado_cabeca = None
        resultado_fim = None

        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                novo = NodoLista(atual.figurinha)
                if resultado_cabeca is None:
                    resultado_cabeca = novo
                    resultado_fim = novo
                else:
                    resultado_fim.proximo = novo
                    resultado_fim = novo
            atual = atual.proximo

        return resultado_cabeca

    def tem_repetida(self, id):

        atual = self._rep_cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return True
            atual = atual.proximo
        return False

    def remover_repetida(self, id):

        if self._rep_cabeca is None:
            return None

        if self._rep_cabeca.figurinha.id == id:
            no = self._rep_cabeca
            self._rep_cabeca = self._rep_cabeca.proximo
            self._rep_tamanho -= 1
            return no.figurinha

        anterior = self._rep_cabeca
        atual = self._rep_cabeca.proximo
        while atual is not None:
            if atual.figurinha.id == id:
                anterior.proximo = atual.proximo
                self._rep_tamanho -= 1
                return atual.figurinha
            anterior = atual
            atual = atual.proximo
        return None


def imprimir_lista(cabeca):

    if cabeca is None:
        print("Nenhuma figurinha encontrada.")
        return
    atual = cabeca
    while atual is not None:
        print(atual.figurinha)
        atual = atual.proximo