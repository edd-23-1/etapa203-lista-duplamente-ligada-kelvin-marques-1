# -*- coding:UTF-8 -*-

class No:
    def __init__(self, dado=None, prox=None, anterior=None):
        self.__dado = dado
        self.__prox = prox
        self.__anterior = anterior

    def __str__(self) -> str:
        return f"Dado: {self.__dado}"

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, valor):
        self.__dado = valor

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, valor):
        self.__prox = valor

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, valor):
        self.__anterior = valor
