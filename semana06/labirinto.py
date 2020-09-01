#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import floor
from turtle import *
import numpy as np

# Acrescenta esta biblioteca ao labirinto
from celula import Celula

class Labirinto:

    def __init__(self, dim, tam_celula):
        """ Construtor do Labirinto """
        self._matriz = self.ler_matriz_fixa() # Carrega uma matriz fixa
        self._dim = dim # Atributo que armazena a dimensão da matriz
        self._tam_celula = tam_celula # Atributo que armazena o tamanho da célula

        self._turtle = Turtle() # A tartaruga que desenha o caminho do labirinto
        self._turtle.hideturtle() # Esconde a tartaruga

    def criar_celula(self, coord_matr=None, coord_turt=None):
        """ Cria uma célula com o tamanho de célula e dimensão de _matriz
            definidas como atributos na classe Labirinto
        """
        return Celula(coord_matr, coord_turt, self._tam_celula, self._dim)

    def ler_matriz_aleatoria(self, dim):
        """ Retorna uma matriz quadrada na dimensão especificada com números
        aleatórios (0's e 1's)
        """
        return np.random.randint(2, size=(dim,dim))

    def ler_matriz_fixa(self):
        """ Retorna uma matriz fixa """

        return  [[1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1],
                 [0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0],
                 [0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0],
                 [0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0],
                 [0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0],
                 [1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,1,1],
                 [1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0],
                 [1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0],
                 [1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1],
                 [1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1],
                 [1,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0],
                 [1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0],
                 [0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0],
                 [0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0],
                 [0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1],
                 [1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1],
                 [1,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0],
                 [1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,0],
                 [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    def criar_labirinto(self, p1=420, p2=420, p3=370, p4=0):
        """ Cria o gráfico do labirinto baseado nos valores da matriz """
        setup(p1, p2, p3, p4)

        # Para cada linha da matriz
        for lin in range(self._dim):
            # Para cada coluna da matriz
            for col in range(self._dim):
                # Testa se a coordenada da matriz (lin, col) é caminho (=1)
                if (self._matriz[lin][col] == 1):
                    # Em caso positivo, transforma em coordenada Turtle.
                    # Atenção: Numa coordenada Turtle (x,y), o eixo x refere-se à coluna e o eixo y à linha
                    # Numa coordenada da matriz (lin, col), o primeiro elemento é a linha e o segundo a coluna

                    celula = self.criar_celula(coord_matr=(lin, col))
                    # Pinta a celula na posição (x,y) com a cor especificada
                    self.desenhar_celula(celula, 'blue')

                    self.desenhar_pastilha(celula, 'white')

    def cel_aleatoria(self):
        """ Retorna os índices de uma posição que seja caminho
        """
        i, j = np.random.randint(self._dim, size=(2))
        while (not self.eh_caminho(i, j)):
            i, j = np.random.randint(self._dim, size=(2))

        celula = self.criar_celula(coord_matr=(i,j))
        return celula

    def desenhar_pastilha(self, celula, cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar a pastilha
        """
        x, y = celula.coord_turt_centralizada()
        self._turtle.up()
        self._turtle.goto(x, y)
        self._turtle.down()
        self._turtle.dot(3, cor)

    def eh_caminho(self, lin, col):
        """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
            False caso contrário.
            Por exemplo, na matriz a seguir:
            [[ 1  0  0 ]
             [ 0  1  0 ]
             [ 0  0  1 ]]
            a chamada de função 'eh_caminho(0,0)' retorna True e
            a chamada de função 'eh_caminho(0,1)' retorna False
        """
        return lin >= 0 and col >= 0 and                    \
               lin < self._dim and col < self._dim and      \
               self._matriz[lin][col] == 1

    def desenhar_celula(self, celula, cor):
        """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
        x, y = celula.coord_turtle()
        self._turtle.color(cor)
        self._turtle.up()
        self._turtle.goto(x,y)
        self._turtle.down()
        self._turtle.begin_fill()
        for _ in range(4):
            self._turtle.forward(self._tam_celula)
            self._turtle.left(90)
        self._turtle.end_fill()
        self._turtle.up()

    def obter_vizinhos(self, celula):
        """ Retorna os vizinhos de uma celula """
        lin, col = celula.coord_matriz()
        vizinhos = []

        if (self.eh_caminho(lin-1, col)):
            vz_cima = self.criar_celula(coord_matr=(lin-1, col))
            vizinhos.append(vz_cima)

        if (self.eh_caminho(lin, col-1)):
            vz_esquerdo = self.criar_celula(coord_matr=(lin, col-1))
            vizinhos.append(vz_esquerdo)

        if (self.eh_caminho(lin, col+1)):
            vz_direito = self.criar_celula(coord_matr=(lin, col+1))
            vizinhos.append(vz_direito)

        if (self.eh_caminho(lin+1, col)):
            vz_baixo = self.criar_celula(coord_matr=(lin+1, col))
            vizinhos.append(vz_baixo)

        return vizinhos
