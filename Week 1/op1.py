def imprime_matriz(minha_matriz):
	for i in range(len(minha_matriz)):
			print(*minha_matriz[i])

def main():
	minha_matriz = [[1, 2], [3, 4]]
	imprime_matriz(minha_matriz)

main()