### EJERCICIO 15 ###

'''
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
'''

pago = float(input('Proporcione el pago sin el impuesto: '))
impuesto = float(input('Proporcione el impuesto: '))

def pago_con_impuesto(pago,impuesto):
    pago_total = pago + pago*(impuesto/100)
    return pago_total

resultado = pago_con_impuesto(pago,impuesto)
print(f'El pago es de: {pago}, el impuesto aplicado es de: {impuesto}. El total de la compra es: {resultado}')

