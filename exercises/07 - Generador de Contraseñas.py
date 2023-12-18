### EJERCICIO 7 ###

'''
Crear un generador de contraseña utilizando el módulo random
'''

import random

letras = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['|','!','#','$','%','&','/','(',')','=','*','-','+']


print('Welcome to the PyPassword Generator!')
num_letras = int(input('How many letters would you like in your password?\n'))
num_numeros = int(input('How many numbers would you like?\n'))
num_simbolos = int(input('How many symbols would you like?\n'))

largo_total = num_letras + num_numeros + num_simbolos

lista_letras_random = []
lista_numeros_random = []
lista_simbolos_random = []

for letra in range(0, num_letras):
    lista_letras_random += random.choice(letras)

for numero in range(0, num_numeros):
    lista_numeros_random += random.choice(numeros)

for simbolo in range(0, num_simbolos):
    lista_simbolos_random += random.choice(simbolos)

# 1. Concatenamos las listas, creando una sola
lista_nueva = lista_letras_random + lista_numeros_random + lista_simbolos_random
# 2. Mezclamos las letras usando el módulo random con su función shuffle
random.shuffle(lista_nueva)
# 3. Unimos los caracteres usando la función join
lista_unida = ''.join(lista_nueva)
print(f'La contraseña es: {lista_unida}')


