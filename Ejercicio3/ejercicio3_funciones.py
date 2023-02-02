'''
EJERCICIO 3 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 3 --> Funciones

3. Escribe una función funcionLista(función, lista) que reciba otra función creada
anteriormente y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada
uno de los elementos de la lista.
Por ejemplo, la función que se le pasa calcula el cubo de un número.
La lista que se pasa es una lista de números enteros. A cada número de la lista se le aplica la
función y se calculará el cubo de todos ellos, mostrándolos en otra lista nueva.
Si la lista que se pasara fuera [1,2,3,4,5] la función devolvería [1,8,27,64,125]
'''

print('**********************************************************************')
print('EJERCICIO 3 --> Funciones')
print('----------------------------------------------------------------------')

# Escribimos la función funcionLista(función, lista).
def funcionLista(funcion, lista):
    # Creamos una lista vacía para guardar los resultados.
    lista_resultados = []
    # Recorremos la lista.
    for elemento in lista:
        # Añadimos el resultado de la función a la lista vacía.
        lista_resultados.append(funcion(elemento))
    # Devolvemos la lista con los resultados.
    return lista_resultados

# Creamos una función que calcula el cubo de un número.
def cubo(numero):
    return numero ** 3
# Creamos una lista con los números del 1 al 5.
lista = [1, 2, 3, 4, 5]
# Llamamos a la función funcionLista(función, lista) y le pasamos la función cubo y la lista.
print('Resuelto 1 - Cubo')
print(funcionLista(cubo, lista))

# Creamos una función que calcula el cuadrado de un número.
def cuadrado(numero):
    return numero ** 2
# Creamos una lista con los números del 1 al 5.
lista = [1, 2, 3, 4, 5]
# Llamamos a la función funcionLista(función, lista) y le pasamos la función cuadrado y la lista.
print('Resuelto 2 - Cuadrado')
print(funcionLista(cuadrado, lista))