def menor_nome(nomes):
	menor = len(nomes[0])
	nome = nomes[0]
	for i in range(len(nomes)-1):
		x = len(nomes[i].strip())
		if menor > x:
			menor = x
			nome = nomes[i]
	return nome.strip().capitalize()

menor = menor_nome(['zé', ' lu', 'fê'])
print(menor)

