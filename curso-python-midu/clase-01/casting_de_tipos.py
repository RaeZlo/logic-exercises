"""
Ejercicio 3: Casting de tipos
Convierte la cadena 12345 a un entero y luego a un float.
Convierte el float 3.99 a un entero. ¿Qué ocurre?
"""

a = "12345"
print(f"De cadena a entero: {int(a)}")  # Convierte la cadena "12345" a un entero
print(f"De cadena a float: {float(a)}")  # Convierte la cadena "12345" a un float

b = 3.99
print(f"De float a entero: {int(b)}")  # Convierte 3.99 a un entero, perdiendo los decimales
