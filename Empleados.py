"""Programa que busca un empleado por cedula y si lo encuentra muestra sus datos"""
Empleado=[
            ["11263060","Alexis Gonzales","calle Margarita","2623344","12/04/92","Caracas","Soltero",1,"Activo","20/10/2024",2,30],
            ["11231597","Patricia Elena Parra Bullones","calle San Roque, Navalcarnero,Madrid, codigo 28600,Numero 20, Escalera 3, piso 3 ,puerta C","(0251)2627715","12/04/75","Barquisimeto,Edo Lara","Comprometida",21,"Activo","15/12/2024",0,20]

         ]

print("Datos del Empleado")
print("")
fil=len(Empleado)
col=len(Empleado[0])
Emp=(input("Introduzca la cedula del empleado:?"))
for  i in range (fil):
    for j in range (col):
        if (Empleado[i][j])==Emp:    
            print("")
            print("Cedula:",Empleado[i][j])
            print("Nombre:",Empleado[i][j+1])
            print("Direccion:",Empleado[i][j+2])
            print("Telefono:",Empleado[i][j+3])
            print("Fecha de Nacimiento:",Empleado[i][j+4])
            print("Lugar de Nacimiento:",Empleado[i][j+5])
            print("Estado Civil:",Empleado[i][j+6])
            print("Numero de hijos:",Empleado[i][j+7])
            print("Status:",Empleado[i][j+8])
            print("Fecha de Ingreso:",Empleado[i][j+9])
            print("Numero de Sanciones:",Empleado[i][j+10])
            print("N_Horas_Sem:",Empleado[i][j+11])
print("")
print("Fin del Programa")
