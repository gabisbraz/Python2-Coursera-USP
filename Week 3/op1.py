class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.a = lado1
		self.b = lado2
		self.c = lado3

	def retangulo(self):
		if self.a % 3 == 0 and self.b % 4 == 0 and self.c % 5 == 0:
			return True
		else:
			return False

def main():
	t = Triangulo(3, 4, 5)
	print(t.retangulo())

main()