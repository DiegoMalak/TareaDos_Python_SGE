'''
EJERCICIO 5 DE LA SEGUNDA PRÁCTICA DE PYTHON
EJERCICIO 5 --> Funciones

5. Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las
asignaturas y las notas numéricas de un alumno y devuelva otro diccionario con las asignaturas en
mayúsculas y las calificaciones correspondientes a las notas con palabras.

El criterio será el siguiente: nota <5 → Suspenso; 5 <= nota < 7 → Aprobado;
7 <= nota < 9 → Notable; 9 <= nota <=10 → Sobresaliente. La nota no puede sobrepasar 10.

Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}
y devuelve el diccionario {'ANDROID’:’Notable’, ‘HILOS’:’Aprobado’, ‘PYTHON’:’Sobresaliente’,
‘INTERFACES’:’Suspenso’ }
'''

print('**********************************************************************')
print('EJERCICIO 5 --> Funciones')
print('----------------------------------------------------------------------')


# Escribimos la función calificaPalabras(diccionario).
def calificaPalabras(diccionario):
    # Creamos un diccionario vacío.
    diccionario_calificaciones = {}
    # Recorremos el diccionario.
    for i in diccionario:
        # Creamos una variable para almacenar la nota.
        nota = diccionario[i]
        # Creamos una variable para almacenar la calificación.
        calificacion = ''
        # Comprobamos la nota y asignamos la calificación correspondiente.
        # Ya que nos dan la nota en números.
        if nota < 5:
            calificacion = 'Suspenso'
        elif nota >= 5 and nota < 7:
            calificacion = 'Aprobado'
        elif nota >= 7 and nota < 9:
            calificacion = 'Notable'
        elif nota >= 9 and nota <= 10:
            calificacion = 'Sobresaliente'
        # Añadimos al diccionario la asignatura en mayúsculas y su calificación.
        diccionario_calificaciones[i.upper()] = calificacion  # Añadimos al diccionario la asignatura en mayúsculas
        # y su calificación.
    # Devolvemos el diccionario.
    return diccionario_calificaciones


# Creamos un diccionario con las asignaturas y las notas numéricas de un alumno.
print('Resuelto 1')
diccionario = {'Android': 8.2, 'Hilos': 5, 'Python': 9.3, 'Interfaces': 4.4}
# Llamamos a la función calificaPalabras(diccionario) y le pasamos el diccionario.
print(calificaPalabras(diccionario))
print('------------------------------------')

# Creamos otro diccionario con las asignaturas y las notas numéricas de un alumno.
print('Resuelto 2')
diccionario = {'Android': 9.2, 'Hilos': 8, 'Python': 10, 'Interfaces': 8.6, 'Base de datos': 8}
# Llamamos a la función calificaPalabras(diccionario) y le pasamos el diccionario.
print(calificaPalabras(diccionario))