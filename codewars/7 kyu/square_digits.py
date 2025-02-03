"""
Eleva al cuadrado cada dígito de un número y concatena los resultados para formar un nuevo número.
"""

def square_digits(num):
    # Inicializamos una cadena vacía para almacenar los dígitos al cuadrado.
    resultado = ""
    for digito in str(num):
        # Convertimos el dígito (que es una cadena) a un número entero.
        # Elevamos el número al cuadrado.
        # Convertimos el resultado al cuadrado nuevamente a una cadena y lo concatenamos al resultado.
        resultado += str(int(digito) ** 2)
    # Convertimos la cadena resultante nuevamente a un número entero y lo retornamos.
    return int(resultado)

def alternativa(num):
    # La expresión generadora eleva al cuadrado cada dígito y lo convierte a una cadena.
    # La función join() concatena todas las cadenas resultantes en una sola cadena.
    # Finalmente, se convierte la cadena resultante a un número entero.
    return int("".join(str(int(digito)**2) for digito in str(num)))

respuesta1 = square_digits(9119)
print(respuesta1)

respuesta2 = alternativa(765)
print(respuesta2)
