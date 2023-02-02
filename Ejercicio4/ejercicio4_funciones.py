'''
EJERCICIO 4 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 4 --> Funciones

4. Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario
con las palabras que contiene y su longitud.
Por ejemplo, la función recibe la frase ‘Hola y adiós’ y devuelve un diccionario de la forma
{‘Hola’:4, ‘y’:1, ‘adiós’:5}
'''

print('**********************************************************************')
print('EJERCICIO 4 --> Funciones')
print('----------------------------------------------------------------------')

# Escribimos la función palabrasLongitud(frase).
def palabrasLongitud(frase):
    # Lo que hace la funcion es generar un diccionario con las palabras de la frase y su longitud.
    # Creamos un diccionario vacío.
    diccionario = {}
    # Separamos la frase en palabras.
    palabras = frase.split() # split() sin parámetros separa por espacios.
    # Recorremos la lista de palabras.
    for i in palabras:
        # Añadimos al diccionario la palabra y su longitud.
        diccionario[i] = len(i) # len() devuelve la longitud de un string.
    # Devolvemos el diccionario.
    return diccionario # Devolvemos el diccionario.

# Creamos una frase.
frase = 'Hola y adiós'
# Llamamos a la función palabrasLongitud(frase) y le pasamos la frase.
print('Resuelto 1')
print(palabrasLongitud(frase))
print('------------------------------------')

# Creamos otra frase.
frase = 'Hola, me llamo Diego'
# Llamamos a la función palabrasLongitud(frase) y le pasamos la frase.
print('Resuelto 2')
print(palabrasLongitud(frase))
