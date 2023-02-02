'''
EJERCICIO 2 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 2 --> Funciones

2. Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números
enteros. Se mostrará un histograma cuyas columnas midan el valor de los números.
Por ejemplo: histograma([4, 9, 2,7]) debería imprimir lo siguiente:
****
*********
**
*******
'''

print('**********************************************************************')
print('EJERCICIO 2 --> Funciones')
print('----------------------------------------------------------------------')

# Escribimos la función histograma(lista_números).
def histograma(lista_numeros):
    # Lo que hace la funcion es generar un histograma.
    for i in lista_numeros:
        print('*' * i)
    # Devolvemos el valor de la cadena.
    return lista_numeros

# Llamamos a la función histograma y le pasamos la lista [4, 9, 2, 7].
print('Resuelto 1')
histograma([4, 9, 2, 7])
print('------------------------------------')

# Hacemos otra prueba con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
print('Resuelto 2')
histograma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])