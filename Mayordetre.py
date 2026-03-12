print("**********************************************************")
print("*Programa que determina el numero mayor de tres numeros*")
print("**********************************************************")
num1=int(input("Por favor introduzca el primer numero: "))
num2=int(input("Por favor introduzca el segundo numero: "))
num3=int(input("Por favor introduzca el tercer numero: "))
if (num1>=num2) and (num1>=num3):
    print("El numero",num1,"es el mayor de los tres numeros")
if (num2>=num1) and (num2>=num3):
    print("El numero",num2,"es el mayor de los tres numeros")
if (num3>=num1) and (num3>=num2):
    print("El numero",num3,"es el mayor de los tres numeros")

