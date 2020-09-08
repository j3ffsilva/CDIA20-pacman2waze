#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from labirinto import Labirinto
from agente import Agente
from random import choice
from percursos import Waze
from celula import Celula

c = Celula(coord_matr=(0,0), tam_cel=10, dim=40)

print(c.coord_turtle())
