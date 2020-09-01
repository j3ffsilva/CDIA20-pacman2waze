#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from agente import Agente
from labirinto import Labirinto
from turtle import *
from time import sleep

def main():
    tracer(False)
    hideturtle()
    bgcolor('black')

    dimensao_da_matriz = 20
    tam_celula = 20

    # Cria o labirinto
    lab = Labirinto(dimensao_da_matriz, tam_celula)
    lab.criar_labirinto()

    # Cria o agente
    tam_agente = 20
    agente = Agente(0, tam_agente, "yellow")
    agente.add_labirinto(lab)
    agente.desenhar_se()

    terminou_percurso = False
    intervalo_entre_frames = 0.1
    while (not terminou_percurso):
        terminou_percurso = agente.percorrer()
        # Atualiza o turtle e finaliza
        update()
        sleep(intervalo_entre_frames)
    done()

main()
