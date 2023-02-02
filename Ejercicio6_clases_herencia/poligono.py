'''
EJERCICIO 6 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 6 -→ Clases y Herencia
CLASE POLÍGONO

1. Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.
Al crear un objeto, en el constructor __init__( ), se indica el número de lados que va a tener y
se crea una lista que va a tener ese número de elementos cuyos valores iniciales serán 0.

• La clase Poligono() tendrá un método llamado darlados() que le pedirá al usuario que
introduzca uno a uno los valores de todos los lados.
• La clase Polígono() tendrá otro método llamado verlados() que mostrará uno a uno los
valores introducidos de todos los lados.
• Se va a hacer una clase llamada Triangulo() que hereda de la clase Poligono().
Al crear un objeto triángulo, se invoca al constructor de la clase Poligono() al que se indica el
número de lados = 3.
• La clase Triangulo() tendrá un método area() que calcule y muestre el área del triángulo.
Puede ser cualquier tipo de triángulo. Puedes usar la fórmula de Herón.
• La clase Triangulo() tendrá un método perimetro() que calcule y muestre el perímetro del
triángulo (suma de sus lados).
• Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar todos los
métodos tanto de la clase Polígono() como de la clase Triangulo().
'''

print('**********************************************************************')
print('EJERCICIO polígono -→ Clases y Herencia')
print('----------------------------------------------------------------------')

# Importamos la librería math para poder usar la función sqrt().
import math


# Creamos la clase Polígono().
class Poligono:
    # Definimos el constructor.
    def __init__(self, lados):
        # Creamos una lista con tantos elementos como lados tenga el polígono.
        self.lados = [0] * lados

    # Definimos el método darlados().
    def darlados(self):
        # Recorremos la lista.
        for i in range(len(self.lados)):
            # Pedimos al usuario que introduzca el valor de cada lado.
            self.lados[i] = float(input('Valor del lado ' + str(i + 1) + ': '))

    # Definimos el método verlados().
    def verlados(self):
        # Recorremos la lista.
        for i in range(len(self.lados)):
            # Mostramos el valor de cada lado.
            print('Lado ' + str(i + 1) + ': ' + str(self.lados[i]))


# Creamos la clase Triangulo() que hereda de la clase Polígono().
class Triangulo(Poligono):
    # Definimos el constructor.
    def __init__(self):
        # Invocamos al constructor de la clase Polígono() y le pasamos el número de lados.
        Poligono.__init__(self, 3)

    # Definimos el método area() redondeando el valor final a 2 decimales.
    def area(self):
        # Para poder calcular el área del triángulo conociendo sus lados, usamos la fórmula de Herón.
        # Para ello, primero calculamos el semiperímetro del triángulo y luego tenemos que calcular
        # el área con la fórmula de Herón.
        # Esta fórmula sería --> raízCuadrada(semiperímetro * (semiperímetro - lado1) * (semiperímetro - lado2) * (semiperímetro - lado3))
        # Calculamos el semiperímetro.
        heron = (self.lados[0] + self.lados[1] + self.lados[2]) / 2
        # Calculamos el área.
        area = math.sqrt(heron
                         * (heron - self.lados[0])
                         * (heron - self.lados[1])
                         * (heron - self.lados[2]))
        # Mostramos el área, redondeando el valor final a 2 decimales.
        print('Área: ' + str(round(area, 2)))

    # Definimos el método perímetro().
    def perimetro(self):
        # Calculamos el perímetro.
        perimetro = self.lados[0] + self.lados[1] + self.lados[2]
        # Mostramos el perímetro.
        print('Perímetro: ' + str(perimetro))


# Creamos dos objetos de la clase Triangulo().
triangulo1 = Triangulo()
triangulo2 = Triangulo()

# Invocamos al método darlados() de la clase Triangulo().
print('Introduzca los valores de los lados del triángulo 1.')
triangulo1.darlados()
print('')
print('Introduzca los valores de los lados del triángulo 2.')
triangulo2.darlados()
print('--> Lados introducidos correctamente.')

# Invocamos al método verlados() de la clase Triangulo().
print('')
print('---- VALORES DE LOS LADOS DADOS ----')
print('Valores de los lados del triángulo 1.')
triangulo1.verlados()
print('')
print('Valores de los lados del triángulo 2.')
triangulo2.verlados()
print('--> Valores de los lados mostrados correctamente.')

# Vamos a decir que tipo de triángulo es cada uno, según el valor de sus lados.
# Para ello, vamos a comparar los valores de los lados de cada triángulo.
# Si los tres lados son iguales, es un triángulo equilátero.
# Si dos lados son iguales, es un triángulo isósceles.
# Si los tres lados son diferentes, es un triángulo escaleno.
# Hacemos la comparación de los lados del triángulo 1.
print('')
print('---- TIPO DE TRIÁNGULO ----')
if triangulo1.lados[0] == triangulo1.lados[1] == triangulo1.lados[2]:
    print('El triángulo 1 es EQUILÁTERO.')
elif triangulo1.lados[0] == triangulo1.lados[1] \
        or triangulo1.lados[0] == triangulo1.lados[2] \
        or triangulo1.lados[1] == triangulo1.lados[2]:
    print('El triángulo 1 es ISÓSCELES.')
else:
    print('El triángulo 1 es ESCALENO.')
# Hacemos la comparación de los lados del triángulo 2.
if triangulo2.lados[0] == triangulo2.lados[1] == triangulo2.lados[2]:
    print('El triángulo 2 es EQUILÁTERO.')
elif triangulo2.lados[0] == triangulo2.lados[1] \
        or triangulo2.lados[0] == triangulo2.lados[2] \
        or triangulo2.lados[1] == triangulo2.lados[2]:
    print('El triángulo 2 es ISÓSCELES.')
else:
    print('El triángulo 2 es ESCALENO.')
print('--> Tipos de triángulo mostrados correctamente.')

# Invocamos al método area() y perimetro() de la clase Triangulo().
# Redondeamos los valores de las áreas y perímetros a 2 decimales.
print('')
print('---- RESULTADOS ----')
print('Área y perímetro del triángulo 1.')
triangulo1.area()
triangulo1.perimetro()
print('')
print('Área y perímetro del triángulo 2.')
triangulo2.area()
triangulo2.perimetro()
print('--> Área y perímetro mostrados correctamente.')

print('----------------------------------------------------------------------')
