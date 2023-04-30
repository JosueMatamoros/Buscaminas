from emoji import iconos

#Matriz principal del juego
juego = []
celdas_activadas=[]
#Limpiar terminal
print("/u033c",end = '')

#Encabezado del juego 
print("".center(50))
print("Buscaminas".center(50))
print("".center(50))

#excepciones 
try:
    x = int(input("Digite el ancho del area del juego."))
except:
    x = 20
try:
    y = int(input("Digite el alto del area del juego."))
except:
    y = 15
try:
    dificultad= int(input("Digite el porcentaje de minas"))
except:
    dificultad = 15

# Agregar muro de fondo al juego
i = 0 
while i < y: 
    j = 0
    fila = []
    while j < x:
        fila.append(iconos.MURO.value)
        j += 1
    juego.append(fila)
    i += 1

#Calcula de la cantidad de minas 
cantidad_minas =  int(((x*y)*dificultad)/100)

#importar la función random 
from random import random as rand

#coloca las minas en la matriz del juego sin duplicar
while cantidad_minas > 0:
    nuevox = int(x*rand())
    nuevoy = int(y*rand())
    if juego [nuevoy][nuevox] != iconos.MINA.value:
        juego [nuevoy][nuevox] = iconos.MINA.value
        cantidad_minas -= 1

#Rellenar las pistas

import logica
def rellenar():
    y = 0 
    while y < len(juego): 
        x = 0
        fila = []
        while x < len(juego[y]):
            if juego[y][x] != iconos.MINA.value:
                juego[y][x] = logica.bombas_vecinas(x, y, juego)  
            x += 1
        y += 1

#Modulo de la impresión del juego.
from interfaz import MainWindow
rellenar()


