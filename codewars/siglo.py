"""
Crea una función que determine el siglo al que pertenece un año dado.
"""

def siglo(anio:int) -> int:
    # Sumamos 99 al año para asegurar que los años que terminan en 00 (como 1900, 2000)
    # se asignen al siglo siguiente.
    # Luego, hacemos una división entera por 100 para obtener el número del siglo.
    return (anio + 99) // 100

respuesta = siglo(1999)
print(respuesta)
