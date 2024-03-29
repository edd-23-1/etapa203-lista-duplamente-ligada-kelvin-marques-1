# -*- coding:UTF-8 -*-
from no import No

class ListaDuplamenteLigadaOrdenada:
    """
    Implementação de Lista Duplamente Ligada com Capacidade
    A lista a ser implementada deverá ser em ordem crescente
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__fim = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Lista Duplamente Ligada com capacidade: {capacidade}")


    # Retorna True se a lista duplamente ligada está vazia, False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
        return self.__qtdItens == 0

    
    # retorna True se a lista duplamente ligada está cheia, False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        if self.__capacidade is None:
            return False
        else:
            return self.__qtdItens == self.__capacidade


    # Retorna uma referência para o primeiro item da lista duplamente ligada
    # Caso a lista esteja vazia, retorna None
    def first(self) -> No:
        # implementação do método
        if self.__inicio is None:
            return None
        else:
            return self.__inicio

    
    # Retorna uma referência para o último item da lista duplamente ligada
    # Caso a lista esteja vazia, retorna None
    def last(self) -> bool:
        # implementação do método
        if self.__fim is None:
            return None
        else:
            return self.__fim


    # insere um elemento na lista duplamente ligada em ordem crescente em seguida retorna True
    # se a lista duplamente ligada estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor) -> bool:
        # implementação do método
        if self.is_full():
            raise Exception("Lista duplamente ligada ordenada cheia")

        novoNo = No(valor)

        # Caso a lista esteja vazia, o novoNo será o início e o fim da lista
        if self.is_empty():
            self.__inicio = novoNo
            self.__fim = novoNo
        else:
            # Inserir o novoNo em ordem crescente na lista
            noAtual = self.__inicio

            while noAtual is not None and valor > noAtual.dado:
                noAtual = noAtual.prox

            # Inserir o novoNo antes de noAtual
            if noAtual is None:
                novoNo.anterior = self.__fim
                self.__fim.prox = novoNo
                self.__fim = novoNo
            elif noAtual == self.__inicio:
                novoNo.prox = self.__inicio
                self.__inicio.anterior = novoNo
                self.__inicio = novoNo
            else:
                novoNo.anterior = noAtual.anterior
                novoNo.prox = noAtual
                noAtual.anterior.prox = novoNo
                noAtual.anterior = novoNo

        self.__qtdItens += 1
        return True

    
    # remove um elemento da lista duplamente ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista duplamente ligada, retorne False
    # se a lista duplamente ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self, valor) -> bool:
        # implementação do método
        if self.is_empty():
            raise Exception("Lista duplamente ligada ordenada vazia")

        noAtual = self.__inicio

        while noAtual is not None:
            if noAtual.dado == valor:
                # Remover o nó atual
                if noAtual == self.__inicio and noAtual == self.__fim:
                    # Caso o nó seja o único nó na lista
                    self.__inicio = None
                    self.__fim = None
                elif noAtual == self.__inicio:
                    # Caso o nó seja o primeiro nó da lista
                    self.__inicio = noAtual.prox
                    self.__inicio.anterior = None
                elif noAtual == self.__fim:
                    # Caso o nó seja o último nó da lista
                    self.__fim = noAtual.anterior
                    self.__fim.prox = None
                else:
                    # Caso o nó esteja no meio da lista
                    noAtual.anterior.prox = noAtual.prox
                    noAtual.prox.anterior = noAtual.anterior

                self.__qtdItens -= 1
                return True
            
            noAtual = noAtual.prox

        return False


    # retornar True caso o elemento esteja presente na lista duplamente ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        noAtual = self.__inicio

        while noAtual is not None:
            if noAtual.dado == valor:
                return True
            noAtual = noAtual.prox

        return False


    # retorna uma lista de string com valores dos elementos da lista duplamente ligada
    # imprima os elementos da lista duplamente ligada do primeiro para o último
    # caso a lista duplamente ligada esteja vazia, imprime uma mensagem informando
    # que a lista duplamente ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        if self.is_empty():
            print("A lista duplamente ligada ordenada está vazia.")
            return []

        values = []
        noAtual = self.__inicio

        while noAtual is not None:
            values.append(noAtual.dado)
            noAtual = noAtual.prox
            
        return values
    

    # retorna a quantidade de elementos na lista duplamente ligada
    # se a lista duplamente ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        return self.__qtdItens
