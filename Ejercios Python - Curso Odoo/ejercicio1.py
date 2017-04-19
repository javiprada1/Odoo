print "Ejercicio 1"
nombres = ["Maria","Alberto","Ana","Pedro","Rosa","Juan"]
print "Los nombres de chicos son: "+nombres[1]+", "+nombres[3]+", "+nombres[5]
print "Los nombres de chicas son: "+nombres[0]+", "+nombres[2]+", "+nombres[4]

print "Ejercicio 2"
INVENTORY = {'gold':500,'pouch':['flint', 'twine','gemstone'],'backpack':['xylophone','dagger','bedroll','bread loaf']}
INVENTORY['backpack'].sort()
INVENTORY['backpack'].remove('dagger')
print INVENTORY

print "Ejercicio 3"
L=['xylophone','dagger','bedroll','bread loaf']
L.append('drum')
L.insert(2,'trompet')
L.remove(L[3])
print L
