### EJERCICIO 4 ###
'''
El usuario debe proporcionar:
 - nombre del libro
 - ID del libro (Entero)
 - Precio (Flotante)
 -Envio Gratuito o no (True/False)

'''

nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('Proporciona el precio del libro: '))
envio = input('Envio gratuito, eliga Si o No: ')
envio = envio.lower()

if envio == 'si':
    envio = True
elif envio == 'no':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir si o no'

print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio: {envio}
''')