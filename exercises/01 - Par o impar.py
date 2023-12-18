### EJERCICIO 1

'''
Ingresar un número y mediante un algoritmo, decir si es par o impar.
'''

numero = int(input('Escribe un valor numérico: '))

if numero %2 == 0:
    print(f'El número seleccionado fue: [{numero}], este valor es PAR')
else:
    print(f'El número seleccionado fue: [{numero}], este valor es IMPAR')
