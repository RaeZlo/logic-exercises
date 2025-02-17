"""
Ejercicio 3: Factorial de un número
Pide al usuario que introduzca un número entero positivo.
Calcula su factorial usando un bucle while.
El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. 
Por ejemplo, el factorial de 5
5! = 5 x 4 x 3 x 2 x 1 = 120.
"""

numero = int(input("Ingresa un número entero positivo: "))

# Se inicializan dos variables: contador y factorial, ambas en 1.
# 'contador' servirá para recorrer los números desde 1 hasta el número introducido.
# 'factorial' almacenará el resultado del producto de esos números.
contador, factorial = 1, 1

# Se utiliza un bucle while para calcular el factorial
# El bucle continuará mientras el valor de 'contador' sea menor o igual al número ingresado.
while contador <= numero:
    # En cada iteración, se multiplica 'factorial' por el valor actual de 'contador'
    factorial *= contador
    # Se incrementa 'contador' en 1 para pasar al siguiente número
    contador += 1

print(f"El factorial de {numero} es: {factorial}")
