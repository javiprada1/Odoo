class Coche:

	def __init__(self, gasolina):
		self.gasolina = gasolina
		print "Tenemos "+str(self.gasolina)+" litros"
	def arrancar(self):
		if self.gasolina > 0:
			print "Arranca"
		else:
			print "No arranca"
	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -= 1
			print "Quedan "+str(self.gasolina)+ " litro"
		else:
			print "No se mueve"

