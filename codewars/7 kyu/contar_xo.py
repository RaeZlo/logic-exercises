"""
Crea una función que determine si una cadena de texto contiene la misma cantidad de letras 
'x' y 'o', sin importar mayúsculas o minúsculas.
Si el número de 'x' y 'o' es el mismo, la función debe retornar True; en caso contrario, debe retornar False.
"""

def contar_xo(palabra: str) -> bool:
    # Convertimos la palabra a minúsculas para ignorar diferencias entre 'X' y 'x'.
    palabra = palabra.lower()
    # Contamos cuántas veces aparecen 'x' y 'o' en la cadena.
    return palabra.count("x") == palabra.count("o")

def alternativa(palabra:str) -> bool:
    x, o = 0
    for char in palabra.lower():
        if char == "x":
            x += 1
        elif char == "o":
            o += 1
    return x == o

respuesta = contar_xo("xoxp")
print(respuesta) # Respuesta esperada: False

respuesta2 = alternativa("xxoo")
print(respuesta2)
