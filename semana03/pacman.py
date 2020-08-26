#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

def ler_matriz():
    return [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]


def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    tracer(False)
    hideturtle()
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    matriz = ler_matriz()
    lado = 20
    tam_celula = 20
    dimensao_da_matriz = len(matriz)
    for lin in range(dimensao_da_matriz):
        for col in range(dimensao_da_matriz):
            if (matriz[lin][col] == 1):
                x, y = em_coord_turtle(lin, col, dimensao_da_matriz, tam_celula)
                desenhar_celula(x, y, 'blue', lado)
    update()

def desenhar_celula(x, y, cor, lado):
    """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
    color(cor)
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(lado)
        left(90)
    end_fill()
    up()

def em_coord_turtle(lin, col, dim, tam_celula):
    """ Dada uma coordenada da matriz (lin,col) transforma em coordenada Turtle """
    meio = dim // 2
    x = (col - meio) * tam_celula
    y = (meio - lin) * tam_celula
    return x, y

def main():
    criar_labirinto()
    done()
main()
