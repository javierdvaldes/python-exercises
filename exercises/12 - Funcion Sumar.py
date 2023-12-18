### EJERCICIO 12 ###
'''
Crea una función para sumar los valores de tipo numerico utilizando argumentos variables.
Regresar la suma de todos los valores pasados como argumentos
'''

#SOLUCION 1
def sumar(*numeros):
    return sum(numeros)

resultado = sumar(58,6,5,8,487,2,3,1,5,24)
resultado2 = sumar(-5,-6,-8,-548,-6)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {resultado2}')

#SOLUCION 2
def sumar2(*numeros):
    resultado = 0
    for valor in numeros:
        resultado += valor
    return resultado

suma = sumar2(4,5,9,8,562,7,5,6,3,25)
print(f'El resultado de la suma es: {suma}')

