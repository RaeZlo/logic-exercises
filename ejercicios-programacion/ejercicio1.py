"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    # Iteramos a través de los números del 1 al 100 (inclusive)
    for number in range(1, 101):
        # Si el número es múltiplo de 3 y de 5, se imprime "FizzBuzz"
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # Si solo es múltiplo de 3, se imprime "Fizz"
        elif number % 3 == 0:
            print("Fizz")
        # Si solo es múltiplo de 5, se imprime "Buzz"
        elif number % 5 == 0:
            print("Buzz")
        # Si no es múltiplo ni de 3 ni de 5, se imprime el número
        else:
            print(number)

# Llamada a la función para ejecutar el programa
fizzbuzz()
