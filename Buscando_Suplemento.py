
"""Usando el doble ciclo for para buscar.Mostrando por pantalla la busqueda de 
un suplemento e imprime el campo con su titulo"""
MisSuplementos=[["Citrato de Magnesio",2,5.42],
                ["Potasio",3,4.28],
                ["Vitamina C",4,2.16],
                ["Vitamina D",4,3.24],
                ["Vitamina B3",3,3.34],
                ["NAD",2,5.54],
                ]
print("Lista de Mis Suplementos")
print("")
fil=len(MisSuplementos)
col=len(MisSuplementos[0])
Sup=(input("Introduzca el nombre del Suplemento:?"))
for  i in range (fil):
    for j in range (col):
       if (MisSuplementos[i][j])==Sup:    
            print("Si existe en stock")
            print("__________________________________")
            print("Suplemento:",MisSuplementos[i][j])
            print("Cantidad:",MisSuplementos[i][j+1])
            print("Precio:",MisSuplementos[i][j+2])
            print("__________________________________")

print("")
print("Fin del Programa y gracias por consultar")
        