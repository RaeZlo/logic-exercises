"""
Ejercicio 2: Suma de números pares (while)
Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
"""

contador = 1
suma_pares = 0
while contador <= 20:
    if contador % 2 == 0:
        suma_pares += contador
    contador += 1

print(f"La suma de los números pares hasta 20 es: {suma_pares}")
