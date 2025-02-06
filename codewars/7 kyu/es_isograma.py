"""
Crea una función que determine si una palabra es un isograma.
Un isograma es una palabra en la que ninguna letra se repite, sin importar si está en mayúsculas o minúsculas.
"""

def es_isograma(palabra:str) -> bool:
    # Convertimos la palabra a minúsculas y la almacenamos en un conjunto.
    # El conjunto `set()` elimina automáticamente las letras repetidas.
    # Si la cantidad de letras únicas es igual a la longitud original de la palabra,
    # significa que no hay letras repetidas y es un isograma.
    return len(set(palabra.lower())) == len(palabra) 

respuesta = es_isograma("perro")
print(respuesta) # Salida esperada: False
