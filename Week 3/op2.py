class Triangulo:

    triangulo = []
    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3
        triangulo = [self.a, self.b, self.c]

    def semelhantes(self, triangulo):
        q = self.a / triangulo.a
        if q == self.b / triangulo.b and q == self.c / triangulo.c:
            return True
        else:
            return False

def main():
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 8, 10)
    print(t1.semelhantes(t2))

main()