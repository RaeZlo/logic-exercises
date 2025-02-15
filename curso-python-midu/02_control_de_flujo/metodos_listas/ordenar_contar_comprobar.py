"""
Ejercicio 4: Ordenar y contar
Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
Ordena la lista de forma ascendente usando sort().
Cuenta cuántas veces aparece el número 2 en la lista usando count().
Comprueba si el número 7 está en la lista usando in.
"""

lista = [5, 2, 8, 1, 9, 4, 2]

# Imprimir la lista original
print(f"Lista desordenada: {lista}")

# Ordenar la lista de forma ascendente con sort()
lista.sort()

# Imprimir la lista ordenada
print(f"Lista ordenada: {lista}")

# Contar cuántas veces aparece el número 2 en la lista
contar_2 = lista.count(2)

# Imprimir cuántas veces aparece el número 2
print(f"El 2 aparece {contar_2} veces.")

# Comprobar si el número 7 está en la lista usando 'in'
print(f"El 7 está presente en la lista: {7 in lista}")
