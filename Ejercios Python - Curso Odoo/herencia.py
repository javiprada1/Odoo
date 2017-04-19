class Instrumento:
	def __init__(self,precio):
		self.precio = precio
		print "El instrumento cuesta "+str(self.precio)+" euros"
	def tocar(self):
		print "Estamos tocando musica"
	def romper(self):
		print "Eso lo pagas tu"
		print "Son "+str(self.precio)+" euros"
class Trompeta(Instrumento): #Trompeta tiene el metodo tocar y romper
	def __init__(self,precio):
		self.precio = precio
		print "La trompeta cuesta"+str(precio)

	def tocar_trompeta(self):
		print "Estamos tocando la trompeta"

class Guitarra(Instrumento): #Trompeta tiene el metodo tocar y romper
	pass

b=Trompeta(50) #Inicializa Trompeta
b.tocar_trompeta() #Imprime estamos tocando la trompeta
b.romper() #Imprime eso lo pagas tu. Son 4 euros. Metodo Heredado

#Python permite la herencia multiple
# Class D(C,B)
# print D.__mro__
#
#
