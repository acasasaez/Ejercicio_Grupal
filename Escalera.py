n = int (input(" Introduce el número de escalones de tu escalera: "))
for i in range (1):
    a = " "
    for j in range (0,n):
        a = a + " "
        for g in range (0, i+1):
            a = a + "#"
            print (a)