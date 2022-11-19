def ordenada(lista):
	for i in range(len(lista)):
		min = i
		for k in range(i + 1, len(lista)):
			if lista[min] > lista[k]:
				min = k
				return False
	return True

def main():
	print(ordenada([3, 6, 7, 9]))

main()