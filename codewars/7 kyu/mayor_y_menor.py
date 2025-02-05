"""
Crea una función que reciba una cadena de números enteros separados por 
espacios y devuelva el número más alto y el número más bajo en formato de cadena.
"""

def mayor_y_menor(numbers: str) -> str:
    # Convertimos la cadena en una lista de enteros y se ordena de menor a mayor
    numbers = sorted([int(i) for i in numbers.split()])
    # Retornamos el número mayor (último en la lista ordenada) y el número menor (primero en la lista ordenada)
    return f"{numbers[-1]} {numbers[0]}"

def alternativa(numbers:str) -> str:
    numbers = [int(i) for i in numbers.split()]
    return f"{max(numbers)} {min(numbers)}"


respuesta = mayor_y_menor("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(respuesta)  # Salida esperada: "42 -9"

respuesta2 = mayor_y_menor("1 9 3 4 -5")
print(respuesta2) # Salida esperada: "9 -5"
