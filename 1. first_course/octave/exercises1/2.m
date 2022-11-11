a = linspace(1, 8, 8) #Esta función divide un espacio en N partes
                      #(siendo N el último número del paréntesis)

v = [1, 2, 3] #Creamos un vector cualquiera "v"
u = [5, 4, 2] #Creamos un vector cualquiera "u"
prod_escalar_vu = dot(v, u) #Calculamos el producto escalar entre v y u mediante
                            #la función "dot"

prod_vectorial_vu = cross(v, u) #Calculamos el producto vectorial entre v y u
                                #mediante la función "cross"

e_1 = 4 #Creamos un escalar cualquiera "e_1"
e_2 = 4 #Creamos un escalar cualquiera "e_2"
mat_id_1 = eye(e_1) #Creamos la matriz identidad con N=e_1 filas y N=e_1
                    #columnnas
mat_id_2 = eye(e_1, e_2) #Creamos la matriz identidad con N=e_1 filas y M=e_2
                         #columnas

n1 = 8 #Creamos un escalar cualquiera "n1"
x = zeros(n1) #Creamos la matriz cuadrada de dimensión N=n1 cuyos elementos son
              #ceros

n2 = (8) #Creamos un escalar cualquiera "n2"
y = ones(n2) #Creamos una matriz cuadrada de dimensión N=n2 cuyos elementos son
             #unos
