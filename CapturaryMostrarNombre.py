print("Hola")
print("Introduce 3 nombres y apellidos por favor: ") 

Cantidad=0
Seguir=1
while ((Cantidad<3)and(Seguir==1)):

   
   Nombre=input("Nombres y apellidos por favor: ")
   print("El nombre que intrudujistes fue:" , Nombre)
   Seguir=input("Estas de acuerdo con el nombre?,Si=1 y No=2:" )
   Seguir=int(Seguir)
   print("Felicidades tu nombre se ha escrito correctamente")

   Cantidad=(Cantidad+1) 
   print("van " ,Cantidad,"Nombres")
print("Adios!")   
      

