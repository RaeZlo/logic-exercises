"""
Crea una función que reciba un número entero no negativo y reorganice sus dígitos 
en orden descendente (de mayor a menor) para formar el número más grande posible.
"""

def orden_descendente(num: int) -> int:
    # Convertimos el número a una cadena para poder separar sus dígitos
    # Ordenamos los dígitos en orden descendente usando sorted() con reverse=True
    # Unimos los dígitos ordenados en una nueva cadena y la convertimos a entero
    return int("".join(sorted(str(num), reverse=True)))

respuesta = orden_descendente(42145)
print(respuesta)  # Salida esperada: 54421
