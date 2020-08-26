#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import floor
from turtle import *
import numpy as np


""" Funções já implementadas """

def ler_matriz_fixa():
    """ Retorna uma matriz fixa """
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
    """ Cria o gráfico do labirinto baseado nos valores da matriz """
    tracer(False)
    hideturtle()
    bgcolor('black')
    setup(p1, p2, p3, p4)

    # Para cada linha da matriz
    for lin in range(dim):
        # Para cada coluna da matriz
        for col in range(dim):
            # Testa se a coordenada da matriz (lin, col) é caminho (=1)
            if (matriz[lin][col] == 1):
                # Em caso positivo, transforma em coordenada Turtle.
                # Atenção: Numa coordenada Turtle (x,y), o eixo x refere-se à coluna e o eixo y à linha
                # Numa coordenada da matriz (lin, col), o primeiro elemento é a linha e o segundo a coluna
                x, y = em_coord_turtle(lin, col)
                # Pinta a celula na posição (x,y) com a cor especificada
                desenhar_celula(x, y, 'blue')

                desenhar_pastilha(x, y, 'white')

    # Mostra as transformações na tela.
    # Necessário porque o Tracer() está desligado
    update()

def desenhar_celula(x, y, cor):
    """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
    color(cor)
    up()
    goto(x,y)
    down()
    begin_fill()
    for _ in range(4):
        forward(tam_celula)
        left(90)
    end_fill()
    up()

""" Funções de testes """

def teste1_transf_coord_funcionou():
    """ Testa as transformações de coordenadas """
    for lin in range(dim):
        for col in range(dim):
            x, y = em_coord_turtle(lin, col)
            if ( not (lin, col) == em_coord_matriz(x, y) ):
                return False
    return True

def teste2_transf_coord_funcionou():
    """ Testa as transformações de coordenadas """
    meio = dim // 2
    tam_celula = 20
    n = meio * tam_celula * 10
    for k1 in range(-n, n, 10):
        for k2 in range(n, -n, -10):
            x = k1 / 10
            y = k2 / 10
            lin, col = em_coord_matriz(x, y)
            if (not chao_da_celula(x, y) == em_coord_turtle(lin, col) ):
                return False
    return True

def testar_transf_de_coord():
    """ Roda os testes de transformações de coordenadas """
    if (teste1_transf_coord_funcionou() and \
        teste2_transf_coord_funcionou()):
        return "Todas as transformações de coordenadas funcionaram"
    else:
        return "As transformações de coordenadas não funcionaram"


""" Funções auxiliares """

def uso_do_floor():
    """ Função de exemplo do uso do floor (chao_da_celula) """
    for i in range(-200,200):
        print("{}\t{}".format(i, int(floor(i, 20)) ))

def chao_da_celula(x, y):
    """ Dadas coordenadas do Turtle (x,y), retorna as coordenadas do início de uma célula.
        Por exemplo, na celula da origem com tamanho 20, a coordenada Turtle (10,10)
        representa o meio da célula. A chamada de função 'chao_da_celula(10, 10)' retorna
        as coordenadas de início dessa célula (0,0)
        Dica: para entender, veja o exemplo da função: 'uso_do_floor()''
    """
    chao_x = int(floor(x, tam_celula))
    chao_y = int(floor(y, tam_celula))
    return chao_x, chao_y

def em_coord_turtle(lin, col):
    """ Dados os índices da matriz (lin, col), retorna as coordenadas do Turtle correspondentes.
        Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
        a chamada de função 'em_coord_turtle(0,0)' deve retornar (-200,200) e a
        chamada de função 'em_coord_turtle(10,10)' deve retornar (0,0)
    """
    meio = dim // 2
    x = (col - meio) * tam_celula
    y = (meio - lin) * tam_celula
    return x, y

def em_coord_matriz(x, y):
    """ Dada uma coordenada do Turtle (x,y), retorna os índices correspondentes da matriz
        Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
        a chamada de função 'em_coord_matriz(-200, 200)' deve retornar (0,0) e a
        chamada de função 'em_coord_matriz(0, 0)' deve retornar (10,10).
        Dica: utilize a função 'chao_da_celula(x, y)'
    """
    x, y = chao_da_celula(x, y)
    meio = dim // 2
    lin = int(meio - (y / tam_celula))
    col = int(meio + (x / tam_celula))
    return lin, col


def adicionar_agente():
    """ Desenha o agente no labirinto """
    lin, col = cel_aleatoria()
    x, y = em_coord_turtle(lin, col)
    desenhar_agente(x, y, 'yellow')


def ler_matriz_aleatoria(dim):
    """ Retorna uma matriz quadrada na dimensão especificada com números
        aleatórios (0's e 1's)
        Dica: utilize numpy.random.randint()
    """
    return np.random.randint(2,size=(dim,dim))

def cel_aleatoria():
    """ Retorna os índices de uma posição que contenha 1
        Por exemplo, na matriz a seguir:
        [[ 1  0  0 ]
         [ 0  1  0 ]
         [ 0  0  1 ]]
        Somente os elementos da diagonal principal [(0,0), (1,1), (2,2)]
        poderiam ser retornados
        Dica: utilize numpy.random.randint()
    """
    i, j = np.random.randint(dim, size=(2))
    while (not eh_caminho(i, j)):
        i, j = np.random.randint(dim, size=(2))
    return i, j

def eh_caminho(lin, col):
    """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
        False caso contrário.
        Por exemplo, na matriz a seguir:
        [[ 1  0  0 ]
         [ 0  1  0 ]
         [ 0  0  1 ]]
        a chamada de função 'eh_caminho(0,0)' retorna True e
        a chamada de função 'eh_caminho(0,1)' retorna False
    """
    return matriz[lin][col] == 1

def desenhar_agente(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar o agente (i.e., pacman, fantasmas)
    """
    c = tam_celula // 2
    up()
    goto(x + c,y + c)
    down()
    dot(tam_agente, cor)

def desenhar_pastilha(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar a pastilha
    """
    c = tam_celula // 2
    up()
    goto(x + c,y + c)
    down()
    dot(3, cor)

#matriz = ler_matriz_fixa()
matriz = ler_matriz_aleatoria(20)
dim = len(matriz)
tam_celula = dim
tam_agente = dim


def main():

    criar_labirinto()
    adicionar_agente()
    done()

    # Utilize esse comando para testar se as trasnformações das coordenadas
    # estão funcionando. Ao final da execução, o resultado deve ser que todas as transformações funcionaram
    print(testar_transf_de_coord())

main()
