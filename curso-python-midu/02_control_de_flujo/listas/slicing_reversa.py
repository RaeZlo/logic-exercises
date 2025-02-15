"""
Ejercicio 6: Reversa parcial
Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
"""

lista = [1, 2, 3, 4, 5, 6]

# Calcular el índice central para dividir la lista
centro = len(lista) // 2

# Invertir solo la primera mitad de la lista usando slicing y concatenación
primera_mitad_invertida = lista[0:centro][::-1]  # Invertir la primera mitad
segunda_mitad = lista[centro:]  # Mantener la segunda mitad igual

# Concatenar las dos partes para obtener el resultado final
resultado = primera_mitad_invertida + segunda_mitad

print(resultado)
