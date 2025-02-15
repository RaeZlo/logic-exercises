"""
Ejercicio 2: Combinar y limpiar listas
Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
Extiende lista_a con lista_b usando extend().
Elimina la primera aparición del número 1 en lista_a usando remove().
Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
Limpia completamente lista_b usando clear().
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

# Extender lista_a con los elementos de lista_b
lista_a.extend(lista_b)

# Eliminar la primera aparición del número 1 en lista_a
lista_a.remove(1)

# Eliminar el elemento en el índice 3 de lista_a y guardar el valor eliminado
elemento_eliminado = lista_a.pop(3)

# Imprimir el elemento que fue eliminado con pop()
print(f"Elemento eliminado: {elemento_eliminado}")  # Output: Elemento eliminado: 5

# Limpiar completamente lista_b
lista_b.clear()

print("Lista a:", lista_a)  # Output: Lista a: [2, 3, 4, 6, 1, 2]
print("Lista b:", lista_b)  # Output: Lista b: []
