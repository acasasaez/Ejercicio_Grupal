import math
import os 
import random
import re
import sys 
class coordenadas:
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
        self.extremo1 = coordenadas(x1,y1)
        self.extremo2 = coordenadas (x2,y2)
