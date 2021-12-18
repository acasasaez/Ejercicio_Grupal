import math
import os
import random
import re
import sys

def simpleArraySum(matriz):
    suma = 0
    for fila in matriz:
        for n in fila:
            suma += n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'Suma_matriz_simple' , 'w')
matriz_count = int(input().strip())
print("Escribe la lista de números que desea operar ")
matriz = list(map(int, input().rstrip().split()))


result = simpleArraySum(matriz)

fptr.write(str(result) + '\n')

fptr.close()


