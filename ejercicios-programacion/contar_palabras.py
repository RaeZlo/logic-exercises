"""
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que
 lo resuelvan automáticamente.
"""

import re  # Importamos el módulo `re` para trabajar con expresiones regulares.

def contar_palabras(texto: str) -> dict:
    
    # Normalizamos el texto a minúsculas y extraemos solo palabras y números
    palabras = re.findall(r"[a-zA-Z0-9]+", texto.lower())

    # Diccionario para almacenar la frecuencia de cada palabra
    contador_palabras = {}

    # Recorremos cada palabra en la lista
    for palabra in palabras:
        if palabra not in contador_palabras:
            contador_palabras[palabra] = 1  # Si la palabra no está en el diccionario, la agregamos con valor 1
        else:
            contador_palabras[palabra] += 1  # Si ya existe, incrementamos su contador

    return contador_palabras  # Retornamos el diccionario con los conteos

resultado = contar_palabras("Hola mundo, hola mundo. Este es un ejemplo, un ejemplo muy bueno.")
print(resultado)
