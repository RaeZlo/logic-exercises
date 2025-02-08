"""
Crea una función que reciba una lista de nombres y devuelva una nueva lista con solo aquellos 
nombres que tienen exactamente 4 letras.
"""

def filtrar_amigos(nombres: list) -> list:
    # Filtramos los nombres usando comprensión de listas
    # Solo se incluyen aquellos que tengan exactamente 4 caracteres.
    
    return [nombre for nombre in nombres if len(nombre) == 4]

respuesta = filtrar_amigos(["pepe", "amparo", "lara", "armando"])
print(respuesta)  # Salida esperada: ['pepe', 'lara']
