#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

def ler_matriz():
    return [[1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0],\
            [1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1],\
            [1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1],\
            [1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0],\
            [0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0],\
            [0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],\
            [0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1],\
            [0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1],\
            [0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1],\
            [0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1],\
            [0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],\
            [1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0],\
            [1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0],\
            [0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1],\
            [0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1],\
            [0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1],\
            [1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1],\
            [1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,1],\
            [1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0],\
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    tracer(False)
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    matriz = ler_matriz()
    for lin in range(len(matriz)):
        for col in range(len(matriz)):
            if (matriz[lin][col] > 0):
                xt, yt = em_coord_turtle(lin, col)
                desenhar_celula(xt, yt, 'blue')

def desenhar_celula(xt, yt, cor):
    """ Dada uma coordenada do Turtle, desenha um quadrado (célula) na posição """
    color(cor)
    up()
    goto(xt, yt)
    down()
    begin_fill()
    for _ in range(4):
        forward(20)
        left(90)
    end_fill()
    up()

def em_coord_turtle(xm, ym):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    meio_y = 20 // 2
    yt = (ym - meio_y) * 20
    meio_x = (20 - 1) // 2
    xt = (meio_x - xm) * 20
    return xt, yt

def main():
    criar_labirinto()
    done()

main()
