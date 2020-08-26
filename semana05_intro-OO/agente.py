#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

def desenhar_agente(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar o agente (i.e., pacman, fantasmas)
    """
    c = tam_celula // 2
    up()
    goto(x + c,y + c)
    down()
    dot(tam_agente, cor)
