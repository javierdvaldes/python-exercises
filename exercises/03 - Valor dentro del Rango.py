### EJERCICIO 3 ###

'''
El usuario proporcionara un valor entre 0 y 5. Mediante un algoritmo hay que decir si el número entra dentro del rango
'''

valor = int(input('Eliga un valor entre 0 y 5: '))
valorMinimo = 0
valorMaximo = 5

if (valor >= valorMinimo) and (valor <= valorMaximo):
    print(f'El {valor}, se encuentra dentro del rango')
else:
    print('El valor está fuera del rango')