'''
EJERCICIO 1 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 1 --> Funciones

1. Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número
entero n y un carácter. Devolverá el carácter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el
número.
'''

print('**********************************************************************')
print('EJERCICIO 1 --> Funciones')
print('----------------------------------------------------------------------')

# Escribimos la función generar_n_caracteres(n, carácter).
def generar_n_caracteres(n, caracter):
    # Lo que hace la funcion es generar 'n' caracteres.
    print(caracter * n)
    # Devolvemos el valor de la cadena.
    return caracter * n

# Llamamos a la función generar_n_caracteres y le pasamos el número 5 y el carácter 'x'.
print('Resuelto 1')
generar_n_caracteres(5, 'x')
print('------------------------------------')

# Hacemos otra prueba con el número 10 y el carácter 'diego'.
print('Resuelto 2')
generar_n_caracteres(10, 'diego')