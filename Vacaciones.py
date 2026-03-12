print("********************************************************************")
print("Sistema de  control de Vacaciones")
print("********************************************************************")
nombre_Emp=input("Introduzca el nombre del empleado por favor:")
clave_Dep=int(input("Introduzca la clave del departamento por favor:"))
antiguedad=float(input("Introduzca los años de trabajo en la empresa del empleado por favor:"))

if clave_Dep==1:
    print("Perteneces al departamento de Mantenimiento")
    if (antiguedad >=1 and antiguedad <2):
        print("El empleado/a",nombre_Emp,"tiene derecho a 6 dias de vacaciones")
    elif(antiguedad >=2 and antiguedad <= 6):
        print("El empleado/a",nombre_Emp,"tiene derecho a 14 dias de vacaciones") 
    elif(antiguedad >=7):
        print("El empleado/a",nombre_Emp,"tiene derecho a 20 dias de vacaciones") 
    else:
        print("El empleado/a",nombre_Emp,"Aun notiene derecho a vacaciones")
               
if clave_Dep==2:
    print("Perteneces al departamento de Administracion")
    if (antiguedad >=1 and antiguedad <2):
        print("El empleado/a",nombre_Emp,"tiene derecho a 7 dias de vacaciones")
    elif(antiguedad >=2 and antiguedad <= 6):
        print("El empleado/a",nombre_Emp,"tiene derecho a 15 dias de vacaciones") 
    elif(antiguedad >=7):
        print("El empleado/a",nombre_Emp,"tiene derecho a 22 dias de vacaciones") 
    else:
        print("El empleado/a",nombre_Emp,"Aun notiene derecho a vacaciones")
    
    
if clave_Dep==3:
    print("Perteneces al departamento de Informatica")
    if (antiguedad >=1 and antiguedad <2):
        print("El empleado/a",nombre_Emp,"tiene derecho a 10 dias de vacaciones")
    elif(antiguedad >=2 and antiguedad <= 6):
        print("El empleado/a",nombre_Emp,"tiene derecho a 20 dias de vacaciones") 
    elif(antiguedad >=7):
        print("El empleado/a",nombre_Emp,"tiene derecho a 30 dias de vacaciones") 
    else:
        print("El empleado/a",nombre_Emp,"Aun notiene derecho a vacaciones")
    
    
if clave_Dep >3:
    print("La clave del departamento no existe:")
