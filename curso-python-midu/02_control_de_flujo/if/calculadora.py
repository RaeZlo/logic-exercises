"""
Ejercicio 2: Calculadora simple
Pide al usuario dos números y una operación (+, -, *, /)
Realiza la operación y muestra el resultado (maneja la división entre zero)
"""

num1 = int(input("Ingresa el primer número de la operación: "))
num2 = int(input("Ingresa el segundo número de la operación: "))
operador = input("Ingresa el operador (+, -, *, /): ")

if operador == "+":
    resultado = f"El resultado de la suma es: {num1+num2}"
elif operador == "-":
    resultado = f"El resultado de la resta es: {num1-num2}"
elif operador == "*":
    resultado = f"El resultado de la multiplicación es: {num1*num2}"
elif operador == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = f"El resultado de la división es: {num1/num2}"

if "resultado" in locals():
    print(resultado)
