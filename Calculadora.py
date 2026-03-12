
seguir=1
while seguir ==1:

    print("**********************************************************")
    print("*Calcuadora con menu de opciones*")
    print("**********************************************************")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Division Entera")
    print("6.Exponente")
    print("7.Modulo o Resto")
    opc=int(input("Por favor introduzca la opcion deseada: "))

    if  opc==1:
        print("Elegistes Suma")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1+num2
        print("El resultado de la operacion es:",result)

    elif  opc==2:
        print("Elegistes Resta")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1-num2
        print("El resultado de la operacion es:",result)
    elif  opc==3:
        print("Elegistes Multiplicacion")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1*num2
        print("El resultado de la operacion es:",result)
    elif  opc==4:
        print("Elegistes Division")
        num1=float(input("Por favor introduzca el primer numero: "))
        num2=float(input("Por favor introduzca el segundo numero: "))
        result=num1/num2
        print("El resultado de la operacion es:",round(result,2))
    elif  opc==5:
        print("Elegistes Division Entera")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1//num2
        print("El resultado de la operacion es:",result)
    elif  opc==6:
        print("Elegistes Exponente")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1**num2
        print("El resultado de la operacion es:",result)
    elif  opc==7:
        print("Elegistes Modulo")
        num1=int(input("Por favor introduzca el primer numero: "))
        num2=int(input("Por favor introduzca el segundo numero: "))
        result=num1%num2
        print("El resultado de la operacion es:",result)
    else:
        print("La opcion elegida no existe vuelve a  intentar")
    seguir=int(input("desea seguir si=1 o no=2:"))   
    
    print("Gracias por entrar al sistema de Calculadora Python") 
