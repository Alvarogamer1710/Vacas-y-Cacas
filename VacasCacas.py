#!/usr/bin/env python3
# Juego de la vaca y el granjero
# Version mas sencilla y estilo estudiante

import random
import time

HIERBA = '"'
VACIO = ' '
CACA = 'O'
VACA = 'V'
TRACTOR = 'T'

def pedir_num(mensaje, minimo, maximo):
    ok = False
    while not ok:
        try:
            n = int(input(mensaje))
            if n < minimo or n > maximo:
                print('valor fuera de rango')
            else:
                ok = True
        except:
            print('tienes que poner un numero')
    return n

def crear_tablero(ancho, alto):
    t = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(HIERBA)
        t.append(fila)
    return t

def mostrar_tablero(tab, pos_vaca, pos_tractor):
    for y in range(len(tab)):
        linea = ''
        for x in range(len(tab[0])):
            if x == pos_vaca[0] and y == pos_vaca[1]:
                linea += VACA + ' '
            elif x == pos_tractor[0] and y == pos_tractor[1]:
                linea += TRACTOR + ' '
            else:
                linea += tab[y][x] + ' '
        print(linea)
    print()

def hay_hierba(tab):
    for f in tab:
        for c in f:
            if c == HIERBA:
                return True
    return False

dir = {
    1: (0,-1),
    2: (1,0),
    3: (0,1),
    4: (-1,0)
}

print('Juego de la vaca y el granjero')
ancho = pedir_num('ancho del terreno (2-30): ',2,30)
alto = pedir_num('alto del terreno (2-30): ',2,30)

print('posicion inicial de la vaca:')
vy = pedir_num('fila (0-{}): '.format(alto-1),0,alto-1)
vx = pedir_num('columna (0-{}): '.format(ancho-1),0,ancho-1)

vaca = [vx, vy]
tractor = [0,0]

tab = crear_tablero(ancho, alto)
tab[vaca[1]][vaca[0]] = VACIO

cacas = {}
turno = 0
movs_vaca = 0

print('empieza el juego...')

while hay_hierba(tab):
    turno += 1
    # mover vaca
    d = random.randint(1,4)
    dx, dy = dir[d]
    nx = vaca[0] + dx
    ny = vaca[1] + dy
    if nx>=0 and nx<ancho and ny>=0 and ny<alto:
        # guarda posicion anterior
        x_ant, y_ant = vaca[0], vaca[1]
        vaca = [nx,ny]
        if tab[ny][nx] == HIERBA:
            tab[ny][nx] = VACIO
        movs_vaca += 1
        # cada 5 movimientos deja caca en la celda anterior
        if movs_vaca % 5 == 0:
            tab[y_ant][x_ant] = CACA
            cacas[(x_ant,y_ant)] = turno

    # mover tractor (2 casillas)
    dt = random.randint(1,4)
    dxt, dyt = dir[dt]
    for i in range(2):
        ntx = tractor[0] + dxt
        nty = tractor[1] + dyt
        if ntx<0 or ntx>=ancho or nty<0 or nty>=alto:
            break
        if tab[nty][ntx] == CACA:
            tab[nty][ntx] = VACIO
            if (ntx,nty) in cacas:
                del cacas[(ntx,nty)]
            tractor = [ntx,nty]
            break
        else:
            tractor = [ntx,nty]

    # regenerar hierba despues de 7 turnos
    claves = list(cacas.keys())
    for p in claves:
        if turno - cacas[p] >= 7:
            if tab[p[1]][p[0]] == CACA:
                tab[p[1]][p[0]] = HIERBA
            del cacas[p]

    print('Turno', turno)
    mostrar_tablero(tab, vaca, tractor)
    time.sleep(random.randint(1,3))

print('La vaca ha limpiado toda la hierba! fin del juego')
