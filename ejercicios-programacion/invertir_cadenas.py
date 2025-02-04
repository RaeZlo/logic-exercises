"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadenas(palabra:str) -> str:
    # La sintaxis `palabra[::-1]` es una forma concisa de invertir una cadena en Python.
    # El slicing `[start:stop:step]` permite seleccionar subcadenas de una cadena:
    # - `start`: Índice inicial (inclusivo) del corte. Si se omite, se asume el inicio.
    # - `stop`: Índice final (exclusivo) del corte. Si se omite, se asume el final.
    # - `step`: Paso del corte. Un valor negativo (-1 en este caso) indica que se recorre la cadena de atrás hacia adelante.
    # Al omitir `start` y `stop` y usar un paso de -1, se obtiene una nueva cadena con los caracteres en orden inverso.
    return palabra[::-1]

respuesta = invertir_cadenas("Hola mundo")
print(respuesta)
