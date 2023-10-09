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

	#-----------------------------------Para saber cuando hay un comenatrio
	if cad[:2]=='/*':
		for i in range(2,len(cad[2:])):
			if cad[i]=='*' and cad[i+1]=='/':
				aux=j
			else:
				j+=1
		return aux+3
	elif cad[:2]=='//':
		for i in cad:
			if i=='\n':
				break
			else:
				j+=1
		return j
	elif cad[0]=='(':
		print(Token(tipoToken.LEFT_PAREN,cad[0],None).toString())
		estructura.almacenar(tipoToken.LEFT_PAREN,cad[0],None)
		return 0
	elif cad[0]==')':
		print(Token(tipoToken.RIGHT_PAREN,cad[0],None).toString())
		estructura.almacenar(tipoToken.RIGHT_PAREN,cad[0],None)
		return 0
	elif cad[0]=='{':
		print(Token(tipoToken.LEFT_BRACE,cad[0],None).toString())
		estructura.almacenar(tipoToken.LEFT_BRACE,cad[0],None)
		return 0
	elif cad[0]=='}':
		print(Token(tipoToken.RIGHT_BRACE,cad[0],None).toString())
		estructura.almacenar(tipoToken.RIGHT_BRACE,cad[0],None)
		return 0
	elif cad[0]==',':
		print(Token(tipoToken.COMMA,cad[0],None).toString())
		estructura.almacenar(tipoToken.COMMA,cad[0],None)
		return 0
	elif cad[0]=='.':
		print(Token(tipoToken.DOT,cad[0],None).toString())
		estructura.almacenar(tipoToken.DOT,cad[0],None)
		return 0
	elif cad[0]=='-':
		print(Token(tipoToken.MINUS,cad[0],None).toString())
		estructura.almacenar(tipoToken.MINUS,cad[0],None)
		return 0
	elif cad[0]=='+':
		print(Token(tipoToken.PLUS,cad[0],None).toString())
		estructura.almacenar(tipoToken.PLUS,cad[0],None)
		return 0
	elif cad[0]==';':
		print(Token(tipoToken.SEMICOLON,cad[0],None).toString())
		estructura.almacenar(tipoToken.SEMICOLON,cad[0],None)
		return 0
	elif cad[0]=='/':
		print(Token(tipoToken.SLASH,cad[0],None).toString())
		estructura.almacenar(tipoToken.SLASH,cad[0],None)
		return 0
	elif cad[0]=='*':
		print(Token(tipoToken.STAR,cad[0],None).toString())
		estructura.almacenar(tipoToken.STAR,cad[0],None)
		return 0
	#-------------------Para cuando son más de dos caracteres
	elif cad[0]=='!':
		if len(cad)>1:
			if cad[1]=='=':
				print(Token(tipoToken.BANG_EQUAL,cad[0]+cad[1],None).toString())
				return 2
			else:
				print(Token(tipoToken.BANG,cad[0],None).toString())
				return 0
		else:
			print(Token(tipoToken.BANG,cad[0],None).toString())
			return 0
	elif cad[0]=='=':
		if len(cad)>1:
			if cad[1]=='=':
				print(Token(tipoToken.EQUAL_EQUAL,cad[0]+cad[1],None).toString())
				return 2
			else:
				print(Token(tipoToken.EQUAL,cad[0],None).toString())
				return 0
		else:
			print(Token(tipoToken.EQUAL,cad[0],None).toString())
			return 0
	elif cad[0]=='>':
		if len(cad)>1:
			if cad[1]=='=':
				print(Token(tipoToken.GREATER_EQUAL,cad[0]+cad[1],None).toString())
				return 2
			else:
				print(Token(tipoToken.GREATER,cad[0],None).toString())
				return 0
		else:
			print(Token(tipoToken.GREATER,cad[0],None).toString())
			return 0
	elif cad[0]=='<':
		if len(cad)>1:
			if cad[1]=='=':
				print(Token(tipoToken.LESS_EQUAL,cad[0]+cad[1],None).toString())
				return 2
			else:
				print(Token(tipoToken.LESS,cad[0],None).toString())
				return 0
		else:
			print(Token(tipoToken.LESS,cad[0],None).toString())
			return 0
	#--------------Palabras clave----------------------------------
	elif cad[:3]=='and':
		print(Token(tipoToken.AND,cad[:3],None).toString())
		estructura.almacenar(tipoToken.AND,cad[:3],None)
		return 3
	elif cad[:4]=='else':
		print(Token(tipoToken.ELSE,cad[:4],None).toString())
		estructura.almacenar(tipoToken.ELSE,cad[:4],None)
		return 4
	elif cad[:5]=='false':
		print(Token(tipoToken.FALSE,cad[:5],None).toString())
		estructura.almacenar(tipoToken.FALSE,cad[:5],None)
		return 5
	elif cad[:3]=='fun':
		print(Token(tipoToken.FUN,cad[:3],None).toString())
		estructura.almacenar(tipoToken.FUN,cad[:3],None)
		return 3
	elif cad[:3]=='for':
		print(Token(tipoToken.FOR,cad[:3],None).toString())
		estructura.almacenar(tipoToken.FOR,cad[:3],None)
		return 3
	elif cad[:2]=='if':
		print(Token(tipoToken.IF,cad[:2],None).toString())
		estructura.almacenar(tipoToken.IF,cad[:2],None)
		return 2
	elif cad[:4]=='null':
		print(Token(tipoToken.NULL,cad[:4],None).toString())
		estructura.almacenar(tipoToken.NULL,cad[:4],None)
		return 4
	elif cad[:2]=='or':
		print(Token(tipoToken.OR,cad[:2],None).toString())
		estructura.almacenar(tipoToken.OR,cad[:2],None)
		return 2
	elif cad[:5]=='print':
		print(Token(tipoToken.PRINT,cad[:5],None).toString())
		estructura.almacenar(tipoToken.PRINT,cad[:5],None)
		return 5
	elif cad[:6]=='return':
		print(Token(tipoToken.RETURN,cad[:6],None).toString())
		estructura.almacenar(tipoToken.RETURN,cad[:6],None)
		return 6
	elif cad[:4]=='true':
		print(Token(tipoToken.TRUE,cad[:4],None).toString())
		estructura.almacenar(tipoToken.TRUE,cad[:4],None)
		return 4
	elif cad[:3]=='var':
		print(Token(tipoToken.VAR,cad[:3],None).toString())
		estructura.almacenar(tipoToken.VAR,cad[:3],None)
		return 3
	elif cad[:6]=='return':
		print(Token(tipoToken.RETURN,cad[:6],None).toString())
		estructura.almacenar(tipoToken.RETURN,cad[:6],None)
		return 6
	elif cad[:5]=='while':
		print(Token(tipoToken.WHILE,cad[:5],None).toString())
		estructura.almacenar(tipoToken.WHILE,cad[:5],None)
		return 5
	#--------------------------Literales-----------
	#Para cadenas
	elif cad[0]=='\"':
		while cad[j]!='\"':
			j+=1
		print(Token(tipoToken.STRING,cad[:j+1],None).toString())
		return j+1
	elif cad[0].isdigit():
		punto=0
		for i in range(len(cad)):
			if cad[i].isdigit():
				j+=1
			elif cad[i]=='.':
				#Para que salga con un número 1.
				if i <len(cad)-1:
					if cad[i+1].isdigit() and punto==0:
						j+=1
						punto=1
					else:
						break
				else:
					break
			else:
				break
		print(Token(tipoToken.NUMBER,cad[:j-1],cad[:j-1]).toString())
		return j-1
	elif cad[0].isalpha():
		for i in cad:
			if i.isdigit() or i.isalpha() or i=='_' or i=='-':
				j+=1
			else:
				break
		print(Token(tipoToken.IDENTIFIER,cad[:j-1],None).toString())
		return j-1
	else:
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
