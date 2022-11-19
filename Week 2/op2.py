def primeiro_lex(lista):
	elemento1 = lista[0]
	for elemento2 in lista:
		if elemento1 > elemento2:
			elemento1 = elemento2
	return elemento1

print(primeiro_lex(['AAAAAA', 'b']))