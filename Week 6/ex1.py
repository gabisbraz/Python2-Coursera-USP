def soma_lista(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		return soma_lista(lista[1:]) + lista[0]

print(soma_lista([7]))