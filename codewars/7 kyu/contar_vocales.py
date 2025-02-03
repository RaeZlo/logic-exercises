"""
Crea una función que cuente el número de ocurrencias de las vocales (A, E, I, O, U) en una cadena, 
tanto en mayúsculas como en minúsculas.
"""

def contar_vocales(cadena: str) -> int:
    # Utilizamos una expresión generadora para iterar sobre cada letra de la cadena.
    # Si la letra está presente en el conjunto de vocales, se suma 1 a un contador implícito.
    # Finalmente, la función sum() calcula la suma total de estos 1s, que corresponde al número de vocales.
    return sum(1 for letra in cadena if letra in "AEIOUaeiou")

respuesta = contar_vocales("pepe es raro")
print(respuesta)
