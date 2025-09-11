class retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    def diagonal(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Base = {self.x}, Altura = {self.h}, Area = {self.area()}, Diagonal = {self.diagonal()}"