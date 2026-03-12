"""Programa que une dos listas de notas y las muestra por pantalla"""
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
meses2=["Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
meses.append(17)#agrega un numero al final de la lista 
meses2.append(18)
meses.insert(0,"Lista 1")#agrega un elemento en una posicion de la lista
meses2.insert(0,"Lista 2")#agrega un elemento en una posicion de la lista
meses.remove(17)#elimina un elemento en una posicion de la lista
meses2.remove(18)#elimina un elemento en una posicion de la lista

print(*meses, sep=',')#el asterisco es para mostrar la lista de una forma mas estetica sin los corchetes
# y separados por comas con el indicador sep

print(*meses2, sep=',')
print("\n")#salto de linea
misMeses=[meses,meses2]#union de dos listas
misMeses.sort()# muestra la lista ordenada
print("Primera lista ordenada")
print("\n")#salto de linea
print(*misMeses, sep=',')
print("\n")#salto de linea
print("La union de las dos listas")
print("\n")
print(' l1 ',end="")
print(*misMeses, sep=' l2')
misMeses.insert(1,"Union")#inserta un elemento nuevo en la lista y en una posicion
print(*misMeses)