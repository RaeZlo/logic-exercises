"""
Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
"""

lista = ["Manzana", "pera", "BANANA", "naranja"]

# Ordenar la lista sin diferenciar entre mayúsculas y minúsculas
# Usamos key=str.lower para comparar las cadenas sin tener en cuenta las mayúsculas/minúsculas
lista.sort(key=str.lower)

print(lista)  # Output: ['BANANA', 'Manzana', 'naranja', 'pera']
