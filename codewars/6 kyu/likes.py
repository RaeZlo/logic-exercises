"""
Crea una función que reciba una lista de nombres y devuelva un mensaje indicando cuántas personas 
han dado "me gusta", siguiendo estas reglas:
0 personas → "No hay me gustas."
1 persona → "{nombre} le dio me gusta."
2 personas → "{nombre1} y {nombre2} le dieron me gusta."
3 personas → "{nombre1}, {nombre2} y {nombre3} le dieron me gusta."
"""

def likes(nombres: list) -> str:
    match nombres:
        case []:  # Caso cuando la lista está vacía
            return "No hay me gustas."
        case [a]:  # Un solo nombre
            return f"{a} le dio me gusta."
        case [a, b]:  # Dos nombres
            return f"{a} y {b} le dieron me gusta."
        case [a, b, c]:  # Tres nombres
            return f"{a}, {b} y {c} le dieron me gusta."
        case [a, b, *rest]:  # Más de tres nombres
            return f"{a}, {b} y {len(rest)} más dieron me gusta."

print(likes([]))  # "No hay me gustas."
print(likes(["Pedro"]))  # "Pedro le dio me gusta."
print(likes(["Juan", "Ana"]))  # "Juan y Ana le dieron me gusta."
print(likes(["Carlos", "Lucía", "Marta"]))  # "Carlos, Lucía y Marta le dieron me gusta."
print(likes(["Juan", "Ana", "Carlos", "Luis"]))  # "Juan, Ana y 2 más dieron me gusta."
