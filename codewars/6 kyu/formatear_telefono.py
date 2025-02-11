"""
Implementa una función que reciba una lista de 10 dígitos numéricos y los convierta en un 
formato de número telefónico estándar.
El formato esperado es:
(XXX) XXX-XXXX
"""

def formatear_telefono(numeros: list) -> str:
    # Verificamos que la lista tenga exactamente 10 dígitos
    if len(numeros) == 10:
        # Utilizamos el operador * para desempaquetar la lista en la plantilla de formato
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*numeros)
    
    # Si la lista no tiene 10 elementos, devolvemos un mensaje de error
    return "Error: La lista debe contener exactamente 10 números."

print(formatear_telefono([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # (123) 456-7890
print(formatear_telefono([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # (987) 654-3210
print(formatear_telefono([1, 2, 3]))  # Error: La lista debe contener exactamente 10 números.
