#busca_sequencial

def busca(lista, x):
	for i in range(len(lista)):
		if lista[i] == x:
			return i
	return False

def main():
  print(busca([12, 13, 14, 15], 15))

main()