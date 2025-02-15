"""
Ejercicio 1: Añadir y modificar elementos
Crea una lista con los números del 1 al 5.
Añade el número 6 al final usando append().
Inserta el número 10 en la posición 2 usando insert().
Modifica el primer elemento de la lista para que sea 0.
"""

# Crear la lista inicial con los números del 1 al 5
lista = [1, 2, 3, 4, 5]

# Añadir el número 6 al final de la lista
lista.append(6)

# Insertar el número 10 en la posición 2
lista.insert(2, 10)

# Modificar el primer elemento de la lista para que sea 0
lista[0] = 0

print(lista)  # Output: [0, 2, 10, 3, 4, 5, 6]
