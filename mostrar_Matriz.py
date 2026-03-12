"""Codigo que imprime por pantalla una lista anidada"""



MisNumeros=[[1,2,3,4,5,6,7,8,9,10],
            [1,2,3,4,5,6,7,8,9,11],
            [1,2,3,4,5,6,7,8,9,12],
            [1,2,3,4,5,6,7,8,9,13]]
print(MisNumeros)
print("")
for fil in MisNumeros:
    for col in fil:
      print(col)