def busca(lista, elemento):
	inicio = 0
	final = len(lista) - 1
	while inicio <= final:
		meio = (inicio + final) // 2
		print(meio)
		if lista[meio] == elemento:
			return meio
		else:
			if elemento < lista[meio]:
				final = meio - 1
			else:
				inicio = meio + 1
	return False
