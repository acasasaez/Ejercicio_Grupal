lucia = 0
carlitos = 0

def claridad ():
    a = [0,1,2]
    b= [0,1,2]
    global lucia
    global carlitos
    a[0]= int(input("Introduzca la puntuación de Lucía"))
    b[0]=int(input("Introduzca la puntuación de Carlitos"))
    while a [0]>100 or b[0]> 100 or a[0]<0 or b[0]<0:
        print ("Las puntuaciones asignadas deben estar entre 0 y 100")
        a[0]= int(input("Introduzca la puntuación de Lucía"))
        b[0]=int(input("Introduzca la puntuación de Carlitos"))
    
    if a[0]>b[0]:
           lucia+= 1
           print ("Lucía tiene", lucia,"puntos.")
           print("Carlitos tiene", carlitos, "puntos.")
    elif a[0] < b[0]:
            carlitos += 1
            print ("Lucía tiene", lucia,"puntos.")
            print("Carlitos tiene", carlitos, "puntos.")
    else:
            print ("EMPATE")
            print ("Lucía tiene", lucia,"puntos.")
            print("Carlitos tiene", carlitos, "puntos.")
def originalidad ():
    a = [0,1,2]
    b =[0,1,2]
    global lucia
    global carlitos 
    a[1] = int(input("Introduzca la puntuación de Lucía"))
    b [1]= int (input ("Introduzca la puntuación de Carlitos "))
    while a[1]> 100 or b[1]> 100 or a[1]< 0 or b[1]< 0:
        print ("Las puntuaciones asignadas deben estar comprendidas entre 0 y 100")
        a[1] = int(input("Introduzca la puntuación de Lucía"))
        b [1]= int (input ("Introduzca la puntuación de Carlitos "))
    
    if a[1]>b[1]:
            lucia += 1
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
    elif a[1] < b [1]:
            carlitos +=1
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
    else:
            print ("EMPATE")
            print ("Lucía tiene",lucia,"puntos.")
            print("Carlitos tiene",carlitos,"puntos.")
def dificultad ():
    a = [0, 1, 2]
    b=[0,1,2]
    global lucia
    global carlitos
    a[2] = int (input ("Introduzca la puntuación de Lucía"))
    b[2]= int(input("Introduzca la puntuación de Carlitos"))
    while a[2]> 100 or b[2]> 100 or a[2]< 0 or b[2]< 0:
        print ("Las puntuaciones asignadas deben estar entre 0 y 100")
        a[2] = int (input ("Introduzca la puntuación de Lucía"))
        b[2]= int(input("Introduzca la puntuación de Carlitos"))
    
    if a [2]> b[2]:
            lucia +=1
            print ("Lucía tiene", lucia, "puntos.")
            print ("Carlitos tiene", carlitos, "puntos")
    elif a[2] < b[2]:
            carlitos += 1
            print ("Lucía tiene", lucia, "puntos.")
            print ("Carlitos tiene", carlitos, "puntos")
    else: 
            print ("EMPATE")
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
print("Puntuaciones en originalidad")
originalidad()
print("Puntuaciones en dificultad")
dificultad()
compara()


