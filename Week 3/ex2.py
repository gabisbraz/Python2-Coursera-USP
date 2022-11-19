class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.a = lado1
		self.b = lado2
		self.c = lado3

	def tipo_lado(self):
		if self.a == self.b  and self.b  == self.c:
			return "equilátero"
		elif self.a == self.b  or self.a == self.c or self.b  == self.c:
			return "isósceles"
		elif self.a != self.b  and self.a != self.c and self.b != self.c:
			return "escaleno"

def main():
	t = Triangulo(4, 5, 8)
	print(t.tipo_lado())

main()