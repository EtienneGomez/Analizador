from tipoToken import tipoToken
from Token import Token
import interprete as scan
import os,sys

os.system('clear')

if len(sys.argv)>1 and len(sys.argv)<3:
	if os.path.exists(sys.argv[1]):
		#print('\"Scaneando\" el archivo '+sys.argv[1])
		archivo=open(sys.argv[1],'r')
		cont=archivo.read()
