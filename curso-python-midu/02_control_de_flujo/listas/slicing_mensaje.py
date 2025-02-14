"""
Ejercicio 1: El mensaje secreto
Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
"""

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

# Utilizamos slicing para obtener los elementos de la lista "mensaje" que corresponden al mensaje "secreto".
# Empezamos desde el índice 7 (el primer carácter de "s") hasta el final de la lista.
# El índice 7 es el primero donde aparece la letra "s", que forma parte de la palabra "secreto".
# Al no especificar el índice final en el slicing, Python incluirá todos los elementos hasta el final de la lista.
print(mensaje[7:])  # El resultado será la lista que contiene ["s", "e", "c", "r", "e", "t", "o"]
