A = [2,1,3;
     1,1,1;
     1,3,2] #Establecemos la matriz A
b = [10;
     6;
     13]
C = inv(A) #Establecemos que C es la inversa de A
I = A * C #Comprobamos que A * C es la matriz identidad
TA = transpose(A) #Calculamos la transpuesta de A
size_A = size(A)
determinante_A = det(A)
traza_A = trace(A)
diegonal_A = diag(A)

solucion = linsolve(A, b) #Resolvemos el sistema de ecuaciones
