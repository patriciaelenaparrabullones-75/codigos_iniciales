
resp="S"
while (resp=="S"):
    print("")
    Menu="""
        Elija una de las Tres Opciones:

        1= Lista de Alimentos

        2= Lista de Verduras

        3= Lista de Especias

        """

    print(Menu)
    
    opcion=input("Digite una opcion entre 1 y 3: ")
    opcion=int(opcion)

    if opcion==1:
        print("")
        print("Lista 1: Carnes")
        Lista1=[['pollo',24,7.5],
                ['cerdo',24,7.5],
                ['carne roja',24,7.5],
                ['Atun',24,7.5],
                ['Gambas',24,7.5],
                ['Costillas',24,7.5]]
        print(*Lista1,sep="/")
        """print(f"{Lista1[0]}, \n{Lista1[1]}, \n{Lista1[2]},\n{Lista1[3]},\n{Lista1[4]},\n{Lista1[5]}")"""
        resp=input("Desea Seguir Si=S No=N: ")
    if opcion==2:
        print("opc2")
        print("Lista 2: Verduras")
        Lista2=[['Cebolla',24,7.5],['Cilantro',24,7.5],['pepino',24,7.5]]
        print(f"{Lista2[0]}, \n{Lista2[1]}, \n{Lista2[2]}")
        print(*Lista2,sep="/")
        resp=input("Desea Seguir Si=S No=N: ")
         
    if opcion==3:
        print("opc3")
        print("Lista 3: Frutas")
        Lista3=[['fresas',24,7.5],['naranjas',24,7.5],['Limones',24,7.5]]
        print(f"{Lista3[0]}, \n{Lista3[1]}, \n{Lista3[2]}")
        print(Lista3)
        resp=input("Desea Seguir Si=S No=N: ")
        
    elif opcion > 3:
        print("Opcion fuera del rango!") 
        resp=input("Desea Seguir Si=S No=N: ")
        
    
         

           
