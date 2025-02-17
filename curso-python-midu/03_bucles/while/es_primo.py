"""
Ejercicio 6: Números primos hasta N
Pide al usuario que introduzca un número entero positivo N.
Imprime todos los números primos menores o iguales que N usando un bucle while.
Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.
"""

# Pedimos al usuario que ingrese un número entero positivo N
N = int(input("Ingrese un número entero positivo N: "))

# Comenzamos con el primer número que podría ser primo, es decir, el 2
numero = 2

# Utilizamos un bucle while para recorrer todos los números desde 2 hasta N
while numero <= N:
    # Verificamos si 'numero' es primo
    es_primo = True  # Suponemos que el número es primo al principio
    
    # Comprobamos si el número es divisible por algún número entre 2 y la raíz cuadrada de 'numero'
    divisor = 2
    while divisor <= (numero // 2):
        if numero % divisor == 0:  # Si 'numero' es divisible por 'divisor', no es primo
            es_primo = False
            break  # Salimos del bucle, ya que no es primo
        divisor += 1
    
    # Si es primo, lo imprimimos
    if es_primo:
        print(numero)
    
    # Incrementamos 'numero' para verificar el siguiente número
    numero += 1
