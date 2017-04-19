class Instrumento:
	def __init__(self,precio):
		self.precio = precio
		print "El instrumento cuesta "+str(self.precio)+" euros"
	def tocar(self):
		print "Estamos tocando musica"
	def romper(self):
		print "Eso lo pagas tu"
		print "Son "+str(self.precio)+" euros"
class Trompeta(Instrumento): #Trompeta tiene el método tocar y romper
	pass
class Guitarra(Instrumento): #Trompeta tiene el método tocar y romper
	pass

