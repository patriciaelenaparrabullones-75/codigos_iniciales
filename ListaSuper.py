
"""Este programa recoge la lista de compras de Supermercado y las muestra un menu segun el rubro.Ya sea
Viveres,Verduras o Detergentes"""
"""nombre=input("Hola,escriba sun ombre por favor:")
print("Bienvenido",nombre, "a las listas de Compras")"""

print("")
resp=input("Desea revisar una de las listas ? Si=1 y No=2: ")            
resp=int(resp)
while (resp==1):
    print("")
    menu="""
        Elija una de las Seis Opciones:

        1= Lista de Alimentos

        2= Lista de Verduras

        3= Lista de Especias

        4= Lista de Frutas

        5= Lista de Detergentes

        6= Lista de Suplementos """

    print(menu)
    print("")
    opcion=input("Digite una opcion entre 1 y 6: ")
    opcion=int(opcion)

    if (opcion==1):
        print("")
        print("_"*125)
        print("")
        print("Lista 1: Mis Alimentos:")
        print("")
        print("_"*125)
        print("")
    
        MisAlimentos = ["1) Carnes Rojas",
                        "2) Pollo",
                        "3) Cerdo",
                        "4) Pescados",
                        "5) Atun",
                        "6) Huevos",
                        "7) Queso(Amarillo Gouda,blanco,madurado,de cabra,mozarella,azul,requeson)",
                        "8) Jamon de pavo",
                        "9) Tocineta",
                        "10) Salchichon",
                        "11) Jamon York",
                        "12) Aceite de Oliva",
                        "13) Aceite de Coco",
                        "14) Mantequilla",
                        "15) Queso crema",
                        "16) Sal Rosada",
                        "17) Sal gruesa",
                        "18) Bicarbonato de Sodio",
                        "19) Leche liquida",
                        "20) Leche en polvo",
                        "21) Mostaza ",
                        "22) Salsa de Soya ",
                        "23) Vinagre Blanco ",
                        "24) Jamon Curado ",
                        "25) Vinagre de Manzana ",
                        "26) Cafe",
                        "27) Te",
                        "28) Miel",
                        "29) Yogurt Griego",
                        "30) Manteca",
                        "31) Sal fina"]


        for Alimentos in MisAlimentos:
            print(Alimentos)       

            print("")
            print("")
        
    if (opcion==2):
        print("")
        print("_"*125)
        print("")
        print("Lista 2: Mis Verduras:")
        print("")
        print("_"*125)
        print("")

        MisVerduras=[
                     "1)  Ajo",
                     "2)  Cebollas",
                     "3)  Zanahoria",
                     "4)  Remolachas",
                     "5)  Tomates",
                     "6)  Brocoli",
                     "7)  Coliflor",
                     "8)  Aguacate",
                     "9)  Esparragos",
                     "10) Acelga",
                     "11) Espinacas",
                     "12) Repollo",
                     "13) Champiñones",
                     "14) Guisantes",
                     "15) Cilantro",
                     "16) Perejil",
                     "17) Pepino",
                     "18) Apio España",
                     "19) Calabacin",
                     "20) Pimenton",
                     "21) Ahuyama"
                     ]
        
        for Verduras in MisVerduras:
        
            print(Verduras)
            print("")
            print("")

    if (opcion==3):
        print("")
        print("_"*125)
        print("")
        print("Lista 3: Mis Especias:")
        print("")
        print("_"*125)
        print("")

        MisEspecias=["1)  Pimienta",
                     "2)  Ajo en polvo",
                     "3)  Cebolla en Polvo",
                     "4)  Paprica",
                     "5)  Curcuma",
                     "6)  Oregano en Polvo",
                     "7)  Romero",
                     "8)  Hiervas Provensales",
                     "9)  Eneldo",
                    "10)  Limocillo",
                    "11)  Canela",
                    "12)  Clavos de Olor",
                    "13)  Anis Estrellado",
                    "14)  Vainilla",
                    "15)  Jengibre"
                    ]
        """print(MisEspecias[14])"""""
        for Especias in MisEspecias:
            print(Especias)    

    if (opcion==4):
        print("")
        print("_"*105)
        print("")
        print("Lista 4: Mis Frutas:")
        print("")
        print("_"*105)
        print("")

        MisFrutas= ["1) Fresas",
                    "2) Naranjas",
                    "3) Limas",
                    "4) Limones",
                    "5) Arandanos",
                    "6) Moras",
                    "7) Peras",
                    "8) Manzanas",
                    "9) Mandarinas",
                    "10)Pina",
                    "11)Kiwi"]

        for Frutas in MisFrutas:
            print(Frutas)     
 

    if (opcion==5):
        print("")
        print("_"*105)
        print("")
        print("Lista 5: Mis Detergentes:")
        print("")
        print("_"*105)
        print("")

        MisDetergentes= ["1)  Desengrasante",
                         "2)  Limpia Cristales",
                         "3)  Jabon Liquido de Ropas",
                         "4)  Jabon de Bañarse",
                         "5)  Champu",
                         "6)  Papel Toilet",
                         "7)  Toalin",
                         "8)  Crema Dental",
                         "9)  Desodorante",
                        "10)  Jabon en Polvo",
                        "11)  Bicarbonato de Sodio",
                        "12)  Desinfectante",
                        "13)  Vinagre de Alcohol",
                        "14)  Lavaplatos Liquido",
                        "15)  Suavisante",
                        "16)  Servilletas",
                        "17)  Limpia Maderas", 
                        "18)  Amoniacal"
                        ]
        for Detergentes in MisDetergentes:
            print(Detergentes)     

    if (opcion==6):
        print("")
        print("_"*125)
        print("")
        print("Lista 6: Mis Suplementos:")
        print("")
        print("_"*125)
        print("")

        MisSuplementos= ["1) Citrato de Magnesio",
                         "2) Vitamina C",
                         "3) Vitamina D",
                         "4) Vitamina B3",
                         "5) NAD",
                         "6) Retro Resveratrol",
                         "7) Potasio"
                         ]

        for Suplementos in MisSuplementos:
            print(Suplementos)

    if (opcion > 6):
        print("Opcion fuera del rango!")
    MisAlimentos.append("32) Galletas Maria Dorada")   
    MisAlimentos.insert(32,"33) Salami")
    MisAlimentos.insert(33,"34) Chorizo")
    print(*MisAlimentos)
    MisFrutas= ["1) Fresas",
                    "2) Naranjas",
                    "3) Limas",
                    "4) Limones",
                    "5) Arandanos",
                    "6) Moras",
                    "7) Peras",
                    "8) Manzanas",
                    "9) Mandarinas",
                    "10)Pina",
                    "11)Kiwi"]
    MisAlimentos.extend(MisFrutas)
    print("Mi Lista de Alimentos unida a mi lista de frutas")
    print(*MisAlimentos,sep=",")
    MisAlimentos2=MisAlimentos
    print("Duplicando la lista de Mis Alimentos")
    print(*MisAlimentos2)
    resp=input("Desea Seguir Si=1 No=2: ")
    resp=int(resp)
    print("Hasta pronto")
        
 


           

   

      



            
  