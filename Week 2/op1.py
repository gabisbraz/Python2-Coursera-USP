def conta_letras(frase, contar="vogais"):
	vogal = ["a", "e", "i", "o", "u"]
	cont_vogal = 0
	cont_consoante = 0
	for letra in frase:
		if letra.lower() in vogal:
			cont_vogal += 1
		elif letra.lower() not in vogal and letra != " ":
			cont_consoante += 1
	if contar == "vogais" or contar == None:
		return cont_vogal
	else:
		return cont_consoante

print(conta_letras('programamos em python', 'consoantes'))
