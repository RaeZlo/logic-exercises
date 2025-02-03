"""
Crea una función que elimine todas las vocales (a, e, i, o, u) de una cadena, 
tanto en mayúsculas como en minúsculas.
"""

def remover_vocales(palabra: str) -> str:
    for letra in "aeiouAEIOU":
        # Iteramos sobre cada vocal y la reemplazamos por una cadena vacía en la palabra.
        # El método replace() modifica la cadena original y devuelve una nueva cadena.
        palabra = palabra.replace(letra, "")
    return palabra

def alternativa(palabra: str) -> str:
    # Creamos una nueva cadena concatenando solo las letras que no son vocales.
    # La expresión generadora `letra for letra in palabra if letra not in "aeiou"` crea una nueva cadena
    # con las letras que cumplen la condición.
    return "".join(letra for letra in palabra if letra not in "aeiouAEIOU")

respuesta1 = remover_vocales("pepe es raro")
print(respuesta1)

respuesta2 = alternativa("Mara es alta")
print(respuesta2)
