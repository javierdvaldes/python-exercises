### EJERCICIO 19 ###
print('HERENCIAS')
'''
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta. Las cuales van a heredar de la
clase padre Vehiculo.
'''

class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas




class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo (montaña, urbana, etc): ' + str(self.tipo)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo



print('CREAMOS OBJETO DE LA CLASE VEHICULO')
vehiculo = Vehiculo('Azul', '4')
print(vehiculo)

print('CREAMOS OBJETO DE LA CLASE COCHE')
coche = Coche('Rojo', 4, 120)
print(coche)

print('CREAMOS OBJETO DE LA CLASE BICICLETA')
bicicleta = Bicicleta('Gris', 2, 'Montaña')
print(bicicleta)