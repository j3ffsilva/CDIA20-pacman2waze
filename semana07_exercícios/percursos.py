#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celula import Celula

class Waze:

    def __init__(self, labirinto):
        """ Construtor. Inicializa o objeto com uma referência ao labirinto,
            uma lista de coordenadas a ser seguida pelo agente, e um atributo
            que indica se o percurso já foi finalizado.
        """
        self.labirinto = labirinto
        self.lst_coord = []
        self.finalizado = None

    def obter_prox_coord(self):
        """ Retorna a próxima coordenada ao agente """
        if (len(self.lst_coord) > 0):
            item = self.lst_coord.pop(0)
            # Caso a lista fique vazia após a retirada (pop) do elemento,
            # significa que o percurso acabou
            if (len(self.lst_coord) == 0):
                self.finalizado = True
            return item
        return

    def fim_percurso(self):
        """ Mostra se o percurso está finalizado (True ou False) """
        return self.finalizado == True

    def esta_sem_coord(self):
        """ Mostra se a lista de coordenadas está vazia (True ou False) """
        return len(self.lst_coord) == 0

    def gerar_percurso(self, celula):
        """ Gera um percurso no labirinto a partir de uma determinada célula """
        lab = self.labirinto # Para melhorar a legibilidade
        visitadas = [] # Indica quais células já foram visitadas
        # lst_coord: indica as coordenadas que o agente deve seguir para
        #            percorrer todo o labirinto
        lst_coord = []

        # Algoritmo de busca em profundidade
        self.__dfs(celula, visitadas, lst_coord)

        self.lst_coord = lst_coord

        # Logo após ter gerado o percurso, o agente ainda não o percorreu.
        # Por esta razão, este atributo é inicializado como False
        self.finalizado = False

    def __dfs(self, celula, visitadas, lst_coord):
        """ Implementação do algoritmo de busca em profundidade """
        if (celula in visitadas):
            return
        lst_coord.append(celula)
        visitadas.append(celula)

        lab = self.labirinto # Para melhorar a legibilidade
        vizinhas = lab.obter_vizinhos(celula)
        for cel_vizinha in vizinhas:
            if (cel_vizinha not in visitadas):
                self.__dfs(cel_vizinha, visitadas, lst_coord)
                lst_coord.append(celula)
