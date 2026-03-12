#CONJUNTOS:Son agrupaciones de elementos desordenados, con elementos unicos
import numpy
misFrutas=         {"1) Fresas",
                    "2) Naranjas",
                    "3) Limas",
                    "4) Limones",
                    "5) Arandanos",
                    "6) Moras",
                    "7) Peras",
                    "8) Manzanas",
                    "9) Mandarinas",
                    "10)Pina",
                    "11)Kiwi"}
print("Mostrando mi conjunto donde guardo frutas ")
print(*misFrutas)
misFrutas.discard("11)Kiwi")
#En los conjuntos no se puede eliminar sin la funcion discard
print(*misFrutas, sep="/")
misFrutas.add("11)Kiwi")
print("Agregando un elemento al conjunto")
print(*misFrutas)

misVerduras=[
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
#misFrutas.update(misVerduras)
misFrutas.union(misVerduras)# para unir dos conjuntos
print("Union de una lista a un conjunto")
print(*misFrutas)
print("El tamano de mi conjunto es de:",len(misFrutas),"elementos")
print("10)Pina" in misFrutas)
print("10)Pina" not in misFrutas)

        

    