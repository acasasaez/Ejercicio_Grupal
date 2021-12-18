# Ejercicio_Grupal
En esta entrega nos ha tocado realizar un trabajo grupal. Para ello, como siempre, hemos tenido que crear un repositorio, en este caso compartido, dejamos aquí el enlace al mismo:https://github.com/acasasaez/Ejercicio_Grupal.git

Este grupo está compuesto por Andrea Casas y Miguel Guerra.

Nuestra tarea consta de 8 ejercicios:

Ejercicio 1: Suma de una matriz simple:

En este ejercicio debíamos crear un programa que como resultado nos devolviese la suma de los elementos de una matriz.

Ejercicio 3: Suma muy grande
Para este ejercicio también debíamos crear un programa que nos devolviese como resultado la suma de los elementos de una matriz, pero esta vez tenindo en cuenta de que estos elementos podían ser muy grandes.

Debido a que mi ompañero y yo no encontrábamos una gran diferencia entre ambos ejercicios, hemos propuesto el mismo código para los 2. En este, el "lector" es quien elige el número de filas y columnas de dicha de matriz, y también todos y cada uno de los elementos de la misma. Finalmente, el programa devuelve la lista que representa la matriz y el resultado de la suma de todos sus elementos.


Ejercicio 2: Comparación de problemas:

En esta tarea se debía crear un código que permitiese evaluar y comparar los resultados con respecto a 2 trabajos. Estos trabajos están evaluados en 3 categorías, del 1 al 100: claridad, originalidad y dificultad. El trabajo 1 corresponde a Lucía y el 2 a Carlitos.

Por cada categoría en la que el trabajo 1 tuviese mayor puntuación, Lucía gana un punto. 

Por cada categoría en la que el trabajo 2 obtuviese mayor puntuación, Carlitos gana un punto.

En caso de empate ninguno de los 2 gana puntos.

Finalmente, quien obtenga más puntos en total (teniendo en cuenta las 3 categorías) será el ganador.
Además, el programa también nos devuelve una "tabla" con los puntos totales de cada uno.

Ejercicio 4: La escalera:

En esta ocasión, nos tocaba crear un programa que nos devolviese como resultado una escalera. Para poder hacerlo hemos elaborado un código que funciona de la siguiente manera:

Inicialmente, este pide al "lector" que introduzca el número de peldaños que tiene la escalera.
Por último, a partir de un bucle y mediante "#" nos devuelve como resultado dicha escalera.

Ejercicio 5: Las piedras:

Dos jugadores llamados P1 Y P2 están jugando un juego con un número inicial de n piedras. Jugador1 
siempre juega primero, y los dos jugadores se mueven en turnos alternos. Las reglas del juego son las 
siguientes:

En un solo movimiento, un jugador puede eliminar ,2,3 o 5 , o piedras del tablero de juego.

Si un jugador no puede hacer un movimiento, ese jugador pierde el juego.

Dado el número inicial de piedras, busque e imprima el nombre del ganador.

Cada jugador juega de manera óptima, lo que significa que no harán un movimiento que les haga perder 
el juego si existe un movimiento ganador.

• Por ejemplo, si n=4, P1 puede hacer los siguientes movimientos:

• P1 elimina 2 piedras quedando 2. P2 luego eliminará 2 piedras y ganar.

• P1 elimina 3 piedras quedando 1 . P2 no se puede mover y pierde.

*NOTA: Ni el código ni la descripción de la tarea son propios ya que no entendíamos la dinámica del juego

Ejercicio 6: La rana:
En este ejercicio debíamos crear un laberinto en el cual estuviese encerrada nuestra rana.

La dinámica es sencilla, el laberinto se componen de celdas que pueden estar vacías, obstaculizadas o tener una bomba.

"#" denota un obstáculo.

• A denota una celda libre donde la rana está inicialmente.

• denota una celda con una mina.

• % denota una celda con una salida.

• denota una celda libre (que puede contener una entrada a un túnel).

*las celdas adyacentes son aquellas que comparten un lado.

