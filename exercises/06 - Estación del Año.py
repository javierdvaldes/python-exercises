### EJERCICIO 6 ###

'''
El usuario tiene que proporcionar un valor del 1 al 12. El programa debe devolver en que estación se encuentra
'''

numero = int(input('Eliga un número del 1 al 12: '))

if not numero in range(1,13):
    print('Tu número no está dentro del rango, vuelve a elegir un número')
    exit()


if numero in [12,1,2]:
    print('Te encuentras en verano')
elif numero in [3,4,5]:
    print('Te encuentras en otoño')
elif numero in [6,7,8]:
    print('Te encuentras en invierno')
elif numero in [9,10,11]:
    print('Te encuentras en primavera')

#OTRA FORMA DE RESOLVER

mes = int(input('Eliga un número del 1 al 12: '))

if not mes in range(1,13):
    print('Tu número no está dentro del rango, vuelve a elegir un número')
    exit()
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'

print(f'Para el mes de: {mes}, la estación del año es: {estacion}')


