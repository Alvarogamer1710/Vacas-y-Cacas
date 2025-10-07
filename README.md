# Simulación: Vaca y Granjero en el Terreno

## Descripción General

Este programa simula un pequeño juego en el que una **vaca** va comiendo hierba en un terreno para desbrozarlo, mientras un **granjero con su tractor** recoge los mojones que la vaca va dejando. El juego se desarrolla automáticamente por turnos y finaliza cuando la vaca ha comido toda la hierba del terreno.

El programa se ejecuta en la consola y muestra el estado del tablero turno a turno, con un retraso aleatorio entre 1 y 3 segundos entre movimientos.

## Requisitos

* Python 3.7 o superior
* Librerías estándar de Python (`random`, `time`, `sys`)

No se requieren dependencias externas.

## Ejecución

Para ejecutar el juego, abre una terminal en la carpeta donde se encuentra el archivo `vaca_parcela.py` y ejecuta:

```bash
python3 vaca_parcela.py
```

A continuación, el programa pedirá:

1. **Ancho** y **alto** del terreno (número de columnas y filas).
2. **Posición inicial** de la vaca (fila y columna, comenzando en 0). La posición (0,0) está reservada para el tractor.

## Reglas del Juego

### Elementos del Terreno

* **Hierba (`"`)**: cubre todo el terreno al inicio.
* **Vaca (`V`)**: se mueve una casilla por turno y come la hierba al pasar.
* **Tractor (`T`)**: el granjero, que recoge mojones.
* **Mojón (`O`)**: aparece cada 5 movimientos de la vaca.
* **Terreno limpio (`.`)**: zona donde ya no hay hierba ni mojones.

### Movimiento de la Vaca

* Se mueve **1 casilla por turno** en una dirección aleatoria (Norte, Este, Sur u Oeste).
* Si llega a una celda con hierba (`"`), la come y la deja limpia (`.`).
* Cada **5 movimientos**, deja un **mojón (`O`)** en la celda actual.

### Movimiento del Tractor

* El tractor comienza en la celda (0,0).
* Se mueve **2 casillas por turno** en la misma dirección.
* Si encuentra un mojón dentro de sus dos pasos, se detiene al llegar a él, lo recoge (la celda pasa a `.`) y termina su movimiento.
* Si choca con el borde del terreno, se mueve solo lo que pueda.
* Si encuentra a la vaca, se detiene antes de entrar en su celda.

### Regeneración de Hierba

* Cada mojón (`O`) genera nueva hierba (`"`) **7 turnos** después de haber sido depositado, **salvo** que el tractor lo haya recogido antes.

### Fin del Juego

El juego termina cuando **no queda ninguna hierba (`"`)** en el terreno, aunque puedan quedar mojones sin recoger.

## Ejemplo de Ejecución

```
--- Configuración del terreno ---
Ancho (número de columnas, entero >=1): 5
Alto (número de filas, entero >=1): 4
Introduce la posición inicial de la vaca (fila y columna), empezando en 0.
Fila (0..3): 2
Columna (0..4): 2
```

El programa mostrará turnos como:

```
=============
Turno 1
-------------
T""""
"""""
".V""
"""""
=============
```

## Personalización

Puedes modificar parámetros como:

* Intervalo de espera entre turnos (`time.sleep`) → 1 a 3 segundos.
* Frecuencia de mojones → cada 5 movimientos de la vaca.
* Tiempo de regeneración de hierba → 7 turnos.

## Interrupción

Puedes detener la simulación en cualquier momento con **Ctrl + C**.

## Créditos

Autor: [Tu nombre o equipo de desarrollo]
Licencia: MIT (o la que desees aplicar)

---

Este proyecto fue creado como ejercicio de programación en Python para simular el comportamiento aleatorio de entidades en un entorno bidimensional.