• Cuando Alef está en cualquier celda, puede elegir al azar y con la misma probabilidad moverse 
a una de las celdas adyacentes que no contengan ningún obstáculo. Si esta celda contiene una 
mina, la mina explota y Alef muere. Si esta celda contiene una salida, Alef escapa del laberinto.

Cuando Alef aterriza en una celda con una entrada a un túnel, es inmediatamente transportado 
a través del túnel y arrojado a la celda en el otro extremo del túnel. A partir de entonces, no 
volverá a caer y ahora volverá a moverse aleatoriamente a una de las celdas 
adyacentes. (Posiblemente podría caer en el mismo túnel más tarde).

Es posible que Alef se quede atascado en el laberinto en el caso de que la celda en la que fue 
arrojado desde un túnel esté rodeada de obstáculos por todos lados.

Nuestra tarea era escribir un programa que calcule e imprima una probabilidad de que Alef escape del 
laberinto.

Ejercicio 7: Calificación de estudiantes:

En esta tarea se nos proponía el sufuiente reto:
La Universidad para el nuevo curso va a implementar una nueva poítica de calificación:

Cada estudiante recibe una nota en el rango inclusivo de 0 a 100 .

Si tienes una nota inferior a 40 o menos es una calificación suspensa.

Además a los profesores en la universidad nos gusta redondear los de acuerdo con estas reglas:

Si la diferencia entre una nota y el siguiente múltiplo de es menos que 3 , se redondea hasta el 
siguiente múltiplo de 5 .

Si el valor de la nota es menor que e 40 , no se produce redondeo ya que el resultado seguirá 
siendo una calificación suspensa.

Ejercicio 8: La manzana y la naranja:
Para nuestro último ejercicio se nos propone el siguiente enunciado:

La casa de Sam tiene un manzano y un naranjo que dan frutos en abundancia. Con la información que se 
proporciona a continuación, determine la cantidad de manzanas y naranjas que aterrizan en la casa de 
Sam.

En el diagrama siguiente:

La región roja denota la casa, s donde es el punto de inicio, y t es el punto final. El manzano está a la 
izquierda de la casa y el naranjo está a la derecha.

Suponga que los árboles están ubicados en un solo punto, donde el manzano está en el puntoa , y el 
naranjo está en el punto b .

Cuando una fruta cae de su árbol, aterriza a d unidades de distancia desde su árbol de origen a lo 
largo del eje x. * Un valor negativo de significa que la fruta cayó a d unidades a la izquierda del 
árbol, y un valor positivo de significa que cae a d unidades a la derecha del árbol. *

PONER FIGMAS AQuÏ

