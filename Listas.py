"""Programa que une dos listas de notas y las muestra por pantalla"""
misNotas=[19,20,13,14,15,16,17,18,19,20]
misNotas2=[17,14,13,18,15,16,17,18,19,20]
misNotas.append(17)#agrega un numero al final de la lista 
misNotas2.append(18)
print(*misNotas, sep=',')#el asterisco es para mostrar la lista de una forma mas estetica sin los corchetes
# y separados por comas con el indicador sep
print(*misNotas2, sep=',')
print("\n")#salto de linea
misNotasUnion=[misNotas,misNotas2]#union de dos listas
misNotas.sort()# muestra la lista ordenada
print("Primera lista ordenada")
print("\n")#salto de linea
print(*misNotas, sep=',')
print("\n")#salto de linea
print("La union de las dos listas")
print("\n")
print(' l1 ',end="")
print(*misNotasUnion, sep=' l2')
misNotasUnion.insert(1,"Union")#inserta un elemento nuevo en la lista y en una posicion
print(misNotasUnion)