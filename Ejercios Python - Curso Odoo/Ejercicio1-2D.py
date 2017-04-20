#Ejercicio 1 del segundo dia de Python

#sexo = raw_input('Por favor, introduce tu sexo (h/m)')
#altura = int(input("Introduce tu altura en cm: "))
#peso =  int(input("Por ultimo, introduce tu peso en Kg"))
#print ('Has introducido de forma correcta: Sexo ' + sexo)

def calcula_peso(altura,sexo,peso):
	if str(sexo) == 'h':
		peso_ideal = 50 + 0.75 * (altura - 152.4)
		if peso_ideal < int(peso):
			print "Usted esta por debajo de su peso ideal"
		else:
			print ('Usted esta por encima de su peso ideal')
	else:
		peso_ideal = 50 + 0.67 * (int(altura) - 152.4)
		if peso_ideal < int(peso):
			print ('Usted esta por debajo de su peso ideal')
		else:
			print ('Usted esta por encima de su peso ideal')
calcula_peso(180,'h',250)
