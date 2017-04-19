dato = int(input('Escriba un valor positivo:'))
if dato < 0:
	print 'Mal hecho'
else:
	print 'Bien hecho'
print 'Ha escrito el valor'+str(dato)

i = 1
while i<=3:
	print(i)
	i+=1
print('Programa terminado')

print('Comienzo')
for x in [3,4,5]:
	print "Ahora x vale "+str(x)

#Definicion de metodos
def mi_funcion(param1, param2):
	print param1
	print param2
#Llamada
mi_funcion("hola",2)

def suma(x,y):
	return x+y
print suma(3,5)

def f(x,y):
	return x*2, y*2
print f(3,4)
