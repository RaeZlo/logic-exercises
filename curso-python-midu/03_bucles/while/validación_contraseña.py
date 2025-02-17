"""
Ejercicio 4: Validación de contraseña
Pide al usuario que introduzca una contraseña.
La contraseña debe tener al menos 8 caracteres.
Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
Si la contraseña es válida, imprime "Contraseña válida".
"""

contrasenia = ""

# El bucle seguirá pidiendo una contraseña mientras su longitud sea menor a 8 caracteres
while len(contrasenia) < 8:
    contrasenia = input("Ingrese una contraseña: ")
    
    # Si la longitud de la contraseña es menor a 8, se le pide al usuario que ingrese una nueva
    if len(contrasenia) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")
