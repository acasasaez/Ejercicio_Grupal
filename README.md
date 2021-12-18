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
```EJERCICIO 1 y 3:
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


