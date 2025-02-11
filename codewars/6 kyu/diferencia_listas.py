"""
Implementa una función que calcule la diferencia entre dos listas.
La función debe eliminar todas las coincidencias entre los elementos en la primera lista que 
también estén presentes en la segunda lista.
El orden de los elementos en la primera lista debe mantenerse en el resultado.
"""

def diferencia_listas(lista1: list, lista2: list) -> list:
    # Utilizamos una comprensión de listas para filtrar los elementos de lista1.
    # Para cada elemento "i" en lista1, verificamos si NO está en lista2.
    # Si "i" no está en lista2, lo incluimos en la nueva lista.
    return [i for i in lista1 if i not in lista2]

# Pruebas
print(diferencia_listas([1, 2], [1]))  # [2]
print(diferencia_listas([1, 2, 2, 2, 3], [2]))  # [1, 3]
print(diferencia_listas(["a", "b", "c"], ["b"]))  # ["a", "c"]
print(diferencia_listas([5, 10, 15, 20], [10, 20]))  # [5, 15]
print(diferencia_listas([], [1, 2, 3]))  # []
