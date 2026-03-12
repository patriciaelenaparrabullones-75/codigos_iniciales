first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo isupper()")
print(f"El formato del metodo title se ha aplicado?: {full_Name.isupper()}")


first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo upper()")
print(f"El formato del metodo title se ha aplicado sr./sra.: {full_Name.upper()}")

print("Usando el metodo capitalize()")
print(f"El formato del metodo capitalize()se ha aplicado su nombre: {first_Name.capitalize()}")
print(f"El formato del metodo capitalize()se ha aplicado su apellido: {last_Name.capitalize()}")
print(f"El formato del metodo center()se ha aplicado su nombre completo: {full_Name.center(20,"*")}")
print(f"El formato del metodo count()se ha aplicado su nombre completo contando la cantidad de letras en su nombre completo: {full_Name.count("",1)}")

print(f"El formato del metodo count()se ha aplicado su nombre completo contando la cantidad de letras r en su nombre completo: {full_Name.count("r")}")







