
Seguir=1
while (Seguir==1):  
    a=int(input("Cuantos años tiene tu computador:?"))

    if (a>=0) and (a<=2):
        print("Tu computador es nuevo") 
        print("Puedes continuar con tu PC")

    
    if (a>2):
        print("Tu computador es viejo") 
        print("Considera comprar uno nuevo") 


    if (a<0):
        print("No puedes colocar años negativos")  
        print("Vuelve a intentarlo")  

     
    Seguir=input("Deseas Seguir Si=1/No=2:")
    Seguir=int(Seguir)     
print("_"*135)
print("Adios y Exitos!")
