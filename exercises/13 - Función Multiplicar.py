### EJERCICIO 13 ###
'''
Crear una función para multiplicar los valores de tipo numéricos, utilizando argumentos variables
Luego regresar la multiplicación de todos los argumentos pasados en la función
'''

#SOLUCION 1

def multiplicar(*multi):
    resultado = 1
    for valor in multi:
        resultado *= valor
    return resultado

result = multiplicar(5,6,9,8,10)
print(result)