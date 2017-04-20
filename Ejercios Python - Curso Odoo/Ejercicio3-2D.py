L=['Hola','Soy','Programador','En','Python']

i = 0
cont = 0
while i<len(L):
	a = i+1
	if (a%2==0):
		print "La palabra '"+L[i]+"' es par"
		cont=cont+len(L[i])
	else:
		print "La palabra '"+L[i]+"' es impar"
		cont=cont+len(L[i])
	i+=1

print 'Toda la lista tiene un peso de '+str(cont)

cadena = ''

for x in L:
	cadena = str(x)+cadena

print cadena
