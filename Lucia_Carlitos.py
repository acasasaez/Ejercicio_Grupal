lucia = 0
carlitos = 0

def claridad ():
    a = [0,1,2]
    b= [0,1,2]
    global lucia
    global carlitos
    a[0]= int(input("Introduzca la puntuación de Lucía"))
    b[0]=int(input("Introduzca la puntuación de Carlitos"))
    if a [0]>100 or b[0]> 100 or a[0]<0 or b[0]<0:
        print ("Las puntuaciones asignadas deben estar entre 0 y 100")
    else:
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
    a [2]= int (input ("Introduzca la puntuación de Carlitos "))
    

