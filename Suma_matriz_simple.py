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