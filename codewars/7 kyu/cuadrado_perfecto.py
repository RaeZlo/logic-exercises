"""
Crea una función que determine si un número entero no negativo es un cuadrado perfecto.
"""

def cuadrado_perfecto(numero:int) -> bool:
    # Verificamos que el número sea no negativo y que su raíz cuadrada sea un número entero.
    # Si la raíz cuadrada tiene un residuo de 0 al dividir por 1, significa que es un número entero y, 
    # por lo tanto, el número original es un cuadrado perfecto.
    return numero >= 0 and (numero ** 0.5) % 1 == 0

respuesta = cuadrado_perfecto(25)
print(respuesta) # Respuesta esperada: True
