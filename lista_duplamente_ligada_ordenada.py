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
        pass


    # Retorna uma referência para o primeiro item da lista duplamente ligada
    # Caso a lista esteja vazia, retorna None
    def first(self) -> No:
        # implementação do método
        pass

    
    # Retorna uma referência para o último item da lista duplamente ligada
    # Caso a lista esteja vazia, retorna None
    def last(self) -> bool:
        # implementação do método
        pass


    # insere um elemento na lista duplamente ligada em ordem crescente em seguida retorna True
    # se a lista duplamente ligada estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor) -> bool:
        # implementação do método
        pass

    
    # remove um elemento da lista duplamente ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista duplamente ligada, retorne False
    # se a lista duplamente ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self, valor) -> bool:
        # implementação do método
        pass


    # retornar True caso o elemento esteja presente na lista duplamente ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        pass


    # retorna uma lista de string com valores dos elementos da lista duplamente ligada
    # imprima os elementos da lista duplamente ligada do primeiro para o último
    # caso a lista duplamente ligada esteja vazia, imprime uma mensagem informando
    # que a lista duplamente ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        # implementação do método
        pass
    

    # retorna a quantidade de elementos na lista duplamente ligada
    # se a lista duplamente ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        pass
