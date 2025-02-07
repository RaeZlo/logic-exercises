"""
Considere una matriz/lista de ovejas en la que puede faltar alguna oveja en su lugar. 
Necesitamos una función que cuente la cantidad de ovejas presentes en la matriz (verdadero significa presente).
"""

def contar_ovejas(lista: list) -> int:
    # La expresión generadora `o for o in lista if o is True` crea una secuencia de 1s 
    # donde cada 1 representa un valor True en la lista original.
    # La función `sum()` suma todos los elementos de esta secuencia, dando como resultado
    # el número total de valores True.
    return sum(ovejas for ovejas in lista if ovejas is True)

def alternativa(lista: list) -> int:
    # El método `count(True)` cuenta directamente el número de ocurrencias de True en la lista.
    return lista.count(True)

respuesta = contar_ovejas([True,  True,  True,  False,
                          True,  True,  True,  True ,
                          True,  False, True,  False,
                          True,  False, False, True ,
                          True,  True,  True,  True ,
                          False, False, True,  True])
print(respuesta)

respuesta = alternativa([True,  False, False, True ,
                        True,  True,  True,  True ,
                        False, False, True,  True])
print(respuesta)
