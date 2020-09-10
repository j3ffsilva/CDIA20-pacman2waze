#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from labirinto import Labirinto
from agente import Agente

# Listagem-base

dimensao_da_matriz = 20
tam_celula = 20

# Cria o labirinto
lab = Labirinto(dimensao_da_matriz, tam_celula)
#lab.criar_labirinto()

# Cria o agente
tam_agente = 20
agente = Agente(0, tam_agente, "yellow")
agente.add_labirinto(lab)

print(agente._waze)
agente.add_percurso()
print(agente._waze)


agente.add_percurso()
print(agente._waze)


agente.add_percurso()
print(agente._waze)
