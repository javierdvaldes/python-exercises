### EJERCICIO 16 ###

'''
Convertir de °C a °F. Tambien de °F a °C
'''

#°C a °F

grados_celsius = float(input('Proporcione los grados Celsius: '))

def celsius_a_fahrenheit(grados_celsius):
    c_f = grados_celsius * 9/5 + 32
    return c_f

resultado = celsius_a_fahrenheit(grados_celsius)
print(f'Los grados Celsius {grados_celsius}, pasados a grados Fahrenheit son: {resultado:.2f}')

grados_fahrenheit = float(input('Proporcione los grados Fahrenheit: '))

def fahrenheit_a_celsius(grados_fahrenheit):
    f_c = (grados_fahrenheit-32)* 5/9
    return f_c

resultado2 = fahrenheit_a_celsius(grados_fahrenheit)
print(f'Los grados Fahrenheint {grados_fahrenheit}, pasados a grados Celsius son: {resultado2:.2f}')