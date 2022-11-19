def maiusculas(frase):
	maiusculas = []
	resultado = ""
	for letra in frase:
		if letra >= chr(65) and letra <= chr(90):
			maiusculas.append(letra)
	for letra in maiusculas:
		resultado += letra
	return resultado

print(maiusculas("FraSe"))