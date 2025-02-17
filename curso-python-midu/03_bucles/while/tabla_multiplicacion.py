"""
Ejercicio 5: Tabla de multiplicar
Pide al usuario que introduzca un número.
Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
"""

numero = int(input("Ingrese un número: "))

# Inicializamos el contador en 1 (comienza desde 1 para la tabla de multiplicar)
contador = 1

# El bucle continuará mientras el contador sea menor o igual a 10
while contador <= 10:
    # Calculamos el resultado de la multiplicación
    tabla = numero * contador
    # Imprimimos el resultado de la multiplicación
    print(f"{numero} x {contador} = {tabla}")
    # Incrementamos el contador para la siguiente multiplicación
    contador += 1
