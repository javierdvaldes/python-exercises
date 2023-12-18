### EJERCICIO 5 ###

'''
Desarrolla un algoritmo para jugar contra la computadora al juego piedra, papel y tijera.
Usando las sentencias de control.
'''

import random
#Opciones para jugar
opciones = ('piedra', 'papel', 'tijera')

#Elección del usuario
usuario = input('Selecciona Piedra, Papel o Tijera: ')
usuario = usuario.lower()

if not usuario in opciones:
    print('Tu opción no es válida, tienes que elegir piedra, papel o tijera')
    exit()

#Elección de la computadura, usando el módulo random
computer = random.choice(opciones)

print(f'Elección del usuario: {usuario}')
print(f'Elección computadora: {computer}')

#Empezando a usar las sentencias de control IF/ELIF/ELSE
if usuario == computer:
    print('Empate')
elif usuario == 'piedra':
    if computer == 'tijera':
        print('Piedra gana a tijera, usuario Ganó')
    else:
        print('Papel gana a piedra, computadora ganó')

elif usuario == 'papel':
    if computer == 'piedra':
        print('Papel gana a piedra, usuario Ganó')
    else:
        print('Tijera gana a papel, computadora ganó')

elif usuario == 'tijera':
    if computer == 'papel':
        print('Tijera gana a papel, usuario Ganó')
    else:
        print('Piedra gana a tijera, computadora ganó')