"""
Ejercicio 6: Tabla de multiplicar
Pide al usuario que introduzca un número.
Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
"""

numero = int(input("Ingresa un número: "))
for num in range(1, 11):
    print(numero * num)
