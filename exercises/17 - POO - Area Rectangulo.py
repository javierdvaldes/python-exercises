### EJERCICIO 17 ###

class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def area(self):
        return self.altura * self.base

altura = int(input('Proporciona la altura del rectangulo: '))
base = int(input('Proporciiona la base del rectangulo: '))

rectangulo1 = Rectangulo(altura,base)
print(f'El area del rectangulo es: {rectangulo1.area()}')
