### EJERCICIO 11 ###

'''
Dada la siguiente tupla, crea una lista que contenga los números menores a 5
'''

tupla = (13,1,8,3,2,5,8)

#Primero creamos una lista vacia
lista = []

#Despues voy a recorrer los elementos de la tupla, hago una seleccion y los agrego a la lista vacia

for numero in tupla:
    if numero < 5:
        lista.append(numero)

#Luego imprimimos la lista

print(lista)



