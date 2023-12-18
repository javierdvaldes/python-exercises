### EJERCICIO 8 - AHORCADO JUEGO

''' Proyecto del juego ahorcado'''

import random
from lista_palabras import word_list

# 1. PRIMER PARTE
# Palabra Randóm
palabra_random = random.choice(word_list)
largo_palabra = len(palabra_random)

fin_juego = False
vidas = 6

from art_ahorcado import logo
print(logo)

# 2. SEGUNDA PARTE - Creamos una lista con espacios en blanco
display = []
for _ in range(largo_palabra):
    display += '_'


# 3. TERCER PARTE - Lógica
while not fin_juego:
    letra_usuario = str(input('Escribe una letra: ')).lower()

    if letra_usuario in display:
        print(f'Ya has adivinado: {letra_usuario}')

    for position in range(largo_palabra):
        letra = palabra_random[position]
        if letra == letra_usuario:
            display[position] = letra

    # Comprobamos si el usuario está equivocado
    if letra_usuario not in palabra_random:
        print(f'Elegiste {letra_usuario}, esa letra no está en la palabra. Pierdes una vida')

        vidas -= 1
        if vidas == 0:
            fin_juego = True
            print('Perdiste')

    # Unimos todos los elementos en la lista y lo transformamos en una cadena
    print(f'{" ".join(display)}')

    # Comprobamos si el usuario tiene todas las letras
    if '_' not in display:
        fin_juego = True
        print('Ganaste')

    from art_ahorcado import stages
    print(stages[vidas])



