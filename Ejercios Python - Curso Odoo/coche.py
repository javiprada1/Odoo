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

#Inicializamos el objeto
mi_coche = Coche(3)

print mi_coche.gasolina
mi_coche.arrancar() #Imprime Arranca
mi_coche.conducir() #Imprime quedan dos litros
mi_coche.conducir() #Imprime quedan un litros
mi_coche.conducir() #Imprime quedan 0 litros
mi_coche.conducir() #Imprime no se mueve
mi_coche.arrancar() #Imprime Arranca
