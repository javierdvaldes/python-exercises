### EJERCICIO 2 ###

'''
Proporcionar una edad y mediante un algoritmo, decir si esa persona es adulta, joven o niño.
'''

edad = int(input('Proporciona una edad: '))

if edad < 10 and edad >= 0:
    print('Esta persona es un niño')
elif edad >=10 and edad < 18:
    print('Esta persona es joven')
elif edad >=18:
    print('Esta persona es adulta')
else:
    print('Esta persona no existe')
