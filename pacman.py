#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

def ler_matriz():
    # IMPLEMENTE A LÓGICA A SEGUIR
    return # uma matriz fixa

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # IMPLEMENTE A LÓGICA A SEGUIR
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula

def desenhar_celula(xt, yt, cor):
    """ Dada uma coordenada (xt, yt) do Turtle, desenha um quadrado (célula) na posição """
    # IMPLEMENTE A LÓGICA ESPECIFICADA AQUI

def em_coord_turtle(xm, ym):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    # IMPLEMENTE A LÓGICA ESPECIFICADA AQUI
    return xt, yt

def main():
    criar_labirinto()
    done()

main()
