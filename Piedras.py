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