Códigos:
```
EJERCICIO 1 y 3:
n = int(input("Introduce el número de filas"))
m = int (input("Introduce el número de columnas"))
mat = [[" " for j in range (m)] for i in range (n)]
suma = 0
for i in range (n):
    for j in range (m):
        mat[i][j] = int(input("VALOR DEL ELEMENTO", ))
        suma += mat [i][j]
    
print ("RESULTADO FINAL") 
print (mat)
print(suma)

EJERCICIO 2:
lucia = 0
carlitos = 0

def claridad ():
    a = [0,1,2]
    b= [0,1,2]
    global lucia
    global carlitos
    a[0]= int(input("Introduzca la puntuación de Lucía: "))
    b[0]=int(input("Introduzca la puntuación de Carlitos: "))
    while a [0]>100 or b[0]> 100 or a[0]<0 or b[0]<0:
        print ("Las puntuaciones asignadas deben estar entre 0 y 100")
        a[0]= int(input("Introduzca la puntuación de Lucía: "))
        b[0]=int(input("Introduzca la puntuación de Carlitos: "))
    
    if a[0]>b[0]:
           lucia+= 1
           print ("Lucía tiene", lucia,"puntos.")
           print("Carlitos tiene", carlitos, "puntos.")
    elif a[0] < b[0]:
            carlitos += 1
            print ("Lucía tiene", lucia,"puntos.")
            print("Carlitos tiene", carlitos, "puntos.")
    else:
            print ("empate en  la categoría claridad claridad")
            print ("Lucía tiene", lucia,"puntos.")
            print("Carlitos tiene", carlitos, "puntos.")
def originalidad ():
    a = [0,1,2]
    b =[0,1,2]
    global lucia
    global carlitos 
    a[1] = int(input("Introduzca la puntuación de Lucía: "))
    b [1]= int (input ("Introduzca la puntuación de Carlitos: "))
    while a[1]> 100 or b[1]> 100 or a[1]< 0 or b[1]< 0:
        print ("Las puntuaciones asignadas deben estar comprendidas entre 0 y 100")
        a[1] = int(input("Introduzca la puntuación de Lucía: "))
        b [1]= int (input ("Introduzca la puntuación de Carlitos: "))
    
    if a[1]>b[1]:
            lucia += 1
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
    elif a[1] < b [1]:
            carlitos +=1
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
    else:
            print ("empate en la categoría originalidad")
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
def dificultad ():
    a = [0, 1, 2]
    b=[0,1,2]
    global lucia
    global carlitos
    a[2] = int (input ("Introduzca la puntuación de Lucía: "))
    b[2]= int(input("Introduzca la puntuación de Carlitos: "))
    while a[2]> 100 or b[2]> 100 or a[2]< 0 or b[2]< 0:
        print ("Las puntuaciones asignadas deben estar entre 0 y 100")
        a[2] = int (input ("Introduzca la puntuación de Lucía: "))
        b[2]= int(input("Introduzca la puntuación de Carlitos: "))
    
    if a [2]> b[2]:
            lucia +=1
            print ("Lucía tiene", lucia, "puntos.")
            print ("Carlitos tiene", carlitos, "puntos")
    elif a[2] < b[2]:
            carlitos += 1
            print ("Lucía tiene", lucia, "puntos.")
            print ("Carlitos tiene", carlitos, "puntos")
    else: 
            print ("empate en la categoría dificultad")
            print ("Lucía tiene", lucia, "puntos.")
            print ("Carlitos tiene", carlitos, "puntos")
def compara ():
    global lucia
    global carlitos
    if lucia > carlitos:
        print ("El trabajo ganador es el de Lucía") 
    elif lucia < carlitos:
        print ("El trabajo ganador es el de Carlitos")
    else: 
        print ("Los trabajos han empatadp")
print("Puntuación de los trabajos")
print("Puntuaciones en claridad")
claridad()
print(" ")
print("Puntuaciones en originalidad")
originalidad()
print(" ")
print("Puntuaciones en dificultad")
dificultad()
print(" ")
print ("RESULTADO FINAL:")
a= ["LUCÍA", "CARLITOS"]
c = [lucia, carlitos ]


print (a[0], a [1])
print(" ",c[0], " ", " "," ", c[1])
compara()

EJERCICIO 4:
n = int (input(" Introduce el número de escalones de tu escalera: "))
for i in range (1):
    a = " "
    for j in range (0,n):
        a = a + " "
        for g in range (0, i+1):
            a = a + "#"
            print (a)
            
 EJERCICIO 5:
 import os
def gameOfStrones ():
    ganador = " "
    if (jugadaoptima(n)!=0):
        ganador= "P1 es el ganador"
    else:
        ganador = "P2 es el ganador"
    return ganador
def jugadaoptima(n):
    jugadabuena = 0
    modulo = n%7
    if modulo >= 2 and modulo <=3:
        jugadabuena = 2
    elif modulo ==4:
        jugadabuena = 3
    elif modulo>=5 and modulo<=6:
        jugadabuena = 5
    return jugadabuena
def simulacion (n):
    intentos =0
    ganador = ""
    while ganador != "P1 es el ganador" and ganador != "P2 es el gandor":
        jugada =jugadaoptima(n)
        if jugada == 0:
            if n > 5:
                jugada = 5
            elif n>3:
                jugada =3
            else:
                jugada =2
        print ("Juega P" + str((intentos%2)+1) + "quitando" + str(jugada) + "piedras")
        n = n -jugada
        if(n==1 or n==0):
            ganador = ("P"+str(intentos%2)+1 +"es el ganador")
        intentos+=1
        print (ganador)
if __name__ =="__main__":
    t =int(input().strip())
    for t_itr in range (t):
        n=int(input().strip())
        result = gameOfStrones(n)
        
EJERCICIO 6:
import math
import os 
import random
import re
import sys 
class Coordenadas:
    def __int__ (self, x,y):
        self.x = x
        self.y = y
    def comparate (self,x,y):
        if self.x == x and self.y == y:
            return True
        else: 
            return False
class Tunel:
    def __init__(self,x1,x2,y1,y2):
        self.extremo1 = Coordenadas(x1,y1)
        self.extremo2 = Coordenadas (x2,y2)

def BuscaTunel (casillax, casillay, tuneles):
    coordenadas = Coordenadas(casillax, casillay)
    for t in tuneles:
        if t.extremo1.comparate(casillax,casillay)==True:
            coordenadas.x = t.extremo2.x
            coordenadas.y = t.extremo2.y
        elif t.extremo2.comparate(casillax, casillay):
            coordenadas.x=t.extremo1.x
            coordenadas.y = t.extremo1.y
    return coordenadas

def exploracion(casillax, casillay, laberinto, n, m, tuneles):
    numero =0
    den = 0
    prob = 0.0
    if casillax>0 and laberinto[casillax-1][casillay]!= "#":
        den += 1
        if laberinto [casillax-1][casillay]=="%":
            numero+=1
    if casillax<n-1 and laberinto[casillax+1][casillay]!= "#":
        den+= 1
        if laberinto[casillax+1][casillay]=="%":
            numero+=1
    if casillay<m-1 and laberinto[casillax][casillay+1]!="#":
        den+=1
        if laberinto[casillax][casillay+1]=="%":
            numero+=1
    if casillay > 0 and laberinto[casillax][casillay-1]!="#":
        den +=1
        if laberinto[casillax][casillay-1]== "%":
            numero +=1
    if den == 0:
        return prob
    prob = numero/den
    if casillax> 0 and laberinto [casillax-1][casillay]   == "$":
        laberintocopia= laberinto 
        coordenadas= BuscaTunel(casillax-1,casillay,tuneles)
        laberintocopia [casillax][casillay]= "#"
    prob+= exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillax<n-1 and laberinto[casillax+1][casillay]== "$":
        laberintocopia = laberinto
        coordenadas = BuscaTunel(casillax+1,casillay,tuneles)
        laberintocopia[casillax][casillay]="#"
    
    prob+=exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillay<m-1 and laberinto[casillax][casillay+1]=="$":
        laberintocopia=laberinto
        coordenadas=BuscaTunel(casillax,casillay+1,tuneles)
        laberintocopia[casillax][casillay]="#"
    prob +=exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillay >0 and laberinto[casillax][casillay-1]=="$":
        laberintocopia=laberinto
        coordenadas = BuscaTunel(casillax,casillay,tuneles)
        laberintocopia[casillax][casillay]="#"
    prob += exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    return prob
if __name__ == "__main__":
    print ("Dimensiones del laberinto y número de tuneles:(filas,columnas)")
    first_multiple_input = input().rstrip().split()
    n= int(first_multiple_input[0])
    m= int(first_multiple_input[1])
    k= int(first_multiple_input[2])
    laberinto=[]
    for n_itr in range (n):
        print ("Fila"+str(n_itr)+"del laberinto:(# muro, porcentaje salida, *bomba, $ vacía, o tunel")
        row= input()
        laberinto.append(list(row))
    tuneles=[]
    for k_itr in range (k):
        print("Coordenadas (i1 j1 i2 j2) del tunel" + str(k_itr))
        second_multiple_input = input().rstrip().split()
        i1 =int( second_multiple_input[0])
        j1 = int(second_multiple_input[1])
        i2 = int(second_multiple_input[2])
        j2 = int(second_multiple_input[3])
        tuneles.append(Tunel(i1,j1,i2,j2))
    print("Coordenadas iniciales de la rana:")
    third_multiple_input= input().rstrip().split()
    pos1= int(third_multiple_input[0])
    pos2=int(third_multiple_input[1])
    prob= exploracion(pos1,pos2,laberinto,n,m,tuneles)
    print(prob)

EJERCICIO 7:
