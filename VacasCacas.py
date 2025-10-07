import random
import time
import sys


# -----------------------------------------
# Clase Terreno
# -----------------------------------------
class Terreno:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.celdas = []
        for _ in range(alto):
            fila = []
            for _ in range(ancho):
                fila.append('"')  # hierba inicial
            self.celdas.append(fila)

    def dentro(self, fila, col):
        return fila >= 0 and fila < self.alto and col >= 0 and col < self.ancho

    def get(self, fila, col):
        return self.celdas[fila][col]

    def set(self, fila, col, valor):
        self.celdas[fila][col] = valor

    def hay_hierba(self):
        for r in range(self.alto):
            for c in range(self.ancho):
                if self.celdas[r][c] == '"':
                    return True
        return False

    def imprimir(self, vaca_f, vaca_c, tract_f, tract_c, turno):
        print("\n======== TURNO", turno, "========")
        for r in range(self.alto):
            linea = ""
            for c in range(self.ancho):
                if r == vaca_f and c == vaca_c:
                    linea += "V"
                elif r == tract_f and c == tract_c:
                    linea += "T"
                else:
                    linea += self.celdas[r][c]
            print(linea)
        print("===============================")


# -----------------------------------------
# Clase Vaca
# -----------------------------------------
class Vaca:
    def __init__(self, fila, col):
        self.fila = fila
        self.col = col
        self.movimientos = 0
        self.mojones = []  # lista de [fila, col, turno_creacion]

    def mover(self, terreno, direccion):
        dr = 0
        dc = 0
        if direccion == 1:  # norte
            dr = -1
        elif direccion == 2:  # este
            dc = 1
        elif direccion == 3:  # sur
            dr = 1
        elif direccion == 4:  # oeste
            dc = -1

        nf = self.fila + dr
        nc = self.col + dc

        if terreno.dentro(nf, nc):
            self.fila = nf
            self.col = nc
            if terreno.get(nf, nc) == '"':
                terreno.set(nf, nc, ".")
            self.movimientos += 1
            if self.movimientos % 5 == 0:
                terreno.set(nf, nc, "O")
                self.mojones.append([nf, nc, 0])  # turno = 0 al crear

    def actualizar_mojones(self, terreno):
        nuevos = []
        for m in self.mojones:
            m[2] += 1
            if m[2] >= 7:
                # si aún es mojón, vuelve a hierba
                if terreno.get(m[0], m[1]) == "O":
                    terreno.set(m[0], m[1], '"')
            else:
                nuevos.append(m)
        self.mojones = nuevos

class Tractor:
    def __init__(self):
        self.fila = 0
        self.col = 0

    def mover(self, terreno, direccion, vaca_f, vaca_c):
        dr = 0
        dc = 0
        if direccion == 1:
            dr = -1
        elif direccion == 2:
            dc = 1
        elif direccion == 3:
            dr = 1
        elif direccion == 4:
            dc = -1

        pasos = 0
        while pasos < 2:
            nf = self.fila + dr
            nc = self.col + dc
            if not terreno.dentro(nf, nc):
                break
            if nf == vaca_f and nc == vaca_c:
                break
            if terreno.get(nf, nc) == "O":
                terreno.set(nf, nc, ".")
                self.fila = nf
                self.col = nc
                break
            self.fila = nf
            self.col = nc
            pasos += 1


# -----------------------------------------
# Juego Principal
# -----------------------------------------
def main():
    print("JUEGO DE LA VACA Y CACAS")
    ancho = int(input("Ancho del terreno: "))
    alto = int(input("Alto del terreno: "))

    vf = int(input("Fila inicial de la vaca: "))
    vc = int(input("Columna inicial de la vaca: "))

    if vf == 0 and vc == 0:
        print("La celda (0,0) es del tractor. Elige otra posición.")
        sys.exit(0)

    terreno = Terreno(ancho, alto)
    vaca = Vaca(vf, vc)
    tractor = Tractor()

    # La vaca come la hierba inicial donde está
    terreno.set(vf, vc, ".")

    turno = 0

    while terreno.hay_hierba():
        turno += 1
        dir_v = random.randint(1, 4)
        dir_t = random.randint(1, 4)

        vaca.mover(terreno, dir_v)
        vaca.actualizar_mojones(terreno)
        tractor.mover(terreno, dir_t, vaca.fila, vaca.col)

        terreno.imprimir(vaca.fila, vaca.col, tractor.fila, tractor.col, turno)

        time.sleep(random.randint(1, 3))

    print("Fin del juego: no queda hierba.")
    print("Turnos totales:", turno)


if __name__ == "__main__":
    main()