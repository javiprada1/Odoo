class Persona:

	def __init__(self, sexo, edad):
			self.sexo = sexo
			self.edad = edad
			print "Persona con sexo: "+str(self.sexo)+" y edad: "+str(self.edad)
	def esAdulto(self):
		if int(self.edad) < 12:
			if str(self.sexo)=='h':
				print 'Es un ninyo'
			elif str(self.sexo)=='m':
				print 'Es una ninya'
			else:
				print 'Error por sexo equivocado: '+str(self.sexo)
		else:
			if str(self.sexo)=='h':
				print 'Es un adulto'
			elif str(self.sexo)=='m':
				print 'Es un adulto'
			else:
				print 'Error por sexo equivocado: '+str(self.sexo)

	def comprobarSexo(self):
		if str(self.sexo)=='h' or str(self.sexo)=='m':
			print 'Sexo correcto'
		else:
			print 'Sexo equivocado'

	def rangoDeEdad(self):
		if int(self.edad) < 16:
			print 'Adolescente'
		elif int(self.edad) >= 16 and int(self.edad) < 65:
			print 'Adulto'
		else: 
			print 'Jubilado'

#Inicializamos el objeto
mi_persona = Persona('g',67)
#mi_persona.esAdulto()
#mi_persona.comprobarSexo()
mi_persona.rangoDeEdad()


