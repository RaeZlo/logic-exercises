"""
Crea una función que reciba una palabra y una terminación y devuelva True si la palabra 
termina con la terminación indicada.
Además, crea una función alternativa que realice la misma verificación sin usar el método endswith().
"""

def termina_igual(palabra:str, terminacion:str) -> bool:
    # Utilizamos el método `.endswith()` para verificar si la palabra
    # termina con la cadena dada.
    return palabra.endswith(terminacion)


def alternativa(palabra:str, terminacion:str) -> bool:
    # Se obtiene el segmento final de la palabra con `[-len(ending):]`
    # y se compara con `ending` para ver si coinciden.
    return terminacion in palabra[-len(terminacion):]

respuesta = termina_igual("epep", "e")
print(respuesta)  # Salida esperada: False

respuesta2 = alternativa("Pedro", "ro")
print(respuesta2)  # Salida esperada: True
