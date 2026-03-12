#Argumentos posicionales arbitrarios o variables args
def suma_numeros(*numeros):
    
    suma=sum(numeros)
    print(suma)

print("La suma de todos los numeros es:")
resultado=suma_numeros(7,4,3,2,10)  
#Argumentos de palabras clave arbitrarios KWargs
def Imprimir_info(**info):
    print(info)
    for clave, valor in info.items():
        print(f"{clave}:{valor}")

Imprimir_info(Nombre="Alejandro",Edad=25,Sexo="Masculino")
#Combinando en una funcion los args y los kwargs
def combinando_argumentos(*args,**kwargs):
    print("Mostrando los argumentos args:",args)
    print("Mostrando los argumentos KWargs:",kwargs)

combinando_argumentos(1,2,3,4,5,6, Nombre="Alejandro", Edad=45)    


