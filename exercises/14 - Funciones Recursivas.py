### EJERCICIO 14 ###
print('EJERCICIO 1')
'''
Imprime numeros de 5 a 1 de manera descendente.
'''

def cuenta_atras(num):
    if num >= 1:
        print(num)
        cuenta_atras(num-1)
    elif num == 0:
        return
    elif num <= 0:
        print('Valor incorrecto')
        print('Listo')

cuenta_atras(10)

print('EJERCICIO 2')
'''
Mismo ejercicio pero hacia adelante
'''

def cuenta_adelante(num):
    num += 1
    if num < 10:
        print(num)
        cuenta_adelante(num)
    else:
        print('Listo')

cuenta_adelante(1)
print('EJERCICIO 3')
'''
Factorial 1
'''

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(10))

'''
Factorial 2
'''

def fact(num):
    if num > 1:
        num *= fact(num-1)
    return num
print(fact(10))
