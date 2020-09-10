#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

# add as seguintes bibliotecas
from percursos import Waze

class Agente:

    # inclui cor e tartaruta pro agente
    def __init__(self, id, tam_agente, cor=None):
        # add uma identificação única pro agente
        self._id = id
        self._tam_agente = tam_agente

        # add uma tartaruga específica pro agente
        self._turtle = Turtle()
        self._turtle.hideturtle()

        # define a cor do agente
        self._cor = cor
        # é um gerador de percursos
        self._waze = None

    # adiciona um labirinto
    def add_labirinto(self, lab):
        self._labirinto = lab
        self._posicao = lab.cel_aleatoria()

    # Note que o nome do método mudou um pouco
    def desenhar_se(self, posicao=None):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar o agente (i.e., pacman, fantasmas)
        """
        self._turtle.clear()
        if (not posicao):
            posicao = self._posicao

        x, y = posicao.coord_turt_centralizada()
        self._turtle.up()
        self._turtle.goto(x , y)
        self._turtle.down()
        self._turtle.dot(self._tam_agente, self._cor)

    """ Métodos de percurso """

    def add_percurso(self):
        # Só na primeira vez que o agente não terá um _waze definido
        if (not self._waze):
            self._waze = Waze(self._labirinto) # Cria o objeto _waze passando uma referência do labirinto

    def percorrer(self):
        """ Percorrer significa seguir passar por todas as celulas do labirinto """
        pos_agente = self._posicao # Para melhorar a legibilidade

        self.add_percurso()
        if (self._waze.fim_percurso()): # Questiona se é fim de percurso
            self._waze = None # Se o percurso terminou, reinicializa o _waze
            return True # Se terminou, retorna indicando o término

        if (self._waze.esta_sem_coord()): # Se _waze está criado, mas sem coordenadas
            self._waze.gerar_percurso(pos_agente) # Gere um percurso

        if (not self._waze.esta_sem_coord()): # Se houver coordenadas a serem seguidas
            self._posicao = self._waze.obter_prox_coord() # Obtenha a próx e defina como a posição do agente
            self._labirinto.desenhar_celula(self._posicao, 'red')
            self.desenhar_se() # Desenha o agente na posição em que se encontra

        return False # Se chegou até aqui é o porque não terminou o percurso e retorna False
