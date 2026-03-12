Nombre=" Patricia Elena Parra Bullones "
Edad=50
Pasaporte="186163966"
NIE="Z2953069-N"
Cedu="V-11231597"
F_Nac="12/04/1975"
Estatura=1.57
Peso=78
Signo="Aries"
Ciudad="Madrid,Mostoles"
print("Bienvenido al Sistema")
print("")
NombreExt=input("Introduce tu nombre corto:\n")
if NombreExt=="Patri":
    print("")
    Nombre=Nombre.rstrip(" n  o ll u e s")
    Nombre=Nombre.lstrip(" P a ")
    print(f"Hola:{Nombre}")
    print("")
    print(f"Tu edad es de:{Edad} años")
    print("")
    print(f"Tu fecha de nacimiento es el:{F_Nac}")
    print("")
    print(f"Tu signo es:{Signo}")
    print("")
    print(f"Tu numero de pasaporte es:{Pasaporte}")
    print("")
    print(f"Tu numero de cedula es:{Cedu}")
    print("")
    print(f"Tu numero de NIE es:{NIE}")
    print("")
    print(f"Tu estatura es de {Estatura} cm")
    print("")
    print(f"Tu peso es de {Peso} kg")
    print("")
    print(f"Vives en {Ciudad}")
    print(f"El resultado de la suma de los numeros de tu fecha de nacimiento es:{12+4+1975}")
else:
    print("Persona no registrada")