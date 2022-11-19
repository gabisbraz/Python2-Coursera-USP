#número de colunas da primeira == número de linhas da segunda

def sao_multiplicaveis(m1, m2) :
	qtd_colunas1 = len(m1[0])
	qtd_linhas2 = len(m2)
	if qtd_colunas1 == qtd_linhas2:
		return True
	else:
		return False

def main():
	m1 = [[1], [2], [3]]
	m2 = [[1, 2, 3]]
	print(sao_multiplicaveis(m1, m2))

main()