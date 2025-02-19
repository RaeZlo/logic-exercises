"""
Ejercicio 2: Imprimir números impares del 1 al 20
Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
"""
for num in range(1, 21, 2):
    print(num)

# Alternativa
for num in range(1, 21):
    if num % 2 != 0:
        print(num)
