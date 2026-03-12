
#Estructuras de datos Listas y tuplas
import random
cantidad=int(input("Introduzca la cantidad de veces que se realizara la operacion de numeros aleatorios:"))
minimo=int(input("Introduzca la cantidad el numero minimo:"))
maximo=int(input("Introduzca la cantidad el numero maximo:"))
lista=[]#Declarando lista vacia
for valor in range(cantidad):
    aleatorio=random.randint(minimo,maximo+1)
    #if aleatorio not in lista:
    lista.append(aleatorio)
    print("Numero Aleatorio:",aleatorio)
    #else:continue    
print("Lista de numeros aleatorios:")    
print(*lista, sep=",")
tupla=tuple(lista)
print(tupla)
lista_tupla=list(tupla)
print("Pasando de tupla a lista",lista_tupla)
tupla3=random.sample(range(minimo,maximo),10)
tupla3=tuple(tupla3)#Convirtiendo a tupla
print("tupla aleatoria de 10 numeros:")
print(tupla3)