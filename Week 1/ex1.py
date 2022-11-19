def dimensoes(matriz):
	qtd_linhas = len(matriz)
	qtd_colunas = len(matriz[0])
	print("{}X{}" .format(qtd_linhas, qtd_colunas))


minha_matriz = [[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]]
dimensoes(minha_matriz)