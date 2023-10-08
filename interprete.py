from tipoToken import tipoToken
from Token import Token
import os

#Para mandar los tokens de salida
estructura=Token('','',None)

#Para identificar una cadena
def identificador(cad):
	j=1
	if cad[0].isalpha():
		for i in cad:
			if i.isdigit() or i.isalpha() or i=='_' or i=='-':
				j+=1
			else:
				break
		print(Token(tipoToken.IDENTIFIER,cad[:j-1],None).toString())
		estructura.almacenar(tipoToken.IDENTIFIER,cad[:j-1],None)
		return j-1

def identificar(cad):
	j=1#Para identificar los literales
	aux=1

	return 0

#Funcion para manipular el texto desde un archivo 
def scanerArchivo(cont):
	j=0
	bandera=0
	for i in range(0,len(cont)):
		if j>=len(cont):
			break
		else:
			bandera=identificar(cont[j:])
		if bandera>1:
			j+=bandera
		else:
			j+=1

#Funcion que analice el texto
def lineaComando():
	os.system('clear')
	while True:
		j=0
		bandera=0
		print('\n>>> ',end='')
		cadena=input()
		for i in range(0,len(cadena)):
			if j>=len(cadena):
				break
			else:
				bandera=identificar(cadena[j:])
			if bandera>1:
				j+=bandera
			else:
				j+=1
