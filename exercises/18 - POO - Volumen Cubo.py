### EJERCICIO 18 ###

class Cubo:
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad

    def vol(self):
        return self.alto * self.ancho * self.profundidad

alto = float(input('Proporciona el valor del alto: '))
ancho = float(input('Proporciona el valor del ancho: '))
profundidad = float(input('Proporciona el valor de la profundidad: '))

cubo1 = Cubo(alto,ancho,profundidad)
print(f'El volumen del cubo es: {cubo1.vol():.2f}')
