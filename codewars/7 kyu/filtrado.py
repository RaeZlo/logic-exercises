"""
Crea una función que reciba una lista de números enteros no negativos y cadenas de texto. 
La función debe retornar una nueva lista que contenga únicamente los números enteros, 
eliminando cualquier cadena de texto.
"""

def filtrado(lista:list) -> list:
    # Utilizamos una comprensión de listas para recorrer cada elemento de la lista original.
    # Por cada elemento 'i' en la lista, verificamos si su tipo de dato es 'int'.
    # Si es un número entero, lo incluimos en la nueva lista; de lo contrario, lo descartamos.
    return [i for i in lista if type(i) == int]

respuesta = filtrado([1,2,'a','b'])
print(respuesta) # Salida esperada: [1, 2]
