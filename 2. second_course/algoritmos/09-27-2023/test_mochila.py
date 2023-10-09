nombre1 = "portatil"
peso1 = 2
valor1 = 700
nombre2 = "botella"
peso2 = 1
valor2 = 1
dicObjetos = {}
dicObjetos[nombre1] = {
    "peso" : peso1,
    "valor" : valor1,
    "peso-valor" : (peso1/valor1)
}

dicObjetos[nombre2] = {
    "peso" : peso2,
    "valor" : valor2,
    "peso-valor" : (peso2/valor2) 
}

print(dicObjetos)