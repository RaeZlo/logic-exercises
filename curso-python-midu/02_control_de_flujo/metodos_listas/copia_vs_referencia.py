"""
Ejercicio 5: Copia vs. Referencia
Crea una lista llamada original con los números [1, 2, 3].
Crea una copia de la lista original llamada copia_1 usando slicing.
Crea otra copia llamada copia_2 usando copy().
Crea una referencia a la lista original llamada referencia.
Modifica el primer elemento de la lista referencia a 10.
Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
"""

original = [1, 2, 3]

# Crear una copia de la lista original usando slicing
# El slicing crea una nueva lista en memoria, independiente de la original
copia_1 = original[:]  # Copia superficial

# Crear una copia usando el método copy()
# Similar al slicing, copy() crea una nueva lista independiente de la original
copia_2 = original.copy()  # Copia superficial

# Crear una referencia a la lista original
# 'referencia' no es una copia, es una referencia directa a la lista original
referencia = original  # Referencia a la lista original

# Modificar el primer elemento de la lista 'referencia'
# Dado que 'referencia' es una referencia a 'original', al cambiarla, 
# también cambiamos 'original', porque ambas apuntan al mismo lugar en memoria
referencia[0] = 10

# Imprimir todas las listas para observar los cambios
print(f"Original: {original}")       # Output: Original: [10, 2, 3]
print(f"Copia 1 (slicing): {copia_1}") # Output: Copia 1 (slicing): [1, 2, 3]
print(f"Copia 2 (copy()): {copia_2}") # Output: Copia 2 (copy()): [1, 2, 3]
print(f"Referencia: {referencia}")     # Output: Referencia: [10, 2, 3]

# Comentarios adicionales:
# - 'copia_1' y 'copia_2' son copias superficiales de la lista 'original'.
# - 'referencia' no es una copia, es solo otro nombre para la misma lista en memoria.
# - Si modificamos 'referencia', estamos modificando 'original', ya que ambos 
#   apuntan a la misma ubicación en memoria.
