
  class Token():
    def __init__(self,tipo,lexema):
      self.tipo=tipo
      self.lexema=lexema
      self.literal=None
      self.salida=[]

    def __init__(self,tipo,lexema,literal):
      self.tipo=tipo
      self.literal=lexema
      self.salida=[]

    def toString(self)
        if self.literal==None:
          sal='<'+str(self.tipo)+''+str(self.lexema)+'>'
        else:
          sal='<'+str(self.tipo)+''+str(self.lexema)+''+str(self.literal)+'>'
        return sal

    def almacenar(self,tipo,lexema,literal)
        entrada=['','','']
        entrada[0]=tipo
        entrada[1]=lexema
        entrada[2]=literal
        self.salida+=entrada

    def imprimirEstruc(self):
      print(self.salida)
