def soma_matrizes(m1, m2):
	qtd_linhas1 = len(m1)
	qtd_colunas1 = len(m1[0])
	qtd_linhas2 = len(m2)
	qtd_colunas2 = len(m2[0])
	soma_matrizes = []
	if qtd_linhas1 == qtd_linhas2 and qtd_colunas1 == qtd_colunas2:
		for i in range(qtd_linhas1):
			soma_matrizes.append([])
			for k in range(qtd_colunas1):
				soma_matrizes[i].append(m1[i][k] + m2[i][k])
		return soma_matrizes
	else:
		return False

def main():
	m1 = [[1, 2, 3], [4, 5, 6]]
	m2 = [[2, 3, 4], [5, 6, 7]]
	print(soma_matrizes(m1, m2))

main()