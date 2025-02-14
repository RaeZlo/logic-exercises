"""
Ejercicio 1: Determinar el mayor de dos números
Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 < num2:
    print(f"El número {num1} es menor que {num2}.")
elif num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
else:
    print(f"Los números {num1} y {num2} son iguales.")
