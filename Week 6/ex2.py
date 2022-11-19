def encontra_impares(lista):
	if len(lista) == 0:
		return []
	num = lista.pop(0)
	if num % 2 != 0:
		return [num] + encontra_impares(lista)
	return encontra_impares(lista)

print(encontra_impares([2, 5, 6, 3]))