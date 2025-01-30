"""
Crea una función que tome un número entero como parámetro y retorne 
su valor negativo. Si el número ya es negativo, debe retornar el mismo número.
"""

def numero_negativo(numero: int) -> int:
    # Se utiliza un operador ternario para determinar el resultado:
    # Si el número es mayor que 0, lo negamos.
    # De lo contrario (si es menor o igual a 0), retornamos el mismo número.
    return -numero if numero > 0 else numero

respuesta = numero_negativo(-8)
print(respuesta)  # Imprime -8 (el número ya era negativo)

respuesta = numero_negativo(5)
print(respuesta)  # Imprime -5 (el número era positivo)

respuesta = numero_negativo(0)
print(respuesta)  # Imprime 0 (el número era cero)
