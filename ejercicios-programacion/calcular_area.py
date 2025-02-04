"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
"""

class Poligono:
    def calcular_area(self):
        pass

class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Rectangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

triangulo = Triangulo(5, 10)
cuadrado = Cuadrado(4)
rectangulo = Rectangulo(3, 6)

print("Área del triángulo:", triangulo.calcular_area())
print("Área del cuadrado:", cuadrado.calcular_area())
print("Área del rectángulo:", rectangulo.calcular_area())
